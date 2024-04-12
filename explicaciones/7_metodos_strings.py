# Metodos de cadenas
# Un metodo es lo que le acompana a la variable despues del numero, ejemplo: variable.metodo(parametros opcionales)


# -------------------------------------------------------------------------------------------------------------------------------#


cadena1 = "Stephen"
# UPPER Convierte toda la cadena de texto en mayuscula
resultado = cadena1.upper()
resultado2 = "Buenas tardes".upper()
print(resultado) #? STEPHEN
print(resultado2) #? BUENAS TARDES

# LOWER Convierte toda la cadena de texto a minusculas
resultado = cadena1.lower()
resultado2 = "Buenas tardes".lower()
print(resultado) #? stephen
print(resultado2) #? buenas tardes


# -------------------------------------------------------------------------------------------------------------------------------#


cadenaejemplo = "Hola buenas tardes"
# INDEX Busca una cadena dentro de otra cadena
busqueda = cadenaejemplo.index("a")
print(busqueda) #? 3
# FIND e INDEX hacen lo mismo, la unica diferencia es que find devuelve -1 si no encuentra el valor, en cambio index devuelve un error


# -------------------------------------------------------------------------------------------------------------------------------#


# ISNUMERIC Verifica si el valor es numerico (Numerico pero solo de strings)
busqueda = "hola".isnumeric()
busqueda2 = "3".isnumeric()
busqueda3 = "3asd".isnumeric()
print(busqueda) #? False
print(busqueda2) #? True
print(busqueda3) #? False

# ISALPHA Verifica si el valor solo contiene letras
busqueda = "hola".isalpha()
busqueda2 = "hola3".isalpha()
print(busqueda) #? True
print(busqueda2) #? False

# ALFANUMERICO Verifica si el valor contiene numeros y letras (nada de signos ni espacios)
busqueda = "hola23".isalnum()
busqueda2 = "hola 23".isalnum()
print(busqueda) #? True
print(busqueda2) #? False

# ISDIGIT Verifica si el valor solo son digitos
busqueda = "34234".isdigit()
busqueda2 = "hola3".isdigit()
print(busqueda) #? True
print(busqueda2) #? False


# -------------------------------------------------------------------------------------------------------------------------------#


# STARTSWITH Verifica si una cadena empieza con el valor que proporcionamos
busqueda = "Buenos Dias".startswith("Bue")
print(busqueda) #? True

# ENDSWITH Verifica si una cadena termina con el valor que proporcionamos
busqueda = "Hola".endswith("la")
print(busqueda) #? True


# -------------------------------------------------------------------------------------------------------------------------------#


# REPLACE Reemplaza un valor por otro .replace("valor antiguo", :"valor nuevo")
# En el caso de que no encuentre el valor antiguo simplemente no se va a modificar nada, se va a devolver el valor original
busqueda = "Hola".replace("la", "lu")
print(busqueda) #? Holu

# SPLIT Crea una lista donde el valor que le asignemos a split va a ser donde se separen los valores de la lista
busqueda = "Hola,buenos,dias".split(",")
print(busqueda) #? ['Hola', 'buenos', 'dias']

busqueda = "Hola buenos dias".split(" ")
print(busqueda) #? ['Hola', 'buenos', 'dias']


# -------------------------------------------------------------------------------------------------------------------------------#


# COUNT Cuenta cuantas veces esta precente el valor que le indicamos
busqueda = "a a b a b c d e".count("a")
print(busqueda) #? 3