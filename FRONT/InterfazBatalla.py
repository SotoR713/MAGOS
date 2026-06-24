from FRONT.InterfazPantalla import mostrar_Stats



def imprimir_Curacion(vidaCurada,mago1):
     print(f"recupera {vidaCurada}: vida {mago1.get_hpActual()}/{mago1.get_hpMax()}\n")

def imprimir_IniciarBatalla(mago1,mago2):
     print("=============== ⚔  COMBATE  ⚔ ===============")
     mostrar_Stats(mago1)
     print("--------------------- VS ---------------------")
     mostrar_Stats(mago2)
     print("==============================================")