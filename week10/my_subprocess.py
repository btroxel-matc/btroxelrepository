#!/usr/bin/env python3
#Author: Bryan Troxel
#Description: This lab covers Subprocesses.

import subprocess

myProc=subprocess.run(['ps','-axco','command'],stdout=subprocess.PIPE)
myProcString=myProc.stdout.decode()
myProcList=myProcString.split('\n')

for line in myProcList:
    print(line)

print(f"{len(myProcList[1::])}")