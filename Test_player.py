import unittest
from player import Player
from Juego import Juego


class TenisTest(unittest.TestCase):

    def test_creacion_jugador(self):
        Edu = Player('Edu')
        self.assertEqual(Edu.name, 'Edu')

    def test_inital_score(self):
        Edu = Player('Edu')
        self.assertEqual(Edu.getScore(), 0)

    def test_new_Juego(self):
        RolandGarros = Juego("Roland Garros")
        self.assertEqual(RolandGarros.name, 'Roland Garros')

    def test_añadir_jugador(self):
        Edu = Player('Edu')
        RolandGarros = Juego("Roland Garros")
        RolandGarros.addPlayer1(Edu)

        self.assertEqual(RolandGarros.countPlayers(), 1)

    def test_añadir_otrojugador(self):
        Rafa = Player('Rafa')
        RolandGarros = Juego("Roland Garros")
        RolandGarros.addPlayer2(Rafa)

        self.assertEqual(RolandGarros.countPlayers(), 1)

    def prueba_ganar_jugador_1_juego_con_diferencia_de_dos(self):

        Edu = Player("Edu")
        Rafa = Player("Rafa")

        RolandGarros = Juego("Roland Garros")
        RolandGarros.addPlayer1(Edu)
        RolandGarros.addPlayer2(Rafa)

        RolandGarros.winPoint(Juego.PLAYER1)  # 15 / 0
        RolandGarros.winPoint(Juego.PLAYER1)  # 30 / 0
        RolandGarros.winPoint(Juego.PLAYER1)  # 40 / 0
        RolandGarros.winPoint(Juego.PLAYER1)  # Win / 0

        self.assertEqual(RolandGarros.getWinner(), Juego.PLAYER1)

    def prueba_ganar_jugador_2_juego_con_diferencia_de_dos(self):

        Edu = Player("Edu")
        Rafa = Player("Rafa")

        RolandGarros = Juego("Roland Garros")
        RolandGarros.addPlayer1(Edu)
        RolandGarros.addPlayer2(Rafa)

        RolandGarros.winPoint(Juego.PLAYER2)  # 15 / 0
        RolandGarros.winPoint(Juego.PLAYER2)  # 30 / 0
        RolandGarros.winPoint(Juego.PLAYER2)  # 40 / 0
        RolandGarros.winPoint(Juego.PLAYER2)  # Win / 0

        self.assertEqual(RolandGarros.getWinner(), Juego.PLAYER2)

    def test_jugador1_gana_ventaja(self):

        Edu = Player("Edu")

        Rafa = Player("Rafa")

        RolandGarros = Juego("Roland Garros")
        RolandGarros.addPlayer1(Edu)
        RolandGarros.addPlayer2(Rafa)

        RolandGarros.winPoint(Juego.PLAYER1)  # 15 / 0
        RolandGarros.winPoint(Juego.PLAYER1)  # 30 / 0
        RolandGarros.winPoint(Juego.PLAYER1)  # 40 / 0

        RolandGarros.winPoint(Juego.PLAYER2)  # 15 / 0
        RolandGarros.winPoint(Juego.PLAYER2)  # 30 / 0
        RolandGarros.winPoint(Juego.PLAYER2)  # 40 / 0

        RolandGarros.winPoint(Juego.PLAYER1)  # adv / 40

        self.assertEqual(RolandGarros.getScore(Juego.PLAYER1), 'adv')
        self.assertIsNone(RolandGarros.getWinner())

    def test_jugador2_gana_ventaja(self):
    
        Edu = Player("Edu")

        Rafa = Player("Rafa")

        RolandGarros = Juego("Roland Garros")
        RolandGarros.addPlayer1(Edu)
        RolandGarros.addPlayer2(Rafa)

        RolandGarros.winPoint(Juego.PLAYER1)  # 15 / 0
        RolandGarros.winPoint(Juego.PLAYER1)  # 30 / 0
        RolandGarros.winPoint(Juego.PLAYER1)  # 40 / 0

        RolandGarros.winPoint(Juego.PLAYER2)  # 15 / 0
        RolandGarros.winPoint(Juego.PLAYER2)  # 30 / 0
        RolandGarros.winPoint(Juego.PLAYER2)  # 40 / 0

        RolandGarros.winPoint(Juego.PLAYER2)  # adv / 40

        self.assertEqual(RolandGarros.getScore(Juego.PLAYER2), 'adv')
        self.assertIsNone(RolandGarros.getWinner())

    def test_Jugador1_perdida_ventaja(self):

        Edu = Player("Edu")

        Rafa = Player("Rafa")

        RolandGarros = Juego("Roland Garros")
        RolandGarros.addPlayer1(Edu)
        RolandGarros.addPlayer2(Rafa)

        RolandGarros.winPoint(Juego.PLAYER1)  # 15 / 0
        RolandGarros.winPoint(Juego.PLAYER1)  # 30 / 0
        RolandGarros.winPoint(Juego.PLAYER1)  # 40 / 0

        RolandGarros.winPoint(Juego.PLAYER2)  # 15 / 0
        RolandGarros.winPoint(Juego.PLAYER2)  # 30 / 0
        RolandGarros.winPoint(Juego.PLAYER2)  # 40 / 0

        RolandGarros.winPoint(Juego.PLAYER1)  # adv / 40

        RolandGarros.winPoint(Juego.PLAYER2)  # 40 / 40

        self.assertEqual(RolandGarros.getScore(Juego.PLAYER2), 40)
        self.assertEqual(RolandGarros.getScore(Juego.PLAYER1), 40)

        self.assertIsNone(RolandGarros.getWinner())

    def test_Jugador2_perdida_ventaja(self):
    
        Edu = Player("Edu")

        Rafa = Player("Rafa")

        RolandGarros = Juego("Roland Garros")
        RolandGarros.addPlayer1(Edu)
        RolandGarros.addPlayer2(Rafa)

        RolandGarros.winPoint(Juego.PLAYER1)  # 15 / 0
        RolandGarros.winPoint(Juego.PLAYER1)  # 30 / 0
        RolandGarros.winPoint(Juego.PLAYER1)  # 40 / 0

        RolandGarros.winPoint(Juego.PLAYER2)  # 15 / 0
        RolandGarros.winPoint(Juego.PLAYER2)  # 30 / 0
        RolandGarros.winPoint(Juego.PLAYER2)  # 40 / 0

        RolandGarros.winPoint(Juego.PLAYER2)  # adv / 40

        RolandGarros.winPoint(Juego.PLAYER1)  # 40 / 40

        self.assertEqual(RolandGarros.getScore(Juego.PLAYER1), 40)
        self.assertEqual(RolandGarros.getScore(Juego.PLAYER2), 40)

        self.assertIsNone(RolandGarros.getWinner())

    def test_Jugador1_get_ganador_con_ventaja(self):

        Edu = Player("Edu")

        Rafa = Player("Rafa")

        RolandGarros = Juego("Roland Garros")
        RolandGarros.addPlayer1(Edu)
        RolandGarros.addPlayer2(Rafa)

        RolandGarros.winPoint(Juego.PLAYER1)  # 15 / 0
        RolandGarros.winPoint(Juego.PLAYER1)  # 30 / 0
        RolandGarros.winPoint(Juego.PLAYER1)  # 40 / 0

        RolandGarros.winPoint(Juego.PLAYER2)  # 15 / 0
        RolandGarros.winPoint(Juego.PLAYER2)  # 30 / 0
        RolandGarros.winPoint(Juego.PLAYER2)  # 40 / 0

        RolandGarros.winPoint(Juego.PLAYER1)  # adv / 40

        RolandGarros.winPoint(Juego.PLAYER1)  # Win / 40

        self.assertEqual(RolandGarros.getScore(Juego.PLAYER1), 'win')
        self.assertEqual(RolandGarros.getWinner(), Juego.PLAYER1)

    def test_Jugador2_get_ganador_con_ventaja(self):
    
        Edu = Player("Edu")

        Rafa = Player("Rafa")

        RolandGarros = Juego("Roland Garros")
        RolandGarros.addPlayer1(Edu)
        RolandGarros.addPlayer2(Rafa)

        RolandGarros.winPoint(Juego.PLAYER1)  # 15 / 0
        RolandGarros.winPoint(Juego.PLAYER1)  # 30 / 0
        RolandGarros.winPoint(Juego.PLAYER1)  # 40 / 0

        RolandGarros.winPoint(Juego.PLAYER2)  # 15 / 0
        RolandGarros.winPoint(Juego.PLAYER2)  # 30 / 0
        RolandGarros.winPoint(Juego.PLAYER2)  # 40 / 0

        RolandGarros.winPoint(Juego.PLAYER2)  # 40 / adv

        RolandGarros.winPoint(Juego.PLAYER2)  # 40/ WIN

        self.assertEqual(RolandGarros.getScore(Juego.PLAYER2), 'win')
        self.assertEqual(RolandGarros.getWinner(), Juego.PLAYER2)


if __name__ == '__main__':
    unittest.main()
