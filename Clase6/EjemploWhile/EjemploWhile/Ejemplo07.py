sumaTotal = float(0)
bandera = bool(True)
contador = int(0)
promedio = float
print("Ingrese las notas de los estudiantes de su materia ")
while bandera:
    calificacion = float(input("Ingrese calificacion\n"))
    sumaTotal = sumaTotal + calificacion
    contador = contador + 1
    temporal = int(input("Ingrese el valor de -1 para salir del ciclo\n"))
    if temporal == -1:
        bandera = False
promedio = sumaTotal / contador
print("El promedio final es: %.2f\n"%(promedio))