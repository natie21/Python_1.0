"""
tupla=(1,2,3,4,5,6,7,8)#"NO SE PUEDEN ALTERAR LOS CARACTERES"
tupla2=(9,10,11)
print(type(tupla))
print(tupla[2])
print(tupla[2:6])
print(tupla + tupla2)#Concatena ambas tuplas
"""

#"EJERCICIO 1"
meses=("Enero","Febrero","Marzo","Abril","Mayo","Junio",
       "Julio","Agosto","Septimebre","Octubre","Noviembre","Diciembre")
mes=int(input("Ingresa un numero del 1 al 12 :"))
if mes==1:
    print(meses[0])
elif mes==2:
    print(meses[1])
elif mes==3:
    print(meses[2])
elif mes==4:
    print(meses[3])
elif mes==5:
    print(meses[4])
elif mes==6:
    print(meses[5])
elif mes==7:
    print(meses[6])
elif mes==8:
    print(meses[7])
elif mes==9:
    print(meses[8])
elif mes==10:
    print(meses[9])
elif mes==11:
    print(meses[10])

else:
    print(meses[11])
    #"EJERCICIO 2"
    alfabeto=("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
              "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" )
    num=int(input("Ingresa un numero :"))
   