from cmath import sqrt
from statistics import mode
from gurobipy import GRB, Model, quicksum
from math import sqrt
from datos import N, T, K, I, J, c, m, x, y, D

#### MODELO ####
modelo = Model()
modelo.setParam("TimeLimit", 300)
#Variables
p = modelo.addVars(I,T,K, vtype = GRB.BINARY, name = "p")
n = modelo.addVars(I,J,T,K, vtype = GRB.BINARY, name = "n")

modelo.update()

#Función Objetivo 
objetivo = (quicksum(p[i,t,k] for i in I for t in T for k in K))

#R1
modelo.addConstrs((p[i,t,k] + (sum(n[i,j,t,k] for j in J)) <= 1  for i in I for t in T for k in K), name = "R1")

#R2
modelo.addConstrs((sum(p[i,t,k] for t in T) <= 1 for i in I for k in K), name = "R2")

#R3
modelo.addConstrs((sum(p[i,t,k] for t in T) + sum(n[i,j,t,k] for t in T for j in J) <= 1 for i in I for k in K), name = "R3")

#R4
modelo.addConstrs((sum(n[i,j,m[j,k],k] for i in I) <= c[j] - 1 for j in J for k in K), name = "R4")

#R5
modelo.addConstrs((n[i,j,m[i,k],k] * sqrt((x[i]-x[j])**2 + (y[i]-y[j])**2) <= D  for i in I for j in J for k in K), name = "R5") 

#R6
modelo.addConstrs(((p[i,m[i,k],k]+sum(n[i,j,m[i,k],k] for j in J))*m[i,k] == m[i,k] for i in I for k in K), name = "R6")

#R7
modelo.addConstrs((n[i,j,m[i,k],k]<= p[j,m[i,k],k] for i in I for j in J for k in K), name = "R7")

#R8
modelo.addConstrs((sum(p[i,t,k] for t in T) + sum(n[i,j,t,k] for t in T for j in J)  <= m[i,k] for i in I for k in K), name = "R8")

#R9
modelo.addConstrs((n[i,i,t,k] == 0 for i in I for k in K for t in T), name = "R9")

modelo.setObjective(objetivo, GRB.MINIMIZE)
modelo.optimize()

#Imprimir Valor Objetivo
valor_objetivo = modelo.ObjVal
#################################

#modelo.printAttr("X")
print(f"El valor objetivo para minimizar los autos es de: {modelo.ObjVal}")
print("\n"+"-"*10+" Manejo Soluciones "+"-"*10)
for dia in K:
    suma_autos = sum(p[i,t,dia].x for t in T for i in I)
    suma_pasajeros = sum(n[i,j,t,dia].x for t in T for i in I for j in J)
    print(f"El día {dia} se van {suma_pasajeros+suma_autos} personas en un total de {suma_autos} autos")
    