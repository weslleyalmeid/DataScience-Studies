## AG com PyGAD

1- Resolver o problema abaixo com Algoritmo Genético

Encontrar os valores de w1, w2, w3, w4, w5 e w6 para a seguinte equação

y = w1.x1 + w2.x2 + w3.x3 + w4.x4 + w5.x5 + 6w.x6
onde (x1,x2,x3,x4,x5,x6)=(-6, 5, 3.2, 7.8, -15, 9.4) e y=50

```py
!pip install pygad

import pygad
import numpy

input_x = [-6, 5, 3.2, 7.8, -15, 9.4]
output_y = 50


ga_instance = pygad.GA(num_generations=100,
                       sol_per_pop=10,
                       num_genes=6,
                       num_parents_mating=2,
                       fitness_func=fitness_func,
                       mutation_type="random")

ga_instance.run()
ga_instance.plot_result()

solution, solution_fitness, solution_idx = ga_instance.best_solution()
print(f"Parametros da melhor solução : {solution}")

prediction = numpy.sum(numpy.array(input_x) * solution)
print("Predição da saida da melhor solução : {prediction}".format(prediction=prediction))
```