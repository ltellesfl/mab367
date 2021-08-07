# Atividade 2

## Execução

Primeiramente inicie o servidor
```bash
$ python3 server.py
```
Em um novo terminal inicie o cliente
```bash
$ python3 client.py
> Digite o nome do arquivo ou "fim" para finalizar: exemplo.txt
> Digite a palavra que busca: verde

< A palavra verde se repete 5 vezes.
```
Caso o arquivo requerido não seja encontrado ou tenha algum problema para ser lido será retornado uma mensagem de erro.

```bash
$ python3 client.py
> Digite o nome do arquivo ou "fim" para finalizar: aaaa.txt
> Digite a palavra que busca: verde

< Erro ao abrir o arquivo 'aaaa.txt'
```

Agora o server suporta várias conexões simultaneas. Como pedido no enunciado. E também temos a interação para finalizar o servidor, onde ele aguarda todos os clientes encerrarem para encerrar também. Não aceitando mais conexões após o pedido de encerramento.

```bash
$ python3 server.py
< Pronto para receber conexoes...
< Conectado com:  ('127.0.0.1', 47246)
< Conectado com:  ('127.0.0.1', 47250)
< ('127.0.0.1', 47250)-> encerrou
< ('127.0.0.1', 47246)-> encerrou
> fim
```

