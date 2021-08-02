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

