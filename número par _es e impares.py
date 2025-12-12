print("=== Números pares e impares (1-20) ===")

pares = []
impares = []

for i in range(1, 21):
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

for p in pares:
    print(f"{p} es par")

for imp in impares:
    print(f"{imp} es impar")

print()