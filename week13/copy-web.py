#!/usr/bin/env python3
# Author:   Bryan Troxel
# Description:  Copying a webpage into a file.

import requests

response = requests.get("https://notpurple.com")

with open("my_web_file.html", "w") as cpyweb:
    cpyweb.write(response.text)