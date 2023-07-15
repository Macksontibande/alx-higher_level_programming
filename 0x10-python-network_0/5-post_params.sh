#!/bin/bash
# A script that Send POST request with given variables to a given URL.
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
