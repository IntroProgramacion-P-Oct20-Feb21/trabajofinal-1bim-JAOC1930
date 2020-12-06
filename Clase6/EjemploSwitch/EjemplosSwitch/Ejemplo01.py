resultado = int(0)
valor1 = int(input("Ingrese el primer valor de la operaciom "))
valor2 = int(input("Ingrese el segundo valor de la operacion "))
cp = int(input("Selecciona la operacion que desea realizar\n Ingrese 1 para sumar\n"
+"Ingrese 2 para restar\n Ingrese 3 para multiplicar "))
if cp is 1:
    resultado = valor1 + valor2
elif cp is 2:
    resultado = valor1 - valor2
elif cp is 3:
    resultado = valor1 * valor2
else:
    print("Operacion incorrecta")
print("El resultado de la opecion es: ",resultado)