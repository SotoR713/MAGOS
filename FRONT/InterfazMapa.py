




def imprimir_Cofre_SubirNivel():
                print("Subiste Nivel")
     
def imprimir_Cofre_Curacion(vidaCurar):
                print(f"Recuperaste {vidaCurar} de vida")

def imprimir_Cofre_Batalla():
                print("--BATALLA--")

def imprimir_Cofre_Daño(vidaDaño):
                print(f"Has perdido {vidaDaño}")


def imprimir_Camino(caminoHIstorico,siguiente0,siguiente1):
        
    print(f" {" " * len(caminoHIstorico)} {siguiente0}")
    print(caminoHIstorico)
    print(f" {" " * len(caminoHIstorico)}{siguiente1}")
