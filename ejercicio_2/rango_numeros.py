"""Ejercicio  No. 2
Programa que dado un rango de números enteros , obtiene la cantidad de números que contiene"""

c = 0

print("Ingrese el primer número del rango: ")
xi=int(input())
print(("Ingrese el último número del rango: "))
xf=int(input())

c = 0 
i=xi+1

if xi<xf:
    while i<xf:
        i=i+1

        c=c+1
        print(xi+c)
else:
    print("el xi debe ser menor que xf")

print("La cantidad de números es: " + str(c))
