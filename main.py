from carta import platos            # Documento con la función que permite añadir platos a la carta
from pedido import comanda          # Documento con la función que realiza el pedido
from facturacion import factura     # Documento con la función que calcula el total de lo consumido

if __name__ == '__main__':
    plato, precio = platos()
    pedido = comanda(plato, precio)
    total = factura(pedido, plato, precio)
    print("")
    print("El total de la nota asciende a: " + str(total) + "€")