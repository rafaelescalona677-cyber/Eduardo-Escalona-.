def crear_lista_compras():
    print("\n=== Lista de compras ===")
    lista = []
    while True:
        producto = input("Añade un producto (o escribe 'fin' para terminar): ").strip()
        if producto.lower() == 'fin':
            break
        if producto:  # Evitar agregar entradas vacías
            lista.append(producto)
    return lista

def mostrar_lista(lista):
    print("\nTu lista de compras:")
    for idx, item in enumerate(lista, start=1):
        print(f"{idx}. {item}")

# Uso del programa
lista_compras = crear_lista_compras()
mostrar_lista(lista_compras)