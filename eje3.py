#Escribí un programa que solicite al usuario dos números y los almacene en dos variables. 
#En otra variable, almacená el resultado de la suma de esos dos números y luego mostrá ese resultado en pantalla.
#A continuación, el programa debe solicitar al usuario que ingrese un tercer número, el cual se debe almacenar en una nueva variable. 
#Por último, mostrá en pantalla el resultado de la multiplicación de este nuevo número por el resultado de la suma anterior.
def run():
    n1 = int(input("Ingrese el primer número: "))
    n2 = int(input("Ingrese el segundo número: "))
    suma=n1+n2
    print("La suma de ambos numeros es: ", suma)
    n3 = int(input("Ingrese un tercer número: "))
    multiplicacion=suma*n3
    print("El resultado de la multiplicación de la suma y el tercer numero es: ", multiplicacion)




if __name__=='__main__':
    run()
