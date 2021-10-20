##  Preparar os dados e o ambiente

1. Configurar o jar do spark para aceitar o formato parquet em tabelas Hive
```bash
curl -O https://repo1.maven.org/maven2/com/twitter/parquet-hadoop-bundle/1.6.0/parquet-hadoop-bundle-1.6.0.jar
docker cp parquet-hadoop-bundle-1.6.0.jar jupyter-spark:/opt/spark/jars
```

2. Baixar os dados dos exercícios do treinamento no diretório spark/input (volume no Namenode)
```bash
cd input
sudo git clone https://github.com/rodrigo-reboucas/exercises-data.git .
```

3. Verificar o envio dos dados para o namenode
```bash
docker container exec -it namenode ls /input
```

4. Criar no hdfs a seguinte estrutura: /user/rodrigo/data
```bash
docker container exec -it namenode bash
# desativar modo de seguranca
hdfs dfsadmin -safemode leave
hdfs dfs -mkdir -p /user/weslley/data
```

5. Enviar todos os dados do diretório input para o hdfs em /user/rodrigo/data
```bash
hdfs dfs -put /input/* /user/weslley/data
```