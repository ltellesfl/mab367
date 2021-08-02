import socket

HOST = ''
PORT = 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind((HOST, PORT))
sock.listen(1)

while True: # como pedido no enunciado deixando o servidor em loop infinito
    novoSock, endereco = sock.accept()

    while True:
        rcv = novoSock.recv(1024)
        if not rcv: break

        msg = str(rcv, encoding='utf-8').split(" - ")
        arquivo = msg[0]
        palavra = msg[1]

        try:
            with open(arquivo) as f:
                quantidade = f.read().count(palavra)
            msgRetorno = "\nA palavra " + palavra + " se repete " + str(quantidade) + " vezes.\n"
        except Exception:
            msgRetorno = "\nErro ao abrir o arquivo '" + arquivo + "'\n"
        
        msgByte = str.encode(msgRetorno)
        novoSock.send(msgByte)

    novoSock.close()
sock.close() # nunca será fechado até ser implementado como será finalizado o servidor

