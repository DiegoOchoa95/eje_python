#Escribí un programa que pregunte al usuario si desea analizar calificaciones de alumnos y, sólo si responde “Si” comenzará el procesamiento de los datos, hasta que el usuario ingrese algo diferente de “Si”. Por cada alumno, permitir ingresar su calificación. Si es mayor a 4 el alumno está aprobado. Finalmente, mostrar“Porcentaje de alumnos aprobados: x %” (donde x es el porcentaje de aprobados sobre el total de calificaciones procesadas). También se debe imprimir “Promedio de los aprobados: y” (donde y es la calificación promedio, sólo de los alumnos aprobados).
def run():
    print("INDIQUE: SI, para ingresar al sistema")
    print("INDIQUE: NO, para salir del sistema")
    opcion=input("¿DESEA ANALIZAR CALIFICACIONES?: ")
    opcion=opcion.upper()
    alu_apro=0
    alu_desa=0
    tot_alu=0
    nota_apro=0
    prom=0
    porcentaje=0
    while opcion=="SI":
        calf=int(input("Ingrese calificación: "))
        opcion=input("¿DESEA CONTINUAR?: ").upper()
        if calf>=4:
            alu_apro+=1
            nota_apro+=calf
        elif calf<4:
            alu_desa+=1
    tot_alu=alu_apro+alu_desa 
    prom=nota_apro/alu_apro 
    porcentaje=(alu_apro*100)/tot_alu      
    print("Total de alumnos analizados: ",tot_alu)
    print("Total de alumnos aprobados: ",alu_apro)
    print("Total de alumnos desaprobados: ",alu_desa)
    print("Porcentaje de alumnos aprobados: ",porcentaje,"%")
    print("Promedio de alumnos aprobados: ",round(prom,2))


              

    

if __name__=='__main__':
    run()