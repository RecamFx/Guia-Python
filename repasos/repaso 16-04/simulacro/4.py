def labo(p,s,c):
    nueva_lista = []
    for i in range(len(p)):
        nueva_lista.append(float(p[i]) * float(s[i]))
    nueva_lista2 = []
    for i in range(len(c)):
        nueva_lista2.append(float(c[i])/float(nueva_lista[i]))
    return nueva_lista2

primero = ["5", "6", "8", "9", "10", "12"]
segundo = ["0.1", "0.3", "0.4", "0.01", "0.3", "0.3"]
cuarto = ["3000", "500", "1000", "1200", "500", "1200"]

print(labo(primero, segundo, cuarto))