from FRONT.InterfazPantalla import jefe_Derrotado,mostrar_Stats
from FRONT.InterfazMapa import imprimir_Cofre_Batalla, imprimir_Cofre_Curacion,imprimir_Cofre_Daño,imprimir_Cofre_SubirNivel,imprimir_Camino,imprimir_Donde_Avanzar
from FRONT.InterfazVarios import limpiar_Pantalla,imprimir_Pausas
from BACK.Clases.Eventos import BRival, BJefe, Cofre, Curacion
from BACK.Funciones.Calculadoras import raiz_digital
from BACK.Funciones.Fabrica import crear_Rival, crear_Jefe
from CONTROLADOR.Combate import enfrentamiento, calculo_Repartir_Stats
from Configuracion import porcentajeCuracionCofre, porcentajeCuracionEvento, umbralBatalla, umbralCuracion, umbralSubir, porcentajeDañoCofre

def avanzar(senda):
    imprimir_Pausas()
    limpiar_Pantalla()
    imprimir_Camino(senda.get_caminoHistorico(), senda.get_siguiente0().caracter, senda.get_siguiente1().caracter)
    eleccion = imprimir_Donde_Avanzar(senda.get_siguiente0().nombre, senda.get_siguiente1().nombre)
    senda.registrar_Avance(eleccion)
    if eleccion == "0":
        return senda.get_siguiente0()
    elif eleccion == "1":
        return senda.get_siguiente1()
    

def resolver_Evento(senda, evento):
    if evento == BRival:
        Brival = crear_Rival(senda.get_generador().aleatorio(), len(senda.get_camino()))
        enfrentamiento(senda.get_jugador(), Brival,senda.get_generador())
        senda.marcar_Rival()
    elif evento == BJefe:
        bjefe = crear_Jefe(senda.get_generador().aleatorio(), len(senda.get_camino()))
        enfrentamiento(senda.get_jugador(), bjefe,senda.get_generador())
        senda.agregar_Historial( "→☠")
        jefe_Derrotado()
    elif evento == Curacion:
        senda.get_jugador().curar(senda.get_jugador().get_hpMax()*porcentajeCuracionEvento//100)
        senda.agregar_Historial("→♥") 
    elif evento == Cofre:
        v1 = (senda.get_generador().aleatorio() * senda.get_generador().aleatorio() )// 713
        v1 = raiz_digital(v1)

        if v1 <= umbralSubir:
            senda.get_jugador().subir_Nivel() 
            calculo_Repartir_Stats(senda.get_jugador())               
            mostrar_Stats(senda.get_jugador())
            imprimir_Cofre_SubirNivel()
            senda.agregar_Historial("→[↑]")
        elif v1 <= umbralCuracion:
            vidaCurar=senda.get_jugador().get_hpMax()*porcentajeCuracionCofre//100
            senda.get_jugador().curar(vidaCurar)
            imprimir_Cofre_Curacion(vidaCurar)
            senda.agregar_Historial("→[♥]")
        elif v1 <= umbralBatalla:
            senda.agregar_Historial("[")
            resolver_Evento(senda,BRival)
            imprimir_Cofre_Batalla()
        else:
            vidaDaño=senda.get_jugador().get_hpMax()*porcentajeDañoCofre//100
            senda.get_jugador().recibir_Daño(vidaDaño)
            imprimir_Cofre_Daño(vidaDaño)
            senda.agregar_Historial("→[↓]")