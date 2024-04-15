def cuenta(v, m):
    coeficientes = []
    coeficientes2 = []
    v2 = []
    for i in range(len(v)):
        c = int(v[i])/int(m[i])
        if int(v[i]) > 1200:
            coeficientes2.append(0)
            v2.append(0)
            continue
        coeficientes.append(str(c))
        coeficientes2.append(str(c))
        v2.append(v[i])
    return sorted(coeficientes, reverse=True), coeficientes2, v2

def cuenta2(v,m):
    valor = cuenta(v,m)
    for i in range(len(valor[1])):
        print(f"Coeficiente: {valor[1][i]}, Velocidad: {valor[2][i]}")

def filtro(m):
    lista_filtrada = []
    for i in m:
        if int(i)%3 == 0:
            lista_filtrada.append(i)
    return lista_filtrada

velocidades = ["150000", "500", "300", "1200", "690", "300", "1201"]
masas = ["1000", "900", "300", "69", "1200", "600", "2"]

# ----------------------------------------------------------------------------------------- #

# EJERCICIO 1
print(cuenta(velocidades,masas)[0])

#? ['17.391304347826086', '1.0', '0.575', '0.5555555555555556', '0.5']


# SEPARACION
print()
print("---------------------------------------------------------")
print()


# ----------------------------------------------------------------------------------------- #


# EJERCICIO 2
cuenta2(velocidades,masas)

#? Coeficiente: 0, Velocidad: 0
#? Coeficiente: 0.5555555555555556, Velocidad: 500
#? Coeficiente: 1.0, Velocidad: 300
#? Coeficiente: 17.391304347826086, Velocidad: 1200
#? Coeficiente: 0.575, Velocidad: 690
#? Coeficiente: 0.5, Velocidad: 300
#? Coeficiente: 0, Velocidad: 0


# SEPARACION
print()
print("---------------------------------------------------------")
print()


# ----------------------------------------------------------------------------------------- #


# EJERCICIO 3

print(filtro(masas))

#? ['900', '300', '69', '1200', '600']