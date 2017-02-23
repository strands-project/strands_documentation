#!/usr/bin/env python

# Scrapes all strands-project repositories for any readme files and wikis, and
# puts them into directories by repository

import requests
import getpass
import os
import json
import argparse
import rospkg
import subprocess
import shutil
import base64

ignore_repos = ["laser_filtering", "buildfarm", "metapackages", "jenkins_tools",
                "scitos_common", "strands_ci", "ros_mbt", "navigation_layers",
                "scitos_2d_navigation", "openni_wrapper", "executive_smach", "morse",
                "sicks300", "mjpeg_server", "robomongo", "rosdistro", "strands_management",
                "robomongo", "MIRASimpleClient", "navigation", "semantic_segmentation",
                "rosbridge_suite"]
ignore_filenames = ["authors", "changelog"]

def path_to_arr(path):
    arr = []
    while path:
        arr.append(os.path.basename(path))
        path = os.path.dirname(path)

    return list(reversed(arr))

gh_api = "https://api.github.com"
org = "strands-project"

parser = argparse.ArgumentParser(description="Scrape documentation from the strands project repositories")
parser.add_argument("--private", action="store_true", help="Include private repositories in the scrape. This requires the generation of an OAuth token for github.")
parser.add_argument("--ignore-file", nargs=1, help="File containing the names of repos to ignore in the documentation scrape. One repo per line.")

args = parser.parse_args()
header = ""

if args.private:
    # The first thing to do is get an OAuth token - we will use this in place of the
    # username and password in order to access public and private repositories in
    # the organisation. This allows for many more API requrests to be made

    # Check if we already have a token in the config file
    conf_file = os.path.join(os.path.expanduser("~"), ".strands_doc_oauth.tok")
    if not os.path.isfile(conf_file):
        print("Couldn't find the token file.")

        user = raw_input("Enter your github username: ")
        password = getpass.getpass("Enter your github password:")

        auth_data = json.dumps({"scopes": ["repo"], "note": "strands_documentation scraper"})
        auth = (requests.post(gh_api + "/authorizations", data=auth_data, auth=(user, password))).json()

        # If we already got a token recently, we will receive an error message
        if "token" not in auth:
            print("Couldn't get Github auth token: {0}".format(auth["message"]))
            token = None
        else: # otherwise, save the token to a file so we can use it again later
            with os.fdopen(os.open(os.path.join(os.path.expanduser("~"), ".strands_doc_oauth.tok"), os.O_WRONLY | os.O_CREAT, 0o600), 'w') as handle:
                handle.write(auth["token"])
                token = auth["token"]
    else:
        with open(conf_file, 'r') as f:
            token = f.read()
        print("Found config file with token.")


    if token:
        header = {"Authorization": "token {0}".format(token)}
    else:
        print("Proceeding without auth token.")
        header = ""

# get a list of all the repositories in the organisation
repo_rq = requests.get(gh_api + "/orgs/{0}/repos?type=all".format(org), headers=header)

repos = {repo_data["name"]: repo_data for repo_data in json.loads(repo_rq.text)}
# If there are more than 30 repos, there will be multiple pages
if "link" in repo_rq.headers:
    # keep getting the data until we reach the final page - we can deduce this
    # by there not being a link to the last page, because we are on it.
    while "last" in repo_rq.headers["link"]:
        print(repo_rq.headers["link"])
        # Get the URL for the next page by splitting the links up
        next_pg = repo_rq.headers["link"].split(',')[0].split(';')[0][1:-1]
        repo_rq = requests.get(next_pg, headers=header)
        repos.update({repo_data["name"]: repo_data for repo_data in json.loads(repo_rq.text)})

