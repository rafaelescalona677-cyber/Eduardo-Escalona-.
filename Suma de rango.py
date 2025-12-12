print("=== Suma de rango con for ===")
inicio = int(input("Ingresa número inicial: "))
fin = int(input("Ingresa número final: "))
suma = 0
for i in range(inicio, fin + 1):
    suma += i
print(f"La suma de {inicio} a {fin} es: {suma}\n")