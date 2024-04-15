def filtro(m):
    lista_filtrada = []
    for i in m:
        if int(i)%3 == 0:
            lista_filtrada.append(i)
    return lista_filtrada
            

velocidades = ["150000", "500", "300", "1200", "690", "300"]
masas = ["1000", "900", "300", "69", "1200", "600"]

print(filtro(masas))