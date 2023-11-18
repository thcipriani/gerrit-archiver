#!/usr/bin/env python

import argparse
import json
import urllib.parse as urlparse

import requests

GERRIT = 'https://gerrit.wikimedia.org/r/'
SESSION = requests.Session()

def get_description(repo):
    r = SESSION.get(urlparse.urljoin(GERRIT, f'r/a/projects/{repo}/description'))
    r.raise_for_status()
    # Strip the first five bytes of the Gerrit JSON response
    return r.text[5:]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("repo", help="Repo name (e.g. 'myrepo/repo')")
    ap.add_argument("message", help="Message for archiving the repo")
    args = ap.parse_args()

    # escape slashes in the repo name
    repo = args.repo.replace('/', '%2F')
    description = get_description(repo)
    print(description)



if __name__ == '__main__':
    main()