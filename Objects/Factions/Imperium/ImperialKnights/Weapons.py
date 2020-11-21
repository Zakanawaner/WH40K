from Objects.Common.Weapons import Weapon, Melee, DiceAttackGun, DiceDamageGun


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


class ArmigerAutoCannon(Weapon, DiceAttackGun):
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


class IronStormMissilePod(Weapon, DiceAttackGun):
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


class -Lowintensity(Weapon, DiceAttackGun, DiceDamageGun):
    def __init__(self):
        super().__init__()
        self.RANGE = 36
        self.A = 2D6
        self.S = 6
        self.AP = -2
        self.D = D3
        self.TYPE = "Heavy"


class -Highintensity(Weapon, DiceAttackGun, DiceDamageGun):
    def __init__(self):
        super().__init__()
        self.RANGE = 18
        self.A = D6
        self.S = 12
        self.AP = -4
        self.D = D6
        self.TYPE = "Heavy"


class Meltagun(Weapon, DiceDamageGun):
    def __init__(self):
        super().__init__()
        self.POINTS = 17
        self.S = 8
        self.AP = -4
        self.D = D6
        self.ABILITY = "If the target is within half range of this weapon, roll two dice"
        self.TYPE = "Assault"


class Multi-laser(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 10
        self.RANGE = 36
        self.A = 3
        self.S = 6
        self.TYPE = "Heavy"


class -Standard(Weapon, DiceAttackGun):
    def __init__(self):
        super().__init__()
        self.RANGE = 48
        self.A = 2D6
        self.S = 7
        self.AP = -3
        self.TYPE = "Heavy"


class -Supercharge(Weapon, DiceAttackGun):
    def __init__(self):
        super().__init__()
        self.RANGE = 48
        self.A = 2D6
        self.S = 8
        self.AP = -3
        self.D = 2
        self.ABILITY = "For each hit roll of 1, the bearer suffers 1 mortal wound after"
        self.TYPE = "Heavy"


class Rapid-firebattlecannon(Weapon, DiceAttackGun, DiceDamageGun):
    def __init__(self):
        super().__init__()
        self.POINTS = 100
        self.RANGE = 72
        self.A = 2D6
        self.S = 8
        self.AP = -2
        self.D = D3
        self.TYPE = "Heavy"


class Shieldbreakermissile(Weapon, DiceDamageGun):
    def __init__(self):
        super().__init__()
        self.POINTS = 12
        self.RANGE = 48
        self.S = 10
        self.AP = -4
        self.D = D
        self.ABILITY = "D6"
        self.TYPE = "Heavy"


class Stormspearrocketpod(Weapon, DiceDamageGun):
    def __init__(self):
        super().__init__()
        self.POINTS = 45
        self.RANGE = 48
        self.A = 3
        self.S = 8
        self.AP = -2
        self.D = D6
        self.TYPE = "Heavy"


class Thermalcannon(Weapon, DiceAttackGun, DiceDamageGun):
    def __init__(self):
        super().__init__()
        self.POINTS = 76
        self.RANGE = 36
        self.A = D6
        self.S = 9
        self.AP = -4
        self.D = D6
        self.ABILITY = "If the target is within half range of this weapon, roll two dice"
        self.TYPE = "Heavy"


class Thermalspear(Weapon, DiceAttackGun, DiceDamageGun):
    def __init__(self):
        super().__init__()
        self.RANGE = 30
        self.A = D3
        self.S = 8
        self.AP = -4
        self.D = D
        self.ABILITY = "D6"
        self.TYPE = "Assault"


class Thundercoilharpoon(Weapon):
    def __init__(self):
        super().__init__()
        self.S = 16
        self.AP = -6
        self.ABILITY = "10"
        self.TYPE = "Heavy"


class additionalD(Weapon):
    def __init__(self):
        super().__init__()
        self.RANGE = 3
        self.A = wounds
        self.S = wounds
        self.AP = wounds
        self.D = wounds
        self.ABILITY = "wounds."
        self.TYPE = "mortal"


class TwinIcarusautocannon(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 30
        self.RANGE = 48
        self.A = 4
        self.S = 7
        self.AP = -1
        self.D =
        self.ABILITY = "2"
        self.TYPE = "Heavy"


class Add(Weapon):
    def __init__(self):
        super().__init__()
        self.RANGE = 1
        self.A = all
        self.S = hit
        self.AP = rolls
        self.D = made
        self.ABILITY = "for this weapon against targets"
        self.TYPE = "to"


class thatcanFLY.Subtract(Weapon):
    def __init__(self):
        super().__init__()
        self.RANGE = 1
        self.A = the
        self.S = hit
        self.AP = rolls
        self.D = made
        self.ABILITY = "for this"
        self.TYPE = "from"


class Twinmeltagun(Weapon, DiceDamageGun):
    def __init__(self):
        super().__init__()
        self.A = 2
        self.S = 8
        self.AP = -4
        self.D = D6
        self.ABILITY = "If the target is within half range of this weapon, roll two dice"
        self.TYPE = "Assault"


class Twinsiegebreakercannon(Weapon, DiceAttackGun, DiceDamageGun):
    def __init__(self):
        super().__init__()
        self.POINTS = 35
        self.RANGE = 48
        self.A = 2D3
        self.S = 7
        self.AP = -1
        self.D = D3
        self.TYPE = "Heavy"


class Volcanolance(Weapon, DiceAttackGun, DiceDamageGun):
    def __init__(self):
        super().__init__()
        self.RANGE = 80
        self.A = D6
        self.S = 14
        self.AP = -5
        self.D = 3D3
        self.ABILITY = "You can re-roll failed wound rolls when targeting TITANIC"
        self.TYPE = "Heavy"


class Freedom’sHand(Melee, DiceDamageGun):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.S x= 2
        self.AP = -4
        self.D = 2D
        self.ABILITY = "2D6"
        self.TYPE = "Melee"


class Whenattackingwiththisweapon,youmustsubtract(Weapon):
    def __init__(self):
        super().__init__()
        self.RANGE = 1
        self.A = the
        self.S = hi
        self.AP = hi
        self.D = hi
        self.ABILITY = "hit"
        self.TYPE = "from"


class roll.Treatanydamagerolllessthan(Weapon):
    def __init__(self):
        super().__init__()
        self.RANGE = 6
        self.A = with
        self.S = this
        self.AP = weapon
        self.D = as
        self.ABILITY = "6"
        self.TYPE = "made"


class enemyunitwithin(Weapon):
    def __init__(self):
        super().__init__()
        self.RANGE = 9
        self.A = the
        self.S = bearer
        self.AP = and
        self.D = roll
        self.ABILITY = "a D6. On a 4+ that unit"
        self.TYPE = "of"


class suffersD(Weapon):
    def __init__(self):
        super().__init__()
        self.RANGE = 3
        self.A = wounds
        self.S = wounds
        self.AP = wounds
        self.D = wounds
        self.ABILITY = "wounds."
        self.TYPE = "mortal"


class -Strike(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.S x= 2
        self.AP = -3
        self.D = 3
        self.TYPE = "Melee"


class -Sweep(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.S = User
        self.AP = -2
        self.ABILITY = "Make 2 hit rolls for each attack made with this weapon, instead of 1."
        self.TYPE = "Melee"


class Reaperchainsword(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.POINTS = 30
        self.S += 6
        self.AP = -3
        self.D = 6
        self.TYPE = "Melee"


class Thunderstrikegauntlet(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.POINTS = 35
        self.S x= 2
        self.AP = -4
        self.D =
        self.ABILITY = "6"
        self.TYPE = "Melee"


class Whenattackingwiththisweapon,youmustsubtract(Weapon):
    def __init__(self):
        super().__init__()
        self.RANGE = 1
        self.A = the
        self.S = hi
        self.AP = hi
        self.D = hi
        self.ABILITY = "hit"
        self.TYPE = "from"


class enemyunitwithin(Weapon):
    def __init__(self):
        super().__init__()
        self.RANGE = 9
        self.A = the
        self.S = bearer
        self.AP = and
        self.D = roll
        self.ABILITY = "a D6. On a 4+ that unit"
        self.TYPE = "of"


class suffersD(Weapon):
    def __init__(self):
        super().__init__()
        self.RANGE = 3
        self.A = wounds
        self.S = wounds
        self.AP = wounds
        self.D = wounds
        self.ABILITY = "wounds."
        self.TYPE = "mortal"


class Titanicfeet(Melee, DiceDamageGun):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.S = User
        self.AP = -2
        self.D = D3
        self.ABILITY = "Make 3 hit rolls for each attack made with this weapon."
        self.TYPE = "Melee"


