
import socket
import re

request = b"GET / HTTP/1.1\nHost\n\n"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

address = input("Enter address:  ")
choice = input("1 if you want HEADER; 2 if you want BODY")

s.connect(("{address}".format(address=address), 80))

#s.connect(("www.google.com", 80))

s.send(request)

while 1:
    buf = s.recv(10000)
    if not buf:
        break
    new_buf = buf.decode('utf-8')
    header = re.match("(.*?)<!doctype", str(new_buf), re.DOTALL)
    body = re.search("<!doctype.*", str(new_buf), re.DOTALL)
    # print(str(new_buf))
    print("==================")
    if choice == '1':
        print(header.group(0))
    if choice == '2':
        print(body.group(0))
    break

s.close()