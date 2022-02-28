import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory
from ipopt import *

model = pyo.ConcreteModel()

model.x = pyo.Var(initialize = 5)
opt.options['tol'] = 5
model.y = pyo.Var(bounds=(0, 10))
x = model.x
y = model.y

model.C1 = pyo.Constraint(expr= -x + 2*y*x <= 8)
model.C2 = pyo.Constraint(expr= 2*x + y <= 14)
model.C3 = pyo.Constraint(expr= 2*x - y <= 10)

model.obj = pyo.Objective(expr= x + y*x, sense=maximize)

# opt = SolverFactory('ipopt', executable='/opt/ipopt/Ipopt-3.7.1-linux-x86_64-gcc4.3.2/bin/ipopt')
opt = SolverFactory('ipopt')
opt.solve(model)

model.pprint()

x_value = pyo.value(x)
y_value = pyo.value(y)

print('\n---------------------------------------------------------------------')
print('x=',x_value)
print('y=',y_value)