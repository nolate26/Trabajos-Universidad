#split(saco el \n, pero me queda una lista
#strip("\n")-> saco el \n y me queda como string




#CSV-> comma Separated values
#varios valores separados por lineas
#usamos el split(",")

#metodo join-> opuesto al split
#join(x)


print("+++ Letras separadas")
delimitador = "---"
texto = delimitador.join("Hugo")
print(texto)
print("+++ Palabras separadas")
texto = delimitador.join(["Hugo", "Paco", "Luis"])
print(texto)
print("+++ Lista horizontal")
texto = ' '.join(["Hugo", "Paco", "Luis"])
print(texto)
print("+++ Lista vertical")
texto ='n'.join(["Hugo", "Paco", "Luis"])
print(texto)