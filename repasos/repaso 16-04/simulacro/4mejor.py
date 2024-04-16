# 1 linea
print(list(map(lambda c, n: float(c) / n, ["3000", "500", "1000", "1200", "500", "1200"], list(map(lambda p, s: float(p) * float(s), ["5", "6", "8", "9", "10", "12"], ["0.1", "0.3", "0.4", "0.01", "0.3", "0.3"])))))

# 2 lineas
resultado = list(map(lambda c, n: float(c) / n, ["3000", "500", "1000", "1200", "500", "1200"], list(map(lambda p, s: float(p) * float(s), ["5", "6", "8", "9", "10", "12"], ["0.1", "0.3", "0.4", "0.01", "0.3", "0.3"]))))
print(resultado)