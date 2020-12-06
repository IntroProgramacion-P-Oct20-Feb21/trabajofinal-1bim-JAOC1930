total = float
porcentaje = float(10)
descuento = float
vKilovatios = float(input("Ingrese el costo de kilovatios por hora "))
kConsumidos = float(input("Ingrese los kilovatios consumidos al mes "))
edad = int(input("Ingrese edad "))
total = vKilovatios * kConsumidos
if edad > 5:
    descuento = (porcentaje * total)/100
    total = total - descuento
print("El valor total a pagar es: ",total)