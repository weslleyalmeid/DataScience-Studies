## Control Center

1. Criar um tópico com o nome msg-rapida com 4 partições, 1 replicação e deletar os dados após 5 minutos de uso.
```md
abrir http://localhost:9021/
- topics
- add a topics
- select model dev
- add 5 minutes
- save
```

2. Produzir e consumir 2 mensagens para o tópico msg-rapida
**Consumer**
```bash
docker container exec -it broker bash
kafka-console-consumer --bootstrap-server localhost:9092 --topic msg-rapida
```

**Producer**
```bash
docker container exec -it broker bash
kafka-console-producer --broker-list localhost:9092 --topic msg-rapida
```

3. Qual o nome do cluster?
```bash
CONTROLCENTER.CLUSTER
```

4. Quantos tópicos existem no cluster?
```md
verificar no overview
```

5. Quantas partições existem o tópico msg-cli?
```bash
```

6. Todas as réplicas estão sincronizadas no tópico msg-cli?
```bash
```

7. Qual a política de limpeza do tópico msg-cli?
```bash
```

8. Alterar a política de limpeza do tópico msg-cli para deletar depois de um ano.
```bash
```

9. Qual o diretório de armazenamento de logs do cluster?
```md
- cluster settings
- LOG > log.dirs
```

10. Por padrão os dados são mantidos por quantos dias no Kafka?
```bash
- log.retention.hours
- 168/24 = 7 dias
```

11. Visualizar os gráficos de produção e consumo de dados do tópico msg-rapida.
```bash
```