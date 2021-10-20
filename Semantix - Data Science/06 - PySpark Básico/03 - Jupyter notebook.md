## Correção do Exercício de Testar o Jupyter Notebook

1. Criar o arquivo do notebook com o nome teste_spark.ipynb
```jupyter
```

2. Obter as informações da sessão de spark (spark)
```jupyter
spark
```

3. Obter as informações do contexto do spark (sc)
```jupyter
sc
```

4. Setar o log como INFO.
```jupyter
spark.sparkContext.setLogLevel("INFO")
```

5. Visualizar todos os banco de dados com o catalog
```jupyter
spark.catalog.listDatabases()
```

6. Ler os dados "hdfs://namenode:8020/user/rodrigo/data/juros_selic/juros_selic.json" com uso de Dataframe
```jupyter
leitura_juros = spark.read.json("hdfs:///user/weslley/data/juros_selic/juros_selic.json")
leitura_juros.show(5)
```

7. Salvar o Dataframe como juros no formato de tabela Hive
```jupyter
leitura_juros.write.saveAsTable("juros")
```

8. Visualizar todas as tabelas com o catalog
```jupyter
spark.catalog.listTables()
```

9. Visualizar no hdfs o formato e compressão que está a tabela juros do Hive
```jupyter
!hdfs dfs -ls /user/hive/warehouse
```

10. Ler e visualizar os dados da tabela juros, com uso de Dataframe no formato de Tabela Hive
```jupyter

```

11. Ler e visualizar os dados da tabela juros , com uso de Dataframe no formato Parquet
```jupyter
```