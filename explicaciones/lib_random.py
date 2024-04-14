# FORMAS DE IMPORTAR UNA LIBRERIA
import random # Importando toda la libreria
from random import randint # Importando solo la funcion randint de random
from random import choice # Importando solo la funcion choice de random


# NUMEROS RANDOM
# uso: randint(valor inicial, valor final)
# Lo que hace randint es generar un numero aleatorio entre el valor inicial y el valor final
numero_random1 = randint(0,10)
numero_random2 = random.randint(0,10)
print(numero_random1)
print(numero_random2)



# FUNCION CHOICE
# Lo que hace choice es elegir un valor aleatorio entre los valores que existen en una lista
lista = [500, 100, 1000, 400]

print(f"Elijo: {choice(lista)}")
print(f"Elijo2: {random.choice(lista)}")