from Objects.Factions.Imperium.Common.Weapons import Weapon, Melee, DiceAttackGun, DiceDamageGun, Combi, Flamer_, Plasma, Melta


class WeaponList:
    RangedWeapons = ['BoltPistol', 'Boltgun', 'CombiFlamer', 'CombiMelta', 'CombiPlasma', 'CondemnorBoltgun']
    SpecialWeapons = ['Flamer', 'MeltaGun', 'StormBolter']
    Pistols = ['BoltPistol', 'HandFlamer', 'PlasmaPistol', 'InfernoPistol']
    MeleeWeapons = ['ChainSword', 'PowerMaul', 'PowerSword']
    HeavyWeapons = ['HeavyBolter', 'HeavyFlamer', 'MultiMelta']


# Weapons of the faith
class ArcoFlails(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.S += 1
        self.AP = -1
        self.ABILITY = 'Make D3 hit rolls for each attack made with this weapon, instead of 1.'


class TheArdentBlade(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.S += 4
        self.AP = -3
        self.D = 2


class BlessedBlade(Melee, DiceDamageGun):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.Points = 9
        self.S += 2
        self.AP = -3
        self.D = 'D3'


class ChainSword(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.ABILITY = 'When the bearer fights, it makes 1 additional attack with this weapon.'


class ChirurgeonStools(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.AP = -1


class DeathCultPowerBlades(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.AP = -3


class Dialogusstaff(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.S += 1


class TheMartyrSword(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.S += 3
        self.AP = -3
        self.D = 2
        self.ABILITY = 'When the bearer fights, no more than 4 attacks can be made with this weapon.'


class TheMaceOfCastigation(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.S += 2
        self.AP = -1
        self.D = 2


class NeuralWhips(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.AP = -2
        self.ABILITY = '''When resolving an attack made with this weapon against a unit (other than a Vehicle unit) in
        which no model has a Leadership characteristic higher than 7, add 1 to the wound roll.'''


class PenitentBuzzBlade(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.S += 3
        self.AP = -3
        self.D = 2
        self.ABILITY = '''If the bearer is equipped with two of this weapon, then when the bearer fights, 
        it makes 1 additional attack using this profile.'''


class PenitentEviscerator(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.S += 2
        self.AP = -3
        self.D = 2
        self.ABILITY = 'When resolving an attack made with this weapon, subtract 1 from the hit roll.'


class PenitentFlail(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.S += 1
        self.AP = -2
        self.ABILITY = '''Make 3 hit rolls for each attack made with this weapon, instead of 1. 
        If the bearer is equipped with two of this weapon, then when the bearer fights, 
        it makes 1 additional attack using this profile.'''


class PowerMaul(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.Points = 4
        self.S += 2
        self.AP = -1


class PowerSword(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.Points = 4
        self.AP = -3


class RelicWeapons(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.S += 2
        self.AP = -1


class TheArdentBladeShoot(Flamer_, DiceAttackGun):
    def __init__(self):
        super().__init__()
        self.Range = 8
        self.A = 'D6'
        self.S = 5
        self.AP = -1
        self.TYPE = 'Assault'


class AutoGun(Weapon):
    def __init__(self):
        super().__init__()
        self.Range = 24
        self.S = 3
        self.TYPE = 'Rapid'


class BoltPistol(Weapon):
    def __init__(self):
        super().__init__()
        self.TYPE = 'Pistol'


class Boltgun(Weapon):
    def __init__(self):
        super().__init__()
        self.Range = 24
        self.TYPE = 'Rapid'


class CombiFlamer(Combi):
    def __init__(self):
        super().__init__(Boltgun(), Flamer())
        self.Points = 8


class CombiMelta(Combi):
    def __init__(self):
        super().__init__(Boltgun(), MeltaGun())
        self.Points = 15


class CombiPlasma(Combi):
    def __init__(self):
        super().__init__(Boltgun(), PlasmaGun())
        self.Points = 11


class CondemnorBoltgun(Weapon):
    def __init__(self):
        super().__init__()
        self.Points = 1
        self.Range = 24
        self.ABILITY = '''When resolving an attack made with this weapon against a PSYKER unit, 
        this weapon has a Damage characteristic of D3 for that attack.'''
        self.TYPE = 'Rapid'


class ExorcistConflagrationRockets(DiceAttackGun):
    def __init__(self):
        super().__init__()
        self.Points = 40
        self.Range = 48
        self.A = '3D6'
        self.S = 5
        self.AP = -2
        self.TYPE = 'Heavy'
        self.set_attack_dices(dices=3, die_type=6)


class ExorcistMissileLauncher(DiceAttackGun, DiceDamageGun):
    def __init__(self):
        super().__init__()
        self.Points = 70
        self.Range = 48
        self.A = '3D3'
        self.S = 8
        self.AP = -3
        self.D = 'D6'
        self.TYPE = 'Heavy'
        self.set_attack_dices(dices=3, die_type=3)


class Flamer(Flamer_, DiceAttackGun):
    def __init__(self):
        super().__init__()
        self.Points = 6
        self.Range = 8
        self.A = 'D6'
        self.TYPE = 'Assault'


class FragGrenade(DiceAttackGun):
    def __init__(self):
        super().__init__()
        self.TYPE = 'grenade'
        self.Range = 6
        self.S = 3
        self.A = 'D6'


class HandFlamer(Flamer_, DiceAttackGun):
    def __init__(self):
        super().__init__()
        self.Points = 1
        self.Range = 6
        self.A = 'D6'
        self.S = 3
        self.TYPE = 'Pistol'


class HeavyBolter(Weapon):
    def __init__(self):
        super().__init__()
        self.Points = 10
        self.Range = 36
        self.A = 3
        self.S = 5
        self.AP = -1
        self.TYPE = "Heavy"


class HeavyFlamer(Flamer_, DiceAttackGun):
    def __init__(self):
        super().__init__()
        self.Points = 14
        self.Range = 8
        self.A = 'D6'
        self.S = 5
        self.AP = -1
        self.TYPE = "Heavy"


class HunterKillerMissile(DiceDamageGun):
    def __init__(self):
        super().__init__()
        self.Points = 6
        self.Range = 48
        self.S = 8
        self.AP = -2
        self.D = 'D6'
        self.ABILITY = "The bearer can only shoot with this weapon once per battle."
        self.TYPE = "Heavy"


class ImmolationFlamers(Flamer_, DiceAttackGun):
    def __init__(self):
        super().__init__()
        self.Points = 30
        self.A = '2D6'
        self.S = 5
        self.AP = -1
        self.TYPE = "Assault"


class InfernoPistol(Melta):
    def __init__(self):
        super().__init__()
        self.Points = 7
        self.Range = 6
        self.S = 8
        self.AP = -4
        self.D = 'D6'
        self.TYPE = "Pistol"


class KrakGrenades(DiceDamageGun):
    def __init__(self):
        super().__init__()
        self.Range = 6
        self.S = 6
        self.AP = -1
        self.D = 'D3'
        self.TYPE = "Grenade"
        self.set_damage_dices(dices=1, die_type=3)


class LasPistol(Weapon):
    def __init__(self):
        super().__init__()
        self.S = 3
        self.TYPE = "Pistol"


class MeltaGun(Melta, DiceDamageGun):
    def __init__(self):
        super().__init__()
        self.Points = 14
        self.S = 8
        self.AP = -4
        self.D = 'D6'
        self.TYPE = "Assault"


class MultiMelta(Melta, DiceDamageGun):
    def __init__(self):
        super().__init__()
        self.Points = 22
        self.Range = 24
        self.S = 8
        self.AP = -4
        self.D = 'D6'
        self.TYPE = "Heavy"


class PlasmaGun(Plasma):
    def __init__(self):
        super().__init__(ability_type=1)
        self.Points = 13
        self.Range = 24
        self.S = 7
        self.AP = -3
        self.TYPE = 'RapidFire'


class PlasmaPistol(Plasma):
    def __init__(self):
        super().__init__()
        self.S = 7
        self.AP = -3
        self.TYPE = "Pistol"


class Shotgun(Weapon):
    def __init__(self):
        super().__init__()
        self.A = 2
        self.S = 3
        self.ABILITY = '''When resolving an attack made with this weapon against a unit that is within half range, 
        this weapon has a Strength characteristic of 4 for that attack.'''
        self.TYPE = "Assault"


class StormBolter(Weapon):
    def __init__(self):
        super().__init__()
        self.Points = 2
        self.Range = 24
        self.A = 2
        self.TYPE = "Rapid"


class TwinHeavyBolter(Weapon):
    def __init__(self):
        super().__init__()
        self.Points = 17
        self.Range = 36
        self.A = 6
        self.S = 5
        self.AP = -1
        self.TYPE = "Heavy"


class TwinMultiMelta(Melta, DiceDamageGun):
    def __init__(self):
        super().__init__()
        self.Points = 40
        self.Range = 24
        self.A = 2
        self.S = 8
        self.AP = -4
        self.D = 'D6'
        self.TYPE = "Heavy"
