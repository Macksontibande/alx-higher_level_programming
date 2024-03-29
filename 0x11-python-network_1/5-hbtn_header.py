#!/usr/bin/python3
"""Python script that takes in a URL, sends a request"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)

    # Get specific response headers and ouput
    print(response.headers.get("X-Request-Id"))
