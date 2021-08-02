import socket

HOST = 'localhost'
PORT = 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((HOST, PORT))


while True:
    arquivo = input("Digite o nome do arquivo ou \"fim\" para finalizar: ")
    if arquivo == 'fim':
        break
    palavra = input("Digite a palavra que busca: ")

    msg = arquivo + " - " + palavra

    msgByte = str.encode(msg)
    sock.send(msgByte)
    print(str(sock.recv(1024), encoding='utf-8'))

sock.close()