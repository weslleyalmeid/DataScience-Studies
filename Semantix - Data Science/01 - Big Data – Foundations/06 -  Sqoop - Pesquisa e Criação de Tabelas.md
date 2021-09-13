## Sqoop -  Pesquisa e Criação de Tabelas

Todos os comandos precisam ser executados pelo Sqoop.

1. Mostrar todos os databases
```bash
docker exec -it namenode bash
sqoop list-databases --connect jdbc:mysql://database --username root --password secret
```

2. Mostrar todas as tabelas do bd employees
```bash
sqoop list-tables --connect jdbc:mysql://database/employees --username root --password secret
```

3. Inserir os valores ('d010', 'BI') na tabela departments do bd employees
```bash
# consultar tabela
sqoop eval --connect jdbc:mysql://database/employees --username root --password secret --query "select * from departments"

# inserir tupla
sqoop eval --connect jdbc:mysql://database/employees --username root --password secret --query "insert into departments values ('d010', 'BI')"
```

4. Pesquisar todos os registros da tabela departments
```bash
sqoop eval --connect jdbc:mysql://database/employees --username root --password secret --query "select * from departments"
```

5. Criar a tabela benefits(cod int(2)  AUTO_INCREMENT PRIMARY KEY, name varchar(30)) no bd employees
```bash
sqoop eval --connect jdbc:mysql://database/employees --username root --password secret --query "create table benefits(cod int(2)  AUTO_INCREMENT PRIMARY KEY, name varchar(30))"
```

6. Inserir os valores (null,'food vale') na tabela benefits
```bash
sqoop eval --connect jdbc:mysql://database/employees --username root --password secret --query "insert into benefits values (null,'food vale')"
```

7. Pesquisar todos os registros da tabela benefits
```bash
sqoop eval --connect jdbc:mysql://database/employees --username root --password secret --query "select * from benefits"
```