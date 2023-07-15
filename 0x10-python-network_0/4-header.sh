#!/bin/bash
# script that takes in a URL  sends a GET request, desplay response
curl -sL -X GET -H "X-School-User-Id: 98" "$1"
