## Spark - Exercícios de SQL Queries vs Operações de DataFrame

Realizar as seguintes consultas usando SQL queries e transformações de DataFrame na tabela “tab_alunos” no banco de dados <nome>

1. Visualizar o id e nome dos 5 primeiros registros
```bash
spark.sql("select id_discente, nome from tab_alunos limit 5").show

# vantagem de armazenar em um datagrame, para facilitar a aplicação de métodos seguintes.
val alunosHiveDF = spark.read.table("tab_alunos")
alunosHiveDF.select("id_discente", "nome").limit(5).show
```

2. Visualizar o id, nome e ano quando o ano de ingresso for maior ou igual a 2018
```bash
spark.sql("select id_discente, nome, ano_ingresso from tab_alunos where ano_ingresso >= 2018").show

alunosHiveDF.select("id_discente", "nome", "ano_ingresso").where("ano_ingresso>=2018").show
```

3. Visualizar por ordem alfabética do nome o id, nome e ano quando o ano de ingresso for maior ou igual a 2018
```bash
spark.sql("select id_discente, nome, ano_ingresso from tab_alunos where ano_ingresso >= 2018 order by nome desc").show

alunosHiveDF.select("id_discente", "nome", "ano_ingresso").where("ano_ingresso>=2018").orderBy($"nome".desc).show
alunosHiveDF.select("id_discente", "nome", "ano_ingresso").where("ano_ingresso>=2018").orderBy(alunosHiveDF("nome").desc).show

```

4. Contar a quantidade de registros do item anterior
```bash
spark.sql("select count(id_discente) from tab_alunos where ano_ingresso >= 2018").show

alunosHiveDF.select("id_discente", "nome", "ano_ingresso").where("ano_ingresso>=2018").orderBy(alunosHiveDF("nome").desc).count
```