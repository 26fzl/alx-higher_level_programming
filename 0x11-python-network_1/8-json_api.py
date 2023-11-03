#!/usr/bin/python3
""" module doc """
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    url = "http://0.0.0.0:5000/search_user"
    params = {"q": q}
    r = requests.post(url, data=params)
    try:
        rjson = r.json()
        if rjson:
            print(f'[{rjson["id"]}] {rjson["name"]}')
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
