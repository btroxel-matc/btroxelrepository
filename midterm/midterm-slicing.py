#!/usr/bin/env python3

#Author: Bryan Troxel
#Description: Midterm Activity 3: This activity reads a file into a list and uses slicing.

print("Name: Bryan Troxel")
slco = open("slicing-file.txt", "r")
slc = slco.readlines()
vara=slc[-3:-2:1]
varb=slc[2:5:1]
varc=slc[-10:-15:-2]
vard=slc[10:13:1]
vare=slc[-19:-22:-1]
vara = ''.join(vara)
vara = vara.replace("\n", " ")
varb = ''.join(varb)
varb = varb.replace("\n", " ")
varc = ''.join(varc)
varc = varc.replace("\n", " ")
vard = ''.join(vard)
vard = vard.replace("\n", " ")
vare = ''.join(vare)
vare = vare.replace("\n", " ")
quote=(f'"{vara+varb+varc+vard+vare}"')
print(quote)