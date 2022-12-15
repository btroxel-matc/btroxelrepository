#!/usr/bin/env python3
#Author: Bryan Troxel
#Description: This is the final exam for Python which covers a variety of concepts throughout the semester. The first function "get_response" brings back the HTML text on the webpage. Function number two is named "parse_string" and takes in the URL
# as well, but uses beautiful soup to sift and slice through a hidden message. The third function named "parse_header" takes in the URL and searches through the HTTP and brings back the header. Function four is named "parse_json" and uses JSON to sort through a list of dictionaries.
# The final function "socket_client" takes in only the server to perform a port scan, send a message to the server on the open port, and append the port number to the message sent back from the server.

import argparse, sys, requests, bs4, json, socket


#Function 1
def get_response():
    response = requests.get(URL)
    return (response.text)

#Function 2
def parse_string():
    response=requests.get(URL)
    response.raise_for_status
    soup = bs4.BeautifulSoup(response.text,'html.parser')
    head = soup.select_one('h3')
    cut = head.get_text('h3')
    end = (f"{cut[2::3]} Bryan")
    return (end)

#Function 3
def parse_header():
    response = requests.get(URL)
    head= (response.headers['FALL2022-HEADER'])
    return (head)

#Function 4
def parse_json():
    response = requests.get(URL)
    jsonDict = json.loads(response.text)
    for item in jsonDict['Music And Books']:
        if 'The Shining' == item['title']:
            out = item['publish_info']['publish_year']
    return (out)


#Function 5
def socket_client():
    RHOST = (args.varserver)
    RPORTS = range(6100,6200)
    SND_DATA = b"Bryan Troxel"
    RCV_DATA = ""
    myTimeout = 2

    for RPORT in RPORTS:
        C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        C_SOCK.settimeout(myTimeout)
        try:    
            C_SOCK.connect((RHOST,RPORT))
            C_SOCK.send(SND_DATA)
            RCV_DATA = C_SOCK.recv(1024)
            C_SOCK.close()
            PORT = (f"{RCV_DATA.decode()} Port: {RPORT}")
        except socket.error as e:
            C_SOCK.close()
    return (PORT)

finalarg = argparse.ArgumentParser(description="")

finalarg.add_argument('-s', '--server', metavar='[server]', dest='varserver', type=str, required=True, help='<required> Enter a server name.')
finalarg.add_argument('-q', '--question', metavar='[question]', dest='varquestion', type=int, required=True, help= '<required> Enter an integer between 1 and 5')

args=finalarg.parse_args()

URL=(f"http://{args.varserver}/q{args.varquestion}")

print(f"Name: Bryan Troxel")
print(f"{URL}")
if args.varquestion == 1:
    print(f"ANSWER: {get_response()}")
if args.varquestion == 2:
    print(f"ANSWER: {parse_string()}")
if args.varquestion == 3:
    print(f"ANSWER:{parse_header()}")
if args.varquestion == 4:
    print(f"ANSWER: {parse_json()}")
if args.varquestion == 5:
    print(f"ANSWER: {socket_client()}")