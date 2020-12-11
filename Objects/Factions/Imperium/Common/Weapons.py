import random
from shapely.geometry import Point


# Template classes
class Weapon:
    def __init__(self):
        self.Points = 0
        self.Range = 12
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
        self.ShootingRange = Point(body.centroid.x, body.centroid.y).buffer(self.Range)
        return self.ShootingRange

    def range_on_board(self, body, board):
        pass


class Melee:
    def __init__(self, A=1, S=4):
        self.Points = 0
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


class Combi(Weapon):
    def __init__(self, gun1, gun2):
        super().__init__()
        self.ABILITY = 'Whith both selected, -1 hit roll'
        self.selection_1 = True
        self.selection_2 = False
        self.gun_1 = gun1
        self.gun_2 = gun2

    def set_1(self):
        self.selection_1 = True

    def reset_1(self):
        self.selection_1 = False

    def set_2(self):
        self.selection_2 = True

    def reset_2(self):
        self.selection_2 = False


class Flamer_(Weapon):
    def __init__(self):
        super().__init__()
        self.ABILITY = 'autohit'


class Plasma(Weapon):
    def __init__(self, ability_type=0):
        super().__init__()
        ABILITY = ['If hitroll = 1, -1 wound to the bearer',
                   'If hitroll = 1, -1 wound to the bearer after all the shots of this weapon resolved',
                   'If hitroll = 1, -3 wound to the bearer and the weapon is broken']
        self.ABILITY = ABILITY[ability_type]
        self.supercharge = False

    def set_supercharge(self):
        if not self.supercharge:
            self.supercharge = True
            self.S += 1
            self.D += 1

    def reset_supercharge(self):
        if self.supercharge:
            self.supercharge = False
            self.S -= 1
            self.D -= 1


class Melta(Weapon):
    def __init__(self):
        super().__init__()
        self.ABILITY = 'If target < half range, roll two dice to wound and stay with the best'
