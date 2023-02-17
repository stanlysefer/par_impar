#programa para verificar si el numero es par o impar

#input
x=int(input("Digite un numero: "))

r = x%2
#processing

if r==0:
    msj= "PAR"
else:
    msj= "IMPAR"

print("el numero " + str(x) + " es " + msj)