def menu():
    print("Por favor, elija una opción: ")
    print("1- Registrar un producto")
    print("2- Ver listado de productos")
    print("3- Buscar Producto por su categoría")
    print("4- Calcular promedio de los precios")
    print("5- Salir del programa y guardar productos")
    opcion=int(input("Ingrese su elección: "))
    return opcion

def registro(1):
    plist=[]
    #Debí usar una matriz para esto
    nombre=input("Ingrese el nombre del producto: ")
    categ=input("Ingrese la categoría del producto: ")
    valor=random(10, 1000)
    #No tengo ni idea de como se importa o usa random, ni de como acceder la biblioteca Math
    plist.append(nombre)