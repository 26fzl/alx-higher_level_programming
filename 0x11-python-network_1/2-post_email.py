#!/usr/bin/python3
"""Send a reqyest"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    data = parse.urlencode({'email': email}).encode('utf-8')
    req = request.Request(url, data)
    try:
        with request.urlopen(req) as resp:
            print(resp.read().decode('utf-8'))
