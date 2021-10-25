## Dataset com DataFrame

1. Criar o DataFrame names_us para ler os arquivos no HDFS “/user/<nome>/data/names”
```python
docker exec -it jupyter-spark bash
spark-shell
val names_us = spark.read.csv("/user/weslley/names")
```

2. Visualizar o Schema do names_us
```python
name_us.printSchema
```

3. Mostras os 5 primeiros registros do names_us
```python
name_us.show(5)
```

4. Criar um case class Nascimento para os dados do names_us
```python
case class Nascimento(nome: String, sexo: String, quantidade: Int)
```

5. Criar o Dataset names_ds para ler os dados do HDFS “/user/<nome>/data/names”, com uso do case class Nascimento
```python
import org.apache.spark.sql.Enconders
val schema_names = Enconders.product[Nascimento].schema
val name_ds = spark.read.schema(schema_names).csv("/user/weslley/names").as[Nascimento]
```

6. Visualizar o Schema do names_ds
```python
name_ds.printSchema()
```

7. Mostras os 5 primeiros registros do names_ds
```python
name_ds.show(5)
```

8. Salvar o Dataset names_ds no hdfs “/user/<nome>/ names_us_parquet” no formato parquet com compressão snappy
```python
name_ds.write.save("/user/weslley/names_us_parquet")
spark.read.parquet("/user/weslley/names_us_parquet").printSchema
```
