#ejericio1
for i in range(1,11):
    print(i)

n1=int(input("Ingresa un numero :"))
n2=int(input("Ingresa otro numero :"))
for i in range(n1,n2 +1):
    print(i)





#pedir dos numeros al usuario
num1=int(input("Ingresa el primer numero"))
num2=int(input("Ingresa el segundo numero"))

for i in range(num1,num2 +1):#+1 poeque el range se salta un lugar
    if i % 2==0:
        continue
    print(i)