while True:
    print("***********Menu de conversiones ***********")
    print("1.Convertir a <Euro>")
    print("2.Convertir a <Dolar>")
    print("3.Convertir a <Libra esterlina>")
    print("0.Cerrar el programa")

    op=input("Selecciona la opcion deseada :")
    if op =="1":
        euro=23.82
        cantidad=float(input("Ingresa la cantidad en pesos($MX) que deseas convertir :"))
        cantidad=cantidad*1/euro
        print("El resultado de tu conversión es :" , cantidad)
    elif op=="2":
        dolar=18.81
        cantidad=float(input("Ingresa la cantidad en pesos($MX) que deseas convertir :"))
        cantidad=cantidad*1/dolar
        print("El resultado de tu conversión es :" , cantidad)
    elif op=="3":
        libra=0.041
        cantidad=float(input("Ingresa la cantidad en pesos($MX) que deseas convertir :"))
        cantidad=cantidad*1/libra
        print("El resultado de tu conversión es :" , cantidad)
    elif op =="0":
        print("Saliendo del programa...")
        break
    else:
        print("Opcion invalida, ingresa otra!")

    
