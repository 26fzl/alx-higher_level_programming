#!/usr/bin/python3
"""takes , send and display value """
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    reqs = requests.get(url)
    print(reqs.headers.get("X-Request-Id"))
