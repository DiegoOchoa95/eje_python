#Escribí un programa que, dada una cadena de texto por el usuario, 
#imprima True si la cantidad de caracteres en la cadena es un número impar, 
#o False si no lo es.
def run():
    cadena=input("Ingrese una palabra por favor:")
    cantidad=len(cadena)
    if cantidad%2!=0:
        print(True)
    else:
        print(False)



if __name__=='__main__':
    run()
