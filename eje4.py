#Escribí un programa que solicite al usuario ingresar la cantidad de kilómetros recorridos por una motocicleta
#y la cantidad de litros de combustible que consumió durante ese recorrido.
#Mostrar el consumo de combustible por kilómetro.
def run():
    km=float(input("Ingrese la cantidad de kilometros recorridos: "))
    lt=float(input("Ingrese la cantidad de litros consumidos: "))
    consumo=km/lt
    print("El consumo de combustible por kilometro es: ", consumo)
    
    

if __name__=='__main__':
    run()