sumaTotal = float(0)
bandera = bool(True)
print("Ingrese las notas de los estudiantes de su materia ")
while bandera:
    calificacion = float(input("Ingrese calificacion\n"))
    sumaTotal = sumaTotal + calificacion
    temporal = int(input("Ingrese el valor de -1 para salir del ciclo\n"))
    if temporal == -1:
        bandera = False
print("La sumna de las calificaciones es: %.2f\n"%(sumaTotal))