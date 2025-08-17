import unittest
from tablero import Tablero
class TestTablero(unittest.TestCase):
    def test_tablero(self):
        tablero = Tablero()
        self.assertEqual([["", "", ""], ["", "", ""], ["", "", ""]], tablero.matriz)
    def test_mostrar_tablero(self):
        tablero = Tablero()
        self.assertEqual(tablero.matriz, [["", "", ""], ["", "", ""], ["", "", ""]])
    def test_validar_moviemiento(self):
        tablero = Tablero()
        tablero.poner_ficha("X", 0, 0)
        self.assertFalse(tablero.validar_movimiento(0, 0))
    def test_poner_ficha(self):
        tablero = Tablero()
        tablero.poner_ficha("X", 0, 0)
        self.assertEqual("X", tablero.matriz[0][0])
    def test_ganador_horizontal(self):
        tablero = Tablero()
        tablero.poner_ficha("X", 0, 0)
        tablero.poner_ficha("X", 0, 1)
        tablero.poner_ficha("X", 0, 2)
        self.assertTrue(tablero.ganador())
    def test_ganador_vertical(self):
        tablero = Tablero()
        tablero.poner_ficha("X", 0, 0)
        tablero.poner_ficha("X", 1, 0)
        tablero.poner_ficha("X", 2, 0)
        self.assertTrue(tablero.ganador())
    def test_ganador_diagonal1(self):
        tablero = Tablero()
        tablero.poner_ficha("X", 0, 0)
        tablero.poner_ficha("X", 1, 1)
        tablero.poner_ficha("X", 2, 2)
        self.assertTrue(tablero.ganador())
    def test_ganador_diagonal1(self):
        tablero = Tablero()
        tablero.poner_ficha("X", 0, 2)
        tablero.poner_ficha("X", 1, 1)
        tablero.poner_ficha("X", 2, 0)
        self.assertTrue(tablero.ganador())
    def test_empate(self):
        tablero = Tablero()
        tablero.poner_ficha("X", 0, 0)
        tablero.poner_ficha("O", 0, 1)
        tablero.poner_ficha("X", 0, 2)
        tablero.poner_ficha("O", 1, 0)
        tablero.poner_ficha("O", 1, 1)
        tablero.poner_ficha("X", 1, 2)
        tablero.poner_ficha("X", 2, 0)
        tablero.poner_ficha("X", 2, 1)
        tablero.poner_ficha("O", 2, 2)
        self.assertTrue(tablero.empate(9))
    
if __name__ == "__main__":
    unittest.main()


        