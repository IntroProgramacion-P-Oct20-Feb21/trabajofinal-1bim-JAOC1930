cadena = ""
while True:
    nota = float(input("Ingrese calificaciones "))
    cadena = "%s%.2f\n" %(cadena, nota)

    salida = int(input("Ingrese '-111' para salir del ciclo "))
    if salida == -111:
        break
print("Listado de notas \n%s \n"%(cadena))    
