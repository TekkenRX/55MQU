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
for x in f:
    if x[0] != "#":
        if x[0] == "(":
            a
        else:
            c = x.strip().split(',')
f.close()
n = len(c) #numero vertices
# Variáveis de decisão
model.x = Var(range(n), domain = Boolean)

# Função objetivo
model.obj = Objective(expr = sum([ c[i] * model.x[i] for i in range(n)]), sense = minimize)

# Restrições: o numero de restrições será igual ao número de arestas existentes

#   garante que para cada aresta, pelo menos, um dos vértices adjacentes a ela seja escolhido

#aresta entre os vértices 0 e 1
model.con1 = Constraint(expr = sum([model.x[0] +model.x[1] ]) >= 1)
#aresta entre os vértices 0 e 3
model.con2 = Constraint(expr = sum([model.x[0] +model.x[3] ]) >= 1)
#aresta entre os vértices 1 e 2
model.con3 = Constraint(expr = sum([model.x[1] +model.x[2] ]) >= 1)
#aresta entre os vértices 2 e 3
model.con4 = Constraint(expr = sum([model.x[2] +model.x[3] ]) >= 1)
#aresta entre os vértices 2 e 4
model.con5 = Constraint(expr = sum([model.x[2] +model.x[4] ]) >= 1)
#aresta entre os vértices 3 e 4
model.con6 = Constraint(expr = sum([model.x[3] +model.x[4] ]) >= 1)

# Solução
opt = SolverFactory('glpk')
opt.solve(model, timelimit = 10).write()
for i in range(n):
    print(model.x[i]())
print()
print(model.obj.expr())
