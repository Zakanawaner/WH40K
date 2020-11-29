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


class -Standard(Weapon):
    def __init__(self):
        super().__init__()
        self.RANGE = 24
        self.A = 3
        self.S = 7
        self.AP = -3
        self.D = 2
        self.TYPE = "Heavy"


class -Supercharge(Weapon):
    def __init__(self):
        super().__init__()
        self.RANGE = 24
        self.A = 3
        self.S = 8
        self.AP = -3
        self.D = 3
        self.ABILITY = "If you roll one or more unmodified hit rolls of 1, the bearer suffers 1 mortal wound after all of this weapon’s attacks have been resolved."
        self.TYPE = "Heavy"


class Dakkagun(Weapon):
    def __init__(self):
        super().__init__()
        self.RANGE = 18
        self.A = 3
        self.S = 5
        self.TYPE = "Assault"


class Deffgun(Weapon):
    def __init__(self):
        super().__init__()
        self.RANGE = 48
        self.A = D3
        self.S = 7
        self.AP = -1
        self.D = 2
        self.ABILITY = "Before a unit fires this weapon, roll once for the number of attacks and use this for all deffguns fired by the unit until the end of the phase."
        self.TYPE = "Heavy"


class Deffkannon(Weapon):
    def __init__(self):
        super().__init__()
        self.RANGE = 72
        self.A = 3D6
        self.S = 10
        self.AP = -4
        self.D = D6
        self.TYPE = "Heavy"


class Deffstormmega-shoota(Weapon):
    def __init__(self):
        super().__init__()
        self.RANGE = 36
        self.A = 18
        self.S = 6
        self.AP = -1
        self.TYPE = "Heavy"


class Grotblasta(Weapon):
    def __init__(self):
        super().__init__()
        self.S = 3
        self.TYPE = "Pistol"


