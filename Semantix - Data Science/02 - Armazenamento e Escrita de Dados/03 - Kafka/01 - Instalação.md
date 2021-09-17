## Instalação Cluster Kafka

1. Criar a pasta kafka e inserir o arquivo docker-compose.yml da Guia Arquivos do treinamento
```bash
```

2. Instalação do docker e docker-compose
```bash
```

Docker: https://docs.docker.com/get-docker/ (Links para um site externo.)
Docker-compose: https://docs.docker.com/compose/install/ (Links para um site externo.)
3. Inicializar o cluster Kafka através do docker-compose
```bash
docker-compose up -d
```

4. Listas as imagens em execução
```bash
docker ps
```

5. Visualizar o log dos serviços broker e zookeeper
```bash
docker logs zookeeper

# kafka
docker logs broker
```

6. Visualizar a interface do Confluent Control Center
Acesso: http://localhost:9021/ (Links para um site externo.)
```bash

```