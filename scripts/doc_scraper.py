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

ignore_repos = ["laser_filtering", "buildfarm", "metapackages", "jenkins_tools", "scitos_common", "strands_ci", "ros_mbt", "navigation_layers", "scitos_2d_navigation", "openni_wrapper", "executive_smach", "morse", "sicks300", "mjpeg_server"]

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
#for repo_name in sorted(repos.keys()):
for repo_name in sorted(["strands_navigation"]):
    print("-------------------- {0} --------------------".format(repo_name))
    if repo_name in ignore_repos:
        print("ignoring repo".format(repo_name))
        continue
    

    # We can check if a wiki exists by calling git ls-remote. If it returns an
    # OK, then there is a wiki
    if subprocess.call(["git", "ls-remote", "https://github.com/strands-project/{0}.wiki.git".format(repo_name)], stdout=FNULL, stderr=FNULL) == 0:
        print("Wiki exists. Cloning...")
        wiki_dir = "{0}/{0}.wiki".format(repo_name)
        subprocess.call(["git", "clone", "https://github.com/strands-project/{0}.wiki.git".format(repo_name), wiki_dir])
        # delete the .git directory cloned along with the wiki
        shutil.rmtree(os.path.join(wiki_dir, ".git")

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
    for item in repo_tree["tree"]:
        lower = item["path"].lower()
        if "md" in lower or "readme" in lower:
            path = os.path.join(repo_name, item["path"])
            print("creating file {0}".format(os.path.join(repo_name, item["path"])))
            # We get a url with the item which allows us to retrieve it, in base 64
            file_rq = json.loads(requests.get(item["url"], headers=header).text)
            if not os.path.isdir(os.path.dirname(path)):
                os.mkdir(os.path.dirname(path))

            # decode and output the base64 string to file
            with open(path, 'w') as f:
                f.write(base64.b64decode(file_rq["content"]))
