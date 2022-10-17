#Escribí un programa que le pida al usuario ingresar dos palabras y las guarde #en dos variables, y que luego imprima True si la primera palabra es menor que #la segunda o False si no lo es.
def run():
    p1=input("Ingrese la primera palabra: ")
    p2=input("Ingrese la segunda palabra: ")
    tp1=len(p1)
    tp2=len(p2)
    if tp1>tp2:
        print(True)
    else:
        print(False)
        


if __name__=='__main__':
    run()