from .Turns import PlayerTurn


class Player:
    def __init__(self, name):
        self.Name = name
        self.Army = None
        self.Turn = PlayerTurn()

    def set_name(self, name):
        self.Name = name
