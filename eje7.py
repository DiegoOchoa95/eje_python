#Escribí un programa que solicite al usuario un número y le reste el 15%,
#almacenando todo en una única variable. A continuación, 
#mostrar el resultado final en pantalla.
def run():
    numero= float(input("Ingrese un numero: "))
    numero= round((numero -(numero*0.15)),2)
    print("El resultado es: ", numero)




if __name__=='__main__':
    run()