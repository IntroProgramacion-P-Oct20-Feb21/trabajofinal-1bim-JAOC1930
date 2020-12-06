contador = 1
cadena = ""
while True:
    cadena = "%s Tabla de mulltiplicar del %d\n" %(cadena, contador)
    for i in range (1,11) :
        operacion = i * contador
        cadena = (" %s%d x %d = %d\n" %(cadena, contador, i, operacion))
    cadena = "%s\n" %(cadena)
    contador = contador + 1 
    if contador >= 6:
        break
print("%s" %(cadena))    
