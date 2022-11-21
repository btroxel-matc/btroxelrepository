#!/usr/bin/env python3
#Author: Bryan Troxel
#Description: This is the client script for a server/client file transfer.

import socket

RHOST = 'localhost'
RPORT = 5000
ftr = open('ftransfer.txt', 'r')
SND_DATA = ftr.read()

C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
C_SOCK.connect((RHOST, RPORT))
C_SOCK.send(bytearray(SND_DATA,'utf8'))
ftr.close()
C_SOCK.close()