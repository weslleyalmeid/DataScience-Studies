## Spark Schemas

1. Criar o DataFrame names_us_sem_schema para ler os arquivos no HDFS “/user/<nome>/data/names”
```python
!hdfs dfs -ls /user/weslley/data/names
!hdfs dfs -cat /user/weslley/data/names/yob1880.txt
names_us_sem_schema = spark.read.csv("/user/weslley/data/names")
```

2. Visualizar o Schema e os 5 primeiros registos do names_us_sem_schema
```python
names_us_sem_schema.printSchema()
names_us_sem_schema.show(5)
```

3. Criar o DataFrame names_us para ler os arquivos no HDFS “/user/<nome>/data/names” com o seguinte schema:
nome: String
sexo: String
quantidade: Inteiro
```python
from pyspark.sql.types import *
estrutura_lista = [
	StructField("nome", StringType()),
	StructField("sexo", StringType()),
	StructField("sexo", IntergerType())
]

schema_names = StructType(estrutura_lista)

name_us = spark.read.csv("/user/weslley/data/names", schema=schema_names)
```
4. Visualizar o Schema e os 5 primeiros registos do names_us
```python
name_us.printSchema()
name_us.show(5)
```

5. Salvar o DataFrame names_us no formato orc no hdfs “/user/<nome>/names_us_orc”
```python
names_us.write.orc("/user/weslley/names_us_orc")
!hdfs dfs -ls "/user/weslley/data/names_us_orc"
```
