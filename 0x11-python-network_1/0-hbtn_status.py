#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status."""
import urllib.request

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    response = urllib.request.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode("utf-8")))
