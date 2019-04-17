import socket
import sys

s = socket.socket()
host = socket.gethostname()
# host = input("Please enter the hostname of the server : ")
port = 3000
s.connect((host, port))
name = input("Please enter your username : \n")
print(" Connected to chat server\n")

s.send(name.encode())
s_name = s.recv(1024)
s_name = s_name.decode()
print(s_name, "has joined the chat room ")

while True:
    message = s.recv(1024)
    message = message.decode()
    print(f"{s_name}: {message}\n")
    message = input("Please enter your message: ")
    message = message.encode()
    s.send(message)
    print("Sent\n")