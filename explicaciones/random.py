# Importamos randint
from random import randint

# Creando una lista vacia
nueva_lista = []

# Creamos una variable que almacene un numero random del 0 al 10
randomNum = randint(0,10)

# Hacemos un for que se repita la cantidad de veces que diga la variable anterior
for i in range(randomNum):
    
    # Agregamos numeros random del 0 al nueve a la lista
    nueva_lista.append(randint(0,9))

# Imprimimos la lista
print(nueva_lista)


# Logica:
# Creamos una lista vacia, creamos un for que se repita una cantida de veces random y que en las veces que se repita, que agregue numeros random del 0 al 9
# Por ende vamos a crean una lista con numeros random y que la cantidad de estos numeros tambien sea random