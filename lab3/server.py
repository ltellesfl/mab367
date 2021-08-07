import socket
import select
import sys
import threading

HOST = ''
PORT = 8080

conexoes = {}
entradas = [sys.stdin]

def iniciaServidor():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    sock.bind((HOST, PORT))
    sock.listen(5)
    sock.setblocking(False)
    return sock

def aceitaConexao(sock):
    clisock, endr = sock.accept()
    return clisock, endr

def atendeRequisicoes(clisock, endr):
    while True:
        rcv = clisock.recv(1024)
        if not rcv: 
            print(str(endr) + '-> encerrou')
            clisock.close()
            return

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
        clisock.send(msgByte)

def main():
    sock = iniciaServidor()
    print('Pronto para receber conexoes...')
    entradas.append(sock)
    clientes = []
    while True:
        r, w, e = select.select(entradas, [], [])
        for pronto in r:
            if pronto == sock:
                clisock, endr = aceitaConexao(sock)
                print('Conectado com: ', endr)
                clisock.setblocking(True)

                cliente = threading.Thread(target=atendeRequisicoes, args=(clisock, endr))
                cliente.start()
                clientes.append(cliente)

            elif pronto == sys.stdin:
                cmd = input()
                if cmd == 'fim':
                    for c in clientes:
                        c.join()
                    sock.close()
                    sys.exit()

        
main()
