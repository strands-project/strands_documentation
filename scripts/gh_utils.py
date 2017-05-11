#!/usr/bin/python
try:
    import requests
except:
    print "You need to install the requests module. sudo apt-get install python-requests"
    exit(1)
    
import json
import base64
from xml.dom.minidom import parseString
import sys
import os
import subprocess
import re

user = sys.argv[1]
password = sys.argv[2]

auth = (user,password)

def get_list(url, session=None):
    if session is None:
        session = requests.Session()
    r = session.get(url,auth=auth)
    
    if(r.ok):
        lst = json.loads(r.content)
        if "link" in r.headers and r.headers['link'] !="":
            next_search=re.search("<(.*)>; rel=\"next\"", r.headers['link'],re.IGNORECASE)
            if next_search is not None:
                next=next_search.group(1)
                print next
                lst.extend(get_list(next))
    return lst


def get_repos():
    """
    Gets a list of repositories on the strands account
    Return list of dictionaries
    """
    return get_list('https://api.github.com/orgs/strands-project/repos')
    # r = requests.get('https://api.github.com/orgs/strands-project/repos',auth=auth)
    # if(r.ok):
    #     repos = json.loads(r.content)
    #     return repos
    # return None

def get_repo_tree(repo, sha):
    """
    Gets the tree structure of te given repo at the give sha revision
    """
    r = requests.get('https://api.github.com/repos/strands-project/%s/git/trees/%s?recursive=1'%(repo,sha),auth=auth)
    if(r.ok):
        repos = json.loads(r.content)
        return repos
    return None

def get_file(repo, filepath):
    """
    Gets the contents of a file in the given repo
    """
    r = requests.get('https://api.github.com/repos/strands-project/%s/contents/%s?recursive=1'%(repo,filepath),auth=auth)
    if(r.ok):
        repos = json.loads(r.content)
        return base64.b64decode(repos["content"])
    return None


def get_commits(repo):
    return get_list('https://api.github.com/repos/strands-project/%s/commits?since=2016-04-01T00:00:00Z&until=2018-04-01T00:00:00Z'%(repo))



# Checkout latest version locally
#URLS=[]
#COMMITTERS={}
#repos=get_repos()
#rep_coms={}
#for i,repo in enumerate(repos):
#    r=repo['name']
#    print i+1,'/',len(repos), '   ', r
#    URLS.append(( repo["clone_url"],
#                  repo["name"]) )
#for URL, name in URLS:
#    if os.path.isdir(name):
#        os.chdir(name)
#        subprocess.call(["git","pull"])
#        os.chdir("..")
#    else:
#        subprocess.call(["git","clone",URL])


# repos=get_repos()
# for i,repo in enumerate(repos):
#     r=repo['name']
#     print i+1,'/',len(repos), '   ', r
    
#import sys
#sys.exit(1)

URLS=[]
COMMITTERS={}
print "Getting repos..."
repos=get_repos()
print "Repos: "
for i in repos:
    print " - ",i['name']



# rep_coms={}
# for i,repo in enumerate(repos):
#     r=repo['name']
#     print i+1,'/',len(repos), '   ', r
#     URLS.append(( repo["clone_url"],
#                   repo["name"]) )
#     commits=get_commits(r)
#     print "number of commits: ", len(commits)
#     rep_coms[r]=commits
#     for c in commits:
#         nm=c['commit']['committer']['name']
#         if not COMMITTERS.has_key(nm):
#             COMMITTERS[nm]=0
#         COMMITTERS[nm]+=1

# #    k=raw_input("Nex?")
# #    if k=="no":
# #        break

# import pickle
# f=open("committers","w")
# f.write(pickle.dumps(COMMITTERS))
# f.close()

# f=open("repo_commits","w")
# f.write(pickle.dumps(rep_coms))
# f.close()
# for c in COMMITTERS:
#     print c,"  ",COMMITTERS[c]

# # Checkout latest version locally
# # for URL, name in URLS:
# #     if os.path.isdir(name):
# #         os.chdir(name)
# #         subprocess.call(["git","pull"])
# #         os.chdir("..")
# #     else:
# #         subprocess.call(["git","clone",URL])


    
