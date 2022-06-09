from pyomo.environ import *

#  v0 - v3  \
#  |     |  v4
#  v1 - v2  /

#  v0 a2 v3  a5
#  a0    a3  v4
#  v1 a1 v2  a4


n = 5 #numero vertices
m = 6 #numero arestas
c = [150, 100, 100, 150, 100, 100] #custos das arestas

#   Criação do modelo
model = ConcreteModel()

#   Variáveis de decisão
model.v = Var(range(n), domain = Boolean)
model.a = Var(range(m), domain = Boolean)

#   Função objetivo
model.obj = Objective(expr = sum([ c[i] * model.a[i] for i in range(m)]), sense = minimize)

#    Restrições: o número sempre será de o número de vertices +1

#    garente que todos os vertices precisam ser escolhidos
model.con00 = Constraint(expr = sum([model.v[i] for i in range(n)]) == n)

#    para cada vértice, a soma das arestas que tocam nele deve ser de pelo menos um,
#o que garante que tem pelo menos uma aresta adjacente dele escolhida

#vertice 0
model.con01 = Constraint(expr = model.a[0] + model.a[2] >= 1)
#vertice 1
model.con02 = Constraint(expr = model.a[0] + model.a[1] >= 1)
#vertice 2
model.con03 = Constraint(expr = model.a[1] + model.a[3] + model.a[4] >= 1)
#vertice 3
model.con04 = Constraint(expr = model.a[2] + model.a[3] + model.a[5] >= 1)
#vertice 4
model.con05 = Constraint(expr = model.a[5] + model.a[4] >= 1)

# Solução
opt = SolverFactory('glpk')
opt.solve(model, timelimit = 10).write()
for i in range(m):
    print(model.a[i]())
print()
print(model.obj.expr())