class Grotzooka(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 10
        self.RANGE = 18
        self.A = 2D3
        self.S = 6
        self.TYPE = "Heavy"


class -Bilesquig(Weapon):
    def __init__(self):
        super().__init__()
        self.RANGE = 36
        self.A = 2D6
        self.S = *
        self.ABILITY = "This weapon always wounds on a 4+ unless it is targeting a VEHICLE or TITANIC unit, in which case it wounds on a 6+."
        self.TYPE = "Assault"


class -Biteysquig(Weapon):
    def __init__(self):
        super().__init__()
        self.RANGE = 36
        self.A = 2
        self.S = 5
        self.AP = -3
        self.D = 2
        self.TYPE = "Assault"


class -Boomsquig(Weapon):
    def __init__(self):
        super().__init__()
        self.RANGE = 36
        self.A = 2D3
        self.S = 6
        self.AP = -1
        self.D = D3
        self.TYPE = "Assault"


class -Frag(Weapon):
    def __init__(self):
        super().__init__()
        self.RANGE = 36
        self.A = D6
        self.TYPE = "Heavy"


class -Shell(Weapon):
    def __init__(self):
        super().__init__()
        self.RANGE = 36
        self.S = 8
        self.AP = -2
        self.D = D6
        self.TYPE = "Heavy"


class -Burna(Weapon):
    def __init__(self):
        super().__init__()
        self.RANGE = 8
        self.A = D6
        self.S = 5
        self.AP = -1
        self.ABILITY = "This weapon automatically hits its target."
        self.TYPE = "Assault"


class -Cutta(Weapon):
    def __init__(self):
        super().__init__()
        self.RANGE = 8
        self.A = 2
        self.S = 8
        self.AP = -4
        self.D = D6
        self.ABILITY = "If the target is within half range of this weapon, roll two dice when inflicting"
        self.TYPE = "Assault"


class Killkannon(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 15
        self.RANGE = 24
        self.A = D6
        self.S = 8
        self.AP = -2
        self.D = 2
        self.TYPE = "Heavy"


class Kombi-weaponwithrokkitlaunchaWhenattackingwiththisweapon,chooseoneorbothoftheprofilesbelow.Ifyouchooseboth,subtract(Weapon):
    def __init__(self):
        super().__init__()
        self.RANGE = 1
        self.A = all
        self.S = hit
        self.AP = rolls
        self.D = rolls
        self.ABILITY = "rolls."
        self.TYPE = "from"


class -Rokkitlauncha(Weapon):
    def __init__(self):
        super().__init__()
        self.RANGE = 24
        self.S = 8
        self.AP = -2
        self.D = 3
        self.TYPE = "Assault"


class -Shoota(Weapon):
    def __init__(self):
        super().__init__()
        self.RANGE = 18
        self.A = 2
        self.TYPE = "Assault"


class Kombi-weaponwithskorchaWhenattackingwiththisweapon,chooseoneorbothoftheprofilesbelow.Ifyouchooseboth,subtract(Weapon):
    def __init__(self):
        super().__init__()
        self.RANGE = 1
        self.A = all
        self.S = hit
        self.AP = rolls
        self.D = rolls
        self.ABILITY = "rolls."
        self.TYPE = "from"


class -Shoota(Weapon):
    def __init__(self):
        super().__init__()
        self.RANGE = 18
        self.A = 2
        self.TYPE = "Assault"


class -Skorcha(Weapon):
    def __init__(self):
        super().__init__()
        self.RANGE = 8
        self.A = D6
        self.S = 5
        self.AP = -1
        self.ABILITY = "This weapon automatically hits its target."
        self.TYPE = "Assault"


class Koptarokkits(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 24
        self.RANGE = 24
        self.A = 2
        self.S = 8
        self.AP = -2
        self.D = 3
        self.TYPE = "Assault"


class Kustommega-blasta(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 9
        self.RANGE = 24
        self.S = 8
        self.AP = -3
        self.D = D6
        self.ABILITY = "If you roll one or more unmodified hit rolls of 1, the bearer suffers 1 mortal wound after all of this weapon’s attacks have been resolved."
        self.TYPE = "Assault"


class Kustommega-kannon(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 45
        self.RANGE = 36
        self.A = D6
        self.S = 8
        self.AP = -3
        self.D = D
        self.ABILITY = "D6"
        self.TYPE = "Heavy"


class Kustommega-slugga(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 7
        self.S = 8
        self.AP = -3
        self.D = D
        self.ABILITY = "D6"
        self.TYPE = "Pistol"


class Kustommega-zappa(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 17
        self.RANGE = 36
        self.A = 3D3
        self.S = 8
        self.AP = -3
        self.D = D
        self.ABILITY = "D6"
        self.TYPE = "Heavy"


class Kustomshokkrifle(Weapon):
    def __init__(self):
        super().__init__()
        self.RANGE = 24
        self.A = 2
        self.S = 8
        self.AP = -3
        self.D = D6
        self.ABILITY = "If you roll one or more unmodified hit rolls of 1 for this weapon, the bearer suffers 1 mortal wound after all of this weapon’s attacks have been resolved. Each time you make a wound roll of 6+ for this weapon, the target suffers 1 mortal wound in addition to any other damage."
        self.TYPE = "Assault"


class Kustomshoota(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 2
        self.RANGE = 18
        self.A = 4
        self.TYPE = "Assault"


class Lobba(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 18
        self.RANGE = 48
        self.A = D6
        self.S = 5
        self.ABILITY = "This weapon can target units that are not visible to the bearer."
        self.TYPE = "Heavy"


class Mekspeshul(Weapon):
    def __init__(self):
        super().__init__()
        self.RANGE = 24
        self.A = 9
        self.S = 5
        self.AP = -2
        self.TYPE = "Assault"


class Rivetkannon(Weapon):
    def __init__(self):
        super().__init__()
        self.RANGE = 36
        self.A = 6
        self.S = 7
        self.AP = -2
        self.D = 2
        self.TYPE = "Assault"


class Rokkitkannon(Weapon):
    def __init__(self):
        super().__init__()
        self.RANGE = 24
        self.A = 2D3
        self.S = 8
        self.AP = -2
        self.D = 3
        self.TYPE = "Assault"


class Rokkitlauncha(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 12
        self.RANGE = 24
        self.S = 8
        self.AP = -2
        self.D = 3
        self.TYPE = "Assault"


class Pairofrokkitpistols(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 12
        self.A = 2
        self.S = 7
        self.AP = -2
        self.D = D3
        self.TYPE = "Pistol"


class Shokkattackgun(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 25
        self.RANGE = 60
        self.A = D6
        self.S = 2D6
        self.AP = -5
        self.D = D6
        self.ABILITY = '''Before firing this weapon, roll once to determine the Strength of all its shots. If the result is 11+ each successful hit inflicts D3 mortal wounds on the target in addition to any normal damage.'''
        self.TYPE = "Heavy"


class Shoota(Weapon):
    def __init__(self):
        super().__init__()
        self.RANGE = 18
        self.A = 2
        self.TYPE = "Assault"


class Shotgun(Weapon):
    def __init__(self):
        super().__init__()
        self.A = 2
        self.S = 3
        self.ABILITY = "If the target is within half range, add 1 to this weapon’s Strength."
        self.TYPE = "Assault"


class Skorcha(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 17
        self.RANGE = 8
        self.A = D6
        self.S = 5
        self.AP = -1
        self.ABILITY = "This weapon automatically hits its target."
        self.TYPE = "Assault"


class Skorchamissiles(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 20
        self.RANGE = 24
        self.A = D6
        self.S = 5
        self.AP = -1
        self.ABILITY = "Units do not receive the benefit of cover to their saving throws for attacks made with this weapon."
        self.TYPE = "Assault"


class Slugga(Weapon):
    def __init__(self):
        super().__init__()
        self.TYPE = "Pistol"


class Smashagun(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 16
        self.RANGE = 48
        self.A = D3
        self.S = *
        self.AP = -4
        self.D = D6
        self.ABILITY = "Instead of making a wound roll for this weapon, roll 2D6. If the result is equal to or greater than the target’s Toughness characteristic, the attack successfully wounds."
        self.TYPE = "Heavy"


class Snaggaklaw(shooting)(Weapon):
    def __init__(self):
        super().__init__()
        self.RANGE = 8
        self.ABILITY = "You can re-roll wound rolls for attacks made with this weapon."
        self.TYPE = "Assault"


class Snazzgun(Weapon):
    def __init__(self):
        super().__init__()
        self.RANGE = 24
        self.A = 3
        self.S = 6
        self.AP = -2
        self.D = 2
        self.TYPE = "Heavy"


class Squigbomb(Weapon):
    def __init__(self):
        super().__init__()
        self.RANGE = 18
        self.S = 8
        self.AP = -2
        self.D = D6
        self.ABILITY = "This weapon cannot target units that can FLY. After making an attack with this weapon, the bearer is slain."
        self.TYPE = "Assault"


class -Bilesquig(Weapon):
    def __init__(self):
        super().__init__()
        self.RANGE = 36
        self.A = D6
        self.S = *
        self.ABILITY = "This weapon always wounds on a 4+ unless it is targeting a VEHICLE or TITANIC unit, in which case it wounds on a 6+."
        self.TYPE = "Assault"


class -Biteysquig(Weapon):
    def __init__(self):
        super().__init__()
        self.RANGE = 36
        self.S = 5
        self.AP = 3
        self.D = 2
        self.TYPE = "Assault"


class -Boomsquig(Weapon):
    def __init__(self):
        super().__init__()
        self.RANGE = 36
        self.A = D3
        self.S = 6
        self.AP = -1
        self.D = D3
        self.TYPE = "Assault"


class Stikkbomb(Weapon):
    def __init__(self):
        super().__init__()
        self.RANGE = 6
        self.A = D6
        self.S = 3
        self.TYPE = "Grenade"


class Stikkbombchukka(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 5
        self.A = D6
        self.S = 3
        self.ABILITY = "This weapon can only be fired if a unit is embarked within the vehicle equipped with it."
        self.TYPE = "Assault"


class Stikkbombflinga(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 4
        self.A = 2D6
        self.S = 3
        self.TYPE = "Assault"


class Stikksquig(Weapon):
    def __init__(self):
        super().__init__()
        self.RANGE = 6
        self.A = D6
        self.S = 3
        self.TYPE = "Grenade"


class Supa-shoota(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 10
        self.RANGE = 36
        self.A = 3
        self.S = 6
        self.AP = -1
        self.TYPE = "Assault"


class Supa-gatler(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 28
        self.RANGE = 48
        self.A = 3D6
        self.S = 7
        self.AP = -2
        self.ABILITY = "See Stompa datasheet (pg 117)"
        self.TYPE = "Heavy"


class Supa-rokkit(Weapon):
    def __init__(self):
        super().__init__()
        self.RANGE = 100
        self.A = D6
        self.S = 8
        self.AP = -3
        self.D = D6
        self.ABILITY = "Only one supa-rokkit can be fired by the bearer per turn, and each can only be fired once per battle."
        self.TYPE = "Heavy"


class Tankbustabomb(Weapon):
    def __init__(self):
        super().__init__()
        self.RANGE = 6
        self.A = D3
        self.S = 8
        self.AP = -2
        self.D = D6
        self.TYPE = "Grenade"


class Tellyportblasta(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 11
        self.A = 3
        self.S = 8
        self.AP = -2
        self.ABILITY = "If a model suffers any unsaved wounds from this weapon and is not slain, roll a D6 at the end of the phase. If the result is greater than that model’s Wounds"
        self.TYPE = "Assault"


class Tellyportmega-blasta(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 18
        self.RANGE = 24
        self.A = 3
        self.S = 8
        self.AP = -2
        self.D = D3
        self.ABILITY = "characteristic, it is slain."
        self.TYPE = "Assault"


class Traktorkannon(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 30
        self.RANGE = 48
        self.S = 8
        self.AP = -2
        self.D = D
        self.ABILITY = "D6"
        self.TYPE = "Heavy"


class Twinbigshoota(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 10
        self.RANGE = 36
        self.A = 6
        self.S = 5
        self.TYPE = "Assault"


class Twinboomstikk(Weapon):
    def __init__(self):
        super().__init__()
        self.A = 2
        self.S = 5
        self.ABILITY = "If the target is within half range, add 1 to hit rolls for this weapon."
        self.TYPE = "Assault"


class Wazbommega-kannon(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 12
        self.RANGE = 36
        self.A = D3
        self.S = 8
        self.AP = -3
        self.D = D6
        self.ABILITY = "If you roll one or more unmodified hit rolls of 1 for this weapon, the bearer suffers 1 mortal wound after all of this weapon’s attacks have been resolved."
        self.TYPE = "Heavy"


class Wingmissiles(Weapon):
    def __init__(self):
        super().__init__()
        self.RANGE = 24
        self.S = 8
        self.AP = -2
        self.D = 3
        self.ABILITY = "Add 1 to hit rolls for attacks made with this weapon against VEHICLE units."
        self.TYPE = "Assault"


class Subtract(Weapon):
    def __init__(self):
        super().__init__()
        self.RANGE = 1
        self.A = hit
        self.S = rolls
        self.AP = for
        self.D = attacks
        self.ABILITY = "made with this weapon against all other targets."
        self.TYPE = "from"


class Zzapgun(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 18
        self.RANGE = 36
        self.S = 2D6
        self.AP = -3
        self.D = 3
        self.ABILITY = "Before firing this weapon, roll to determine the Strength of the shot. If the result is 11+ do not make a wound roll – instead, if the attack hits it causes 3 mortal wounds. The bearer then suffers 1 mortal wound."
        self.TYPE = "Heavy"


class Attacksquig(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.S 4=
        self.AP = -1
        self.ABILITY = "Each time a model with an attack squig fights, it can make 2 additional attacks with this weapon."
        self.TYPE = "Melee"


class Bigchoppa(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.POINTS = 5
        self.S += 2
        self.AP = -1
        self.D = 2
        self.TYPE = "Melee"


class Burna(melee)(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.S = User
        self.AP = -2
        self.TYPE = "Melee"


class Buzzsaw(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.S += 2
        self.AP = -2
        self.D = 2
        self.ABILITY = "Each time the bearer fights, it can make 1 additional attack with this weapon."
        self.TYPE = "Melee"


class Choppa(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.S = User
        self.ABILITY = "Each time the bearer fights, it can make 1 additional attack with this weapon."
        self.TYPE = "Melee"


class DaVulcha’sKlaws(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.S += 2
        self.AP = -3
        self.D = D3
        self.ABILITY = "Each time the bearer fights, it can make no more than 3 attacks with this weapon."
        self.TYPE = "Melee"


class Deffrolla(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.POINTS = 19
        self.S += 1
        self.AP = -2
        self.D = 2
        self.ABILITY = "Add 3 to hit rolls for attacks made with this weapon."
        self.TYPE = "Melee"


class Dreadklaw(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.POINTS = 15
        self.S x= 2
        self.AP = -3
        self.D = 3
        self.ABILITY = "Each time the bearer fights, it can make 1 additional attack with each dread klaw it is equipped with."
        self.TYPE = "Melee"


class Dreadsaw(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.POINTS = 10
        self.S += 4
        self.AP = -2
        self.D = 2
        self.ABILITY = "Each time the bearer fights, it can make 1 additional attack with each dread saw it is equipped with."
        self.TYPE = "Melee"


class Drilla(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.S += 1
        self.AP = -4
        self.D = 2
        self.ABILITY = "Each time you roll an unmodified wound roll of 6 for an attack with this weapon, the target suffers 1 mortal wound in addition to any other damage."
        self.TYPE = "Melee"


class Grabbastikk(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.S += 1
        self.ABILITY = "Each time the bearer fights, it can make 1 additional attack with this weapon."
        self.TYPE = "Melee"


class Grabbin’klaw(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.POINTS = 5
        self.S = User
        self.AP = -3
        self.D = D3
        self.ABILITY = "Each time the bearer fights, it can only make a single attack with this weapon."
        self.TYPE = "Melee"


class Grot-prod(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.S += 2
        self.AP = -1
        self.TYPE = "Melee"


class Kanklaw(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.S += 3
        self.AP = -3
        self.D = 3
        self.TYPE = "Melee"


class Killsaw(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.S x= 2
        self.AP = -4
        self.D = 2
        self.ABILITY = "When attacking with this weapon, you must subtract 1 from the hit roll. If a model is armed with two killsaws, add 1 to its Attacks characteristic."
        self.TYPE = "Melee"


class -Crush(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.S x= 2
        self.AP = -4
        self.D = D6
        self.TYPE = "Melee"


class -Smash(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.S = User
        self.AP = -2
        self.D = 2
        self.ABILITY = "Make 3 hit rolls for each attack made with this weapon."
        self.TYPE = "Melee"


class Kustomklaw(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.S x= 2
        self.AP = -3
        self.D = 3
        self.TYPE = "Melee"


class -Smash(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.S x= 2
        self.AP = -5
        self.D = 6
        self.TYPE = "Melee"


class -Slash(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.S = User
        self.AP = -2
        self.D = D3
        self.ABILITY = "Make 3 hit rolls for each attack made with this weapon."
        self.TYPE = "Melee"


class Mork’sTeeth(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.S = User
        self.AP = -1
        self.D = 2
        self.TYPE = "Melee"


class Nosedrill(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.S += 2
        self.AP = -2
        self.D = D3
        self.TYPE = "Melee"


class Powerklaw(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.POINTS = 13
        self.S x= 2
        self.AP = -3
        self.D = D3
        self.ABILITY = "When attacking with this weapon, you must subtract 1 from the hit roll."
        self.TYPE = "Melee"


class Powerstabba(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.POINTS = 3
        self.S = User
        self.AP = -2
        self.TYPE = "Melee"


class Sawblades(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.S += 1
        self.AP = -1
        self.TYPE = "Melee"


class Snaggaklaw(melee)(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.S += 2
        self.AP = -2
        self.D = D3
        self.ABILITY = "You can re-roll wound rolls for attacks made with this weapon."
        self.TYPE = "Melee"


class Spinnin’blades(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.S += 1
        self.ABILITY = "Make D3 hit rolls for each attack made with this weapon."
        self.TYPE = "Melee"


class Tankhammer(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.POINTS = 10
        self.S -=
        self.AP = -
        self.D = -
        self.ABILITY = "Each time the bearer fights, it can only make a single attack with this weapon. If the attack hits, the target suffers D3 mortal wounds and the bearer is slain."
        self.TYPE = "Melee"


class Urtysyringe(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.S = User
        self.ABILITY = "Each time the bearer fights, it can make 1 additional attack with this weapon. This weapon always wounds on a 4+ unless it is targeting a VEHICLE or TITANIC unit, in which case it wounds on a 6+."
        self.TYPE = "Melee"


class Waaagh!banner(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.S += 2
        self.D = 2
        self.TYPE = "Melee"


class Weirdboystaff(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.S += 2
        self.AP = -1
        self.D = D3
        self.TYPE = "Melee"


class Wreckin’ball(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.POINTS = 3
        self.S += 2
        self.AP = -1
        self.D = 2
        self.ABILITY = "Each time the bearer fights, it can make no more than 3 attacks with this weapon."
        self.TYPE = "Melee"

