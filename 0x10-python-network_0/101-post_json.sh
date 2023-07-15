#!/bin/bash
# sends a JSON POST request to a first URL argument, displays response
curl -s -X POST "$1" -H "Content-Type: application/json" -d @"$2"
