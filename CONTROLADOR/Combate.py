from Configuracion import porcentajeCuracionVictoria
from FRONT.InterfazPantalla import mostrar_Stats
from FRONT.InterfazBatalla import imprimir_Curacion,imprimir_IniciarBatalla,imprimir_Final_Turno,imprimir_Turno
from FRONT.InterfazVarios import limpiar_Pantalla,imprimir_Pausas
from CONTROLADOR.Repartir import calculo_Repartir_Stats

def enfrentamiento(mago1,mago2,generador):
    limpiar_Pantalla()
    
    turno = 1

    imprimir_IniciarBatalla(mago1,mago2)
    imprimir_Pausas()
    

    if mago1.get_velocidad() > mago2.get_velocidad():
        primero = mago1
        segundo = mago2
    else:
        primero = mago2
        segundo = mago1
         
    while primero.get_hpActual() > 0 and segundo.get_hpActual() > 0:
        imprimir_Turno(turno)
        daño = primero.calcular_Daño(segundo)
        dañoOriginal=daño
        daño = (primero.calcular_Critico(segundo,generador.aleatorio(),daño))*(segundo.evasion(primero,generador.aleatorio()))
        dañoCritico = daño
        diferenciaValores = dañoCritico-dañoOriginal
        segundo.recibir_Daño(daño)
        if diferenciaValores > 0:
            print("¡¡¡CRITICO!!!")
        elif diferenciaValores<0:
            print(f"El Mago {primero.get_nombre()} ataco, pero {segundo.get_nombre()} esquivo el ataque")
        else:
            print(f"el mago {primero.get_nombre()} ataco y causo {daño} a mago {segundo.get_nombre()}")
        daño = segundo.calcular_Daño(primero)
        dañoOriginal=daño
        daño = (segundo.calcular_Critico(primero,generador.aleatorio(),daño))*(primero.evasion(segundo,generador.aleatorio()))
        dañoCritico=daño
        diferenciaValores=dañoCritico-dañoOriginal
        if segundo.get_hpActual() > 0:
            primero.recibir_Daño(daño)
            if diferenciaValores > 0:
                print("¡¡¡CRITICO!!!")
            elif diferenciaValores<0:
                print(f"El Mago {segundo.get_nombre()} ataco, pero {primero.get_nombre()} esquivo el ataque")            
            else:
                print(f"el mago {segundo.get_nombre()} ataco y causo {daño} a mago {primero.get_nombre()}")

        imprimir_Final_Turno(mago1,mago2)
        
        imprimir_Pausas()
        turno += 1

    if primero.get_hpActual() > segundo.get_hpActual():
        print(f"EL Mago {primero.get_nombre()} derroto a {segundo.get_nombre()}")
        ganador = primero
    else:
        print(f"EL Mago {segundo.get_nombre()} derroto a {primero.get_nombre()}")
        ganador = segundo
    
    if ganador == mago1:
        mago1.subir_Nivel()
        calculo_Repartir_Stats(mago1)
        mostrar_Stats(mago1)
        vidaCurada = mago1.curar((mago1.get_hpMax() * porcentajeCuracionVictoria) // 100)
        imprimir_Curacion(vidaCurada,mago1)
        mostrar_Stats(mago1)
