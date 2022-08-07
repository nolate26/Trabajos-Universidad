### !!!

# En el PDF se encuentran ordenados los resultados y conclusiones!!!

### !!!!


from gurobipy import GRB, Model, quicksum

# diccionarios cuyos valores son [l_c, u_c],
# o sea que es una lista cuyo primer valor es el mínimo de 
# nutrientes y el segundo valor es el máximo de nutrientes
# de cada tipo
categories = {
    'calories': [1700, 2200],
    'protein':  [91, GRB.INFINITY],
    'fat':      [0, 65],
    'sodium':   [0, 1779]}

# Diccionario cuya llave es la comida y su valor es 
# el costo que esta tiene (los valores son los c_f)

foods = {
    'hamburger': 2.49,
    'chicken':   2.89,
    'hot dog':   1.50,
    'fries':     1.89,
    'macaroni':  2.09,
    'pizza':     1.99,
    'salad':     2.49,
    'milk':      0.89,
    'ice cream': 1.59}

#diccionario cuyos valores son los v_fc
nutritionValues = {
    ('hamburger', 'calories'): 410,
    ('hamburger', 'protein'):  24,
    ('hamburger', 'fat'):      26,
    ('hamburger', 'sodium'):   730,
    ('chicken',   'calories'): 420,
    ('chicken',   'protein'):  32,
    ('chicken',   'fat'):      10,
    ('chicken',   'sodium'):   1190,
    ('hot dog',   'calories'): 560,
    ('hot dog',   'protein'):  20,
    ('hot dog',   'fat'):      32,
    ('hot dog',   'sodium'):   1800,
    ('fries',     'calories'): 380,
    ('fries',     'protein'):  4,
    ('fries',     'fat'):      19,
    ('fries',     'sodium'):   270,
    ('macaroni',  'calories'): 320,
    ('macaroni',  'protein'):  12,
    ('macaroni',  'fat'):      10,
    ('macaroni',  'sodium'):   930,
    ('pizza',     'calories'): 320,
    ('pizza',     'protein'):  15,
    ('pizza',     'fat'):      12,
    ('pizza',     'sodium'):   820,
    ('salad',     'calories'): 320,
    ('salad',     'protein'):  31,
    ('salad',     'fat'):      12,
    ('salad',     'sodium'):   1230,
    ('milk',      'calories'): 100,
    ('milk',      'protein'):  8,
    ('milk',      'fat'):      2.5,
    ('milk',      'sodium'):   125,
    ('ice cream', 'calories'): 330,
    ('ice cream', 'protein'):  8,
    ('ice cream', 'fat'):      10,
    ('ice cream', 'sodium'):   180}

#### MODELO ####
modelo = Model()
#modelo.setParam("TimeLimit", 900  )

#Variables
x = modelo.addVars(foods, vtype = GRB.CONTINUOUS, name = "x")
modelo.update()

#Función Objetivo
objetivo = (quicksum(x[f] * foods[f] for f in foods))

# Restricciones 
#R1
modelo.addConstrs((quicksum(nutritionValues[f,c] * x[f] for f in foods) <= (categories[c])[1] for c in categories), name = "R1")

#R2
modelo.addConstrs((quicksum(nutritionValues[f,c] * x[f] for f in foods) >= (categories[c])[0] for c in categories), name = "R2")

modelo.setObjective(objetivo, GRB.MINIMIZE)
modelo.optimize()

#Imprimir Valor Objetivo
valor_objetivo = modelo.ObjVal
#################################

print("\n"+"-"*10+" Manejo Soluciones "+"-"*10)

print(f"A)\nEl valor óptimo que minimiza la dieta es de: {valor_objetivo}")
print("\nGRAMOS POR INGREDIENTE:")

for v in modelo.getVars():
    print(str(v.varName[2:-1])+': '+str(v.x))

print("\nB)\nCOSTOS REDUCIDOS DE LAS VARIABLES EN EL ÓPTIMO:")

for v in modelo.getVars():
    print(str(v.varName[2:-1])+': '+str(v.RC))

