#!/usr/bin/env python3
# Author:   Bryan Troxel
# Description:  Parsing a website.

import requests
from bs4 import BeautifulSoup

response = requests.get("http://notpurple.com")

try:
    response.raise_for_status()
    soup = BeautifulSoup(response.text,'html.parser')
    print(soup.title.text)
    for link in soup.find_all('a'):
        print(f"{link.text}: {link.get('href')}")
except Exception as exc:
    print(f"Something went awry: {exc}")
