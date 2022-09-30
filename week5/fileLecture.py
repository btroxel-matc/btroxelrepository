#!/usr/bin/env python3
# Author:   Bryan Troxel
# Description: Today we are going through the work of
# opening and reading files. Throwing in the multi-line
# print capabilities and function tell()

"""
preambleFile = open("preamble.txt", "r")
preambleContent = preambleFile.read()
print(type(preambleContent))
print(preambleContent)
print(f"Length: {len(preambleContent)}")
preambleFile.close()
"""

"""
preambleFile = open("preamble.txt", "r")
preambleContent = preambleFile.read(25)
print(type(preambleContent))
print(preambleContent)
print(f"Length: {len(preambleContent)}")
preambleFile.close()
preambleFile = open("preamble.txt", "r")
preambleContent = preambleFile.read(25)
print(type(preambleContent))
print(preambleContent)
print(f"Length: {len(preambleContent)}")
preambleFile.close()preambleFile = open("preamble.txt", "r")
preambleContent = preambleFile.read(25)
print(type(preambleContent))
print(preambleContent)
print(f"Length: {len(preambleContent)}")
preambleFile.close()preambleFile = open("preamble.txt", "r")
preambleContent = preambleFile.read(25)
print(type(preambleContent))
print(preambleContent)
print(f"Length: {len(preambleContent)}")
preambleFile.close()
"""


preambleFile = open("preamble.txt", "r")
preambleContent = preambleFile.read(25)
while preambleContent:
    #print(type(preambleContent))
    #print(preambleContent)
    print(f"Reading25chars:  [Length:  {len(preambleContent):05d}] [Index: {preambleFile.tell():05d}]  [Content:  {preambleContent}]")
    preambleContent = preambleFile.read(25)
preambleFile.close()



preambleFile = open("preamble.txt", "r")
preambleContent = preambleFile.readline()
count = 0
totalChar = len(preambleContent)
while preambleContent:
    #print(type(preambleContent))
    count += 1
    print(f"{count:03d}:  [Length:  {len(preambleContent):05d}] [Index: {preambleFile.tell():05d}]  Content:  {preambleContent}")
    preambleContent = preambleFile.readline()
    totalChar += len(preambleContent)
print(f"Length: {totalChar}")
preambleFile.close()

preambleFile = open("preamble.txt", "r")
preambleContent = preambleFile.readlines()
print(f"[Length:  {len(preambleContent):05d}] [Index: {preambleFile.tell():05d}]")
print(f"[Content: {preambleContent}")
print(type(preambleContent))
preambleFile.close()