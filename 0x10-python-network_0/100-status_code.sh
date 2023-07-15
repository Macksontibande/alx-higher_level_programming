#!/bin/bash 
# Sends passed requested argument, and displays only the status response.
curl -sI -w '%{response_code}' "$1" -o /dev/null
