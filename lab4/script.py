# import socket
#
# headers = """\
# POST /auth HTTP/1.1\r
# Content-Type: {content_type}\r
# Content-Length: {content_length}\r
# Host: www.google.com\r
# Connection: close\r
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r
# Accept-Language: en-US,en;q=0.5\r
# Accept-Encoding: gzip, deflate\r
# Referer: http://google.com\r
# \r\n"""
#
# body = 'userName=Anton&password=pass'
# body_bytes = body.encode('ascii')
# header_bytes = headers.format(
#     content_type="application/x-www-form-urlencoded",
#     content_length=len(body_bytes),
#     host="www.google.com" + ":" + "port"
# ).encode('iso-8859-1')
#
# payload = header_bytes + body_bytes
#
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(("www.google.com", 80))
# s.sendall(payload)
# s.close()

import sys
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ipaddr = socket.gethostbyname( 'google.com' )
s.connect((ipaddr,80))

data = "username=test&pass=blah\n\n"

header = ( """
POST / HTTP/1.1
Host: google.com
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://google.com
Cookie: PHPSESSID=blub
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
""" )

contentLength = "Content-Length: " + str( len( data ) ) + "\n\n"
request = (header.encode('iso-8859-1') + contentLength.encode('ascii') + data.encode('ascii'))
s.send(request)
response = s.recv(4096)
s.close()
print(request)
print('--------------------------------------------------------------------------')
print(response)
sys.exit(0)