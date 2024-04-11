# Suma y resta (+ y -)
suma = 10 + 1
resta = 5 - 3

# Multiplicacion y division (* y /)
multi = 10 * 10
division = 12 / 5 # La division siempre devuelve un dato float

# Potenciacion (Exponente **)
potencia = 10**2

# Division baja (//)
division_baja = 12//5 # Devuelve un int, 12/5 es 2.4 pero solo devuelve enteros, por ende devuelve 2

# Modulo o resto (%)
modulo = 14 % 5 # Devuelve un int del resto de la division


print(modulo) #? 2


# La funcion type nos indica que tipo de dato es
tipo_de_dato = type(5.6)
print(tipo_de_dato)


# -------------------------------------------------------------------------------------------------------------------------------#


igual_que = 5 == 6 # Con el primer igual definimos la variable, con los dos iguales comparamos
distinto_que = 5 != 6
mayor_que = 5 > 6
menor_que = 5 < 6
mayor_igual_que = 5 >= 6
menor_igual_que = 5 <= 6

print(igual_que) #? False


# -------------------------------------------------------------------------------------------------------------------------------#


#AND Devuelve verdadero si ambas condiciones se cumplen

resultado = True & True
resultado = True and True

#OR Devuelve verdadero si alguna condicion se cumple, si no se cumple ninguna se devuelve falso

resultado2 = True | False
resultado2 = True or False

#NOT Invierte el valor

resultado3 = not True


print(resultado) #? True
print(resultado2) #? True
print(resultado3) #? False

if 5 > 4 or 5 == 5 or 3 > 2:
    print("SI")