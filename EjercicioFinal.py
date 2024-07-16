def calificaciones(lista):
    final={}
    print(lista)
    #Retornar la edad
    for i in range (len(lista)):
     print("La edad de",lista[i]["Nombre"], " es :", lista[i]["Edad"])
     print("La calificacion de",lista[i]["Nombre"], " es :", lista[i]["Calificaciones"]/10) 
     final.update("Nombre","Nat")
     
   

    






lista=[]
lista.append({"Nombre":"Natalie","Edad":17,"Calificaciones":100})
lista.append({"Nombre":"Juan","Edad":27,"Calificaciones":90})
calificaciones(lista)

