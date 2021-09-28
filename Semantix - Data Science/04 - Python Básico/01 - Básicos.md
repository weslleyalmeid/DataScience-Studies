1. Importe a função randint da biblioteca numpy
```py
from numpy.random import randint
```

2. Crie uma lista de números 15 números aleatórios inteiros, que estejam entre 0 e 10, usando a função randint e o método append de uma lista.
```py
inteiros_15 = []

for i in range(15):
    inteiros_15.append(randint(10))
```

3. Adicione o comando %%timeit no topo da célula que você criou para a função 2, ele irá calcular o tempo médio de execução do seu código
```py
%%timeit

inteiros_15 = []

for i in range(15):
    inteiros_15.append(randint(10))
```

4. Use os argumentos size e type na função randint para repetir a questão 2.
```py
list(randint(10, size=15))
```

5. Calcule o tempo do código feito na questão 4. É menor que o da questão 03?
```py
%%timeit
list(randint(10, size=15))
```

6. Faça uma função com apenas for,range,len, while, if, else, break para ordenar a lista que você criou na questão 04 do menor para o maior número.
```py
def verifica_se_ja_ordenou(lista):
    flag = true

    for i range(len(lista)-1):
        if lista[i] > lista[i+1]:
            flag = False

    return flag

def organiza_elementos(lista):
    ordenado = []

    for i range(len(lista)-1):
        if lista[i] > lista[i+1]:
            ordenado.append(lista[i+1])
            ordenado.append(lista[i])
            ordenado = ordenado + lista[i+2:]
            break
        else:
            ordenado.append(lista[i])
    return ordenado

def ordena_lista(lista, maximo=100):
    ordenado = lista
    
    for i range(maximo):
        
        if verifica_se_ja_ordenou(ordenado):
            print('Lista Ordenada')
            break
    
        else:
            ordenado = organiza_elementos(ordenado)
            print(ordenado)

    return ordenado

ordena_lista(inteiros_15)
```

7. Use a função sorted para refazer a questão 06 
```py
sorted(inteiros_15)
```

8. Calcule o tempo da questão 6 e da questão 07
```py
%%timeit
sorted(inteiros_15)

%%timeit
ordena_lista(inteiros_15)
```