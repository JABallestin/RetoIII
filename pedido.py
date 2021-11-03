def comanda(plato, precio):
    # Declarando e inicilizando variables billetes
    cinco = diez = veinte = cincuenta = cien = doscientos = quinientos = 0
    decision = True
    lista = []
    # Se da la oportunidad al usuario de dejar de pedir en el momento que lo desee
    while decision == True:
        encontrado = False
        print("")
        # Se muestra toda la carta cada vez para que el usuario elija
        for i in range(len(plato)):
            print(plato[i] + ": " + precio[i] + "€")

        # Se pide que el usuario intruzca un plato y se compara con las entradas de la carta
        platos = input("¿Que desea comer?:")
        for j in range(len(plato)):
            # Si existe coincidencia se añade a la lista
            if platos == plato[j]:
                encontrado = True
                lista.append(platos)

        # Si no existe coincidencia se avisa de ello y el plato no se añade a la lista
        if encontrado == False:
            print("El plato insertado no existe en la carta")
        else:
            # Se brinda la oportunidad de seguir añadiendo platos a la lista
            opcion = input("¿Desea seguir añadiendo platos a la lista? (s/n):")
            # Si se contesta que no se desean añadir más platos el bucle se interrumpe y se restorna la lista
            if opcion == "n":
                decision = False
                return lista