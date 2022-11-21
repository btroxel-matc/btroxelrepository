#!/usr/bin/env python3
#Author: Bryan Troxel
#Description: This is the client script for a server/client chat.

import socket

RHOST = 'localhost'
RPORT = 5000
SND_DATA = ""
RCV_DATA = ""

C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
C_SOCK.connect((RHOST, RPORT))
while SND_DATA != 'exit':
    SND_DATA = input("Please enter a value: ")
    C_SOCK.send(bytearray(SND_DATA,'utf8'))
    RCV_DATA = C_SOCK.recv(1024)
    print(RCV_DATA.decode())
C_SOCK.close()