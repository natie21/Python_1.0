"""
try:
    edad=int(input("INgresa tu edad :"))
    print("Tu edad es:",edad)
except:
    print("INgresaste un valor erroneo")#Se muestra si no se ingresa lo deseado
    #while true: se repite ,se puede parar con un break
"""

#EXCEPCIONES MULTIPLES
'''
while True:
    try:
        num1=int(input("Ingresa un numero"))
        resultado=100/num1
        print(resultado)
        break
    except ZeroDivisionError: #indica que no se puede dividir entre cero
        print("No se puede dividir entre 0")
'''
while True:
    try:
        edad=int(input("Ingresa tu edad :"))
        print("Tu edad es:", edad)
        break
    except ValueError: #indica que el vaor es erroneo; except KeyboardInterrupt "has cancelado la ejecucuon"
        print("valor erroneo")

