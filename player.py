class Player:
    
    ZERO = 0
    FIFTEEN = 1
    THIRTY = 2
    FOURTY = 3
    VENTAJA = 4
    WINNER = 5

    def __init__(self, name):
        self.name = name
        self.currentScore = 0

    def getScore(self):
        return self.currentScore

    def incrementScore(self):
        self.currentScore += 1

    def setFourty(self):
        self.currentScore = Player.FOURTY

    def setWinScore(self):
        self.currentScore = Player.WINNER

    def setAdvance(self):
        self.currentScore = Player.VENTAJA
