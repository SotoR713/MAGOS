from FRONT.InterfazPantalla import mostrar_Stats



def imprimir_Curacion(vidaCurada,mago1):
     print(f"recupera {vidaCurada}: vida {mago1.get_hpActual()}/{mago1.get_hpMax()}\n")

def imprimir_IniciarBatalla(mago1,mago2):
     print("=============== ⚔  COMBATE  ⚔ ===============")
     mostrar_Stats(mago1)
     print("--------------------- VS ---------------------")
     mostrar_Stats(mago2)
     print("==============================================")


def imprimir_Final_Turno(mago1,mago2):
     print(f"{mago1.get_nombre()}: {mago1.get_hpActual()}/{mago1.get_hpMax()}           |      {mago2.get_nombre()}: {mago2.get_hpActual()}/{mago2.get_hpMax()}")
     print(f"{"▓"*mago1.get_hpActual()}{"░"* (mago1.get_hpMax()-mago1.get_hpActual())}   |   {"░"* (mago2.get_hpMax()-mago2.get_hpActual())}{"▓"*mago2.get_hpActual()}")


def imprimir_Turno(turno):
     print(f"=============== ⚔  TURNO: {turno}  ⚔ ===============")



def imprimir_Resultado(primero,segundo):
     if primero.get_hpActual() > segundo.get_hpActual():
        print(f"EL Mago {primero.get_nombre()} derroto a {segundo.get_nombre()}")
        ganador = primero
     else:
        print(f"EL Mago {segundo.get_nombre()} derroto a {primero.get_nombre()}")
        ganador = segundo
     return ganador


def imprimir_Resumen_Turno(mago1,mago2,daño,diferenciaValores):
            if diferenciaValores > 0:
                print("¡¡¡CRITICO!!!")
            elif diferenciaValores<0:
                print(f"El Mago {mago2.get_nombre()} ataco, pero {mago1.get_nombre()} esquivo el ataque")            
            else:
                print(f"el mago {mago2.get_nombre()} ataco y causo {daño} a mago {mago1.get_nombre()}")
