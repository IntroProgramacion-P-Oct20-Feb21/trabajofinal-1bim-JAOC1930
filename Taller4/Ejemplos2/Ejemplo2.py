area = float
costoTerreno = float
largo = float(input("Ingrese el largo del terreno "))
ancho = float(input("Ingrese el ancho del terreno "))
costoMetro = float(input("Ingrese el costo de metros cuadrado del terreno "))
nombreComprador = input("Ingrese el nombre del comprador ")
area = largo * ancho
costoTerreno = area * costoMetro
print("El costo del terreno es: %.2f y el comprador es: %s"%(costoTerreno,nombreComprador))