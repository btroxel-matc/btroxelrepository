#!/usr/bin/env python3

#This script is for Lab 2 covering strings.
print("This script is for Lab 2 covering strings")
#Author: Bryan Troxel
print("Author: Bryan Troxel")

varRed = "Red"
varGreen = "Green"
varBlue = "Blue"
varName = "Timmy"
varLoot = 10.4516295

print(f"Your {varGreen: <0s} Output")

print(f"Hello {varName}")
print(f"{varRed}-{varGreen}-{varBlue}")
print(f"Is this {varGreen.lower()} or {varBlue.lower()}?")
print(f"My name is {varName.upper()}")
print(f"[{varRed:+^7}]")
print(f"[{varGreen.lower():=<7}]")
print(f"[{varBlue.lower():*>9}]")
print(f"{varBlue *10}")
print(f"{varLoot}")
print(f"{varLoot: <.1f}")
print(f"I have ${varLoot: <.2f}")
print(f"[{varRed:$^10}][{varGreen:$^10}][{varBlue:$^10}]")
print(f"[ {varRed[::-1]} ][ {varGreen} ][ {varBlue[::-1]} ]")
print(f"First Color:[{varRed}] Second Color:[{varGreen}] Third Color:[{varBlue}]")