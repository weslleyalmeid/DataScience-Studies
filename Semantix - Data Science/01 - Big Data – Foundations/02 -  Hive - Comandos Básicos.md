## Hive - Criação de Tabela Raw

1. Enviar o arquivo local “/input/exercises-data/populacaoLA/populacaoLA.csv” para o diretório no HDFS “/user/aluno/<nome>/data/populacao”

Acessar local do arquivo
```bash
docker-compose up -d
docker exec -it namenode bash 
```

Mover arquivo populacaoLA.csv
```bash
hdfs dfs -mkdir user/aluno/weslley/data/populacao
hdfs dfs -put input/exercises-data/populacaoLA/populacaoLA.csv user/aluno/weslley/data/populacao
hdfs dfs -ls user/aluno/weslley/data/populacao
hdfs dfs -cat user/aluno/weslley/data/populacao/populacaoLA.csv | head -n 3
```


2. Listar os bancos de dados no Hive
```bash
docker exec -it hive-server bash
beeline -u jdbc:hive2://localhost:10000
```

3. Criar o banco de dados <nome>

```bash
create database weslley;
```

4. Criar a Tabela Hive no BD <nome>

Tabela interna: pop
Campos:
zip_code - int,
total_population - int,
median_age - float,
total_males - int,
total_females - int,
total_households - int,
average_household_size - float
Propriedades
Delimitadores: Campo ‘,’ | Linha ‘\n’
Sem Partição
Tipo do arquivo: Texto
tblproperties("skip.header.line.count"="1")’


```bash
create table pop(
zip_code int,
total_population int,
median_age float,
total_males int,
total_females int,
total_households int,
average_household_size float
)
row format delimited
fields terminated by ','
lines terminated by '\n'
stored as textfile
tblproperties("skip.header.line.count"="1");

```

5. Visualizar a descrição da tabela pop
```bash
desc pop
desc formatted pop;
docker-compose stop
```


## Inserir Dados na Tabela Raw

1.Visualizar a descrição da tabela pop do banco de dados <nome>
```bash
docker exec -it hive-server bash
beeline -u jdbc:hive2://localhost:10000
```

2.Selecionar os 10 primeiros registros da tabela pop
```bash
select * from pop limit 10;
```

3.Carregar o arquivo do HDFS “/user/aluno/<nome>/data/população/populacaoLA.csv” para a tabela Hive pop
```bash
# acessando docker do HDFS
docker exec -it namenode bash 

# Verificando a existencia do arquivo
hdfs dfs -ls user/aluno/weslley/data/populacao

# acessando Hive
docker exec -it hive-server bash
beeline -u jdbc:hive2://localhost:10000
use weslley;
load data inpath 'user/aluno/weslley/data/populacao' overwrite into table pop;


```

4.Selecionar os 10 primeiros registros da tabela pop
```bash
select * from pop limit 10;
```

5.Contar a quantidade de registros da tabela pop
```bash
select count(*) from pop;
```
