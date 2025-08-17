from jugador import Jugador
import unittest
class TestJugador(unittest.TestCase):
    def test_crear_jugador(self):
        mijugador = Jugador("Nicolas", "X")
        self.assertEqual("Nicolas", mijugador.nombre)
        self.assertEqual("X", mijugador.ficha)

if __name__ == "__main__":
    unittest.main()