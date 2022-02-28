import pandas as pd, numpy as np
import ortools.linear_solver.pywraplp as otlp
import os.path

FILE_NAME = 'inputs_dados.xlsx'
BASE_DIR = os.path.abspath('.')
DATA = os.path.join(BASE_DIR, 'data', FILE_NAME)


#dados entrada
dados_ger = pd.read_excel(DATA, sheet_name='geracao')
dados_carga = pd.read_excel(DATA, sheet_name='carga')
dados_dep = pd.read_excel(DATA, sheet_name='dependencia')
Ng = len(dados_ger)

solver = otlp.Solver('teste', otlp.Solver.GLOP_LINEAR_PROGRAMMING)

#entrada
Pg = np.zeros(Ng).tolist()
for g in range(Ng):
    Pg[g] = solver.NumVar(0, float(dados_ger.maximo[g]),'Pg[{}]'.format([g]))

#restrições
solver.Add(sum([Pg[g] for g in range(Ng)])==sum(dados_carga.valor))
for c in dados_dep.carga.unique():
    solver.Add(float(dados_carga.valor[c]) <= sum([Pg[g] for g in dados_dep.gerador[dados_dep.carga==c]]))

#obj
solver.Minimize(sum([Pg[g]*float(dados_ger.custo[g]) for g in range(Ng)]))

results = solver.Solve()

if results == otlp.Solver.OPTIMAL:
    print('Resultado encontrado')
else:
    print('Resultado Não encontrado')

for g in range(Ng):
    print('Pg[%i] = %.2f' % (g,Pg[g].solution_value()))