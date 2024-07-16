conjunto=set((1,1,2,2,3,4,5,6))#set convierte a conjunto,conjuto no toma valores repetidos conjunto={}
lista=[1,1,2,3,4,4]#Si permite datos repetidos
print(conjunto)
print(lista)
conjunto.add(20)
conjunto.remove(1)#quitra un elemento
conjunto.discard(1)#quitra un elemento
conjunto.pop()#Elimina elemento aleatorio
print(conjunto)
conjunto.update([1,2,7])#Envia y agrega datos que no esten
print(conjunto)
#conjunto1 & conjunto2 : la interseccion
#conjunto1 | conjunto2 : se unen quitando los elementos repetidos
#conjunto1 .issubset(conjunto2)  : si es subconjuntos