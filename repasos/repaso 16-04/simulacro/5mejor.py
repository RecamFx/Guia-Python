# 1 linea
print([s*v for s,v in zip([int(a1) for a1 in ["1000", "760", "1200"]], [int(a1) for a1 in ["300", "600", "9000"]])])

# 2 lineas
funcion = lambda S,V: [s*v for s,v in zip([int(a1) for a1 in S], [int(a1) for a1 in V])]
print(funcion(["1000", "760", "1200"], ["300", "600", "9000"]))