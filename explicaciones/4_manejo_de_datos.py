
#todo Como llamar un valor de un array:
# Un array esta compueso por casillas que indican su posicion
# EJEMPLO:
array = ["Soy", "un", "array"]
# Las posiciones empiezan a contar desde 0, 1, 2, 3, 4, 5, etc
# Entonces en este array la posicion 1 es... "un". La posicion 0 es... "Soy". Y la posicion 2 es... "array"
# Ahora como las llamamos, de esta forma: variable[posicion]
print(array[0]) #? Soy


#todo Como editar una posicion de un array:
# Teoria: Como sabemos si igualamos valor1 a valor2, que pasa? Valor1 pasa a ser igual a valor 2
valor1 = 10
valor2 = 20
valor1 = valor2
print(valor1) #? 20

# Entonces arrar[posicion] es un valor tambien, por ende lo podemos igualar
array[0] = "Ya no soy"
print(array[0]) #? Ya no soy
print(array) #? ['Ya no soy', 'un', 'array']


# -------------------------------------------------------------------------------------------------------------------------------#


# Pasa lo mismo pero con los strings para LLAMARLOS, no para EDITARLOS
texto = "Hola"
print(texto[0]) #? H