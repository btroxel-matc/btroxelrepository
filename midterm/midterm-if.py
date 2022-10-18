#!/usr/bin/env python3
#Author: Bryan Troxel
#Description: Midterm Activity 1: Flow Control

print("Name: Bryan Troxel")

Total = 0
midtxt = open("Midterm-if.txt", "r")
midif = midtxt.readlines()
for line in midif:
    if "gmeach18@ed.gov" in line:
        id = line.split(",")[0]
        Total+= int(id)
    elif "248.253.63.149" in line:
        id = line.split(",")[0]
        Total+= int(id)
    elif "Whiteland" in line:
        id = line.split(",")[0]
        Total+= int(id)
    elif "80.222.19.190" in line:
        id = line.split(",")[0]
        Total+= int(id)
    elif "Kayley" in line:
        id = line.split(",")[0]
        Total+= int(id)
    elif "dcassyqw@microsoft.com" in line:
        id = line.split(",")[0]
        Total+= int(id)
print(f"The total is: {Total}")
midtxt.close()