import socket
import sys

s = socket.socket()
host = socket.gethostname()
print(" server will start on host : ", host)
port = 3000
s.bind((host,port))
name = input("Please enter your username: \n")
print("Server is waiting for incoming connections\n")
s.listen(1)
conn, addr = s.accept()
print("Received connection\n")
s_name = conn.recv(1024)
s_name = s_name.decode()
print(s_name, "has joined the chat room")
conn.send(name.encode())

while True:
    message = input(str("Please enter your message: "))
    conn.send(message.encode())
    print("Sent\n")
    message = conn.recv(1024)
    message = message.decode()
    print(f"{s_name}: {message}\n")
