import socket

HOST = 'localhost'
PORT = 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((HOST, PORT))

while True:
    msg = input()
    if msg == 'fim':
        break
    msgByte = str.encode(msg)
    sock.send(msgByte)
    print(str(sock.recv(1024), encoding='utf-8'))

sock.close()