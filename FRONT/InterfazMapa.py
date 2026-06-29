




def imprimir_Cofre_SubirNivel():
                print("Subiste Nivel")
     
def imprimir_Cofre_Curacion(vidaCurar):
                print(f"Recuperaste {vidaCurar} de vida")

def imprimir_Cofre_Batalla():
                print("--BATALLA--")

def imprimir_Cofre_Daño(vidaDaño):
                print(f"Has perdido {vidaDaño}")


def imprimir_Camino(caminoHistorico,siguiente0,siguiente1):
        
    print(f" {" " * len(caminoHistorico)}{siguiente0}")
    print(caminoHistorico)
    print(f" {" " * len(caminoHistorico)}{siguiente1}")

def imprimir_Donde_Avanzar(siguiente0,siguiente1):
    eleccion=""
    while eleccion != "0" and eleccion !="1":
        print(f"seleccione a donde avanzar:")
        print(f"0-{siguiente0}")
        print(f"1-{siguiente1}")
        eleccion = input()
    return eleccion