import socket
import sys

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 7000        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'GET\n/index.html\nHTTP/1.1\nHost: 127.0.0.1\n\n')
    data = s.recv(1024)
    # sys.exit()

print('Received: ', repr(data))