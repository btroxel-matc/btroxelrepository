#!/usr/bin/env python3

#Author: Bryan Troxel
#Description: This script covers file manipulations through read only functions.

passwdFile = open("/etc/passwd", "r")
passwdContent = passwdFile.read()
print(f"len() results: {len(passwdContent)}")
print(f"len() function with Read: In a string, the len() function returns the amount of characters it contains.")
print(f"Example for Use: Read is a good option when you need to search the entire contents of a file.")
passwdFile.close()

passwdFile = open("/etc/passwd", "r")
passwdContent = passwdFile.readlines()
print(f"len() results: {len(passwdContent)}")
print(f"len() function with Readlines: When used with a list, the len() function returns the number of elements in a list")
print(f"Example for Use: Readlines is useful for small files to sort objects into a list line by line.")
passwdFile.close()

passwdFile = open("/etc/passwd", "r")
passwdContent = passwdFile.readline()
ffile = passwdContent

while passwdContent:
    passwdContent = passwdFile.readline()
    ffile += passwdContent

totalchar = len(ffile)
print(f"Total Characters: {totalchar}")
print(f"Example for Use: Using the readline function in a loop can be used when looking through a document line by line for specific characteristics like IP addresses.")
passwdFile.close()