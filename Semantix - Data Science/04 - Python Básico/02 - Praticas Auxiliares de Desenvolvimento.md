## Praticas auxiliares de desenvolvimento

1. Crie uma função que encontra filtra os números ímpares de uma lista de inteiros e depois os multiplica por 3.
```py
def filtra_impares(lista):
    impares = [a for a in lista if a%2 !=0]
    
    return impares

def multiplica_elementos(lista, numero =3):
    produto = [a*numero for a in lista]
    return produto
```

2. Crie um módulo que contenha essa função e depois faça o import.
```py

from filtro_multiplicador import filtragem_multiplica as fm
```

3. Crie testes unitários para as funções.
```py
```

4. Faça com que o módulo gere logs e registre em arquivo.
```py

```

5. Use Decorators para incluir mensagens de logs nas funções criadas.
```py
```
