from jugador import Jugador
from tablero import Tablero

class Tateti():
    def __init__(self, nombre1, nombre2):
        self.jugador_1 = Jugador(nombre1, "X")
        self.jugador_2 = Jugador(nombre2, "O")
        self.tablero = Tablero()
        self.turno = "X"
    
    def mostar_tablero(self):
        self.tablero.mostar_tablero()

    def jugador_actual(self):
        if self.turno == "X":
            return self.jugador_1.nombre
        if self.turno == "O":
            return self.jugador_2.nombre
        
    
    def cambio_turno(self):
        if self.turno == "X":
            self.turno = "O"
        else:
            self.turno = "X"
        
    def validar_movimiento(self, fil, col):
        return self.tablero.validar_movimiento(fil, col)

    def poner_ficha(self, turno, fil, col):
        return self.tablero.poner_ficha(turno, fil, col)
    
    def ganador(self):
        return self.tablero.ganador()
    
    def empate(self, contador):
        return self.tablero.empate(contador)




    