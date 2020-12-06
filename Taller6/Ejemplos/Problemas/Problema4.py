contador = 1
cadena = ""
while contador <= 10 :
    nombre = input("Ingrese el nombre del jugador: ")
    cpuntos = int(input("Ingrese la cantidad de puntos anotados: "))
    cfaltas = int(input("Ingrese la cantidad de faltas cometidas: "))
    contador = contador + 1
    cadena = "%s\t%s\t%d\t%d\n" %(cadena, nombre, cpuntos, cfaltas)
print(cadena)    