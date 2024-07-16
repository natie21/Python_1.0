#Factorial 5! = 5*4*3*2*1
def factorial():
    from math import factorial
    num=int(input("INgresa un numero entero positivo :"))
    if num>0:
        print(factorial(num))
    else:
        print("El numero es negatyico y no puedo continuar")

factorial()