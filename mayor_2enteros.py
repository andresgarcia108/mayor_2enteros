#Programa para saber cuál de dos numeros enteros es mayor

#input

print("----------------------------------")
print("Ingrese los dos enteros a comparar")
print("----------------------------------")

x = int(input("Digite el valor de x: " ))
y = int(input("Digite el valor de y: "))

#processing

if x == y:
    print ("Los números son iguales")
else:
    if x > y:
        mayor = x
    else:
        mayor = y

#output
print ("El mayor entre " + str(x) + " y " + str(y) +" es " + str(mayor))