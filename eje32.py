#Escribí un programa que permita al usuario ingresar los montos de las compras #de un cliente (se desconoce la cantidad de datos que cargará, la cual puede #cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario #ingrese el monto 0. Si ingresa un monto negativo, no se debe procesar y se debe #pedir que ingrese un nuevo monto. Al finalizar, informar el total a pagar #teniendo que cuenta que, si las ventas superan el monto total de 1000, se le #debe aplicar un 10% de descuento.
def run():
    print("CALCULO TOTAL A PAGAR")
    print("Finalize el programa ingresando 0")
    monto=int(input("Ingrese monto de producto: "))
    tpagar=0
    while monto>0:
        tpagar=tpagar+monto
        monto=int(input("Ingrese monto de producto: "))
        if monto<0:
            print("Por favor ingrese un numero positivo")
            monto=int(input("Ingrese monto de producto: "))
        elif monto==0:
            break
           
    print("Total a pagar es: ",tpagar)



if __name__=='__main__':
    run()