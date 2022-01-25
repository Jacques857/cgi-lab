#!/usr/bin/env python3
import os
import json

#print environment variables
"""print("Content-Type: application/json")
print()
print(json.dumps(dict(os.environ), indent=2))"""

#print the query parameters
print("Content-Type: text/html")
print()
print(f"<p>query string = {os.environ['QUERY_STRING']}</p>")

#print the user's browser
print(f"<p>browser = {os.environ['HTTP_USER_AGENT']}</p>")