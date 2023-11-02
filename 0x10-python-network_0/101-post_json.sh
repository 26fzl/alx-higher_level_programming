#!/bin/bash
# send a request and dsiplay
curl -sX POST -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
