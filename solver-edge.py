from pyomo.environ import *
import sys

from pyrsistent import v

#   Criação do modelo
model = ConcreteModel()

#   Variáveis de decisão

f = open(sys.argv[1], "r")
c = [] #custos das arestas
n = [] #arestas em cada vértice
for x in f:
    if x[0] != "#":
        if x[0] == "(":
            n.append(x.strip().strip('('))
        else:
            c = x.strip().split(',')
f.close()
m = len(c)
model.a = Var(range(m), domain = Boolean)

#    Restrições: o número sempre será de o número de vertices
model.cons = ConstraintList()

#   para cada vértice, a soma das arestas que tocam nele deve ser de pelo menos um,
#   o que garante que tem pelo menos uma aresta adjacente dele escolhida

def sumVertex(splt):
    soma = 0
    for i in splt:
        soma += model.a[int(i)]
    return soma

for i in n:
    splt = i.split(',')
    print(splt)
    model.cons.add(expr = sumVertex(splt) >= 1)

#   Função objetivo
model.obj = Objective(expr = sum([int(c[i]) * model.a[i] for i in range(m)]), sense = minimize)

# Solução
opt = SolverFactory('glpk')
opt.solve(model, timelimit = 10).write()
for i in range(m):
    print(model.a[i]())
print()
print(model.obj.expr())
