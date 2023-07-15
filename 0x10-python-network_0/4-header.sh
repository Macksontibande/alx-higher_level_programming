#!/bin/bash
# script that takes in a URL  sends a GET request, desplay response
curl -s "$1" -H "X-School-User-Id: 98"
