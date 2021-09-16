## Sqoop - Importação BD Employees

1. Pesquisar os 10 primeiros registros da tabela employees do banco de dados employees

```bash
sqoop eval --connect jdbc:mysql://database/employees --username root --password secret --query "select * from employees limit 10"
```

2. Realizar as importações referentes a tabela employees e para validar cada questão,  é necessário visualizar no HDFS*

Importar a tabela employees, no warehouse  /user/hive/warehouse/db_test_a

```bash
# import table
sqoop import --table employees --connect jdbc:mysql://database/employees --username root --password secret --warehouse-dir /user/hive/warehouse/db_test_a

# validando import no hdfs
hdfs dfs -ls /user/hive/warehouse/db_test_a/employees

# visualizando as primeiros 5 linhas
hdfs dfs -cat /user/hive/warehouse/db_test_a/employees/part-m-00000 | head -n 5

```

Importar todos os funcionários do gênero masculino, no warehouse  /user/hive/warehouse/db_test_b

```bash
# import table com where
sqoop import --table employees --connect jdbc:mysql://database/employees --username root --password secret --where "gender='M'" --warehouse-dir /user/hive/warehouse/db_test_b

# validando import no hdfs
hdfs dfs -ls /user/hive/warehouse/db_test_b/employees

# visualizando as primeiros 5 linhas
hdfs dfs -cat /user/hive/warehouse/db_test_b/employees/part-m-00000 | head -n 5

```

importar o primeiro e o último nome dos funcionários com os campos separados por tabulação, no warehouse  /user/hive/warehouse/db_test_c

```bash
# import table com columns e campos separados por tabulacao
sqoop import --table employees --connect jdbc:mysql://database/employees --username root --password secret --columns "first_name, last_name" --fields-terminated-by '\t' --warehouse-dir /user/hive/warehouse/db_test_c

# validando import no hdfs
hdfs dfs -ls /user/hive/warehouse/db_test_c/employees

# visualizando as primeiros 5 linhas
hdfs dfs -cat /user/hive/warehouse/db_test_c/employees/part-m-00000 | head -n 5
```

Importar o primeiro e o último nome dos funcionários com as linhas separadas por “ : ” e salvar no mesmo diretório da questão 2.C

```bash
# import table com columns e linhas separadas por dois pontos
sqoop import --table employees --connect jdbc:mysql://database/employees --username root --password secret --columns "first_name, last_name" --lines-terminated-by '\t' --warehouse-dir /user/hive/warehouse/db_test_c -delete-target-dir

# validando import no hdfs
hdfs dfs -ls /user/hive/warehouse/db_test_c/employees

# visualizando as primeiros 5 linhas
hdfs dfs -cat /user/hive/warehouse/db_test_c/employees/part-m-00000 | head -n 5
```

* Dica para visualizar no HDFS:
```
$ hdfs dfs -cat /.../db_test/nomeTabela/part-m-00000 | head -n 5
```