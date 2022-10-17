#Escribí un programa para pedir al usuario su nombre y luego el nombre de otra #persona, almacenando cada nombre en una variable. Luego mostrar en pantalla un #valor de verdad que indique si: los nombres de ambas personas comienzan con la #misma letra ó si terminan con la misma letra. Por ejemplo, si los nombres #ingresados son María y Marcos, se mostrará True, ya que ambos comienzan con la #misma letra. Si los nombres son Ricardo y Gonzalo se mostrará True, ya que #ambos terminan con la misma letra. Si los nombres son Florencia y Lautaro se #mostrará False, ya que no coinciden ni la primera ni la última letra.
def run():
    tunombre=input("Ingresa tu nombre: ")
    nombre=input("Ingresa el nombre de alguien mas: ")
    if tunombre[0]==nombre[0]:
        print(True)
    elif tunombre[len(tunombre)-1]==nombre[len(nombre)-1]:
        print(True)
    else:
        print(False)




if __name__=='__main__':
    run()