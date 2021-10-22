## Exercícios - RDD

1. Ler com RDD os arquivos localmente do diretório “/opt/spark/logs/” ("file:///opt/spark/logs/")
```py
!ls /opt/spark/logs
!cat /opt/spark/logs/spark--org.apache.spark.deploy.master.Master-1-jupyter-notebook.out
```

2. Com uso de RDD faça as seguintes operações

a) Contar a quantidade de linhas
```py
log = sc.textFile("file:///opt/spark/logs")
log.count()
```

b) Visualizar a primeira linha
```py
log.first()
```

c) Visualizar todas as linhas
```py
log.collect()
```

d) Contar a quantidade de palavras
```py
# separar as palavras da linha

palavras = log.flatMap(lambda linha: linha.split(" "))
palavras.count()
```

e) Converter todas as palavras em minúsculas
```py
miniscula = palavras.map(lambda palavra: palavra.lower())
miniscula.first()
```

f) Remover as palavras de tamanho menor que 2
```py
minuscula_maior2 = miniscula.filter(lambda palavra: len(palavra) > 2)
minuscula_maior2.count()
```

g) Atribuir o valor de 1 para cada palavra
```py
palavra_1 = minuscula_maior2.map(lambda palavra: (palavra, 1))
palavra_1.first()
```

h) Contar as palavras com o mesmo nome
```py
# juntar as palavras

palavras_reduce = palavra_1.reduceByKey(lambda chave1, chave2: chave1 + chave2)
palavras_reduce.count()
```

i) Visualizar em ordem alfabética
```py
palavras_ordem = palavras_reduce.sortBy(lambda palavra: palavra[0], True)
palavras_ordem.collect()
```

j) Visualizar em ordem decrescente a quantidade de palavras
```py
palavras_ordem = palavras_reduce.sortBy(lambda palavra: palavra[1], False)
palavras_ordem.collect()
```

k) Remover as palavras, com a quantidade de palavras > 1
```py
palavras_ordem_filtro = palavras_ordem.filter(lambda palavra: palavra[1] > 1)
palavras_ordem_filtro.collect()
```

l) Salvar o RDD no diretorio do HDFS /user/<seu-nome>/logs_count_word
```py
palavras_ordem_filtro.saveAsTextFile("/user/weslley/logs_count_word")
!hdfs dfs -ls /user/weslley/logs_count_word
```