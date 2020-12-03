import random


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

    @staticmethod
    def throw_die(die=6):
        return random.randint(1, die)

    def shoot(self):
        return [self.throw_die() for _ in range(self.A)]

    def damage(self):
        return [self.throw_die() for _ in range(self.D)]


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


class BigShoota(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 5
        self.RANGE = 36
        self.A = 3
        self.S = 5
        self.TYPE = "Assault"


class BlitzMissiles(DiceDamageGun):
    def __init__(self):
        super().__init__()
        self.RANGE = 18
        self.S = 6
        self.AP = -1
        self.D = 'D3'
        self.TYPE = "Assault"
        self.set_damage_dices(dices=1, die_type=3)


class BubbleChukka(DiceDamageGun, DiceAttackGun, DiceStrengthGun, DiceArmoryPenetrationGun):
    def __init__(self):
        super().__init__()
        self.POINTS = 30
        self.RANGE = 48
        self.A = 'D6'
        self.S = 'D6'
        self.AP = '-D6'
        self.D = 'D6'
        self.TYPE = "Heavy"


class BurnaShooting(DiceAttackGun):
    def __init__(self):
        super().__init__()
        self.RANGE = 8
        self.A = 'D3'
        self.TYPE = "Assault"
        self.set_attack_dices(dices=1, die_type=3)


class BurnaBottles(DiceAttackGun):
    def __init__(self):
        super().__init__()
        self.RANGE = 6
        self.A = '2D6'
        self.ABILITY = "Units do not receive the benefit of cover to their saving throws for attacks made with this weapon."
        self.TYPE = "Grenade"
        self.set_attack_dices(dices=2, die_type=6)


class BurnaExhaust(DiceAttackGun):
    def __init__(self):
        super().__init__()
        self.RANGE = 8
        self.A = 'D3'
        self.ABILITY = "This weapon automatically hits its target."
        self.TYPE = "Assault"
        self.set_attack_dices(dices=1, die_type=3)
