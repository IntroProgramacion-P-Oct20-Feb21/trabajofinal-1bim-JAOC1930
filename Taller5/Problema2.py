total = float
porcentaje = float(15)
descuento = float
cantidad = float(input("Ingrese la cantidad solicitada "))
precioUni = float(input("Ingrese el precio unitario del producto "))
total = cantidad * precioUni
if cantidad > 50:
    descuento = (total * porcentaje)/100
    total = total * descuento
print("El valor a pagar es: ",total)