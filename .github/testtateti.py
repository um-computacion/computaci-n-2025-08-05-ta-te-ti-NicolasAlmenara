import unittest
from tateti import Tateti
class TestTateti(unittest.TestCase):
    def test_jugador_actual(self):
        tateti = Tateti("Nicolas", "Martin")
        tateti.turno = "O"
        self.assertEqual(tateti.jugador_actual(), "Martin")
    def test_jugador_actual1(self):
        tateti = Tateti("Nicolas", "Martin")
        tateti.turno = "X"
        self.assertEqual(tateti.jugador_actual(), "Nicolas")
    def test_cambio_turno(self):
        tateti = Tateti("Nicolas", "Martin")
        tateti.cambio_turno()
        self.assertEqual(tateti.turno, "O")
    def test_cambio_turno1(self):
        tateti = Tateti("Nicolas", "Martin")
        tateti.turno = "O"
        tateti.cambio_turno()
        self.assertEqual(tateti.turno, "X")


if __name__ == "__main__":
    unittest.main()