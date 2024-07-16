"""
def argumentos(*num):#El * indica que los datos se guardaran enn una tupla
    print(num)
    return type(num)

print(argumentos(10,20,30,40,50))
"""
#Ejercicios

def AreaCuadrado(b,h):
    area=b*h
    return area

def AreaCirculo(r):
    area=2.1416*r**2
    return area

def tamano(*lista):
   return len(lista)

base=float(input("Ingrese la longitud de la base del cuadrado:"))
altura=float(input("Ingrese la longitud de la altura del cuadrado:"))
print(AreaCuadrado(base,altura))
radio= float(input("INgrese el radio del circulo :"))
print(AreaCirculo(radio))


print("El tamaño de la lista es:",tamano(1,2,3,4,5,6,7,8))



