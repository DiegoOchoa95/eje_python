#Escribí un programa que solicite al usuario una letra y, si es una vocal, #muestre el mensaje “Es vocal”. Verificar si el usuario ingresó un string de más #de un carácter y, en ese caso, informarle que no se puede procesar el dato.
def run():
    letra=input("Ingrese una letra: ")
    tamaño=len(letra)
    if tamaño>=2:
        print("Solo ingrese una letra")
    else:
        if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
             print("La letra ingresada es una vocal")
        else:
            print("La letra ingresada en una consonante")
        



if __name__=='__main__':
    run()