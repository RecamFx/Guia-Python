import random
from random import randint
from random import choice

numero_random1 = randint(0,10)
numero_random2 = random.randint(0,10)
print(numero_random1)
print(numero_random2)




lista = [500, 100, 1000, 400]

print(f"Elijo: {choice(lista)}")
print(f"Elijo2: {random.choice(lista)}")



nueva_lista = []
randomNum = randint(0,10)
for i in range(randomNum):
    nueva_lista.append(randint(0,9))

print(nueva_lista)