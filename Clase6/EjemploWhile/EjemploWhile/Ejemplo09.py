limiteTable = int(12)
contador = int(1)
cadena = ""
operacion = int
tabla = int(input("Ingrese el numero de tabla a generar\n"))
print("%sTabla de multiplicar\n"%(cadena))
while contador <= 12:
    operacion = tabla * contador
    print("%s%d*%d=%d\n"%(cadena, tabla, contador, operacion))
    contador = contador + 1
print("%s\n"%(cadena))