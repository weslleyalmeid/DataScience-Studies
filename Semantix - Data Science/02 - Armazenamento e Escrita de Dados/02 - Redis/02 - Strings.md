## Strings

1. Criar a chave "usuario:nome" e atribua o valor do seu nome
```bash
docker container exec -it redis bash
redis-cli

SET usuario:nome Weslley
```

2. Criar a chave "usuario:sobrenome" e atribua o valor do seu sobrenome
```bash
SET usuario:sobrenome Almeida
```

3. Busque a chave "usuario:nome“
```bash
GET usuario:nome
```

4. Verificar o tamanho da chave "usuario:nome“
```bash
STRLEN usuario:nome
```

5. Verificar o tipo da chave "usuario:sobrenome"
```bash
TYPE usario:sobrenome
```

6. Criar a chave "views:qtd" e atribua o valor 100
```bash
SET views:qtd 100
```

7. Incremente o valor em 10 da chave "views:qtd"
```bash
INCRBY views:qtd 10
```

8. Busque a chave "views:qtd"
```bash
ET views:qtd
```

9. Deletar a chave "usuario:sobrenome"
```bash
DEL usuario:sobrenome
```

10. Verificar se a chave "usuario:sobrenome" existe
```bash
EXISTS usuario:sobrenome
```

11. Definir um tempo de 3600 segundos para a chave "views:qtd" ser removida
```bash
EXPIRE views:qtd 3600
```

12. Verificar quanto tempo falta para a chave "views:qtd" ser removida
```bash
TTL views:qtd
```

13. Verificar a persistência da chave "usuario:nome"
```bash
TTL usuario:nome
```

14. Definir para a chave "views:qtd" ter persistência para sempre
```bash
PERSIST views:qtd
```