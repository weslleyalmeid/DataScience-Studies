## Consulta básica em documentos

1. Mostrar todos os documentos da collection produto
```bash
docker container exec -it mongo bash
mongo
use weslley
show collections
db.produto.find({})

```
2. Pesquisar na collection produto, os documentos com os seguintes atributos:

a) Nome = mouse
```bash
db.produto.find({nome:"mouse"})
```

b) Quantidade = 20 e apresentar apenas o campo nome
```bash
db.produto.find({qtd:20}, {_id:0, nome:1})

```
c) Quantidade <= 20 e apresentar apenas os campos nome e qtd
```bash
db.produto.find({qtd:{$lte: 20}}, {nome:1, qtd:1})
```

d) Quantidade entre 10 e 20
```bash
db.produto.find({qtd:{$gte:10, $lte:20}}, {nome:1, qtd:1})
```

e) Conexão = USB e não apresentar o campo _id e qtd
```bash
db.produto.find({"descricao.conexao":"USB"}, {_id:0, qtd:0})

```

f) SO que contenha “Windows” ou “Windows 10”
```bash
db.produto.find({"descricao.so":{$in: ["Windows", "Windows 10"]}}).pretty()
```