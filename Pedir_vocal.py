letra=input("Ingresa una letra :")
if letra.lower()=="a":
    print("Es vocal")
elif letra.lower()=="e":
    print("Es vocal")
elif letra.lower()=="i":
    print("Es vocal")
elif letra.lower()=="o":
    print("Es vocal")
elif letra.lower()=="u":
    print("Es vocal")
else:
    print("La letra que ingresaste NO es vocal")
print("////////////////EJERCICIO 2/////////////////")
num=int(input("Ingresa un número :"))
if num >=1 :
    print("El valor absoluto de ", num, "es: ", num)
elif num<0:
    abs=num*-1


    print("El valor absoluto de ", num, "es: ", abs)
    #Ejercicio rimas
print("///////////////////////EJERCICIO 3////////////////////////")
print("'Ingresa dos palabras'")
p1=input("Primer palabra :")
p2=input("Segunda palabra :")

if p1[-3:]==p2[-3:]:
    print("Las palabras ingresadas riman")
elif p1[-2:]==p2[-2:]:
    print("Las palabras ingresadas riman un poco")
else :
    print("Las palabras No riman")
print("///////////////////////EJERCICIO 4////////////////////////")
print("Partidos disponibles :\nA) Rojo.\nB) Verde.\nC) Azul.")
op=input("Elija el partido que desee:")

if op.upper()=='A':
    print("Usted ha votado por el partido ROJO")
elif op.upper()=='B':
    print("Usted ha votado por el partido VERDE")
elif op.upper()=='C':
    print("Usted ha votado por el partido ROJO")
else:
    print("Opción inválida seleccione otra")

    
   