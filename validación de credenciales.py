print("=== Validación de credenciales ===")
USUARIO_CORRECTO = "admin"
CONTRASENA_CORRECTA = "0902"
intentos_maximos = 4
for intento in range(intentos_maximos):
    usuario = input("Ingrese su usuario: ")
    contrasena = input("Ingrese su contraseña: ")
    
    if usuario == USUARIO_CORRECTO and contrasena == CONTRASENA_CORRECTA:
        print("¡Acceso concedido!")
        break
    else:
        intentos_restantes = intentos_maximos - (intento + 1)
        print(f"Credenciales incorrectas. Intentos restantes: {intentos_restantes}")
else:
    print("Acceso bloqueado.\n")