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

velocidades = ["150000", "500", "300", "1200", "690", "300", "1201"]
masas = ["1000", "900", "300", "69", "1200", "600", "2"]

cuenta2(velocidades,masas)