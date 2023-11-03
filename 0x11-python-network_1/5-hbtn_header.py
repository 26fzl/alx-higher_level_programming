#!/usr/bin/python3
"""takes , send and display value """
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    res = requests.get(url)
    print(r.headers.get("X-Request-Id"))
