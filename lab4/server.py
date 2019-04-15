import socket
import sys
import time

HOST = ''
PORT = 7000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('# Socket created')

# Create socket on port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print('# Bind failed. ')
    sys.exit()

print('# Socket bind complete')

# Start listening on socket
s.listen(10)
print('# Socket now listening')

# Wait for client
conn, addr = s.accept()
print('# Connected to ' + addr[0] + ':' + str(addr[1]))

# Receive data from client
while True:
    data = conn.recv(1024)
    if not data:
        break
    line = data.decode('UTF-8')
    line = line.replace("\n"," ")
    request_method = line.split(' ')[0]
    response = ''
    response_data = ''
    file_requested = ''
    response_code = ''

    if request_method == 'GET':
        file_requested = line.split(' ')[1]

        if file_requested == "/index.html":
            response_data = b"<html><body><h1>Welcome!</h1></body></html>"
            response_code = 200
        else:
            print("File not found. Serving 404 page.")
            response_data = b"<html><body><h1>Error 404: File not found</h1></body></html>"
            response_code = 404
        filepath_to_serve = ".../{f}.".format(f=file_requested)
        print("Serving web page [{fp}]".format(fp=filepath_to_serve))

        response = response_data

        header = ''
        if response_code == 200:
            header += 'HTTP/1.1 200 OK\n'
        elif response_code == 404:
            header += 'HTTP/1.1 404 Not Found\n'

        time_now = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())

        header += 'Date: {now}\n'.format(now=time_now)
        header += 'Server: Simple-Python-Server\n'
        header += 'Connection: close\n\n'  # Signal that connection will be closed after completing the request

        response_header = header.encode() + response

        conn.send(response_header)

    else:
        print("Unknown HTTP request method: {method}".format(method=request_method))
        conn.send(b'Unknown HTTP request method')

    print("Method: {m}".format(m=request_method))
    print( line )
s.close()
