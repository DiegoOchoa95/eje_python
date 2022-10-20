#Escribí un programa que solicite ingresar un nombre de usuario y una #contraseña. Si el nombre es “Gwenevere” y la contraseña es “excalibur”, mostrar #en pantalla “Usuario y contraseña correctos. Puede ingresar a Camelot”. Si el #nombre o la contraseña no coinciden, mostrar “Acceso denegado”.
def run():
    nusuario=input("Ingrese su usuario: ")
    contraseña=input("Ingrese su contraseña: ")
    if nusuario=="Gwenevere" and contraseña=="excalibur":
        print("Usuario y Contraseña correctos. Puedes ingresar a Camelot")
    else:
        print("Acceso denegado")
            


if __name__=='__main__':
    run()