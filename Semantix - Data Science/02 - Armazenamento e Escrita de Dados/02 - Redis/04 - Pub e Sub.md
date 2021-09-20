## Pub/Sub

1. Criar um assinante para receber as mensagens do canal noticias:sp
```bash
subscribe noticias:sp

```

2. Criar um editor para enviar as seguintes mensagens no canal noticias:sp
Msg 1
Msg 2
Msg 3

**Novo terminal**
```bash
publish noticias:sp 'Msg 1'
publish noticias:sp 'Msg 2'
publish noticias:sp 'Msg 3'
```


3. Cancelar o assinante do canal noticias:sp
```bash
ctrl + c

```

4. Criar um assinante para receber as mensagens dos canais com o padrão noticias:*
```bash
redis-cli
psubscribe noticias:*
```

5. Criar um editor para enviar as seguintes mensagens no canal noticias:rj
Msg 4
Msg 5
Msg 6
```bash
publish noticias:rj 'Msg 4'
publish noticias:rj 'Msg 5'
publish noticias:rj 'Msg 6'
```