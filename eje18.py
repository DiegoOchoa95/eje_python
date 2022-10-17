#Escribí un programa que solicite al usuario el ingreso de dos números #diferentes y muestre en pantalla al mayor de los dos.
def run():
    n1=int(input("Ingrese el primer número entero: "))
    n2=int(input("Ingrese el segundo número entero: "))
    if n1>n2:
        print("El número mayor ingresado es: ",n1)
    else:
        print("El número mayor ingresado es: ",n2)




if __name__=='__main__':
    run()