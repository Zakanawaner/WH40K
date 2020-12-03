class Infantry:
    def __init__(self):
        self.POINTS = 0
        self.M = 6
        self.WS = 3
        self.BS = 3
        self.S = 4
        self.T = 4
        self.W = 1
        self.A = 1
        self.Ld = 7
        self.Sv = 3
        self.InvSv = 0
        self.Gun = []

    def replace_gun_1(self, weapon=None):
        if weapon is not None:
            self.POINTS -= self.Gun[0].POINTS if self.Gun[0] is not None else 0
            self.Gun[0] = weapon
            self.POINTS += self.Gun[0].POINTS

    def replace_gun_2(self, weapon=None):
        if weapon is not None:
            self.POINTS -= self.Gun[1].POINTS if self.Gun[1] is not None else 0
            self.Gun[1] = weapon
            self.POINTS += self.Gun[1].POINTS

    def replace_gun_3(self, weapon=None):
        if weapon is not None:
            self.POINTS -= self.Gun[2].POINTS if self.Gun[2] is not None else 0
            self.Gun[2] = weapon
            self.POINTS += self.Gun[2].POINTS

    def replace_gun_4(self, weapon=None):
        if weapon is not None:
            self.POINTS -= self.Gun[3].POINTS if self.Gun[3] is not None else 0
            self.Gun[3] = weapon
            self.POINTS += self.Gun[3].POINTS


class Sergeant:
    def __init__(self):
        self.A += 1
        self.Ld += 1
        self.Gun[4] = None

    # Sergeant weapons List
    def choose_sergeant_weapon(self, sergeant_weapon_1=None, sergeant_weapon_2=None):
        if sergeant_weapon_1 is not None:
            self.POINTS -= self.Gun[0].POINTS
            self.Gun[0] = sergeant_weapon_1
            self.POINTS += self.Gun[0].POINTS
        if sergeant_weapon_2 is not None:
            self.POINTS -= self.Gun[1].POINTS
            self.Gun[1] = sergeant_weapon_2
            self.POINTS += self.Gun[1].POINTS

    def replace_gun_5(self, weapon=None):
        if weapon is not None:
            self.POINTS -= self.Gun[4].POINTS if self.Gun[4] is not None else 0
            self.Gun[4] = weapon
            self.POINTS += self.Gun[4].POINTS


class Vehicle:
    def __init__(self):
        self.POINTS = 0
        self.M = 6
        self.WS = 3
        self.BS = 3
        self.S = 6
        self.T = 7
        self.W = 8
        self.A = 4
        self.Ld = 8
        self.Sv = 3
        self.InvSv = 0
        self.Gun = []
        self.FirstM = 0
        self.SecondM = 0
        self.ThirdM = 0
        self.FirstWS = 0
        self.SecondWS = 0
        self.ThirdWS = 0
        self.FirstBS = 0
        self.SecondBS = 0
        self.ThirdBS = 0
        self.FirstA = 0
        self.SecondA = 0
        self.ThirdA = 0
        self.FirstW = 0
        self.SecondW = 0
        self.SquadPosition = -1
        self.ModelPosition = -1

    def replace_gun_1(self, weapon=None):
        if weapon is not None:
            self.POINTS -= self.Gun[0].POINTS if self.Gun[0] is not None else 0
            self.Gun[0] = weapon
            self.POINTS += self.Gun[0].POINTS

    def replace_gun_2(self, weapon=None):
        if weapon is not None:
            self.POINTS -= self.Gun[1].POINTS if self.Gun[1] is not None else 0
            self.Gun[1] = weapon
            self.POINTS += self.Gun[1].POINTS

    def replace_gun_3(self, weapon=None):
        if weapon is not None:
            self.POINTS -= self.Gun[2].POINTS if self.Gun[2] is not None else 0
            self.Gun[2] = weapon
            self.POINTS += self.Gun[2].POINTS

    def replace_gun_4(self, weapon=None):
        if weapon is not None:
            self.POINTS -= self.Gun[3].POINTS if self.Gun[3] is not None else 0
            self.Gun[3] = weapon
            self.POINTS += self.Gun[3].POINTS

    def replace_gun_5(self, weapon=None):
        if weapon is not None:
            self.POINTS -= self.Gun[4].POINTS if self.Gun[4] is not None else 0
            self.Gun[4] = weapon
            self.POINTS += self.Gun[4].POINTS

    def replace_gun_6(self, weapon=None):
        if weapon is not None:
            self.POINTS -= self.Gun[5].POINTS if self.Gun[5] is not None else 0
            self.Gun[5] = weapon
            self.POINTS += self.Gun[5].POINTS

    def damage_update(self, M=False, WS=False, BS=False, A=False):
        if self.W >= self.FirstW:
            self.M = self.FirstM if M else self.M
            self.WS = self.FirstWS if WS else self.WS
            self.BS = self.FirstBS if BS else self.BS
            self.A = self.FirstA if A else self.A
        if self.FirstW > self.W >= self.SecondW:
            self.M = self.SecondM if M else self.M
            self.WS = self.SecondWS if WS else self.WS
            self.BS = self.SecondBS if BS else self.BS
            self.A = self.SecondA if A else self.A
        if self.W < self.SecondW:
            self.M = self.ThirdM if M else self.M
            self.WS = self.ThirdWS if WS else self.WS
            self.BS = self.ThirdBS if BS else self.BS
            self.A = self.ThirdA if A else self.A
