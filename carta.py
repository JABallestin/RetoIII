def platos():
    plato = []
    precio = []

    for i in range(100):
        plato.append(input("Introduce el plato nº" + str(i + 1) +": "))         # Introduciendo el plato en la lista
        precio.append(input("Introduce su precio: "))                           # Introduciendo el precio del plato en la lista
        decision = input("¿Deseas seguir añadiendo platos a la carta? (s/n): ") # Se interroga al usuario por si quiere añadir
                                                                                # más platos (y precios a las listas)
        if decision == "n":
            break

    return plato, precio