# Atividade 1

O arquivo server.py é o lado passivo que recebe a mensagem e reenvia, e o client.py é o lado ativo que envia a mensagem e recebe uma mensagem do servidor(que no caso é a mesma enviada)

## Execução

Primeiramente inicie o servidor
```bash
$ python3 server.py
```
Em um novo terminal inicie o cliente
```bash
$ python3 client.py
> hello world
< hello world
> TESTE
< TESTE
> fim (to exit)
```
Para encerrar a execução basta digitar a string 'fim' no lado do cliente