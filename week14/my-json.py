#!/usr/bin/env python3
#Author: Bryan Troxel
#Description: This script is to practice the uses of the JSON module. In this particular case, the JSON module will translate into a Python dictionary.

import requests, json, argparse, sys

parser = argparse.ArgumentParser(description="Enter ip address for dictionary.")
parser.add_argument('--ipaddress', metavar='[an ipaddress]', dest='varip', required=True, type=float, help='<required> Enter an ipaddress.')

js_resp = requests.get(f"http://ipinfo.io/{sys.argv[2]}/json")
myDict = json.loads(js_resp.text)

for key in myDict.keys():
    print(f"{key: <10}:{myDict[key]}")