#!/usr/bin/env python3
# Author: Bryan Troxel
# Description: This script covers importing created functions.

import f2c

x = input("Please enter the temperature in Fahrenheit: ")
f2c.convert_temp(int(x))