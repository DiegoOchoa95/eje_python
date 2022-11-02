#Escribí un programa que, dado un número entero por el usuario (guardado como int), muestre la suma de todos sus dígitos. Recordá que vas a necesitar obtener cada uno de los dígitos por separado para poder sumarlos entre sí.
def run():
    numero=int(input("Ingresa un número:"))
    total=0
    while numero != 0:
        ultimoDigito=numero%10
        total=total+ultimoDigito
        numero=numero//10
    print("Suma de los dígitos:", total)


if __name__=='__main__':
    run()