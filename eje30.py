#Escribí un programa que permita al usuario ingresar una frase y luego un #carácter (string de longitud 1) y luego muestre la frase ingresada, pero con #todas las ocurrencias del carácter indicado por el usuario reemplazadas por “*”.
def run():
    frase=input("Ingresar una frase: ")
    caracter=input("Ingrese un caracter: ")
    if len(caracter)>1:
        print("Por favor ingrese un solo caracter")
        caracter=input("Ingrese un caracter: ")
    
    caracter=caracter.lower()
    frase=frase.lower()
    frase=frase.replace(caracter,"*")
    print(frase)


if __name__=='__main__':
    run()