#Escribí un programa que, dado un número entero, muestre su valor absoluto. #Recordá que, para los números positivos su valor absoluto es igual al número
#(el valor absoluto de 52 es 52), mientras que, para los negativos, su valor #absoluto es el número multiplicado por -1 (el valor absoluto de -52 es 52).
def run():
    numero= int(input("Ingrese un número entero: "))
    if numero>0:
        print("El valor absoluto de ",numero," es: ",numero)
    elif numero<0:
        print("El valor absoluto de ",numero," es: ",(numero*-1))
    else:
        print("El numero ingresado es 0, por favor ingrese un numero mayor o menor a cero")



if __name__=='__main__':
    run()