#Escribí un programa que permita al usuario ingresar una cantidad de números #positivos indefinida (la cantidad que ingresará no se conoce y puede cambiar en #cada ejecución), finalizando cuando ingresa el número 0 (que no se tendrá en #cuenta). Una vez terminada la lectura de números, informar cuál fue el mayor de #los números ingresados.
def run():
    
    numero=int(input("Ingrese un numero positivo: "))
    nmax=0
    while numero!=0:        
        if numero>nmax:
            nmax=numero
        numero=int(input("Ingrese un numero positivo: "))
    
    print("El número mayor ingresado es: ",nmax)
    

'''
    mayor=-1
    n=int(input("Número positivo:"))
    while n!=0:
        if n>mayor:
            mayor=n
        n=int(input("Número positivo:"))
    print("Mayor número ingresado:", mayor)
'''


if __name__=='__main__':
    run()