#Escribí un programa que solicite al usuario el ingreso de strings de longitud 1 (un solo carácter), uno por vez. La repetición finalizará cuando se ingrese un string que no tenga longitud 1, o cuando el string ingresado corresponda al dígito numérico 0. Al finalizar, mostrar el string completo que se formó con todos los caracteres ingresados y qué porcentaje de caracteres del total fueron la letra “a”.
def run():
    caracter=""
    string=''
    c_a=0
    c_c=0
    porcentaje=0
    while True:
        caracter=input("Ingrese un caracter: ")
        if caracter=='0' or len(caracter)>1:
            break
        elif caracter=='a' or caracter=='A':
            c_a+=1
        string=string+caracter
        c_c+=1
    
    porcentaje=(c_a/c_c)*100
    print("Cadena de caracter completo: ",string)
    print("Cantidad de letras 'A':",c_a)
    print("Cantidad de caracteres ingresados:",c_c)
    print("Porcentaje de caracteres 'A'",porcentaje," %")

    #Otra forma
    '''
    cadenaTotal=""
    cantidad_a=0
    caracter=input("Escribí un carácter:")
    while (len(caracter)==1 and caracter!="0"):
        cadenaTotal=cadenaTotal+caracter
        if caracter=="a":
            cantidad_a=cantidad_a+1
        caracter=input("Escribí un carácter:")
    print("El string completo es:", cadenaTotal)
    print("Porcentaje de letras 'a':", (cantidad_a*100)/len(cadenaTotal))
    '''


if __name__=='__main__':
    run()



