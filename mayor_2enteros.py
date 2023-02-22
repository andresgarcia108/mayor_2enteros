#Programa para saber cuál de dos numeros enteros es mayor

#input

print("----------------------------------")
print("Ingrese los dos enteros a comparar")
print("----------------------------------")

x = int(input("Digite el valor de x: " ))
y = int(input("Digite el valor de y: "))

#processing

if x > y:
    msj = " es mayor que "
elif x < y:
    msj = " es menor que "
else:
    msj = " es igual que "

#output

print("El número " + str(x) + msj + str (y))



