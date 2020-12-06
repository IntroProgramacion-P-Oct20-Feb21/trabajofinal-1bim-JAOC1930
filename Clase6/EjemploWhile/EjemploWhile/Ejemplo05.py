limite = int(3)
contador = int(1)
sumaTotal = int(0)
promedioFinal = float
print("Ingrese las notas de los estudiantes en su materia ")
while contador <= limite:
    calificacion = float(input("Ingrese calificacion numero %d\n"%(contador)))
    sumaTotal = sumaTotal + calificacion
    contador = contador + 1
promedioFinal = sumaTotal / limite
print("El promedio final es: %.2f\n"%(promedioFinal))
