contador = 1
cadena =""
tipodeOperacion=input("Indique qué tipo de tabla quiere realizar\n"
+"suma\n"
+"o\n"
+"multiplicación: \n")
numeroTabla = int(input("Ingresar el número de tabla: \n"))
limiteTabla = int(input("Ingresar el límite de tabla: \n"))

if tipodeOperacion == "suma":
    cadena = "%s%s\n" %(cadena, "Tabla de sumar")
    while contador <= limiteTabla:
        operacion = numeroTabla + contador
        cadena = "%s%d + %d = %d\n" %(cadena, numeroTabla,
        contador, operacion)
        contador = contador + 1
elif tipodeOperacion == "multiplicación":
    cadena = "%s%s\n" %(cadena, "Tabla de multiplicar")
    while contador <= limiteTabla:
        operacion= numeroTabla * contador
        cadena = "%d%d*%d = %d\n" %(cadena, numeroTabla,
        contador, operacion)
        contador = contador + 1
else:
    cadena = "%s%s\n"%(cadena, "Error en tipo de operación") 
print("%s\n"%(cadena))       