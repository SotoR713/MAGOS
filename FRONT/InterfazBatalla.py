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