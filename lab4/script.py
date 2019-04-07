import socket

host = "https://enu7uwfh93q3o.x.pipedream.net"
port = 8000

headers = """\
POST /auth HTTP/1.1\r
Content-Type: {content_type}\r
Content-Length: {content_length}\r
Host: {host}\r
Connection: close\r
\r\n"""

body = 'userName=Anton&password=pass'
body_bytes = body.encode('ascii')
header_bytes = headers.format(
    content_type="application/x-www-form-urlencoded",
    content_length=len(body_bytes),
    host=str(host) + ":" + str(port)
).encode('iso-8859-1')

payload = header_bytes + body_bytes


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.sendall(payload)


