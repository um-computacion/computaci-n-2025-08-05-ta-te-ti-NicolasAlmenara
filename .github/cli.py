from tateti import Tateti
def main():
    print("Bienvenido al tateti")
    nombre1= str(input("ingrese el nombre del jugador 1: "))
    nombre2= str(input("ingrese el nombre del jugador 2: "))
    juego = Tateti(nombre1, nombre2)
    contador = 0
    while True:
        print("Tablero:")
        juego.mostar_tablero()
        print(f"Es el turno del jugador {juego.jugador_actual()}")
        while True:
            while True:
                try:
                    fila = int(input("ingrese el numero de la fila que quiere ingresar (del 0 al 2): "))
                    if fila in [0, 1, 2]:
                        break
                    else:
                        print("numero de fila invalido, recuerde que el numero debe ser 0, 1 o 2")
                except ValueError:
                    print("debe ingresar un numero entero")
            while True:
                try:
                    columna = int(input("ingrese el numero de la columna que quiere ingresar (del 0 al 2): "))
                    if columna in [0, 1, 2]:
                        break
                    else:
                        print("numero de columna invalido, recuerde que el numero debe ser 0, 1 o 2")
                except ValueError:
                    print("debe ingresar un numero entero")
            if juego.validar_movimiento(fila, columna):
                juego.poner_ficha(juego.turno, fila, columna)
                contador = contador + 1
                break
            else:
                print("ya hay una ficha en esa posicion, escoja otra")
        
        if juego.ganador():
            print(f"El ganador es {juego.jugador_actual()}")
            break
        if juego.empate(contador):
            print("EMPATE!")
            break
        juego.cambio_turno()




if __name__ == '__main__':
    main()



