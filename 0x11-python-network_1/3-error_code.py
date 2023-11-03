#!/usr/bin/python3
"""Sends a request"""
import sys
import urllib.error
import urllib.request

if __name__ == "__main__":
     url = sys.argv[1]

    reqs = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(reqs) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
