from Objects.Factions.Imperium.Common.Weapons import Weapon, Melee, DiceAttackGun, DiceDamageGun


class _Flamer(Weapon):
    def __init__(self):
        super().__init__()
        self.ABILITY = 'autohit'


class ArcheotechPistol(Weapon):
    def __init__(self):
        super().__init__()
        self.RANGE = 15
        self.S = 5
        self.AP = -2
        self.D = 2
        self.TYPE = "Pistol"


class ArmigerAutoCannon(DiceAttackGun):
    def __init__(self):
        super().__init__()
        self.RANGE = 60
        self.A = "2D3"
        self.S = 7
        self.AP = -1
        self.D = 3
        self.set_attack_dices(dices=2, die_type=3)
        self.TYPE = "Heavy"
        self.ABILITY = "Ignore the penalty to hit rolls for moving and firing this"


class AvengerGatlingCannon(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 75
        self.RANGE = 36
        self.A = 12
        self.S = 6
        self.AP = -2
        self.D = 2
        self.TYPE = "Heavy"


class ConflagrationCannon(_Flamer, DiceAttackGun):
    def __init__(self):
        super().__init__()
        self.RANGE = 18
        self.A = '3D6'
        self.S = 7
        self.AP = -2
        self.D = 2
        self.TYPE = "Heavy"
        self.set_attack_dices(dices=3, die_type=6)


class Heavyflamer(_Flamer, DiceAttackGun):
    def __init__(self):
        super().__init__()
        self.POINTS = 17
        self.RANGE = 8
        self.A = 'D6'
        self.S = 5
        self.AP = -1
        self.TYPE = "Heavy"


class HeavyStubber(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 4
        self.RANGE = 36
        self.A = 3
        self.TYPE = "Heavy"


class IronStormMissilePod(DiceAttackGun):
    def __init__(self):
        super().__init__()
        self.POINTS = 16
        self.RANGE = 72
        self.A = 'D6'
        self.S = 5
        self.AP = -1
        self.D = 2
        self.ABILITY = "This weapon can target units that are not visible to"
        self.TYPE = "Heavy"
