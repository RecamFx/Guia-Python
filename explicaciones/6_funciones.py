# Como crear una funcion
# def nombre_de_la_funcion(parametros)

def saludar():
    print("Hola buenos dias")
    
# Ejecutando una funcion
saludar() #? Hola buenos dias


def saludar2(nombre, apellido, edad):
    print(f"Hola {nombre} {apellido}, tenes {edad} anios!")

saludar2("Stephen", "Curry", "36") #? Hola Stephen Curry!


# -------------------------------------------------------------------------------------------------------------------------------#


# Definir parametro de la funcion por defecto
# Si no ponemos el parametro, por defecto le vamos a asignar un valor
# Esto es un parametro opcional
# Se usan solo en los ultimos parametros

def saludar3(apellido, nombre="invitado"):
    print(f"Hola {nombre} {apellido}")

saludar3("Curry") #? Hola invitado
saludar3("Curry", "Stephen") #? Hola Stephen


# -------------------------------------------------------------------------------------------------------------------------------#


# RETURN
# Devuelve un valor
# La funcion va a pasar a ser el valor returneado

def cuenta(num1, num2):
    resultado1 = num1 + num2
    resultado2 = num1 - num2
    return resultado1, resultado2

valor = cuenta(10, 20)
print(valor[0]) #? 30
print(valor[1]) #? -10

# -------------------------------------------------------------------------------------------------------------------------------#
# FUNCIONES INTEGRADAS O BUILD IN
# -------------------------------------------------------------------------------------------------------------------------------#


# MAX y MIN
# Numero maximo y minimo
numeros = [6,2,9,7,8]
numeroMasAlto = max(numeros)
print(numeroMasAlto) #? 9
numeroMasBajo = min(numeros)
print(numeroMasBajo) #? 2

# -------------------------------------------------------------------------------------------------------------------------------#


# ROUND()
# Redondeando un numero a 6 decimales

# Forma anterior de rendondear decimales
numero = 10.345678
print(round(numero * 100) / 100) #? 10.35

# Forma nueva
print(round(numero,2)) # Primer parametro el numero, el segundo parametro, la cantidad de decimales #? 10.34


# -------------------------------------------------------------------------------------------------------------------------------#


# SUM()

# Suma todos los valores de un iterable

numeoros = [10, 34, 278]
print(sum(numeoros)) #? 322


# -------------------------------------------------------------------------------------------------------------------------------#


# LEN()
# Verifica cuantos caracteres tiene un string o cuantas posiciones tiene un array
texto = "hola"
lista = ["hola", "que", "tal"]
print(len(texto)) #? 4
print(len(lista)) #? 3