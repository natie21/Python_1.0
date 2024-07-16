dicc={"Saludo" : "Hola","Usuario" : "Natalie", "Contra" : 1234}
      #clave      valor
"""
print(dicc.keys())#Devuelve las claves
print(dicc.values())#devuelve todos los valores)
print (dicc["Usuario"])#Devuelve el vaor que guarda la clave
dicc["Peso"]="50 kg"#clave/valor se guarda y agrega en el diccionario
dicc["Usuario"]="Nat"#Cuando ya esta la clave solo modifica el valr
print(dicc)
"""
#Metodos
diccionario={1 : 10, 2 : 20, 3 : 30}
diccionario.pop(1)#elimina la clave que le mandas
print(diccionario)
#diccionario.clear()#lo deja vacio
#print(diccionario)
diccionario.get(2)#Trae el valor de esa clave insertada
print(diccionario)
diccionario.setdefault(4,40)#AGREGA la llave y el valor correspondiente
print(diccionario)
#diccionario.update(1,15)#enviarle otro diccionario,y los junta y actualiza en caso
#de que se repitan las claves
diccionario.copy()#saca una copia del diccionario
#del : elimina un conjunto que esta asociado con una clave