## Sqoop - Importação BD Sakila – Carga Incremental

Realizar com uso do MySQL

1. Criar a tabela cp_rental_append, contendo a cópia da tabela rental com os campos rental_id e rental_date
```bash
docker exec -it database bash
mysql -psecret
use sakila
create table cp_rental_append select rental_id, rental_date from rental;

```


2 .Criar a tabela cp_rental_id e cp_rental_date, contendo a cópia da tabela cp_rental_append
```bash
create table cp_rental_id select * from cp_rental_append;
create table cp_rental_date select * from cp_rental_append;
```
 

Realizar com uso do Sqoop - Importações no warehouse /user/hive/warehouse/db_test3 e visualizar no HDFS

3. Importar as tabelas cp_rental_append, cp_rental_id e cp_rental_date com 1 mapeador
```bash
docker exec -it namenode bash

sqoop import --connect jdbc:mysql://database/sakila --username root --password secret --warehouse-dir /user/hive/warehouse/db_test3  -m 1 --table cp_rental_append

sqoop import --connect jdbc:mysql://database/sakila --username root --password secret --warehouse-dir /user/hive/warehouse/db_test3  -m 1 --table cp_rental_id

sqoop import --connect jdbc:mysql://database/sakila --username root --password secret --warehouse-dir /user/hive/warehouse/db_test3  -m 1 --table cp_rental_date

hdfs dfs -ls -h -R /user/hive/warehouse/db_test3
```
 

Realizar com uso do MySQL

4. Executar o sql /db-sql/sakila/insert_rental.sql no container do database
```
$ docker exec -it database bash

$ cd /db-sql/sakila
$ apt-get update
$ apt-get install apt-file
$ apt-file update
$ apt-get install vim
$ vim insert_rental.sql 
"alterar o nome dos order by no final para retal_date e rental_id"
$ mysql -psecret < insert_rental.sql
```

Realizar com uso do Sqoop - Importações no warehouse /user/hive/warehouse/db_test3 e visualizar no HDFS

5. Atualizar a tabela cp_rental_append no HDFS anexando os novos arquivos
```bash
sqoop import --connect jdbc:mysql://database/sakila --username root --password secret --warehouse-dir /user/hive/warehouse/db_test3  -m 1 --table cp_rental_append --append 
```

6. Atualizar a tabela cp_rental_id no HDFS de acordo com o último registro de rental_id, adicionando apenas os novos dados.
```bash
sqoop eval --connect jdbc:mysql://database/sakila --username root --password secret --query "select * from cp_rental_append order by rental_id desc limit 5 "

sqoop import --table cp_rental_id --connect jdbc:mysql://database/sakila --username root --password secret --warehouse-dir /user/hive/warehouse/db_test3  -m 1  --incremental append --check-column rental_id --last-value 16049

```

7. Atualizar a tabela cp_rental_date no HDFS de acordo com o último registro de rental_date, atualizando os registros a partir desta data.

```bash
sqoop import --table cp_rental_date --connect jdbc:mysql://database/sakila --username root --password secret --warehouse-dir /user/hive/warehouse/db_test3  -m 1  --incremental lastmodified --merge-key rental_id --check-column rental_date --last-value '2005-08-23 22:50:12.0'

hdfs dfs -ls -h -R /user/hive/warehouse/db_test3

```

