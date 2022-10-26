#Escribí un programa que, dada una frase por el usuario, la muestre invertida, #sin utilizar una rebanada con paso negativo.
def run():
    #Primera forma
    frase=input("Ingrese una frase: ")
    frase=frase[::-1]
    print(frase)
    
    #Segunda forma
    frase=input("Frase:")
    nueva=""
    i=len(frase)-1
    while i>=0:
        nueva=nueva+frase[i]
        i=i-1
    print(nueva)



if __name__=='__main__':
    run()