print("Cumplen con el criterio de optimalidad, ya que son mayores o iguales que 0 todas las variables no básicas\n")

print("C)\nRANGO DE VALORES QUE ESTÁN LAS CANTIDADES MÁXIMAS Y MÍNIMAS POR NUTRIENTE PARA SEGUIR SIENDO ÓPTIMA (Lado derecho)\n\nINTERVALO CANTIDADES MÁXIMAS POR NUTRIENTE:(u_c)\nAlimento:[] - MAX actual - intervalo: - min y max que puede tomar")

for r in range(4):
    print(str(modelo.getConstrs()[r])[18:-2]+": "+ str(modelo.getConstrs()[r].RHS)+ " -> intervalos: "+ str(modelo.getConstrs()[r].SARHSLow)+'---'+str(modelo.getConstrs()[r].SARHSUp) )

print("\nINTERVALO CANTIDADES MÍNIMAS POR NUTRIENTE:(l_c)\nAlimento:[] - MIN actual - intervalo: - miny max que puede tomar")

for r in range(4):
    print(str(modelo.getConstrs()[r+4])[18:-2]+": "+ str(modelo.getConstrs()[r+4].RHS)+ " -> intervalos: "+ str(modelo.getConstrs()[r+4].SARHSLow)+'---'+str(modelo.getConstrs()[r+4].SARHSUp) )

print("\nD)\nCAMBIO EN VALOR DE LA FUNCIÓN OBJETIVO SI VARIABLE CALORÍAS DISMINUYE 11 UNIDADES\nCalculamos el dual en las variables de calorías")

print("R1 "+str(modelo.getConstrs()[0])[18:-2]+"-> DUAL : "+str(modelo.getConstrs()[0].pi))
print("R2 "+str(modelo.getConstrs()[4])[18:-2]+"-> DUAL : "+str(modelo.getConstrs()[4].pi))

print("Variación de b2 = -11\n("+str(modelo.getConstrs()[0].pi) +" + "+ str(modelo.getConstrs()[4].pi)+ ") * -11" + " = "+ str(modelo.getConstrs()[4].pi*-11)+"= delta z")

print("FO + delta z = nuevo valor")
print(str(valor_objetivo)+ " - " +str(modelo.getConstrs()[4].pi*11) +" = "+ str(valor_objetivo+modelo.getConstrs()[4].pi*-11))
print(f"Por lo tanto, al variar calorias en 11 unidades la función objetivo va a disminuir a {valor_objetivo+modelo.getConstrs()[4].pi*-11}")



print("\nE)")
#### MODELO E)####
m = Model()

#Variables
x0 = m.addVars(foods, vtype = GRB.INTEGER, name = "x0")
m.update()

#Función Objetivo
obj = (quicksum(x0[f] * foods[f] for f in foods))

# Restricciones 
#R1
m.addConstrs((quicksum(nutritionValues[f,c] * x0[f] for f in foods) <= (categories[c])[1] for c in categories), name = "R1")

#R2
m.addConstrs((quicksum(nutritionValues[f,c] * x0[f] for f in foods) >= (categories[c])[0] for c in categories), name = "R2")

m.setObjective(obj, GRB.MINIMIZE)
m.optimize()


print("\n"+"-"*10+" Manejo Soluciones "+"-"*10)

#Imprimir Valor Objetivo
valor_objetivo_nuevo = m.ObjVal
print("Valor objetivo problema inicial: "+str(valor_objetivo) )
print("\nValor objetivo problema nuevo: "+str(valor_objetivo_nuevo) )
print("\nGRAMOS POR INGREDIENTE:")
for v in m.getVars():
    print(str(v.varName[3:-1])+': '+str(v.x))
print("\nPorcentaje del nuevo respecto al anterior: "+str(100*(valor_objetivo_nuevo-valor_objetivo)/valor_objetivo)+"%")
print("Esto quiere decir que el nuevo valor objetivo aumenta aproximadamente un 8% respecto al original, \nlo que hace sentido ya que al tomar valores enteros nos desplazamos de la relajación lineal y empeoramos la función objetivo al movernos del vértice óprimo ")