peso = float(input("Peso en kg: "))
altura = float(input("Altura en m: "))
imc = round(peso / altura**2, 2)
print("Tu IMC es", imc)
