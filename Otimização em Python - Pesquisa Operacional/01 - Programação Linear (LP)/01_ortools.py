import ortools.linear_solver.pywraplp as otlp

solver = otlp.Solver('teste',otlp.Solver.GLOP_LINEAR_PROGRAMMING)


# variables
# lower limit and upper limit
x = solver.NumVar(0,10,'x')
y = solver.NumVar(0,10,'y')


# restrictions
solver.Add(-x + 2*y <= 8)
solver.Add(2*x + y <= 14)
solver.Add(2*x - y <= 10)


# objective function
solver.Maximize(x + y)

results = solver.Solve()

# check if the best solution
if results == otlp.Solver.OPTIMAL:
    print('Resultado Encontrado')
else:
    print('Resultado NÃO Encontrado')
    
# show result
print('x=',x.solution_value())
print('y=',y.solution_value())