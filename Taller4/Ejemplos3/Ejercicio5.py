total = float
mPrestamo = float(input("Ingrese el monto del prestamo "))
interesMensual = float(input("Ingrese el interes mensual "))
total = (mPrestamo/12)+interesMensual
print("El costo al mes es: \n%.2f"%(total))