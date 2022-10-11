#Escribí un programa que le solicite al usuario ingresar una fecha
#formada por 8 números, donde los primeros dos representan el día,
#los siguientes dos el mes y los últimos cuatro el año (DDMMAAAA).
#Este dato debe guardarse en una variable con tipo int (número entero).
#Finalmente, mostrar al usuario la fecha con el formato DD / MM / AAAA.
def run ():
    fecha=int(input("Ingrese una fecha con el siguiente formato DDMMAAAA: "))
    cadena=str(fecha)
    dia=cadena[0,2]
    mes=cadena[2,4]
    año=cadena[4,9]
    print(dia,"/",mes,"/",año)




if __name__=='__main__':
    run()