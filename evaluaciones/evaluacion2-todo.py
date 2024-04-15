from random import randint, choice

 # Generador de nombres random
def nGen():
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    name = []
    for i in range(48):
        n = ""
        for i in range(randint(3,6)):
            n += choice(abc)
        name.append(n)
    return name

# Filtrador, crea dos listas, una con los nombres con "X" y otra sin los nombres con "X"
def filtrarX(nombres): 
    nombres1 = []
    nombres2 = []
    for i in nombres:
        if "x" in i:
            nombres2.append(i)
        else:
            nombres1.append(i)
    return nombres1, nombres2

# Crea un lista que cuente la cantidad de caracteres que tiene cada nombre y los ordena de menor a mayor
def cantidadName(ngen):
    ngen2 = ngen
    cantidades = []
    for i in ngen2:
        cantidades.append(len(i))
    cantidades.sort()
    return cantidades

ej = nGen()
ej12 = filtrarX(ej)
ej3 = cantidadName(ej)

print(ej12[0])
print()
print("-----------------------------------------")
print()
print(ej12[1])
print()
print("-----------------------------------------")
print()
print(ej3)