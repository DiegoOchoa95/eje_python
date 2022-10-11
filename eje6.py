#Escribí un programa que solicite al usuario ingresar tres números para luego mostrarle el promedio de los tres.
def run():
    promedio=0
    for i in range(3):
        numero=float(input("Ingrese un numero: "))
        promedio=round((promedio+numero),2)
    print("El promedio de los 3 numeros ingresados es: \n",promedio/3)




if __name__=='__main__':
    run()