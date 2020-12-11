from Game.Players import Player
from Game import Missions
from Objects import Boards


class CoreGame:
    def __init__(self, player1Name='1', player2name='2'):
        self.Player1 = Player(player1Name)
        self.Player2 = Player(player2name)
        self.Mission = Missions.OnlyWar()
        self.Board = None


