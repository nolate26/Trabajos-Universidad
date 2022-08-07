import random
random.seed(10)

N = 700

#Conjuntos
T = [0, 1, 2, 3, 4]
K = [1, 2, 3, 4, 5]
I = range(1, N + 1) #i
J = range(1, N + 1) #i

#Parámetros
c = {(i): random.randint(5, 7) for i in I}
m = {(i, k): random.randint(0, 4) for i in I for k in K}
x = {(i): random.uniform(-3, 3) for i in I}
y = {(i): random.uniform(-3, 3) for i in I}
D = 0.15