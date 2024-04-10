# IF, FOR, WHILE
# ELSE, ELIF

# ELSE Y ELIF
# Se ejecutan cuando: 
# IF(cuando la funcion no se cumple)
# FOR(cuando termina de ejecutarse)
# WHILE(cuando termina de ejecutarse)

# IF
# Estructura: IF CONDICION: CODIGO
# Ejemplo:

# plata = 100
# if plata < 100:
#     print("Tenes menos de 100 pesos!")
# elif plata > 100:
#     print("Tenes mas de 100 pesos!")
# else:
#     print("Tenes 100 pesos!")

# -------------------------------------------------------------------------------------------------------------------------------#

# FOR
# ESTRUCTURA: for variables in valor: codigo
# El valor puede ser range()

# range(valor, valor, valor) 
# Primer valor(opcional): indica la cantidad donde va a empezar
# Segundo valor(NO OPCIONAL): indica el maximo sin contarse a el mismo
# Tercer valor(OPCIONAL): indica cada cuanto va a contar el for

# range(10) = [0,1,2,3,4,5,6,7,8,9]
# range(5, 10) = [5,6,7,8,9]
# range(5, 10, 2) = [5,7,9]
# for variable in [100, 200, 300]:
#     print(variable)
    
animales = ["cerdo", "cabra", "oveja", "leon", "panda"]

# FORMA NO OPTIMAAAA!
# for animal in range(len(animales)):
#     print(animales[animal])

# FORMA OPTIMA!
# for animal in animales:
#     print(animal)

# for i in "hola":
#     print(i)

# FOR ELSE
# for i in range(10):
#     print(i)
# else:
#     print("BUCLE TERMINADO!")


# FOR BREAK
# for i in range(10):
#     if i > 3:
#         break
#     print(i)


# FOR CONTINUE
# for animal in animales:
#     if animal == "leon":
#         continue
#     print(animal)


# FOR list comprehensions
# numeros = [10,5,6]
# nuemros2 = [numeritos*2 for numeritos in numeros]
# print(nuemros2)


# WHILE ELSE
# contado = 10
# while contado > 0:
#     print(contado)
#     contado -= 1
# else:
#     print("Bucle termiando!")


# WHILE BREAK
# FORMA NO OPTIMA
# bucle = 1
# while bucle == 1:
#     print("hola")
#     bucle = 0

# FORMA OPTIMA
# while True:
#     print("Hola")
#     break

