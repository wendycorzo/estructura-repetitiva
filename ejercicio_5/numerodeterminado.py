número = int(input("ingrese el número: "))
contador=0

while número>0:
    número=número//10
    contador=contador+1

print("El número ingresado tiene " + str(contador) + " digitos ")