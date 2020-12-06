contador= 1 
cadena = ""
while contador <=4:
    nombre = input("Ingresar el nombre del estudiante: ")
    promedio = float(input("Ingrese el promedio del estudiante: "))
    if promedio >=7:
        cadena = "%s\t%s\t%.2f\t%s\n" %(cadena, nombre, promedio, "Aprobado")
    else:
        cadena = "%s\t%s\t%.2f\t%s\n" %(cadena, nombre, promedio, "Reprobado")
    contador = contador +1    
print(cadena)        
