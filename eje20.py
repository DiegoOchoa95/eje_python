#Escribí un programa para solicitar al usuario tres números y mostrar en #pantalla al menor de los tres.
def run():
    n1=int(input("Ingrese el primer numero: "))
    n2=int(input("Ingrese el segundo numero: "))
    n3=int(input("Ingrese el tercer numero: "))
    
    nmayor=max(n1,n2,n3)
        

    print("El numero mayor es: ",nmayor)




if __name__=='__main__':
    run()