#!/usr/bin/python3
"""Python script that takes in a URL and an email,sends POST request"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    values = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    request = urllib.request.Request(url, data)

    with urllib.request.urlopen(request) as response:
        body = response.read()

        print(body.decode("utf-8"))
