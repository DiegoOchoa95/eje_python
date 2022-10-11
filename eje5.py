#Escribí un programa que solicite al usuario el ingreso de una temperatura en escala Fahrenheit 
#(debe permitir decimales) y le muestre el equivalente en grados Celsius. 
# La fórmula de conversión que se usa para este cálculo es: _Celsius = (5/9) * (Fahrenheit-32)_

def run():
    f=float(input("Ingrese temperatura fharenheit: "))
    c=round(((5/9)*f),2)

    print("Grados celcius: ",c)




if __name__=='__main__':
    run()