contador = 0
sumat = 0
cadena = ""
while True:
    nota = float(input("Ingresar calificacion: "))
    cadena = "%s%.2f\n" %(cadena, nota)
    sumat = sumat + nota
    salida = input("Si desea salir del cilo ingrese 'Si' o 'S': ")
    contador = contador + 1
    if (salida == "S") or (salida =="Si"):
        break
promedio = float(sumat / contador)
print("Listado de Notas:\n%s\nPromedio:\n%.2f" %(cadena, promedio))    
