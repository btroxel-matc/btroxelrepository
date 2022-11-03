#!/usr/bin/env python3
# Author: Bryan Troxel
# Description: This script covers importing created functions.

import f2c

def main():
    x = input("Please enter the temperature in Fahrenheit: ")
    print(f"The temperature in Celsius is: {f2c.convert_temp(int(x))}")
    
if __name__ == "__main__":
    main()