multiplicacion2valores = lambda lista1, lista2: [x*z for x,z in zip(lista1,lista2)]

densidades = ["5000", "1600", "760", "3000000", "810", "1000"]
coeficientes = ["0.001", "0.004", "0.0076", "0.0000003", "0.01", "0.01"]

densidades = [float(i) for i in densidades]
coeficientes = [float(i) for i in coeficientes]

print(multiplicacion2valores(densidades, coeficientes))