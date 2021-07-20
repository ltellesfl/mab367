import socket

HOST = ''
PORT = 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind((HOST, PORT))
sock.listen(1)

novoSock, endereco = sock.accept()

while True:
    msg = novoSock.recv(1024)
    if not msg: break
    novoSock.send(msg)

novoSock.close()
sock.close()
