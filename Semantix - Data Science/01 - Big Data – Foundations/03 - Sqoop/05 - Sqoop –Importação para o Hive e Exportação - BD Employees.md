## Sqoop - Importação para o Hive e Exportação - BD Employees


1. Importar a tabela employees.titles do MySQL para o diretório /user/aluno/<nome>/data com 1 mapeador.
```bash
docker exec -it namenode bash

sqoop import --table titles --connect jdbc:mysql://database/employees --username root --password secret --warehouse-dir /user/aluno/weslley/data -m 1

```

2. Importar a tabela employees.titles do MySQL para uma tabela Hive no banco de dados seu nome com 1 mapeador.
```bash
sqoop import --table titles --connect jdbc:mysql://database/employees --username root --password secret -m 1 --hive-import --hive-table weslley.titles
```

3. Selecionar os 10 primeiros registros da tabela titles no Hive.
```bash
docker exec -it hive-server bash
beeline -u jdbc:hive2://localhost:10000
use weslley;
select * from titles limit 10;
```
4. Deletar os registros da tabela employees.titles do MySQL e verificar se foram apagados, através do Sqoop
```bash
docker exec -it namenode bash

sqoop eval --connect jdbc:mysql://database/employees --username root --password secret --query "select * from titles limit 10"

sqoop eval --connect jdbc:mysql://database/employees --username root --password secret --query "truncate table titles"

```
5. Exportar os dados do diretório /user/hive/warehouse/<nome>.db/data/titles para a tabela do MySQL  employees.titles.
```bash

sqoop export --table titles --connect jdbc:mysql://database/employees --username root --password secret --export-dir /user/aluno/weslley/data/titles
```
6. Selecionar os 10 primeiros registros registros da tabela employees.titles do MySQL.
```bash
sqoop eval --connect jdbc:mysql://database/employees --username root --password secret --query "select * from titles limit 10"
```