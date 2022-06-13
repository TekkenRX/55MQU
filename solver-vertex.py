from pyomo.environ import *
import sys

#  v0 - v3 \
#  |    |  v4  
#  v1 - v2 /

# Criação do modelo
model = ConcreteModel()

# Variáveis de decisão
f = open(sys.argv[1], "r")
c = [] # custos dos vértices
m = [] # vértices em cada aresta
for x in f:
    if x[0] != "#":
        if x[0] == "(":
            m.append(x.strip().strip('('))
        else:
            c = x.strip().split(',')
f.close()
n = len(c) #numero vertices
# Variáveis de decisão
model.x = Var(range(n), domain = Boolean)

# Função objetivo
model.obj = Objective(expr = sum([int(c[i]) * model.x[i] for i in range(n)]), sense = minimize)

# Restrições: o numero de restrições será igual ao número de arestas existentes
# garante que para cada aresta, pelo menos, um dos vértices adjacentes a ela seja escolhido
model.cons = ConstraintList()

for i in m:
    splt = i.split(',')
    model.cons.add(expr = model.x[int(splt[0])] + model.x[int(splt[1])] >= 1)

# Solução
opt = SolverFactory('glpk')
opt.solve(model, timelimit = 10).write()
for i in range(n):
    print(model.x[i]())
print()
print(model.obj.expr())
