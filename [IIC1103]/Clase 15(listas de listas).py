#Lista dentro de una lista -> tabla o matriz
M=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]

print(M[1][2]) #7
M[0][3]=20
print(M[0][3]) #20
print(M)

#Numero de Filas 
print(len(M)) #3

#Numero de columnas 
print(len(M[0])) #4

buzz=[1,2,3,4,5,6]
buzz[1]=buzz[1]-1
print(buzz)
