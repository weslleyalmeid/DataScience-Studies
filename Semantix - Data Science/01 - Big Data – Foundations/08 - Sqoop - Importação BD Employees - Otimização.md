## Sqoop - Importação BD Employees- Otimização

Realizar com uso do MySQL

1. Criar a tabela cp_titles_date, contendo a cópia da tabela titles com os campos title e to_date
```bash
# acessar database
docker exec -it database bash

# acessar mysql
mysql -psecret

use employees;


create table cp_titles_date select title, to_date from titles;
```

2. Pesquisar os 15 primeiros registros da tabela cp_titles_date
```bash
select * from cp_titles_date limit 15;
```

3. Alterar os registros do campo to_date para null da tabela cp_titles_date, quando o título for igual a Staff

Realizar com uso do Sqoop - Importações no warehouse /user/hive/warehouse/db_test_<numero_questao> e visualizar no HDFS
```bash
update cp_titles_date set to_date=NULL where title='Staff';
```

4. Importar a tabela titles com 8 mapeadores no formato parquet
```bash
docker exec -it namenode bash

# 8 mapeadores, formato parquet
sqoop import --table titles --connect jdbc:mysql://database/employees --username root --password secret -m 8 --as-parquetfile --warehouse-dir /user/hive/warehouse/db_test2_4

hdfs dfs -ls -h  /user/hive/warehouse/db_test2_4/titles
```

5. Importar a tabela titles com 8 mapeadores no formato parquet e compressão snappy
```bash

sqoop import --table titles --connect jdbc:mysql://database/employees --username root --password secret -m 8 --as-parquetfile --warehouse-dir /user/hive/warehouse/db_test2_5 --compress --compression-codec org.apache.hadoop.io.compress.SnappyCodec

hdfs dfs -ls -h  /user/hive/warehouse/db_test2_5/titles
```

6. Importar a tabela cp_titles_date com 4 mapeadores (erro)

```bash
sqoop import --table cp_titles_date --connect jdbc:mysql://database/employees --username root --password secret --warehouse-dir /user/hive/warehouse/db_test2_6
```
Importar a tabela cp_titles_date com 4 mapeadores divididos pelo campo título no warehouse /user/hive/warehouse/db_test2_title
```bash
sqoop import -Dorg.apache.sqoop.splitter.allow_text_splitter=true --table cp_titles_date --connect jdbc:mysql://database/employees --username root --password secret --warehouse-dir /user/hive/warehouse/db_test2_title --split-by title
```

Importar a tabela cp_titles_date com 4 mapeadores divididos pelo campo data no warehouse /user/hive/warehouse/db_test2_date
```bash
sqoop import -Dorg.apache.sqoop.splitter.allow_text_splitter=true --table cp_titles_date --connect jdbc:mysql://database/employees --username root --password secret --warehouse-dir /user/hive/warehouse/db_test2_date --split-by to_date

```
Qual a diferença dos registros nulos entre as duas importações?
```bash

hdfs dfs -count -h user/hive/warehouse/db_test2_title

hdfs dfs -ls -h -R /user/hive/warehouse/db_test2_title

hdfs dfs -count -h user/hive/warehouse/db_test2_date

hdfs dfs -ls -h -R /user/hive/warehouse/db_test2_date

hdfs dfs -cat /user/hive/warehouse/db_test2_title/cp_titles_date/part-m-00001 | head -n 5
```




