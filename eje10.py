#Escribí un programa que solicite al usuario que ingrese cuántos shows musicales
#ha visto en el último año y almacene ese número en una variable.
#A continuación mostrar en pantalla un valor de verdad (True o False)
#que indique si el usuario ha visto más de 3 shows.
def run():
    show=int(input("Ingresa la cantidad de shows musicales que ha visto: "))
    if show>3:
        print(True)
        print("Ustes ha visto ",show," shows musicales.")
    else:
        print(False)
        print("Usted ah visto menos de 3 shows musicales")



if __name__=='__main__':
    run()