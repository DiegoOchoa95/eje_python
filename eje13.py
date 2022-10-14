#Escribí un programa que le solicite al usuario su edad y la guarde en una variable.
#Que luego solicite la cantidad de artículos comprados en una tienda
#y la guarde en otra variable. 
#Finalmente, mostrar en pantalla un valor de verdad (True o False) 
#que indique si el usuario es mayor de 18 años de edad 
#y además compró más de 1 artículo.
def run():
    edad= int(input("Ingrese su edad: "))
    articulo=int(input("Ingrese la cantidad de articulos comprados: "))
    if edad>18 and articulo>1:
        print(True)
    else:
        print(False)



if __name__=='__main__':
    run()
