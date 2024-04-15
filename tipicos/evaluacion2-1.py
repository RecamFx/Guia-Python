from random import choice
from random import randint

def nombresGenerator():
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    names = []

    for i in range(48):
        nombre = ""
        for a in range(randint(3,5)):
            nombre += choice(abc)
        names.append(nombre)
    return names

def filterX(namess):
    nombresX = []
        
    for i in namess:
        if "x" in i:
            nombresX.append(i)
        
    return nombresX

# Nombres generados
nGen = nombresGenerator()

print(filterX(nGen))