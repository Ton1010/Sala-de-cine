fila=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
def reserva(fila):
    #fila
    f = int(input("¿Que fila quiere?: "))
    while f<=0 or f>3:
        print("Solo tenemos 3 filas")
        f = int(input("¿Que fila quiere?: "))
        
    print("Estas son las sillas en la fila",f)
    print("")
    print(fila[f-1])
    print("_______________________________")
    #silla
    
    s = int(input("¿Que puesto quiere?: "))
    

    if f-1 == 0:
        if s>0 and s<=5:
            print("Has escogido el puesto",s)
            if s == 1:
                s = 0
            if s ==2:
                s = 1
            if s==3:
                s = 2
            if s ==4:
                s =3
            if s ==5:
                s = 4
            puesto = fila[f-1][s]
            if puesto ==0:
                print("El puesto solicitado no está disponible")
            else:
                fila[f-1][s] = 0
                
                
        else:
            print("La silla solicitada no está disponible en esta fila")
            print("Volvamos a empezar")
            reserva(fila)

    else:
        if f-1 ==1:
            if s>5 and s<=10:
                print("Has escogido el puesto",s)
                if s == 6:
                    s = 0
                if s ==7:
                    s = 1
                if s==8:
                    s = 2
                if s ==9:
                    s =3
                if s ==10:
                    s = 4
                puesto = fila[f-1][s]
                if puesto ==0:
                    print("El puesto solicitado no está disponible")
                else:
                    fila[f-1][s] = 0
            else:
                print("La silla solicitada no está disponible en esta fila")
                print("Volvamos a empezar")
                reserva(fila)
                
        else:
            if f-1 ==2:
                if s>10 and s<=15:
                    print("Has escogido el puesto",s)
                    if s == 11:
                        s = 0
                    if s ==12:
                        s = 1
                    if s==13:
                        s = 2
                    if s ==14:
                        s =3
                    if s ==15:
                        s = 4
                    puesto = fila[f-1][s]
                    if puesto ==0:
                        print("El puesto solicitado no está disponible")
                    else:
                        fila[f-1][s] = 0
                else:
                    print("La silla solicitada no está disponible en esta fila")
                    print("Volvamos a empezar")
                    reserva(fila)
    return fila

def ver(fila):
    print("Estas son las sillas de la sala de cine disponibles en el momento")
    print(fila[0])
    print(fila[1])
    print(fila[2])
    print("")

def menu():
    opc = 1
    while opc>0 and opc!=3:
        print("")
        print(" Bienvenido al  Menu")
        print("")
        print("1. Crear reserva")
        print("2. Visualizar todas las sillas")
        print("3. Salir")
        print("")
        opc = int(input("¿Que opción desear realizar?: "))
        print("_______________________________")
        print("")
        if opc ==1:
            reserva(fila)
        if opc ==2:
            ver(fila)
        if opc>3:
            print("Opcion no disponible")
            print("")
            opc = int(input("¿Que opción desear realizar?: "))
menu()
print("Muchas gracias por usar nuestro sistema de reserva")
print("Para tu puesto en el cine")
print("Disfruta la peli :)")
