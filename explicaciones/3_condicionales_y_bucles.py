# Condicionales y bucles
# If, for, while, else y elif

# Funcionamiento:
# if condicion: codigo
# for variable in valor: codigo
# while condicion: codigo

# else y elif se escribe despues de los condicionales
# elif es un if si no se cumple el primer if

# Siempre que se cumpla la condicion se va a ejecutar


# -------------------------------------------------------------------------------------------------------------------------------#


# IF
plata = 100

if plata < 100:
    print("Tenes menos de 100 de plata!")
elif plata > 100:
    print("Tenes mas de 100 de plata!") #? Tenes mas de 100 de palta!
else:
    print("Tenes 100 de plata!")
  
  
# -------------------------------------------------------------------------------------------------------------------------------#
    
    
# FOR
# Para el for una de las opciones es usar el range()
# range(valor de inicio opcional, valor final)

for i in range(5, 10):
    print(i)

#? 5
#? 6
#? 7
#? 8
#? 9

    
# -------------------------------------------------------------------------------------------------------------------------------#


# WHILE

contador = 10

while contador > 0:
    print(contador)
    contador -= 1

#? 9
#? 8
#? 7
#? 6
#? 5
#? 4
#? 3
#? 2
#? 1


# -------------------------------------------------------------------------------------------------------------------------------#


# BUCLES

while True:
    print("esto es un bucle") #? Esto es un bucle
    break # La funcion break sirve para frenar un bucle


# Sirve para fors tambien
# Aca le decimos que si i es mayor a 5 que pare todo el codigo (cuando se ejecuta break no importa en que parte del codigo estas, se frena todo)
for i in range(10):
    if i > 5:
        break
    print(i)
0
#? 1
#? 2
#? 3
#? 4
#? 5


# -------------------------------------------------------------------------------------------------------------------------------#


# Leer arrays
# Forma optima
animales = ["cerdo", "cabra", "obeja", "leon", "panda"]

for animal in animales:
    print(animal)

#? cerdo
#? cabra
#? obeja
#? leon
#? panda


# Tambien se puede hacer con strings
texto = "Hola Mundo!"
for i in texto:
    print(i)

#? H
#? o
#? l
#? a
#? 
#? M
#? u
#? n
#? d
#? o
#? !


# -------------------------------------------------------------------------------------------------------------------------------#


# For else
# Los else en los for actuan cuando termina el codigo

for i in range(10):
    print(i)
else:
    print("Termino el bucle!")

#? 0
#? 1
#? 2
#? 3
#? 4
#? 5
#? 6
#? 7
#? 8
#? 9
#? Termino el bucle!


# -------------------------------------------------------------------------------------------------------------------------------#


# Continue
# El continue hace que se saltee al siguiente bucle

frutas = ["manzana", "naranja", "uva", "frutilla"]
for i in frutas:
    if i == "uva":
        continue # Aca le decimos que si es uva la fruta que saltee al siguiente bucle, asi evitando que imprima la fruta
    print(i)

#? manzana
#? naranja
#? frutilla


# -------------------------------------------------------------------------------------------------------------------------------#


# list comprehensions
# Supongamso que quiero multiplicar los numeros de una lista por 2, como seria

# Forma no optima:
# numeros = [2, 4, 5, 7, 9, 20]
# listanueva = []
# for i in range(len(numeros)):
#     listanueva.append(numeros[i]*2)
# print(listanueva) #? [4, 8, 10, 14, 18, 40]


# Forma optima:
numeros = [2, 4, 5, 7, 9, 20]
nueva_lista = [x*2 for x in numeros]
print(nueva_lista) #? [4, 8, 10, 14, 18, 40]