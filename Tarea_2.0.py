def Mayor_menor() :
    num1=int(input("Ingresa el primer numero :"))
    num2=int(input("Ingresa el segundo numero :"))
    if num1>num2:
        print("1")
    elif num2>num1:
        print("-1")
    else:
        print(0)


# variable.strip(): verifica que haya valores en la variable
def Factura():
    while True:
      try:   
        precio=float(input("Ingrese el precio al que se le agregara el IVA:"))
        break
      except:
        print("Ingresate un valor erroneo")

    iva=int(input("Ingrese el IVA que se agregara:"))

    if iva !=0:
        if iva>0:
            total=((precio*iva)/100)+precio
            return total
        else:
            print("El iva no puedes ser menor a 0 ingresa otro porcentaje")
    else:
        total=((precio*0.21)/100)+precio
        return total
 

Mayor_menor()

print("El monto de su factura es :",Factura())