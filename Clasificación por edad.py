
print("=== Clasificación por edad ===")
edad = int(input("Ingresa tu edad: "))
if edad < 18:
    print("Menor de edad")
elif 18 <= edad <= 65:
    print("Adulto")
else:
    print("Adulto mayor")
print()