## Instalação

Instalação do docker e docker-compose
Acesso: https://docs.docker.com/get-docker/ (Links para um site externo.)
Baixar as imagens do mongo e mongo-express
Iniciar o MongoDB através do docker-compose

Listas as imagens em execução
```bash
docker-compose up -d
docker ps
docker container ls
```
Listar os bancos de dados do MongoDB
```bash
docker container exec -it mongo bash
mongo
show dbs
```

Visualizar através do Mongo Express os bancos de dados
```bash
docker container exec -it mongo-express
```
Acesso: http://localhost:8081/