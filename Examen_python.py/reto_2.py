print("-------TIEMPO DE SUEÑO-------")
rango={
    'Bebes':'12-15',
    'niños_pequeños':'11-14',
    'niños_escolar':'9-12',
    'adolescentes':'8-10',
    'jovenes':'7-9',
    'adultos':'7-9',
    'adulto_mayor':'7-8'

}
edad=float(input("Ingresa tu edad (si fueran meses coloca un punto antes, ejem(0.3)) :"))
if edad <=1:
    print(f"El tiempo de sueño acorde a tu edad es de: {rango['Bebes']} hrs")
elif edad== 1 or edad ==2:
     print(f"El tiempo de sueño acorde a tu edad es de: {rango['niños_pequeños']} hrs")
elif edad >= 3 and edad <=13:
      print(f"El tiempo de sueño acorde a tu edad es de: {rango['niños_escolar']} hrs")
elif edad >=14 and edad <=17:
      print(f"El tiempo de sueño acorde a tu edad es de: {rango['adolescentes']} hrs")
elif edad >=18 and edad <=25:
      print(f"El tiempo de sueño acorde a tu edad es de: {rango['jovenes']} hrs")
elif edad >=26 and edad <=64:
      print(f"El tiempo de sueño acorde a tu edad es de: {rango['adultos']} hrs")
elif edad >=65:
       print(f"El tiempo de sueño acorde a tu edad es de: {rango['adulto_mayor']} hrs")
else:
      print("Ingresa una edad correcta!")