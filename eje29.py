#Escribí un programa que permita al usuario ingresar 6 números enteros, que #pueden ser positivos o negativos. Al finalizar, mostrar la sumatoria de los #números negativos y el promedio de los positivos. No olvides que no es posible #dividir por cero, por lo que es necesario evitar que el programa arroje un #error si no se ingresaron números positivos.
def run():
    nn=0
    np=0
    c=0
    for i in range(6):
        numero=int(input("Ingrese un numero entero: "))
        if numero%2!=0:
            nn=nn+numero
        elif numero%2==0:
            np=np+numero
            c+=1            
    
    print("suma de los numero negativos: ",nn)
    print("Promedio de los numeros positivos: ",round((np)/c,2))
    



if __name__=='__main__':
    run()