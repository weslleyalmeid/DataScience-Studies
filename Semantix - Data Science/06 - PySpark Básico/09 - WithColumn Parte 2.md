## Exercícios - WithColumn 2/2


1. Criar um dataframe para ler o arquivo no HDFS /user/<nome/data/juros_selic/juros_selic
```py
from pyspark.sql.functions import *
from pyspark.sql.types import *
juros = spark.read.csv("/user/weslley/data/juros_selic/juros_selic", sep=";", header="true")
```

2. Agrupar todas as datas pelo ano em ordem decrescente e salvar a quantidade de meses ocorridos, o valor médio, mínimo e máximo do campo valor com a seguinte estrutura:
```py
juros_ano = juros.withColumn("anor", split(col("data"),"/").getItem(2))
juros_valor = juros_ano.withColumn("valor", regexp_replace(col("valor"), "\,", "\.").cast(FloatType()))


juros_relatorio = juros_valor.groupBy("ano").agg(count("ano").alias("Meses"), format_number(avg("valor"), 2).alias("Valor Médio"), min("valor").alis("Valor Mínimo"), max("valor").alis("Valor Máximo")).sort(desc("ano"))
```

3. Salvar no hdfs:///user/<nome>/relatorioAnual com compressão zlib e formato orc
```py
juros_relatorio.write.orc("/user/weslley/relatorio_anual", compression="zlib")
```