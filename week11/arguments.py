#!/usr/bin/env python3
#Author: Bryan Troxel
#Description: This lab covers the use of Argparse in Python.

import argparse

import sys

parser = argparse.ArgumentParser(description="This is Bryan Troxel's Script")

parser.add_argument('-m', dest='basic', type=str, help='Enter some text')
parser.add_argument('-i', '--integer', metavar='[an integer]', dest='varinteger', required=True, type=int, help='<required> Enter a simple Integer.')
parser.add_argument('-d', '--float', metavar='[a float]', dest='varfloat', type=float, help='Enter a simple float.')
parser.add_argument('-s', '--string', metavar='[a string]', dest='varstring', type=str, help='Enter a simple string.')
parser.add_argument('-l', metavar='[strings]', dest='varlist', type=str, nargs='+', help='Enter a list of strings (space delimited)')
parser.add_argument('-t', '--set-true', dest='falsetrue', default=False, action='store_true', help='Toggle from default False to True.')
parser.add_argument('-f', '--setfalse', dest='truefalse', default=True, action='store_false', help='Toggle from default True to False.')
parser.add_argument('-v', '--version', dest='version', action='version', version='%(prog)s 2.5', help="Show program's version number and exit.")

args = parser.parse_args()

print(type(args.varinteger),args.varinteger)
print(type(args.varlist),args.varlist)
print(type(args.varstring),args.varstring)
print(type(args.varfloat),args.varfloat)