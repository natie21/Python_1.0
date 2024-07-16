"""
Problema:

Crea una función que reciba una lista de diccionarios.
Cada diccionario representa una transacción bancaria con las claves
id_transaccion, monto, tipo y fecha. 
La función debe calcular y retornar el balance final de la cuenta bancaria,
la cantidad total de transacciones por tipo (deposito o retiro),
y un diccionario con las fechas como claves y 
la suma de montos de todas las transacciones realizadas en cada fecha como valores.

La función debe manejar las siguientes excepciones:

Si alguna transacción no tiene el formato correcto (falta alguna clave), debe ignorar esa transacción y continuar con las demás.
Si monto no es un número positivo, debe lanzar un mensaje de error específico para esa entrada.
Si tipo no es un valor válido (deposito o retiro), debe lanzar un mensaje de error específico para esa entrada.
Si fecha no es una cadena de texto con el formato YYYY-MM-DD, debe lanzar un mensaje de error específico para esa entrada

"""



def transaccion_bancaria(lista_transaccion):
    montoPorFecha={}
    balance_final=0
    cantidadTipo={"deposito" :0 ,"retiro" :0}



    for transaccion in lista_transaccion:
        try:
            if not all(clave in transaccion for clave in ["id_transaccion","monto","tipo","fecha"]):
                raise KeyError("Falta una clave en el diccionario de la transacción")
            id_transaccion=transaccion["id_transaccion"]
            monto=transaccion["monto"]
            tipo=transaccion["tipo"]
            fecha=transaccion["fecha"]
            if not isinstance(monto,(int,float)) or monto <=0:
                raise ValueError (f"Monto no valido en la transaccion :{id_transaccion}")
            if tipo not in ["deposito","retiro"]:
                raise ValueError(f"Tipo no vaido para la transaccion")
            if not isinstance(fecha,str) or len(fecha) !=10 or fecha[4] !="-" or fecha[7] !="-":
                raise ValueError (f"Verifica que la fecha de la transaccion {id_transaccion} sea valido")
            if tipo =="deposito":
                balance_final+=monto
                cantidadTipo ["deposito"] +=1
            elif tipo=="retiro":
                balance_final-=monto
                cantidadTipo ["retiro"]+=1
            if fecha not in montoPorFecha:
                montoPorFecha[fecha]=0
                montoPorFecha[fecha]+=monto
        except KeyError as ke:
            print(f"Error: {str(ke)}")
        except ValueError as Ve:
            print(f"Error: {str(Ve)}")
    return {
            "Balance final" : balance_final,
            "Cantidad por tipo" : cantidadTipo,
            "Montos por fecha" : montoPorFecha

        }

        


transacciones=[
    {"id_transaccion" : "AB01", "monto" : 2000,"tipo" : "retiro" , "fecha" :"2024-06-07"},
    {"id_transaccion" : "AB02", "monto" : -3600,"tipo" : "retiro" , "fecha" :"2024-17-05"},
    {"id_transaccion" : "AB03", "monto" : 2800.50,"tipo" : "retiro" , "fecha" :"2024-08-07"},
    {"id_transaccion" : "AB04", "monto" : 700,"tipo" : "deposito" , "fecha" : "2024-08"},
    {"id_transaccion" : "AB05", "monto" : 200,"tipo" : "abono" , "fecha" :"2024-06-07"},
    {"id_transaccion" : "AB06", "monto" : 4000,"tipo" : "deposito"}

]

print(transaccion_bancaria(transacciones))