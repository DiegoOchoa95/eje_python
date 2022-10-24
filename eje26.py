#Escribí un programa que, dada una frase por el usuario, muestre la cantidad #total de vocales (tanto mayúsculas como minúsculas) que contiene.

def run():
    frase=input("Escribe una frase: ")
    frase=frase.upper()
    c=0
    for i in range(len(frase)):
        if frase[i]=="A" or frase[i]=="E" or frase[i]=="I" or frase[i]=="O" or frase[i]=="U" :
            c+=1
        

    print("En la frase hay ", c, " vocales")



if __name__=='__main__':
    run()

"""

#Codigo extra
frase=input("Frase:")
vocales="aeiouAEIOU"
cantidad=0
for i in frase:
    if i in vocales:
        cantidad=cantidad+1
print("Vocales:", cantidad)

"""