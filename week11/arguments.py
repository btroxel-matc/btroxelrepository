#!/usr/bin/env python3
#Author: Bryan Troxel
#Description: This lab covers the use of Argparse in Python.

import argparse

import sys

parser = argparse.ArgumentParser(description="This is Bryan Troxel's Script")

parser.add_argument('-m', dest='basic', type=str, help='Enter some text')
parser.add_argument('-i', '--integer', metavar='[an integer]', dest='[an integer]', required=True, type=int, help='Enter a simple Integer.')
parser.add_argument('-d', '--float', metavar='[a float]', dest='[a float]', type=float, help='Enter a simple float.')
parser.add_argument('-s', '--string', metavar='[a string]', dest='[a string]', type=str, help='Enter a simple string.')
parser.add_argument('-l', metavar='[strings] [[strings] ...]', dest='[strings] [[strings] ...]', action='append', nargs='+', help='Enter a list of strings (space delimited)')
parser.add_argument('-t', '--set-true', dest='falsetrue', default=False, action='store_true', help='Toggle from default False to True.')
parser.add_argument('-f', '--setfalse', dest='truefalse', default=True, action='store_false', help='Toggle from default True to False.')
parser.add_argument('-v', '--version', dest='version', action='version', version='%(prog)s 2.5', help="Show program's version number and exit.")

if len(sys.argv) == 1:
    print(parser.print_help())
else:
    arguments = parser.parse_args()
    print(arguments)