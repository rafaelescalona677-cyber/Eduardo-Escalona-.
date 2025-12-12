def mostrar_menu():
    print("\n=== Menú Interactivo ===")
    print("1) Saludar")
    print("2) Calcular suma")
    print("3) Salir")

def opcion_saludar():
    print("¡Hola! Bienvenido al programa.")

def opcion_calcular():
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        resultado = num1 + num2
        print(f"La suma de {num1} + {num2} es: {resultado}")
    except ValueError:
        print("Por favor, ingresa valores numéricos válidos.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ").strip()
        
        if opcion == "1":
            opcion_saludar()
        elif opcion == "2":
            opcion_calcular()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()