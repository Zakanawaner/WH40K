import random
from shapely.geometry import Point


# Template classes
class Weapon:
    def __init__(self):
        self.POINTS = 0
        self.RANGE = 12
        self.A = 1
        self.S = 4
        self.AP = 0
        self.D = 1
        self.ABILITY = None
        self.LIST = None
        self.TYPE = None
        self.ShootingRange = None

    @staticmethod
    def throw_die(die=6):
        return random.randint(1, die)

    def shoot(self):
        return [self.throw_die() for _ in range(self.A)]

    def damage(self):
        return [self.throw_die() for _ in range(self.D)]

    def range_clean(self, body):
        self.ShootingRange = Point(body.centroid.x, body.centroid.y).buffer(self.RANGE)
        return self.ShootingRange

    def range_on_board(self, body, board):
        pass


class Melee:
    def __init__(self, A=1, S=4):
        self.POINTS = 0
        self.A = A
        self.S = S
        self.AP = 0
        self.D = 1
        self.ABILITY = None
        self.LIST = None
        self.TYPE = 'Melee'

    @staticmethod
    def throw_die(die=6):
        return random.randint(1, die)

    def punch(self):
        return [self.throw_die() for _ in range(self.A)]

    def damage(self):
        return [self.throw_die() for _ in range(self.D)]


class DiceAttackGun(Weapon):
    def __init__(self, dices=1, die_type=6):
        super().__init__()
        self.attack_dices = dices
        self.attack_die_type = die_type

    def set_attack_dices(self, dices=1, die_type=6):
        self.attack_dices = dices
        self.attack_die_type = die_type

    def shoot(self):
        attacks = 0
        for i in range(self.attack_dices):
            attacks += self.throw_die(self.attack_die_type)
        return [self.throw_die() for _ in range(attacks)]


class DiceDamageGun(Weapon):
    def __init__(self, dices=1, die_type=6):
        super().__init__()
        self.damage_dices = dices
        self.damage_die_type = die_type

    def set_damage_dices(self, dices=1, die_type=6):
        self.damage_dices = dices
        self.damage_die_type = die_type

    def damage(self):
        wounds = 0
        for i in range(self.damage_dices):
            wounds += self.throw_die(self.damage_die_type)
        return [self.throw_die() for _ in range(wounds)]


class DiceStrengthGun(Weapon):
    def __init__(self, dices=1, die_type=6):
        super().__init__()
        self.strength_dices = dices
        self.strength_die_type = die_type

    def set_strength_dices(self, dices=1, die_type=6):
        self.strength_dices = dices
        self.strength_die_type = die_type

    def set_strength(self):
        return self.throw_die()


class DiceArmoryPenetrationGun(Weapon):
    def __init__(self, dices=1, die_type=6):
        super().__init__()
        self.ap_dices = dices
        self.ap_die_type = die_type

    def set_armory_penetration_dices(self, dices=1, die_type=6):
        self.ap_dices = dices
        self.ap_die_type = die_type

    def set_armory_penetration(self):
        return self.throw_die()
