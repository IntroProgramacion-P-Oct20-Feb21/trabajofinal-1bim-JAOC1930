limiteInferior = int(10)
limiteSuperior = int(20)
contador = int(10)
suma = int(0)
while (contador >= limiteInferior) & (contador <= limiteSuperior):
    suma = suma + contador
    print("Contador %d\n"%(contador))
    contador = contador + 1
print("La suma final es %d\n"%(suma))
