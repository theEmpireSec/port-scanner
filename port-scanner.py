import socket
import threading
import os
import sys
os.system('clear')

print ('		______          _                                              ')
print ('		| ___ \        | |                                             ')
print ('		| |_/ /__  _ __| |_ ______ ___  ___ __ _ _ __  _ __   ___ _ __ ')
print ("		|  __/ _ \| '__| __|______/ __|/ __/ _` | '_ \| '_ \ / _ \ '__|")
print ('		| | | (_) | |  | |_       \__ \ (_| (_| | | | | | | |  __/ |   ')
print ('		\_|  \___/|_|   \__|      |___/\___\__,_|_| |_|_| |_|\___|_|   ')
print ('-'*80)
print (' Author    ≥ King')
print (' Instagram ≥ @the.empiresec')
print (' GitHub    ≥ https://github.com/theEmpireSec')
print ('-'*80)
usage='Usage: python3 port-scanner.py <target> <start-port> <end-port>'
if len(sys.argv) != 4:
	print(usage)
	sys.exit()
print('Scaning target >',sys.argv[1])
try:
	host = sys.argv[1]
except socket.gaierror:
	print('Name resolution err')
	sys.exit()
start_port=int(sys.argv[2])
end_port=int(sys.argv[3])
def scan(port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(2)
	if s.connect_ex((host,port)):
		pass
	else:
		print(port,'> open')

for port in range(start_port,end_port+1):
	thread=threading.Thread(target=scan,args=(port,))
	thread.start()
