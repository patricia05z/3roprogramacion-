import math

a= float(input("ingrese valor de a:"))
b= float(input("ingrese valor de b:"))
c= float(input("ingrese valor de c:"))

if a == 0:  
    print("no es una ecuacion de segundo grado")
     
else:
    discriminante = b**2 - 4*a*c 
    
    if discriminante > 0 :
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        print(f"la solucion son:x1 {x1} y x2 = {x2}")
    elif discriminante ==0:
        x= -b / (2*a)
        print(f"la resolucion es unica es: x = {x}")

    else:
        print("la ecuacion no tiene soluciones reales")
        