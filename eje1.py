#Escribí un programa que solicite al usuario que ingrese su nombre. 
# El nombre se debe almacenar en una variable llamada nombre. 
# A continuación se debe mostrar en pantalla el texto “Ahora estás en la matrix, 
# [usuario]”, donde “[usuario]” se reemplazará por el nombre que el usuario haya ingresado.

def run():
    nombre= input("Ingrese su nombre: ")
    print("Ahora estas en la matrix", nombre)



if __name__=='__main__':
    run()