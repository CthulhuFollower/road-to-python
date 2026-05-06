nombres = ["Julian", "Julio", "Alfredo", "Miguel", "Kike", "Miguel"]
numeros_locos = [12, 8, 32, 1, 4, 9, 23]

nombres_numeros = nombres + numeros_locos

nombres.append("pepe")
nombres.insert(0, "Guerrilla")
nombres.insert(0, "Zero")
nombres.remove("Kike")

print(nombres.pop())


print(nombres.index("Julio"))
print(nombres.count("Miguel"))
print(nombres)
print(numeros_locos)
print(nombres_numeros)

print(nombres_numeros.clear())