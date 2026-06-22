def enfrentamiento(mago1,mago2,generador):
    turno = 1
    print("=============== ⚔  COMBATE  ⚔ ===============")
    mago1.mostrar_Stats()
    print("--------------------- VS ---------------------")
    mago2.mostrar_Stats()
    print("----------------------------------------------")
    input("Presione ENTER para iniciar")

    if mago1.get_velocidad() > mago2.get_velocidad():
        primero = mago1
        segundo = mago2
    else:
        primero = mago2
        segundo = mago1
         
    while primero.get_hpActual() > 0 and segundo.get_hpActual() > 0:
        print(f"turno {turno}")
        daño = primero.calcular_Daño(segundo)
        v1=daño
        daño = (primero.calcular_Critico(segundo,generador.aleatorio(),daño))*(segundo.evasion(primero,generador.aleatorio()))
        v2 = daño
        v3 = v2-v1
        segundo.recibir_Daño(daño)
        if v3 > 0:
            print("¡¡¡CRITICO!!!")
        elif v3<0:
            print(f"El Mago {primero.get_nombre()} ataco, pero {segundo.get_nombre()} esquivo el ataque")
        else:
            print(f"el mago {primero.get_nombre()} ataco y causo {daño} a mago {segundo.get_nombre()}")
        daño = segundo.calcular_Daño(primero)
        v1=daño
        daño = (segundo.calcular_Critico(primero,generador.aleatorio(),daño))*(primero.evasion(segundo,generador.aleatorio()))
        v2=daño
        v3=v2-v1
        if segundo.get_hpActual() > 0:
            primero.recibir_Daño(daño)
            if v3 > 0:
                print("¡¡¡CRITICO!!!")
            elif v3<0:
                print(f"El Mago {segundo.get_nombre()} ataco, pero {primero.get_nombre()} esquivo el ataque")            
            else:
                print(f"el mago {segundo.get_nombre()} ataco y causo {daño} a mago {primero.get_nombre()}")
        print(f"{mago1.get_nombre()}: {mago1.get_hpActual()}/{mago1.get_hpMax()}           |      {mago2.get_nombre()}: {mago2.get_hpActual()}/{mago2.get_hpMax()}")
        print(f"{"▓"*mago1.get_hpActual()}{"░"* (mago1.get_hpMax()-mago1.get_hpActual())}   |   {"░"* (mago2.get_hpMax()-mago2.get_hpActual())}{"▓"*mago2.get_hpActual()}")
        input()
        turno += 1

    if primero.get_hpActual() > segundo.get_hpActual():
        print(f"EL Mago {primero.get_nombre()} derroto a {segundo.get_nombre()}")
        ganador = primero
    else:
        print(f"EL Mago {segundo.get_nombre()} derroto a {primero.get_nombre()}")
        ganador = segundo
    
    if ganador == mago1:
        mago1.subir_Nivel()
        mago1.curar((mago1.get_hpMax() * 3) // 10)
    
        
    mago1.mostrar_Stats()
