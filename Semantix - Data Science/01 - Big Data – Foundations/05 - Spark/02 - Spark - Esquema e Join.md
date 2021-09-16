## Spark - Exercícios de Esquema e Join

1. Criar o DataFrame alunosDF para ler o arquivo no hdfs “/user/aluno/<nome>/data/escola/alunos.csv” sem usar as “option”
```bash
val alunosDF = spark.read.csv("user/aluno/weslley/data/escola/alunos.csv")
```

2. Visualizar o esquema do alunosDF
```bash
alunosDF.printSchema
```

3. Criar o DataFrame alunosDF para ler o arquivo “/user/aluno/<nome>/data/escola/alunos.csv” com a opção de Incluir o cabeçalho
```bash
val alunosDF = spark.read.option("header","true").csv("user/aluno/weslley/data/escola/alunos.csv")
```

4. Visualizar o esquema do alunosDF
```bash
alunosDF.printSchema
```

5. Criar o DataFrame alunosDF para ler o arquivo “/user/aluno/<nome>/data/escola/alunos.csv” com a opção de Incluir o cabeçalho e inferir o esquema
```bash
val alunosDF = spark.read.option("header","true").option("inferSchema","true").csv("user/aluno/weslley/data/escola/alunos.csv")
```

6. Visualizar o esquema do alunosDF
```bash
alunosDF.printSchema
```

7. Salvar o DaraFrame alunosDF como tabela Hive “tab_alunos” no banco de dados <nome>
```bash
alunosDF.write.saveAsTable("weslley.tab_alunos")

```

8. Criar o DataFrame cursosDF para ler o arquivo “/user/aluno/<nome>/data/escola/cursos.csv” com a opção de Incluir o cabeçalho e inferir o esquema
```bash
val cursosDF = spark.read.option("header","true").option("inferSchema","true").csv("user/aluno/weslley/data/escola/cursos.csv")

cursosDF.printSchema

```

9. Criar o DataFrame alunos_cursosDF com o inner join do alunosDF e cursosDF quando o id_curso dos 2 forem o mesmo
```bash
val alunos_cursosDF = alunosDF.join(cursosDF, "id_curso")
```

10. Visualizar os dados, o esquema e a quantidade de registros do alunos_cursosDF
```bash
alunos_cursosDF.show(10)
alunos_cursosDF.printSchema
alunos_cursosDF.count
```