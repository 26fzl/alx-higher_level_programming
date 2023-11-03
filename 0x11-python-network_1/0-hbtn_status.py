#!/usr/bin/python3
"""script fetching https://alx-intranet.hbtn.io/status."""
import urllib.request


if __name__ == "__main__":
    reqs = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(reqs) as resp:
        body = resp.read()
        print("Body resp:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
