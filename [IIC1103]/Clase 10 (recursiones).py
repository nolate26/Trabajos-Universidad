#Funciones dentro de funciones 
#>Recursión, llamar a una función sobre si misma y se va repitiendo lo mismo
# Es una técnica de resolución de problemas , es una función que se define a si misma 


#Pasos Recursion:
# 1- pensarlo mas facil
# 2- asumir que funciona
# 3- Caso base 
# 4- Caso recursivo
# 5- pensar parametros
# 6- pensar valor de retorno 




#EJEMPLO FACTORIAL 

#De manera iterativa:
n = int(input("Elige un número:"))
def factorial(n):
    if n!=0:
        resultado = 1
        num= 1
        while num <= n:
            resultado*=num
            num+=1
        return resultado
    else:
        return 1

print("El factorial de", n, "es", factorial(n))

#De manera recursiva:
def factorial(n):
    if n ==0:
        return 1
    else:
        fact = n* factorial(n-1)
        return fact
n=int(input("Elige un numero:"))
print("El factorial de", n, "es", factorial(n))

# Toda función recursiva nesecita un caso base (limite mas pequeño)
#  Ej: factorial 0==1

# Multiplos Recursivos:
# Desarrolle f. recursiva para entregar el n-esimo múltiplo de un imput del usuario

def multiplo_m(n,m):
    if n==1:
        return m
    else:
        enesimo_multiplo = m + multiplo_m(n-1,m)
        return enesimo_multiplo

m=int(input("Multiplo de que número:"))
n=int(input("Cuantas veces:"))
print(multiplo_m(n,m))
