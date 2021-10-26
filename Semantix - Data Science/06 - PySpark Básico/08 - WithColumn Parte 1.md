## Exercícios - WithColumn 1/2

1. Criar um dataframe para ler o arquivo no HDFS /user/<nome/data/juros_selic/juros_selic
```py
from pyspark.sql.functions import *
!hdfs dfs -cat /user/weslley/data/juros_selic/juros_selic
juros = spark.read.csv("/user/weslley/data/juros_selic/juros_selic", sep=";", header="true")
juros.show(5)
```

2. Alterar o formato do campo data para “MM/dd/yyyy”
```py
# transformando data para timestamp
juros_americano_unix = juros.withColumn("data", unix_timestamp(col("data"), "dd/MM/yyyy"))
# transformando timestramp para formato data personalizado
juros_americano = juros.withColumn("data", from_unixtime(col("data"), "MM/dd/yyyy"))
```

3. Com uso da função from_unixtime crie o campo “ano_unix”, com a informação do ano do campo data
```py
juros_unixtime = juros_americano.withColumn("ano_unix", from_unixtime(unix_timestamp(col("data"), "MM/dd/yyyy"), "yyyy"))
```

4. Com uso de substring crie o campo “ano_str”, com a informação do ano do campo data
```py
juros_substring = juros_unixtime.withColumn("ano_str", substring(col("data"),7,4))
juros_substring.show(3)
```

5. Com uso da função split crie o campo “ano_str”, com a informação do ano do campo data
```py
juros_split = juros_substring.withColumn("ano_split", split(col("data"),"/").getItem(2))
juros_split.show(3)
```

6. Salvar no hdfs /user/rodrigo/juros_selic_americano no formato CSV, incluindo o cabeçalho
```py
juros_split.write.csv("/user/weslley/juros_selic", header="true")
!hdfs dfs -cat /user/weslley/data/juros_selic/juros_selic
```