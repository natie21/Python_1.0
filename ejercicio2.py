print("******EJERCICIO 1******")
a=-2
b=6
c=5
dis= ((b)**2)-(4*a*c)
#res=dis / (2*a)
raiz= dis**0.5
x1= (-b+raiz)/(2*a)
x2=(-b-raiz)/(2*a)
print("El valor de x1 es = ", x1 )
print("El valor de x2 es = ", x2 )
print("*******EJERCICIO 2**********")
p1=3.0
p2=3.0
p3=3.0
PP=(p1+p2+p3)/3
EP=10
EF=10
PROM=( PP + 2*EP + 3*EF)/6
print("El promedio final es :", PROM)

print("********EJERCICIO 3**********")
vocal=input("Ingresa una vocal en minusculas :")
print (vocal.upper())
letra=input("Ingresa una letra mayuscula :")
print(letra.lower())
print(vocal, letra)
print("********EJERCICIO 4**********")
nombre=input("Ingresa tu nombre :")
sexo=input("Cuál es tu sexo ?")
edad=int(input("Ingresa tu edad :"))
print("Te llamas: < ", nombre ,">")
print("Tu edad es: < ", edad ,">")
print("Eres: < ", sexo ,">")
