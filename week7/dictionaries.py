#!/usr/bin/env python3

# Author: Bryan Troxel
# Description: This Lab covers the use and modification of dictionaries in Python.

#Create a dictionary
IPDICT = {"FQDN1": {"servername" : "server1.testlab.com", "IP" : "192.168.1.10"},
         "FQDN2": {"servername" : "server2.testlab.com", "IP" : "192.168.1.11"},
         "FQDN3": {"servername" : "server3.testlab.com", "IP" : "192.168.1.12"},
         "FQDN4": {"servername" : "server4.testlab.com", "IP" : "192.168.1.13"},
         "FQDN5": {"servername" : "server5.testlab.com", "IP" : "192.168.1.14"},
         "FQDN6": {"servername" : "server6.testlab.com", "IP" : "192.168.1.15"}}

#List all of the FQDN's in dictionary.
for FQDN1 in IPDICT:
        print(f"FQDN:{IPDICT[FQDN1]['servername']}")
print("\n")
#List all of the IP Adresses in dictionary.
for FQDN1 in IPDICT:
        print(f"IP Address:{IPDICT[FQDN1]['IP']}")
print("\n")
#List all of the full records (key/value pairs)
for FQDN1 in IPDICT:
        print(f"Key:{IPDICT[FQDN1]['servername']}")
        print(f"Value:{IPDICT[FQDN1]['IP']}\n")
print("\n")

#Add a few more names to address mappings. Continue the ip address sequence above for their values. 
IPDICT["FQDN7"] = '{"servername" : "server7.testlab.com", "IP" : "192.168.1.16"},'
IPDICT["FQDN8"] = '{"servername" : "server8.testlab.com", "IP" : "192.168.1.17"},'

#Test if server2.testlab.com is in dictionary.
print(f"Checking for server2.testlab.com... {IPDICT['FQDN2']}")

#Test if server10.testlab.com is in dictionary.
print(f"Checking for server10.testlab.com... {IPDICT['FQDN10']}")