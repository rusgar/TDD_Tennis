  
class Juego:

    PLAYER1 = 0
    PLAYER2 = 1

    scores = [ 0 , 15 , 30 , 40, 'adv', 'win']

    def __init__(self, name):
        self.name = name
        self.winner = None
        self.players = []

    def addPlayer1(self,player):
        self.players.insert(Juego.PLAYER1, player)

    def addPlayer2(self,player):
        self.players.insert(Juego.PLAYER2, player)

    def countPlayers(self):
        return len(self.players)

    def winPoint(self, playerIndex):
        oponentIndex = int(not playerIndex)

        player = self.getPlayer(playerIndex)
        oponent = self.getPlayer(oponentIndex)

        playerScore = self.getScore(playerIndex)
        oponentScore = self.getScore(oponentIndex)

       
        if playerScore == 40:
            if oponentScore == 40:
                
                player.setAdvance()
            elif oponentScore == 'adv':
                
                oponent.setFourty()
            else:
                player.setWinScore()
                self.setWinner(playerIndex)
        else:
            player.incrementScore()

        if playerScore == 'adv':
            player.setWinScore()
            self.setWinner(playerIndex)

    def getPlayer(self,playerIndex):
        return self.players[playerIndex]

    def getScore(self,playerIndex):
        playerScore = self.players[playerIndex].getScore()
        return Juego.scores[playerScore]

    def getWinner(self):
        return self.winner
    
    def setWinner(self,player):
        self.winner = player
        self.players[player].setWinScore()