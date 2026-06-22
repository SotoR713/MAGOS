
def raiz_digital(numero):
    while numero >= 10:
        suma = 0
        for i in str(numero):
            suma += int(i)
        numero = suma
    return numero





