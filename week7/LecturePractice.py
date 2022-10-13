#!/usr/bin/env python3

# Author: Bryan Troxel
# Description: Week 7, Lecture

import json

#demoDict = {}
#print(type(demoDict))


#demoDict = {"Mom":True,"is":False,"best":True}
#print(type(demoDict))
#print(demoDict)
#print(type(demoDict["Mom"]))
#print((demoDict["Mom"]))


with open("dictionaries.py","r") as dictFile:
    strDict = dictFile.read()
    print(type(strDict))
    print(strDict)
    dictDict = json.loads(strDict)
# print(type(dictDict))
# print(dictDict)
# print(f"Value of recInteger is {dictDict['recInteger']} and the data type is {type(dictDict['recInteger'])}")
# print(f"Value of recInteger is {dictDict['recFloat']} and the data type is {type(dictDict['recFloat'])}")
# print(f"Value of recInteger is {dictDict.get['recString']} and the data type is {type(dictDict['recString'])}")
# print(f"Value of recInteger is {dictDict.get['recList']} and the data type is {type(dictDict['recList'])}")

# # Keys, Values, Items
# print(f"Keys: {dictDict.keys()}")
# print(f"Values: {dictDict.values()}")
# print(f"Items: {dictDict.items()}")

# #You can add more key value pairs
# dictDict["recBoolean"] = True
# dictDict["recTuple"]= (2,2.718281828459045, "I am a string in a tuple")
# print(f"Value of recBoolean is {dictDict.get('recBoolean')} and the data type is {type(dictDict['recBoolean'])}")")

# # Flow control
# if "recInteger" in dictDict:
#     print(f"Value of re")

#     if 

# # Value of 3.14?
# if 3.14 in dictDict:
#     print("Finding values, not just keys")
# else:
#     print("Must only be keys when using an in statement in a dictionary")

#Sort
# print("\n")
# print(sorted{dictDict})
# print(type{sorted(dictDict)})
# print("\n")

# for key in sorted(dictDict):
#     print(key, dictDict[key])
# print("\n")

# # Reverse Sort
# for key in sorted(dictDict, reverse=True):
#     print(key, dictDict[key])
# print("\n")

dictDict["embeddedDict"] = {"person1": }