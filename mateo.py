import datetime
fecha = datetime.datetime.now()
O2 = 1
clave = 0
NOMBRE = "SIN REGISTRO"
EDAD = "SIN REGISTRO"
RUT = "SIN REGISTRO"
PATENTE_VEHICULAR = "SIN REGISTRO"
while (O2 == 1) or (clave == 1):
    print ("Bienvenido a UBER que desea hacer hoy?")
    O1= int(input("PRESIONE \n '1' PARA REGISTRARSE (OBLIGATORIO) SI YA LO ESTA OMITIR \n '2' PARA COMENZAR UN VIAJE NUEVO \n '3' PARA CONSULTAR DATOS \n '4' PARA SALIR DE LA APLICACION UBER \n"))
    if (O1 == 1):
        O2 = 2
        while (O2 == 2 ):
            NOMBRE = input("Ingresar nombre ")
            EDAD = input("Ingresar edad ")
            RUT =int(input("Ingresar rut (SIN PUNTOS, NI GUION) "))
            PATENTE_VEHICULAR =input("Ingresar patente vehicular ")
            O2=int(input("Esta seguro que quiere continuar? '1' = Si  '2' = No \n"))
            clave=1
    if (O1 == 2):
        if (clave==0):
            print("\n DEBE REGISTRARSE ANTES DE PODER HACER UNA CARRERA \n volviendo a menu.....")
        if (clave== 1):
            print ("\n Usted esta empezando un viaje \n")
            X = int(input("Inserte el destino en (LATITUD) (Y) en METROS "))
            Y = int(input("Inserte el destino en (LONGITUD) (X) en METROS "))
            X1= 0
            Y2= 0
            print("\n Bienvenido al sistema de navegacion de UBER, primero, Al acelerar aumentara la velocidad a 10km/h (2,7m/s) \n Por cada metro se cobraran 50 pesos \n")
            while (X1 != X and Y2 != Y):
                boton1= 0
                velocidad = 0
                apagado= 0
                encender=int(input("1- Encender movil \n"))
                if (encender == 1):
                    while (apagado != 3):
                        X1 = -9999 if X1 < -9999 else X if X1 > X else X1
                        print("\nRECORDATORIO SU DESTINO ESTA EN ",X," (X), ",Y," (Y) \nSu distancia recorrida es de  ",X1," (X)")
                        print("Su velocidad actual es de ",velocidad,"m/s \n")
                        print("1- Acelerar movil")
                        print("2- Girar movil")
                        print("3- Apagar movil y detener ")
                        print("4- Avanzar (", velocidad * 10, " metros)")
                        boton1=int(input("Seleccione "))
                        if (X1 == X):
                            print("\n Hay una pared a continuacion, Porfavor gire o termine su recorrido si ya ha llegado apagando el vehiculo. \n")
                        if (boton1 == 3):
                            apagado = 3
                        if (boton1 == 1):
                            velocidad = 2.7 + velocidad
                        if (boton1==4):
                            X1 = X1 + (velocidad * 10)
                        if (boton1 == 2):
                            boton1 = 0
                            while (boton1 != 2) and (apagado != 3):                    
                                Y2 = -9999 if Y2 < -9999 else Y if Y2 > Y else Y2
                                print("\n RECORDATORIO SU DESTINACION ESTA EN ",X," (X), ",Y," (Y)")
                                print("Su distancia recorrida es de ",Y2,"(Y)")
                                print("Su velocidad actual es de ",velocidad,"m/s")
                                print("1- Acelerar movil")
                                print("2- Girar movil")
                                print("3- Apagar movil y detener")
                                print("4- Avanzar ", velocidad * 10," metros \n")
                                if (Y2==Y):
                                    print("\n Hay una pared a continuacion, Porfavor gire o termine su recorrido si ya ha llegado apagando el vehiculo.")
                                boton1=int(input("Seleccione "))
                                if (boton1==3):
                                    apagado = 3
                                    boton1 = 2
                                if (boton1 == 1):
                                    velocidad = 2.7 + velocidad
                                if (boton1 == 4):
                                    Y2 = Y2 + (velocidad * 10)
            print("\nUSTED A RECORRIDO = ", (X+Y), " METROS")
            print("PRECIO QUE DEBE PAGAR EL PASAJERO = ", (X+Y)*50, "$")
            print("USTED ENTREGO AL PASAJERO a las", fecha,)
            respuesta=int(input("\n fin del destino 1- Volver al menu "))
    if (O1 == 3):
        print("\n NOMBRE DE CONDUCTOR:", NOMBRE, "\n EDAD:", EDAD, "\n RUT:", RUT, "\n PATENTE DEL AUTOMOVIL:", PATENTE_VEHICULAR)
        ok=input("Presione ENTER para volver al menu ")
    if (O1 == 4):
        O2 = 10
        clave == 0  