# This is where the bulk of the work is done. We check each repository for
# readme files and see if it has a wiki. If we find files there, we copy them
# and put them in directories corresponding to the name of the repository
FNULL = open(os.devnull, 'w')
for repo_name in sorted(repos.keys()):
#for repo_name in ["g4s_deployment", "rosbridge_suite", "v4r", "v4r_ros_wrappers"]:
    print("-------------------- {0} --------------------".format(repo_name))
    if repo_name in ignore_repos:
        print("ignoring repo".format(repo_name))
        continue

    # We can check if a wiki exists by calling git ls-remote. If it returns an
    # OK, then there is a wiki
    if subprocess.call(["git", "ls-remote", "https://github.com/strands-project/{0}.wiki.git".format(repo_name)], stdout=FNULL, stderr=FNULL) == 0:
        wiki_dir = "docs/{0}/wiki".format(repo_name)
        if not os.path.isdir(wiki_dir):
            print("Wiki exists. Cloning...")
            subprocess.call(["git", "clone", "https://github.com/strands-project/{0}.wiki.git".format(repo_name), wiki_dir])
            # delete the .git directory cloned along with the wiki
            shutil.rmtree(os.path.join(wiki_dir, ".git"))
            # rename the Home.md file to index.md so it works properly with mkdocs
            #os.rename(os.path.join(wiki_dir, "Home.md"), os.path.join(wiki_dir, "index.md"))

    # The main readme file in the repo is easily retrieved, but just do this using the tree instead
    #readme_rq = requests.get(gh_api + "/repos/{0}/{1}/readme".format(org, repo_name), headers=header)

    # We also need to look at the whole repository to find the readmes for
    # subdirectories, since there are many such cases. First, get the current
    # commit sha on the default branch
    sha_rq = requests.get(gh_api + "/repos/{0}/{1}/commits".format(org, repo_name), headers=header)
    latest_sha = json.loads(sha_rq.text)[0]["sha"]
    # Use that sha to get the commit tree
    tree_rq = requests.get(gh_api + "/repos/{0}/{1}/git/trees/{2}?recursive=1".format(org, repo_name, latest_sha), headers=header)
    repo_tree = json.loads(tree_rq.text)

    # Look through the tree and try to find things which are likely to be readme-type files
    print("Looking for readme files...")
    # We gather readmes here so we can remap any links in them, which we need to
    # do because we will change the filenames to make the documentation appear
    # in a nicer way. Gather them in a dict which will group multiple readmes in
    # the same subdirectory, which we want to handle differently.
    readmes = {}
    for item in repo_tree["tree"]:
        lower_fname, lower_ext = os.path.splitext(os.path.basename(item["path"].lower()))
        if lower_fname not in ignore_filenames and (lower_ext == ".md" or lower_fname == "readme"):
            # The first directory in the path we get is a subdirectory in the
            # repo, and we use this as the key for each readme found in that
            # subdirectory
            split_path = path_to_arr(os.path.dirname(item["path"]))
            key = split_path[0] if split_path else "index"
            if key not in readmes:
                readmes[key] = []
            readmes[key].append((item, split_path, lower_fname))

    for subpkg in readmes.keys():
        print("processing {0}".format(subpkg))
        # The path we get in each item is something like
        # strands_navigation/topological_rviz_tools/readme.md. When using
        # mkdocs, this will generate the documentation in subheadings for each
        # subdirectory, whereas we would prefer it to be grouped under
        # strands_navigation. So, we will save the data in readme.md to
        # strands_navigation/topological_rviz_tools.md. In the case of packages
        # with multiple readmes, we will create a separate directory for them so
        # they are in their own section.

        base_path = os.path.join("docs", repo_name)

        multiple = False
        if len(readmes[subpkg]) > 1:
            # sometimes the top level may have multiple files, but we don't want
            # to put them in a subdirectory
            if subpkg != "index":
                base_path = os.path.join(base_path, subpkg)
            multiple = True

        for readme in readmes[subpkg]:
            if multiple:
                if len(readme[1]) <= 1:
                    if readme[2] == "readme":
                        fname = "index.md"
                    else:
                        fname = readme[2] + ".md"
                else:
                    print("path is long: {0}".format(readme[1]))
                    fname = os.path.basename(os.path.dirname(readme[0]["path"])) + ".md"
            else:
                if len(readme[1]) == 0:
                    fname = "index.md"
                else:
                    fname = os.path.basename(os.path.dirname(readme[0]["path"])) + ".md"

            path = os.path.join(base_path, fname)
            print("Saving {0} to {1}".format(readme[0]["path"], path))
            if not os.path.isdir(os.path.dirname(path)):
                os.makedirs(os.path.dirname(path))

            # Get the contents of the readme file from github and output them to a file
            file_rq = json.loads(requests.get(readme[0]["url"], headers=header).text)
            # decode and output the base64 string to file
            with open(path, 'w') as f:
                f.write(base64.b64decode(file_rq["content"]))
