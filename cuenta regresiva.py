def cuenta_regresiva(n):
    if n < 0:
        print("¡FIN!\n")
    else:
        print(n)
        cuenta_regresiva(n - 1)

print("=== Cuenta regresiva ===")
numero = int(input("Ingresa un número entero para cuenta regresiva: "))
cuenta_regresiva(numero)