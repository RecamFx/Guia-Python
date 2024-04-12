# Metodos de listas
# Un metodo es lo que le acompana a la variable despues del numero, ejemplo: variable.metodo(parametros opcionales)

# -------------------------------------------------------------------------------------------------------------------------------#


# APPEND Agrega elementos a una lista
listaAp = [1, 2, 3]
listaAp.append(4)
print(listaAp) #? [1, 2, 3, 4]

# INSERT Agrega un elemento a una lista en un lugar en especifico
# el elemento que ocupaba su lugar anteriormente es desplazado una vez a la derecha
# .inster(posicion, valor a agregar)
listaINS = [1, 2, 3, 4, 5, 6 ,7]
listaINS.insert(1, 43)
print(listaINS) #? [1, 43, 2, 3, 4, 5, 6, 7]

# EXTEND Agrega una lista a otra lista 
listaADD = [10, 36, 30]
listaEXT = [1, 2, 3, 4, 5, 6, 7]
listaEXT.extend(listaADD)
print(listaEXT) #? [1, 2, 3, 4, 5, 6, 7, 10, 36, 30]
listaEXT.extend([60, 80, 100])
print(listaEXT) #? [1, 2, 3, 4, 5, 6, 7, 10, 36, 30, 60, 80, 100]


# -------------------------------------------------------------------------------------------------------------------------------#


# POP Elimina un elemento de una lista en base a su posicion, se escribe .pop(posicion a eliminar)
# Si en la posicion que le ponemos el numero es negativo, vuelve a la parte de atras a de la lista y lo elimina
# Es decir, si pusimos -1 borra el ultimo elemento de la lista, lo mismo con -2 anteultimo y asi sucesivamente
listaPOP = [1, 2, 3, 4, 5]
listaPOP.pop(1)
print(listaPOP) #? [1, 3, 4, 5]
listaPOP.pop(-1)
print(listaPOP) #? [1, 3, 4]

# REMOVE Remueve un elemento de la lista segun su valor, si no encuentra el valor especificado devuelve un error
listaREM = ['h', 'o', 'l', 'a']
listaREM.remove("l")
print(listaREM) #? ['h', 'o', 'a']

# CLEAR Elimina todos los elementos de la lista
listaCL = ['h', 'o', 'l', 'a']
listaCL.clear()
print(listaCL) #? []


# -------------------------------------------------------------------------------------------------------------------------------#


# SORT Ordena los elementos de forma ascendente, no funciona con cadenas de texto
# Si le agregamos dentro de sort el parametro reverse=True, lo que hace es invertirlos, es decir de forma desendente
# True es 1 y False es 0
listaS = [0,1,4,2,5,6,3,True,False]
listaS.sort()
print(listaS) #? [0, False, 1, True, 2, 3, 4, 5, 6]
listaS.sort(reverse=True)
print(listaS) #? [6, 5, 4, 3, 2, 1, True, 0, False]


# -------------------------------------------------------------------------------------------------------------------------------#


# INDEX Busca segun el valor y nos devuelve la posicion
listaINDEX = ["hola", "buenas", "tardes"]
print(listaINDEX.index("hola"))


# -------------------------------------------------------------------------------------------------------------------------------#


# JOIN junta todos las posiciones de una lista y las separa segun los argumentos, ejemplo: "argumentos".join(lista)
listaJOIN = ["hola", "buenas", "tardes"]
listaJOIN2 = " ".join(listaJOIN) # Le digo que separe las posiciones con espacios
print(listaJOIN2) #? Hola buenas tardes
listaJOIN3 = "".join(listaJOIN) # Le digo que no separe las posiciones
print(listaJOIN3) #? Holabuenastardes