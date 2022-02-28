import pandas as pd
import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory
import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory
import time

model = pyo.ConcreteModel()

interval = range(1, 6)

# VARIAVEIS
# Xi, y >= 0
# Xi int para todo interval
model.x = pyo.Var(interval, bounds=(0,None), within=Integers)
model.y = pyo.Var(bounds=(0,None))

# atribuindo model para evitar chamar
x = model.x
y = model.y


# RESTRICOES
model.C1 = pyo.Constraint(expr = sum([x[i] for i in interval]) + y <= 20)

# para todo i
model.C2 = pyo.ConstraintList()
for i in interval:
    model.C2.add(expr = x[i] + y >= 15)
    
model.C3 = pyo.Constraint(expr = sum([i * x[i] for i in interval]) >= 10)
model.C4 = pyo.Constraint(expr = x[5] + 2*y >= 30)
# model.pprint()


model.obj = pyo.Objective(expr= sum([x[i] for i in interval]) + y, sense=minimize)

start = time.time()
opt = SolverFactory('gurobi')
# opt = SolverFactory('glpk')
opt.solve(model)
end = time.time()

# model.pprint()

print('\n---------------------------------------------------------------------')
for i in interval:
    print(f'x={x[i].value}')
print('y=',y.value)

print(f'Time: {end - start:.4f}')
