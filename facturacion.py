def factura(lista, plato, precio):
    totalNota = 0
    for i in range(len(lista)):                 # Comparamos el pedido del cliente con la carta
        for j in range(len(plato)):
            if plato[j] == lista[i]:
                totalNota += float(precio[j])   # Si existe coincidencia, se acumula el precio del plato

    return totalNota                            # Devolvemos el total acumulado a la página principal,
                                                # para mostrar el resultado