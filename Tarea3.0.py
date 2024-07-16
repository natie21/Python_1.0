def division(n1,n2):
    try:
      resultado=n1/n2
      return resultado
    except ZeroDivisionError:
        return"No se puede divir entre 0"
    except ValueError:
      return"ingresa valores numericos"
    return resultado

n1=int(input("Ingrese un numero :"))
n2=int(input("Ingrese un numero :"))
print(division(n1,n2))
#Dentro del if se manda excepcion con un return

#Ejercicio2