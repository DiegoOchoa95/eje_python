#Escribí un programa que solicite al usuario el ingreso de dos palabras,
#las cuales se guardarán en dos variables distintas.
#A continuación, almacená en una variable la concatenación de la primera palabra,
#más un espacio, más la segunda palabra. 
#Mostrá este resultado en pantalla.
def run():
    p1=input("Ingrese una palabra: ")
    p2=input("Ingrese una segunda palabra: ")
    union=p1+" "+p2
    print(union)


if __name__=='__main__':
    run()