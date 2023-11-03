#!/usr/bin/python3
"""Sends a request"""
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]

    try:
        resp = requests.get(url)
        resp.raise_for_status()
        utf8_d = resp.text
        print(utf8_d)

    except requests.exceptions.HTTPError as err:
        print(f"Error code: {err.response.status_code}")

