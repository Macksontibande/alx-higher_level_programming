#!/bin/bash
# script that makes a request, cause server to respond a message You got me!,in response.
curl -sL -X PUT -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me_3
