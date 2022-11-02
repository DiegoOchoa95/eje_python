#Escribí un programa para solicitar al usuario que ingrese números enteros positivos (la cantidad que ingresará no se conoce y la decide el usuario). La lectura de números finalizará cuando el usuario ingrese el número -1. 
#Por cada número ingresado, mostrar la cantidad de dígitos pares y la cantidad de dígitos impares que tiene. Al finalizar, mostrar cuántos números múltiplos de 3 ingresó el usuario.
def run():
    multiplosDe3=0
    numero=int(input("Número (-1 para terminar el programa):"))
    
    while numero!=-1:
        if numero%3 == 0:
            multiplosDe3=multiplosDe3+1
        digitosPares=0
        digitosImpares=0
        while numero!=0:
            ultimodigito=numero%10
            if ultimodigito%2==0:
                digitosPares=digitosPares+1
            else:
                digitosImpares=digitosImpares+1
            numero=numero//10
        print("Dígitos pares:", digitosPares)
        print("Dígitos impares:", digitosImpares)
        numero=int(input("Número (-1 para terminar el programa):"))
    print("Se ingresaron", multiplosDe3, "múltiplos de 3.")


if __name__=='__main__':
    run()