#Escribí un programa que permita saber si un año es bisiesto. Para que un año #sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto #que también sea divisible por 400.
def run():
    año=int(input("Ingrese un año: "))
    if año%4==0 and año%100!=0:
        print("El año ingresado es bisiesto")
    else:
        print("El año ingresado no es bisiesto")
        


if __name__=='__main__':
    run()