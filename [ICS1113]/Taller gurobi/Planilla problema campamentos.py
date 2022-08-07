from gurobipy import GRB, Model, quicksum
from random import randint, seed

seed(10)

# Definicion de data: Definir Localidades y Sitios

Localidades = range(10) #I
Sitios = range(20) #J

# Definir valores para los parámetros p_i () , d_ij, f_j, c_j y el parámetro constante P 

p = {i: randint(10, 100) for i in Localidades}
d = {(i, j): randint(10, 20) for i in Localidades for j in Sitios}
f = {j: randint(1, 2) for j in Sitios}
c = {j: randint(10, 20) for j in Sitios}
P = 1000

# Crea un modelo vacío
model = Model()

# Crea las variables de decisión x_j, y_ji, s_j y w
x = model.addVars(Sitios, vtype = GRB.BINARY, name = "x_j")
y = model.addVars(Localidades, Sitios, vtype = GRB.BINARY, name = "y_ij")
s = model.addVars(Sitios, vtype = GRB.INTEGER, name = "s_j")
w = model.addVar(vtype = GRB.INTEGER, name = "w")
# Llama a update para agregar las variables al modelo

model.update()


# Restricciones 

# Crea la restriccion : Definicion de w
model.addConstrs((w >= d[i, j] * y[i, j] for i in Localidades for j in Sitios), name="R1")

# Crea la restriccion : Si se asigna un campamento a una localidad, éste debe construirse
model.addConstrs((x[j]>= y[i,j] for i in Localidades for j in Sitios), name="R2")

# Crea la restriccion : Cada localidad debe tener un campamento asignado
model.addConstrs( (quicksum(y[i, j] for j in Sitios) == 1 for i in Localidades ), name="R3")

# Crea la restriccion: Gente asociada a un campamento
model.addConstrs((s[j] >= quicksum(y[i,j]*p[i] for i in Localidades)  for j in Sitios), name="R4")

# Crea la restriccion: No se debe incurrir en un costo superior a P 
model.addConstr((quicksum(x[j]*c[j] + s[j]*f[j] for j in Sitios) <= P), name="R5")


# Escribe la funcion objetivo
objetivo = w
model.setObjective(objetivo, GRB.MINIMIZE)

# Optimiza tu problema
model.optimize()

# Muestra los valores de las soluciones
print("\n"+"-"*10+" Manejo Soluciones "+"-"*10)
print(f"El valor objetivo es de: {model.ObjVal}")
for sitio in Sitios:
    if x[sitio].x != 0:
        print(f"Se construye un campamento en el sitio {sitio}")
    if s[sitio].x != 0:
        print(f"Se asignan {s[sitio].x} personas para vacunarse en el campamento construido en el sitio {sitio}")
    for localidad in Localidades:
        if y[localidad, sitio].x != 0:
            print(f"Se asocia la localidad {localidad} con el campamento ubicado en el sitio {sitio}")

# ¿Cuál de las restricciones son activas?
print("\n"+"-"*9+" Restricciones Activas "+"-"*9)
for constr in model.getConstrs():
    if constr.getAttr("slack") == 0:
        print(f"La restriccion {constr} está activa")
model.printAttr("X")