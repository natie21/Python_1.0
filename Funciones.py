"""
num="70"
list=[12,23,1,4,7,45]
print(type(int(num)))#Convierte a entero
print(type(float(num)))#Convierte a float
print(len(list))#Tamaño de la lista
print(max(list))#numero ma grande de la loista .min umero menor
"""
def saludar():
    print("Hola mundo")

saludar()#Mandar a llamar a la funcion
def tabla7():
    for i in range(10 + 1):
        print("7 x {} = {}".format(i,i*7))
tabla7()