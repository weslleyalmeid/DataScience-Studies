## Spark - Exercícios de DataFrame

1. Enviar o diretório local “/input/exercises-data/juros_selic” para o HDFS em “/user/aluno/<nome>/data”
```bash
docker exec -it namenode bash

hdfs dfs -put /input/exercises-data/juros_selic/ /user/aluno/weslley/data
hdfs dfs -ls /user/aluno/weslley/data
```

2. Criar o DataFrame jurosDF para ler o arquivo no HDFS “/user/aluno/<nome>/data/juros_selic/juros_selic.json”
```bash
docker exec -it spark bash
spark-shell
val jurosDF = spark.read.json("/user/aluno/weslley/data/juros_selic/juros_selic.json")


```

3. Visualizar o Schema do jurosDF
```bash
jurosDF.printSchema
```

4. Mostrar os 5 primeiros registros do jutosDF
```bash
jurosDF.show(5)

# mostra valores completo do campo
jurosDF.show(5, false)
```

5. Contar a quantidade de registros do jurosDF
```bash
jurosDF.count
```

6. Criar o DataFrame jurosDF10 para filtrar apenas os registros com o campo “valor” maior que 10
```bash
val jurosDF10 = jurosDF.where("valor > 10")
```

7. Salvar o DataFrame jurosDF10  como tabela Hive “<nome>.tab_juros_selic”
```bash
jurosDF10.write.saveAsTable("weslley.tab_juros_selic")
```

8. Criar o DataFrame jurosHiveDF para ler a tabela “<nome>.tab_juros_selic”
```bash
val jurosHiveDF = spark.read.table("weslley.tab_juros_selic")
```

9. Visualizar o Schema do jurosHiveDF
```bash
jurosHiveDF.printSchema
```

10. Mostrar os 5 primeiros registros do jurosHiveDF
```bash
jurosHiveDF.show(5)
```

11. Salvar o DataFrame jurosHiveDF no HDFS no diretório “/user/aluno/nome/data/save_juros” no formato parquet
```bash
# save default parquet
jurosHiveDF.write.parquet("/user/aluno/weslley/data/save_juros")
jurosHiveDF.write.save("/user/aluno/weslley/data/save_juros")

```

12. Visualizar o save_juros no HDFS
```bash
docker exec -it namenode bash
hdfs dfs -ls /user/aluno/weslley/data/save_juros
```

13. Criar o DataFrame jurosHDFS para ler o diretório do “save_juros” da questão 8
```bash
docker exec -it spark bash
spark-shell

# load default parquet
val jurosHDFS = spark.read.parquet("/user/aluno/weslley/data/save_juros")
val jurosHDFS = spark.read.load("/user/aluno/weslley/data/save_juros")

```

14. Visualizar o Schema do jurosHDFS
```bash
jurosHDFS.printSchema
```

15. Mostrar os 5 primeiros registros do jurosHDFS
```bash
jurosHDFS.show(5)
```