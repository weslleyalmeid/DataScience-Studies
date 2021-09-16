## Instalação

1. Instalação do docker e docker-compose
```bash
docker-compose up -d
docker ps
docker container ls
```

2. Baixar a imagem do redis
```bash
docker pull redis
```

3. Iniciar o Redis através do docker-compose
```bash
docker-compose up -d
```
4. Listas as imagens em execução
```bash
docker ps
docker container ls
```

5. Verificar a versão do Redis
```bash
docker container exec -it redis redis-server --version
docker container exec -it redis redis-cli --version

docker container -it redis bash
redis-server version
redis-cli version
```
6. Acessar o Redis CLI
```bash
docker container -it redis bash
redis-cli
```