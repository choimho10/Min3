#!/usr/bin/python3
import socket

host = ''
port = 10241
BUFF_SIZE = 128
BACKLOG = 5

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = (host, port)
sock.bind(server_address)

sock.listen(BACKLOG)

while True:
    print("wating for request...")
    data_sock, address = sock.accept()
    print("{}".format(address[1]))
    print("echo request from {} port {}".format(address[0], address[1]))
    message = data_sock.recv(BUFF_SIZE)
    #message = message.decode()
    if message:
        server_respone = "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/html\r\n\r\n "
        "<HTML><BODY>"
        "<H1> Hello, World! </H1>"
        "</BODY></HTML>"
        data_sock.sendall(server_respone.encode())

    data_sock.close()
