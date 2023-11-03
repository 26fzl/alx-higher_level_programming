#!/usr/bin/python3
"""Send a reqyest"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    params = {"email": email}
    utf_params = urllib.parse.urlencode(params).encode('utf-8')
    reqs = urllib.request.Request(url, data=utf_params, method='POST')
    with urllib.request.urlopen(reqs) as resp:
        print(resp.read().decode('utf-8'))
