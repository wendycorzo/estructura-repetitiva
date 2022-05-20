a=int(input("Escribe el valor de a: "))
b=int(input("Escribe el valor de b: "))


if a<b:
   cant_num=0
   a=a+1
   while(a<b):
       r= a%2
       if r ==0:
          cant_num=cant_num+1
       a=a+1
   print("La cantidad de numero es" , cant_num)
else:
    print("a debe ser menor que b ")
