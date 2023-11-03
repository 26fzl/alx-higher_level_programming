#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status."""
import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)

    body = response.content
    utf8_content = body.decode("utf-8")

    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode("utf-8")))
