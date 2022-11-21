#!/usr/bin/env python3
#Author: Bryan Troxel
#Description: This is the server script for a client/server file transfer.

import socket

LHOST = ''
LPORT = 5000
RCV_DATA = ''
FTFILE = open('ftransferserver.txt','w')
L_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
L_SOCK.bind((LHOST, LPORT))

while 1:
    L_SOCK.listen(1)
    L_CONN, L_ADDR = L_SOCK.accept()
    while 1:
        RCV_DATA = L_CONN.recv(1024).decode()
        FTFILE.write(RCV_DATA)
        print(RCV_DATA)
        break
    break
L_SOCK.close()
FTFILE.close()