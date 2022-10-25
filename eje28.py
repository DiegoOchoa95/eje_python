#Escribí un programa que, dado un número entero positivo, calcule y muestre su #factorial. El factorial de un número se obtiene multiplicando todos los números #enteros positivos que hay entre el 1 y ese número. El factorial de 0 es 1.
#1,2,3,4,5
def run():
    numero=int(input("Ingrese un numero para hallar su factorial: "))
    n2=2
    fact=1
    for i in range(numero-1):
        fact=fact*n2
        print(fact)
        n2+=1
      


if __name__=='__main__':
    run()