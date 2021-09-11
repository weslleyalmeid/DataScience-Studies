## Hive - Criação de Tabela Particionada

1. Criar o diretório “/user/aluno/<nome>/data/nascimento” no HDFS
```
docker-compose up -d
docker exec -it namenode hdfs dfs -ls /
docker exec -it namenode hdfs dfs -mkdir user/aluno/weslley/data/nascimento

```

2. Criar e usar o Banco de dados <nome>
```
docker exec -it hive-server bash
beeline -u jdbc:hive2://localhost:10000
show databases;
use weslley;
show tables;
```

3. Criar uma tabela externa no Hive com os parâmetros:

a) Tabela: nascimento

b) Campos: nome (String), sexo (String) e frequencia (int)

c) Partição: ano

d) Delimitadores:

i) Campo ‘,’

ii)  Linha ‘\n’

e) Salvar

i) Tipo do arquivo: texto

ii) HDFS: '/user/aluno/<nome>/data/nascimento’

```
create external table nascimento(
nome string,
sexo string,
frequencia int
)
partitioned by (ano int)
row format delimited
fields terminated by ','
lines terminated by '\n'
stored as textfile
location '/user/aluno/weslley/data/nascimento';

```


4.Adicionar partição ano=2015
```
alter table nascimento add partition(ano=2015);
```

5.Enviar o arquivo local “input/exercises-data/names/yob2015.txt” para o HDFS no diretório /user/aluno/<nome>/data/nascimento/ano=2015
```
hdfs dfs -put /input/exercises-data/names/yob2015.txt /user/aluno/weslley/data/nascimento/ano=2015
```

6.Selecionar os 10 primeiros registros da tabela nascimento no Hive
```
select * from nascimento limit 10;
```

7.Repita o processo do 4 ao 6 para os anos de 2016 e 2017.

```
-- docker Hive
alter table nascimento add partition(ano=2016);
alter table nascimento add partition(ano=2017);

select * from nascimento where ano=2016 limit 10;
select * from nascimento where ano=2017 limit 10;

-- docker HDFS
hdfs dfs -put /input/exercises-data/names/yob2016.txt /user/aluno/weslley/data/nascimento/ano=2016
hdfs dfs -put /input/exercises-data/names/yob2017.txt /user/aluno/weslley/data/nascimento/ano=2017

```
A lógica de particionamento, é realizar a partição com base nas consultas mais utilizadas no comando where.