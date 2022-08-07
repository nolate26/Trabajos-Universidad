from gurobipy import Model, GRB

# Generar el modelo
model = Model()

# Se instancian variables de decision
x = model.addVar(vtype = GRB.CONTINUOUS, name="x")
y = model.addVar(vtype = GRB.CONTINUOUS, name="y")
z = model.addVar(vtype = GRB.CONTINUOUS, name="z")

# Llamamos a update
model.update()

# Restricciones
model.addConstr(3*x + y + 2*z <= 8, name="R1")
model.addConstr(x + 2*y + z <= 10, name="R2")
model.addConstr(-x - y -3*z >= -14, name="R3")

# Funcion Objetivo y optimizar el problema

objetivo = 2*x + 4*y + 5*z
model.setObjective(objetivo, GRB.MAXIMIZE)
model.optimize()

# Manejo Soluciones 
print("\n"+"-"*10+" Manejo Soluciones "+"-"*10)
print(f"EL valor objetivo es de: {model.Objval}")
print(f"La variable x toma el valor de {x.x}")
print(f"La variable y toma el valor de {y.x}")
print(f"La variable z toma el valor de {z.x}")

# Holguras (0 significa que la restricción es activa)
print("\n"+"-"*9+" Restricciones Activas "+"-"*9)
for constr in model.getConstrs():
    if constr.getAttr("slack") == 0:
        print(f"La restricción {constr} está activa")
