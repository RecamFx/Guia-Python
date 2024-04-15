def cuenta(v, m):
    coeficientes = []
    for i in range(len(v)):
        c = int(v[i])/int(m[i])
        if int(v[i]) > 1200:
            continue
        coeficientes.append(str(c))
    return sorted(coeficientes, reverse=True)

velocidades = ["150000", "500", "300", "1200", "690", "300"]
masas = ["1000", "900", "300", "69", "1200", "600"]

print(cuenta(velocidades, masas))