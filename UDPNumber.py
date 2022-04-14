import socket
host = "0.0.0.0"
port = 10240
BUFF_SIZE = 128

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (host, port)
sock.bind(server_address)
print(sock)

while True:

    print("wating for request...")
    message, client_address = sock.recvfrom(BUFF_SIZE)
    print("echo request from {} port {}".format(client_address[0], client_address[1]))
    print("echo message : {}".format(message.decode()))
    data = message.decode()
    try:
        num = int(data)
        if num % 2:
            answer ="홀수  입니다."
        else:
            answer = "짝수입니다."
    except ValueError:
            answer = "숫자가아닙니다."

    sock.sendto(answer.encode(), client_address)

sock.close()
