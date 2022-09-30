def drawPrincipalMenu():
    print("Gestion de inventario")
    print("\t1.-Consultar producto")
    print("\t2.-Agregar producto")
    print("\t3.-Actualizar cantidad")
    print("\t4.-Actualizar precio de costo")
    print("\t5.-Actualizar precio publico")
    print("\t6.-Desechar producto")
    print("\t7.-Vender")
    print("\t8.-Consultar ganancias")
    print("\t9.-Salir")
    choice = input("Opcion: ")
    if(choice.isnumeric()):
        return int(choice)
    else:
        return choice