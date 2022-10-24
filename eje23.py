#Escribí un programa que le solicite al usuario un número entero y muestre todos #los números correlativos entre el 1 y el número ingresado por el usuario.
def run():
    numero=int(input("Ingrese un numero entero: "))
    for i in range(numero):
        i+=1
        print(i)
        
       


if __name__=='__main__':
    run()
    