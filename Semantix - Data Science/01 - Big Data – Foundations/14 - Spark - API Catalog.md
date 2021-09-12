## Spark - Exercícios da API Catalog

Realizar os exercícios usando a API Catalog.

1. Visualizar todos os banco de dados
```bash
spark.catalog.listDatabases.show(false)
```

2. Definir o banco de dados “seu-nome” como principal
```bash
spark.catalog.setCurrentDatabase("weslley")
```

3. Visualizar todas as tabelas do banco de dados “seu-nome”
```bash
spark.catalog.listTables.show
```

4. Visualizar as colunas da tabela tab_alunos
```bash
spark.catalog.listColumns("tab_alunos").show
```

5.  Visualizar os 10 primeiros registos da tabela "tab_alunos" com uso do spark.sql
```bash
spark.read.table("tab_alunos").show(10)
spark.sql("select * from tab_alunos limit 10").show()
```

## Nota
Um dataset é mais rápido que um dataframe, pois, o dataset tem um schema associado.