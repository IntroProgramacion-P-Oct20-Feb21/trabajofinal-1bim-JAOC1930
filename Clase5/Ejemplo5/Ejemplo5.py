porcentaje1 = float(10)
porcentaje2 = float(15)
porcentaje3 = float(20)
subtotal = float
valorTotal = float
descuento = float
numeroDias = float(input("Ingrese el numero de dias que se hospedará "))
precioHabitacion = float(input("Ingrese el valor diario de la habitacion "))
if (numeroDias > 5) & (numeroDias <=10):
    subtotal = numeroDias * precioHabitacion
    descuento = (porcentaje1 * subtotal)/100
    valorTotal = subtotal - descuento
else:
    if (numeroDias > 10) & (numeroDias <=15):
        subtotal = numeroDias * precioHabitacion
        descuento = (porcentaje2 * subtotal)/100
        valorTotal = subtotal - descuento
    else:
        if numeroDias > 15:
            subtotal = numeroDias * precioHabitacion
            descuento = (porcentaje3 * subtotal)/100
            valorTotal = subtotal - descuento
        else:
            subtotal = numeroDias * precioHabitacion
            descuento = 0
            valorTotal = subtotal - descuento
print("El valor subtotal es: %.2f\n El decuento es: %.2f\n El valor total a pagar es: %.2f"%(subtotal, 
descuento, valorTotal))
