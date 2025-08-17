
class Tablero:
    def __init__(self):
        self.matriz = [["", "", ""], ["", "", ""], ["", "", ""]]
    
    def mostar_tablero(self):
        for fila in self.matriz:
            print (fila)
    
    def validar_movimiento(self, fil, col):
        if self.matriz[fil][col] == "":
            return True
        else:
            return False
    
    def poner_ficha(self, turno, fil, col):
        if self.validar_movimiento(fil, col):
            self.matriz[fil][col] = turno
            return True
        else:
            return False
    
    def ganador(self):
        for fila in self.matriz:
            if fila[0] == fila[1] == fila[2] != "":
                return True
        for col in range(3):
            if self.matriz[0][col] ==  self.matriz[1][col] == self.matriz[2][col] != "":
                return True
        if self.matriz[0][0] == self.matriz[1][1] == self.matriz[2][2] != "":
            return True
        if self.matriz[0][2] == self.matriz[1][1] == self.matriz[2][0] != "":
            return True
        return False
    
    def empate(self, contador):
        if not self.ganador() and contador >= 9:
            return True
        return False

        


