# Como crear una funcion
# def nombre_de_la_funcion(parametros)

def saludar():
    print("Hola buenos dias")
    
# Ejecutando una funcion
saludar() #? Hola buenos dias


def saludar2(nombre):
    print(f"Hola {nombre}!")

saludar2("Stephen") #? Hola Stephen!


# -------------------------------------------------------------------------------------------------------------------------------#


# Definir parametro de la funcion por defecto
# Si no ponemos el parametro, por defecto le vamos a asignar un valor

def saludar3(nombre="usuario"):
    print(f"Hola {nombre}")

saludar3() #? Hola usuario
saludar3("Camilo") #? Hola Camilo


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