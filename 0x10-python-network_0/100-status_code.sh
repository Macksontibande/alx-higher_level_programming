#!/bin/bash 
# Sends passed requested argument, and displays only the status response.
curl -s -L -X HEAD -w "%{http_code}" "$1"
