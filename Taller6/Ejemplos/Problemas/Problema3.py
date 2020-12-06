contador = 1
cadena = ""
while contador <= 5:
    nombre = input("Ingresar el nombre del empleado: ")
    nDias = int(input("Ingrese el número de días trabajos: "))
    cDias = float(input("Ingrese el costo del día trabajado: "))

    totalp = nDias * cDias
    cadena = "%s\t%s\t%d\t%.2f$\t%.2f$\n" %(cadena,
    nombre, nDias, cDias,totalp)
    contador = contador +1
print(cadena)