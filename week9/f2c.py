#!/usr/bin/env python3
# Author: Bryan Troxel
# Description: This lab covers the use of Functions

def convert_temp(degrees_fahrenheit):
    degrees_celsius = (degrees_fahrenheit - 32) * 5/9
    print("The temperature is ", degrees_celsius)

def main():
    convert_temp(32)

if __name__ == "__main__":
    main()