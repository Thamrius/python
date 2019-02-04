#!/usr/bin/python

import socket
import sys

if len(sys.argv) !=2:
	print "Usage: vrfy.py <text file>"
	sys.exit(0)

filepath = sys.argv[1]
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 	# Create a Socket
#change hostname to address you want to test
connect = s.connect(('127.0.0.1',25))			# Connect to the Server
banner = s.recv(1024)					# Receive the banner
print banner

with open(filepath) as fp:
	line = fp.readline()
	cnt = 1
	while line:		
		s.send('VRFY ' + line)		 	#VRFY a user
		result=s.recv(1024)
		print result
		line = fp.readline()
		cnt += 1
s.close()	
