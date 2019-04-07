
import socket

request = b"GET / HTTP/1.1\nHost: www.google.com\n\n"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("www.google.com", 80))


s.send(request)

while 1:
    buf = s.recv(1000)
    if not buf:
        break
    print(buf)

s.close()