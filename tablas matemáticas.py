def suma_tabla(n):
    for i in range(1, 11):
        print(f"{n} + {i} = {n + i}")

def resta_tabla(n):
    for i in range(1, 11):
        print(f"{n} - {i} = {n - i}")

def multiplicacion_tabla(n):
    for i in range(1, 11):
        print(f"{n} × {i} = {n * i}")

def division_tabla(n):
    for i in range(1, 11):
        if i != 0:
            print(f"{n} ÷ {i} = {n / i:.2f}")
        else:
            print("No se puede dividir por 0")

def main():
    print("=== Tablas matemáticas ===")
    numero = int(input("Ingresa un número: "))
    print("Operaciones disponibles: suma, resta, multi, div")
    operacion = input("Selecciona operación: ").lower()

    if operacion == "suma":
        suma_tabla(numero)
    elif operacion == "resta":
        resta_tabla(numero)
    elif operacion == "multi":
        multiplicacion_tabla(numero)
    elif operacion == "div":
        division_tabla(numero)
    else:
        print("Operación no válida")

if __name__ == "__main__":
    main()