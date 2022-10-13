#!/usr/bin/env python3

# Author: Bryan Troxel
# Description: This Lab covers the use and modification of dictionaries in Python.

#Create a dictionary
IPDICT = {"server1.testlab.com":"192.168.1.10",
          "server2.testlab.com":"192.168.1.11",
          "server3.testlab.com":"192.168.1.12",
          "server4.testlab.com":"192.168.1.13",
          "server5.testlab.com":"192.168.1.14",
          "server6.testlab.com":"192.168.1.15"}

#List all of the FQDN's in dictionary.
print(IPDICT.keys())

#List all of the IP Adresses in dictionary.
print(IPDICT.values())

#List all of the full records (key/value pairs)
print(IPDICT.items())

#Add a few more names to address mappings. Continue the ip address sequence above for their values. 
IPDICT["server7.testlab.com"] = "192.168.1.16"
IPDICT["server8.testlab.com"] = "192.168.1.17"
print(IPDICT)

#Test if server2.testlab.com is in dictionary.
if "server2.testlab.com" in IPDICT:
    print("Yes, server2.testlab.com exists.")
else:
    print("No, server2.testlab.com does not exist.")

#Test if server10.testlab.com is in dictionary.
if "server10.testlab" in IPDICT:
    print("Yes, server10.testlab.com exists.")
else:
    print("No, server10.testlab.com does not exist.")