def convertir_celsius_a_fahrenheit():
    try:
        celsius = float(input("Ingresa temperatura en Celsius: "))
        fahrenheit = (celsius * 9 / 5) + 32
        print(f"{celsius}°C equivalen a {fahrenheit:.1f}°F\n")
    except ValueError:
        print("Por favor, ingresa un número válido.\n")

print("=== Conversor Celsius a Fahrenheit ===")
convertir_celsius_a_fahrenheit()