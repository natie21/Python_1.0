lista1=[]
num=0
def pedirNum():
    i=0
    while i<=5:
        num=int (input("Ingresa un numero :"))
        lista1.append(num)
        i+=1

def Ordenar():
    lista1.sort()
    pares=[]
    impares=[]
    for i in lista1:
        if i % 2 ==0:
            pares.append(i)
        else:
            impares.append(i)
    print("Lista de pares :" , pares)
    print("Lista de impares :" , pares)

pedirNum()
Ordenar()
   
    