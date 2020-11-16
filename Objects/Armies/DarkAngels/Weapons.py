from ...Common.Weapons import Weapon, Melee, DiceAttackGun, DiceDamageGun


class Gauntlet(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.S *= 2
        self.ABILITY = 'When attacking -1 to hit'


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


class Shock(Weapon):
    def __init__(self):
        super().__init__()
        self.ABILITY = 'If Infantry hit by this, cannot do overwatch and -1 to hit until end of turn'
        self.S = 0
        self.AP = 0
        self.D = 0

    def damage(self):
        pass


class Shotgun(Weapon):
    def __init__(self):
        super().__init__()
        self.ABILITY = '+1 S if target < 6"'


class _Flamer(Weapon):
    def __init__(self):
        super().__init__()
        self.ABILITY = 'autohit'


class Melta(Weapon):
    def __init__(self):
        super().__init__()
        self.ABILITY = 'If target < half range, roll two dice to wound and stay with the best'


class Grav(Weapon):
    def __init__(self):
        super().__init__()
        self.ABILITY = 'if target 3+ save or better, D = D3'


class Icarus(Weapon):
    def __init__(self):
        super().__init__()
        self.ABILITY = '+1 to hit flying enemies, -1 to the rest'


class Whirlwind(Weapon):
    def __init__(self):
        super().__init__()
        self.ABILITY = 'Can shoot units that are not visible to the model'


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


class CycloneFragMissile(DiceAttackGun):
    def __init__(self):
        super().__init__()
        self.RANGE = 36
        self.A = '2D3'
        self.set_attack_dices(dices=2, die_type=3)
        self.TYPE = 'heavy'


class CycloneKrakMissile(DiceDamageGun):
    def __init__(self):
        super().__init__()
        self.RANGE = 36
        self.A = 2
        self.S = 8
        self.AP = -2
        self.D = 'D6'
        self.TYPE = 'heavy'


class TyphoonFragMissile(DiceAttackGun):
    def __init__(self):
        super().__init__()
        self.RANGE = 48
        self.A = '2D6'
        self.set_attack_dices(dices=2, die_type=6)
        self.TYPE = 'heavy'


class TyphoonKrakMissile(DiceDamageGun):
    def __init__(self):
        super().__init__()
        self.RANGE = 48
        self.A = 2
        self.S = 8
        self.AP = -2
        self.D = 'D6'
        self.TYPE = 'heavy'


class FragMissile(DiceAttackGun):
    def __init__(self):
        super().__init__()
        self.RANGE = 48
        self.A = 'D6'
        self.TYPE = 'heavy'


class KrakMissile(DiceDamageGun):
    def __init__(self):
        super().__init__()
        self.RANGE = 48
        self.S = 8
        self.AP = -2
        self.D = 'D6'
        self.TYPE = 'heavy'


class FragShell(DiceAttackGun):
    def __init__(self):
        super().__init__()
        self.TYPE = 'Assault'
        self.RANGE = 24
        self.S = 3
        self.A = 'D6'


class KrakShell(DiceDamageGun):
    def __init__(self):
        super().__init__()
        self.TYPE = 'Assault'
        self.RANGE = 24
        self.A = 2
        self.S = 6
        self.AP = -1
        self.D = 'D3'
        self.set_damage_dices(dices=1, die_type=3)


# Armory of the Rock
class AbsolvorBoltPistol(Weapon):
    def __init__(self):
        super().__init__()
        self.RANGE = 16
        self.S = 5
        self.AP = -1
        self.TYPE = 'pistol'


class Assaultbolter(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 10
        self.RANGE = 18
        self.A = 3
        self.S = 5
        self.AP = -1
        self.TYPE = 'assault'


class AssaultCannon(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 22
        self.RANGE = 24
        self.A = 6
        self.S = 6
        self.AP = -1
        self.TYPE = 'Heavy'


class AssaultPlasmaIncinerator(Plasma):
    def __init__(self):
        super().__init__()
        self.POINTS = 17
        self.RANGE = 24
        self.A = 2
        self.S = 6
        self.AP = -4
        self.TYPE = 'Assault'


class AstartesGrenadeLauncher(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 11
        self.RANGE = 24
        self.TYPE = 'Assault'
        self.frag_krak = False
        self.gun = FragGrenade()

    def set_frag(self):
        self.frag_krak = False
        self.gun = FragGrenade()

    def set_krak(self):
        self.frag_krak = True
        self.gun = KrakGrenade()


class AstartesShotgun(Shotgun):
    def __init__(self):
        super().__init__()
        self.A = 2
        self.TYPE = 'Assault'


class AutoboltRifle(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 1
        self.RANGE = 24
        self.A = 2
        self.TYPE = 'Assault'


class AutoboltStormGauntlets(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 12
        self.RANGE = 18
        self.A = 6
        self.TYPE = 'Assault'


class AvengerMegabolter(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 35
        self.RANGE = 36
        self.A = 10
        self.S = 6
        self.AP = -1
        self.TYPE = 'Heavy'


class BlackSwordMissileLauncher(Weapon):
    def __init__(self):
        super().__init__()
        self.RANGE = 36
        self.S = 7
        self.AP = -3
        self.D = 2
        self.TYPE = 'Heavy'


class BoltCarbine(Weapon):
    def __init__(self):
        super().__init__()
        self.RANGE = 24
        self.A = 2
        self.TYPE = 'Assault'


class BoltPistol(Weapon):
    def __init__(self):
        super().__init__()
        self.LIST = 'pistols'
        self.TYPE = 'pistol'


class Boltgun(Weapon):
    def __init__(self):
        super().__init__()
        self.LIST = 'sergeant1'
        self.TYPE = 'rapid'
        self.RANGE = 24


class BoltRifle(Weapon):
    def __init__(self):
        super().__init__()
        self.RANGE = 30
        self.S = 4
        self.AP = -1
        self.TYPE = 'RapidFire'


class BoltsStormGauntlet(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 22
        self.A = 3
        self.TYPE = 'Pistol'


class CerberusLauncher(DiceAttackGun):
    def __init__(self):
        super().__init__()
        self.POINTS = 5
        self.RANGE = 18
        self.A = 'D6'
        self.TYPE = 'Heavy'


class CombiBolter(Combi):
    def __init__(self):
        super().__init__(Boltgun(), Boltgun())
        self.POINTS = 2
        self.selection_1 = True
        self.selection_2 = True


class CombiFlamer(Combi):
    def __init__(self):
        super(Combi).__init__(Boltgun(), Flamer())
        self.POINTS = 11


class CombiGrav(Combi):
    def __init__(self):
        super().__init__(Boltgun(), Flamer())
        self.POINTS = 17


class CombiMelta(Combi):
    def __init__(self):
        super().__init__(Boltgun(), MeltaGun())
        self.POINTS = 19


class CombiPlasma(Combi):
    def __init__(self):
        super().__init__(Boltgun(), PlasmaGun())
        self.POINTS = 15


class CycloneMissileLauncher(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 50
        self.frag_krak = False
        self.gun = CycloneFragMissile()

    def set_frag(self):
        self.frag_krak = False
        self.gun = CycloneFragMissile()

    def set_krak(self):
        self.frag_krak = True
        self.gun = CycloneKrakMissile()


class DeathWindLauncher(DiceAttackGun):
    def __init__(self):
        super().__init__()
        self.POINTS = 5
        self.A = 'D6'
        self.S = 5
        self.TYPE = 'Assault'


class TheDeliverer(Weapon):
    def __init__(self):
        super().__init__()
        self.AP = -1
        self.D = 2
        self.TYPE = 'Pistol'


class DemolisherCannon(DiceAttackGun, DiceDamageGun):
    def __init__(self):
        super().__init__()
        self.RANGE = 24
        self.A = 'D3'
        self.set_attack_dices(dices=1, die_type=3)
        self.S = 10
        self.AP = -3
        self.D = 'D6'
        self.ABILITY = 'If target is a 5+ unit squad, A = D6'
        self.TYPE = 'Heavy'


class Flamer(_Flamer, DiceAttackGun):
    def __init__(self):
        super().__init__()
        self.POINTS = 9
        self.TYPE = 'assault'
        self.RANGE = 8
        self.A = 'D6'


class FlameStormCannon(_Flamer, DiceAttackGun):
    def __init__(self):
        super().__init__()
        self.POINTS = 30
        self.RANGE = 8
        self.A = 'D6'
        self.S = 6
        self.AP = -2
        self.D = 2
        self.TYPE = 'Heavy'


class FlameStormGauntlets(_Flamer, DiceAttackGun):
    def __init__(self):
        super().__init__()
        self.RANGE = 18
        self.A = '2D6'
        self.set_attack_dices(dices=2, die_type=6)
        self.TYPE = 'Assault'


class FragGrenade(DiceAttackGun):
    def __init__(self):
        super().__init__()
        self.TYPE = 'grenade'
        self.RANGE = 6
        self.S = 3
        self.A = 'D6'


class FragStormGrenadeLauncher(DiceAttackGun):
    def __init__(self):
        super().__init__()
        self.POINTS = 4
        self.RANGE = 18
        self.A = 'D6'
        self.TYPE = 'Assault'


class GravPistol(Grav):
    def __init__(self):
        super().__init__()
        self.POINTS = 8
        self.S = 5
        self.AP = -3
        self.TYPE = 'Pistol'


class GravCannonGravAmp(Grav):
    def __init__(self):
        super().__init__()
        self.POINTS = 28
        self.RANGE = 24
        self.A = 4
        self.S = 5
        self.AP = -3
        self.TYPE = 'Heavy'


class GravGun(Grav):
    def __init__(self):
        super().__init__()
        self.POINTS = 15
        self.TYPE = 'rapid'
        self.RANGE = 18
        self.S = 5
        self.AP = -3
        self.ABILITY = 'if target 3+ save or better, D = D3'


class GrenadeHarness(DiceAttackGun):
    def __init__(self):
        super().__init__()
        self.POINTS = 8
        self.A = 'D6'
        self.AP = -1
        self.TYPE = 'Assault'


class HeavyBoltPistol(Weapon):
    def __init__(self):
        super().__init__()
        self.AP = -1
        self.TYPE = 'Pistol'


class HeavyBolter(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 10
        self.RANGE = 36
        self.A = 3
        self.S = 5
        self.AP = -1
        self.TYPE = 'Heavy'


class HeavyFlamer(_Flamer, DiceAttackGun):
    def __init__(self):
        super().__init__()
        self.POINTS = 17
        self.RANGE = 8
        self.A = 'D6'
        self.S = 5
        self.AP = -1
        self.TYPE = 'Heavy'


class HeavyOnslaughtGatlingCannon(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 36
        self.RANGE = 30
        self.S = 5
        self.AP = -1
        self.TYPE = 'Heavy'


class HeavyPlasmaCannon(Plasma, DiceAttackGun):
    def __init__(self):
        super().__init__(ability_type=1)
        self.POINTS = 17
        self.RANGE = 36
        self.A = 'D3'
        self.set_attack_dices(dices=1, die_type=3)
        self.S = 7
        self.AP = -3
        self.TYPE = 'Heavy'


class HeavyPlasmaIncinerator(Plasma):
    def __init__(self):
        super().__init__()
        self.POINTS = 17
        self.RANGE = 36
        self.S = 8
        self.AP = -4
        self.TYPE = 'Heavy'


class HunterKillerMissile(DiceDamageGun):
    def __init__(self):
        super().__init__()
        self.POINTS = 6
        self.RANGE = 48
        self.S = 8
        self.AP = -2
        self.D = 'D6'
        self.ABILITY = 'Only one shoot per battle'
        self.TYPE = 'Heavy'


class HurricaneBolter(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 10
        self.RANGE = 24
        self.A = 6
        self.TYPE = 'RapidFire'


class IcarusIronHailHeavyStubber(Icarus):
    def __init__(self):
        super().__init__()
        self.POINTS = 6
        self.RANGE = 36
        self.A = 3
        self.AP = -1
        self.TYPE = 'Heavy'


class IcarusRocketPod(Icarus, DiceAttackGun):
    def __init__(self):
        super().__init__()
        self.POINTS = 6
        self.RANGE = 24
        self.A = 'D3'
        self.set_attack_dices(dices=1, die_type=3)
        self.S = 7
        self.AP = -1
        self.TYPE = 'Heavy'


class IcarusStormCannon(Icarus):
    def __init__(self):
        super().__init__()
        self.POINTS = 17
        self.RANGE = 48
        self.A = 3
        self.S = 7
        self.AP = -1
        self.D = 2
        self.TYPE = 'Heavy'


class IronHailHeavyStubber(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 6
        self.RANGE = 36
        self.A = 3
        self.AP = -1
        self.TYPE = 'Heavy'


class KheresPatternAssault(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 25
        self.RANGE = 24
        self.A = 6
        self.S = 7
        self.AP = -1
        self.TYPE = 'Heavy'


class KrakGrenade(DiceDamageGun):
    def __init__(self):
        super().__init__()
        self.TYPE = 'grenade'
        self.RANGE = 6
        self.S = 6
        self.AP = -1
        self.D = 'D3'
        self.set_damage_dices(dices=1, die_type=3)


class KrakStormGrenade(DiceDamageGun):
    def __init__(self):
        super().__init__()
        self.POINTS = 4
        self.RANGE = 18
        self.S = 6
        self.AP = -1
        self.D = 'D3'
        self.set_damage_dices(dices=1, die_type=3)
        self.TYPE = 'Assault'


class LasTalon(DiceDamageGun):
    def __init__(self):
        super().__init__()
        self.POINTS = 40
        self.RANGE = 24
        self.A = 2
        self.S = 9
        self.AP = -3
        self.D = 'D6'
        self.TYPE = 'Heavy'


class LasCannon(DiceDamageGun):
    def __init__(self):
        super().__init__()
        self.POINTS = 25
        self.RANGE = 48
        self.S = 9
        self.AP = -3
        self.D = 'D6'
        self.TYPE = 'Heavy'


class LionsWrath(Combi):
    def __init__(self):
        super().__init__(MasterCraftedBoltgun(), PlasmaGun())


class MacroPlasmaIncinerator(Plasma, DiceAttackGun):
    def __init__(self):
        super().__init__(ability_type=1)
        self.POINTS = 31
        self.RANGE = 36
        self.A = 'D6'
        self.S = 8
        self.AP = -4
        self.D = 1
        self.TYPE = 'Heavy'


class MasterCraftedAutoBoltRifle(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 4
        self.RANGE = 24
        self.A = 2
        self.D = 2
        self.TYPE = 'Assault'


class MasterCraftedBoltgun(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 3
        self.RANGE = 24
        self.AP = -1
        self.D = 2
        self.TYPE = 'RapidFire'


class MasterCraftedStalkerBoltRifle(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 5
        self.RANGE = 36
        self.AP = -2
        self.D = 2
        self.TYPE = 'Heavy'


class MeltaBomb(DiceDamageGun):
    def __init__(self):
        super().__init__()
        self.POINTS = 5
        self.RANGE = 4
        self.S = 8
        self.AP = -4
        self.D = 'D6'
        self.ABILITY = 'If target vehicule, reroll all failed wounds'
        self.TYPE = 'Grenade'


class MeltaGun(Melta, DiceDamageGun):
    def __init__(self):
        super().__init__()
        self.POINTS = 17
        self.RANGE = 12
        self.S = 8
        self.AP = -4
        self.D = 'D6'
        self.TYPE = 'Assault'


class MissileLauncher(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 25
        self.frag_krak = False
        self.gun = FragMissile()

    def set_frag(self):
        self.frag_krak = False
        self.gun = FragMissile()

    def set_krak(self):
        self.frag_krak = True
        self.gun = KrakMissile()


class MultiMelta(Melta, DiceDamageGun):
    def __init__(self):
        super().__init__()
        self.POINTS = 27
        self.RANGE = 24
        self.S = 8
        self.AP = -4
        self.D = 'D6'
        self.TYPE = 'Heavy'


class OnslaughtGatlingCannon(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 16
        self.RANGE = 24
        self.A = 6
        self.S = 5
        self.AP = -1
        self.TYPE = 'Heavy'


class PlasmaBlaster(Plasma):
    def __init__(self):
        super().__init__(ability_type=1)
        self.POINTS = 17
        self.RANGE = 18
        self.A = 2
        self.S = 7
        self.AP = -3
        self.D = 1
        self.TYPE = 'Assault'


class PlasmaCannon(Plasma, DiceAttackGun):
    def __init__(self):
        super().__init__(ability_type=1)
        self.POINTS = 21
        self.RANGE = 36
        self.A = 'D3'
        self.set_attack_dices(dices=1, die_type=3)
        self.S = 7
        self.AP = -3
        self.TYPE = 'Heavy'


class PlasmaCutter(Plasma):
    def __init__(self):
        super().__init__()
        self.POINTS = 7
        self.RANGE = 12
        self.S = 7
        self.AP = -3
        self.TYPE = 'Assault'


class PlasmaExterminator(Plasma, DiceAttackGun):
    def __init__(self):
        super().__init__(ability_type=1)
        self.POINTS = 17
        self.RANGE = 18
        self.A = 'D3'
        self.S = 7
        self.AP = -3
        self.TYPE = 'Assault'


class PlasmaGun(Plasma):
    def __init__(self):
        super().__init__(ability_type=1)
        self.POINTS = 13
        self.RANGE = 24
        self.S = 7
        self.AP = -3
        self.TYPE = 'RapidFire'


class PlasmaIncinerator(Plasma):
    def __init__(self):
        super().__init__(ability_type=1)
        self.POINTS = 15
        self.RANGE = 30
        self.S = 7
        self.AP = -4
        self.TYPE = 'RapidFire'


class PlasmaPistol(Plasma):
    def __init__(self):
        super().__init__()
        self.POINTS = 7
        self.RANGE = 12
        self.S = 7
        self.AP = -3
        self.TYPE = 'Pistol'


class PlasmaStormBattery(Plasma, DiceAttackGun):
    def __init__(self):
        super().__init__(ability_type=2)
        self.RANGE = 36
        self.A = 'D6'
        self.S = 7
        self.AP = -3
        self.D = 2
        self.TYPE = 'Heavy'


class PlasmaTalon(Plasma):
    def __init__(self):
        super().__init__(ability_type=1)
        self.RANGE = 18
        self.A = 2
        self.S = 7
        self.AP = -3
        self.TYPE = 'Assault'


class PredatorAutoCannon(DiceAttackGun):
    def __init__(self):
        super().__init__()
        self.POINTS = 40
        self.RANGE = 48
        self.A = '2D3'
        self.set_attack_dices(dices=2, die_type=3)
        self.S = 7
        self.AP = -1
        self.D = 3
        self.TYPE = 'Heavy'


class RavenWingGrenadeLauncher(Weapon):
    def __init__(self):
        super().__init__()
        self.RANGE = 24
        self.frag_krak = False
        self.gun = FragShell()

    def set_frag(self):
        self.frag_krak = False
        self.gun = FragShell()

    def set_krak(self):
        self.frag_krak = True
        self.gun = KrakShell()


class ReaperAutoCannon(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 18
        self.RANGE = 36
        self.A = 4
        self.S = 7
        self.AP = -1
        self.TYPE = 'Heavy'


class ReductorPistol(Weapon):
    def __init__(self):
        super().__init__()
        self.RANGE = 3
        self.AP = -3
        self.D = 2
        self.TYPE = 'Pistol'


class RiftCannon(DiceAttackGun):
    def __init__(self):
        super().__init__()
        self.RANGE = 18
        self.A = 'D3'
        self.set_attack_dices(dices=1, die_type=3)
        self.S = 10
        self.AP = -3
        self.D = 3
        self.ABILITY = '(pg124)'
        self.TYPE = 'Heavy'


class ShockGrenade(Shock):
    def __init__(self):
        super().__init__()
        self.RANGE = 6
        self.A = 'D3'
        self.TYPE = 'Grenade'


class SkySpearMissileLauncher(DiceDamageGun):
    def __init__(self):
        super().__init__()
        self.RANGE = 60
        self.S = 9
        self.AP = -3
        self.D = 'D6'
        self.ABILITY = '+1 to hit FLY units and reroll failed hit rolls'
        self.TYPE = 'Heavy'


class SniperRifle(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 4
        self.RANGE = 36
        self.ABILITY = 'Can shoot a CHARACTER even if its not the closest. If roll 6 to wound, add mortal wound'
        self.TYPE = 'Heavy'


class StalkerBoltrifle(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 2
        self.RANGE = 36
        self.AP = -2
        self.TYPE = 'Heavy'


class StormBolter(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 2
        self.RANGE = 24
        self.A = 2
        self.TYPE = 'RapidFire'


class StormStrikeMissileLauncher(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 21
        self.RANGE = 72
        self.S = 8
        self.AP = -3
        self.D = 3
        self.TYPE = 'Heavy'


class TwinAssaultCannon(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 44
        self.RANGE = 24
        self.A = 12
        self.S = 6
        self.AP = -1
        self.TYPE = 'Heavy'


class TwinBoltGun(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 2
        self.RANGE = 24
        self.A = 2
        self.TYPE = 'RapidFire'


class TwinHeavyBolter(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 17
        self.RANGE = 36
        self.A = 6
        self.S = 5
        self.AP = -1
        self.TYPE = 'Heavy'


class TwinHeavyPlasmaCannon(Plasma, DiceAttackGun):
    def __init__(self):
        super().__init__()
        self.POINTS = 34
        self.RANGE = 36
        self.A = '2D3'
        self.set_attack_dices(dices=2, die_type=3)
        self.S = 7
        self.AP = -3
        self.TYPE = 'Heavy'


class TwinLasCannon(DiceDamageGun):
    def __init__(self):
        super().__init__()
        self.POINTS = 50
        self.RANGE = 48
        self.A = 2
        self.S = 9
        self.AP = -3
        self.D = 'D6'
        self.TYPE = 'Heavy'


class TwinMultiMelta(Melta, DiceDamageGun):
    def __init__(self):
        super().__init__()
        self.POINTS = 54
        self.RANGE = 24
        self.A = 2
        self.S = 8
        self.AP = -4
        self.D = 'D6'
        self.TYPE = 'Heavy'


class TwinStormBolter(Weapon):
    def __init__(self):
        super().__init__()
        self.RANGE = 24
        self.A = 4
        self.TYPE = 'RapidFire'


class TyphoonMissileLauncher(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 50
        self.RANGE = 48
        self.frag_krak = False
        self.gun = TyphoonFragMissile()

    def set_frag(self):
        self.frag_krak = False
        self.gun = TyphoonFragMissile()

    def set_krak(self):
        self.frag_krak = True
        self.gun = TyphoonKrakMissile()


class VolkiteCharger(Weapon):
    def __init__(self):
        super().__init__()
        self.POINTS = 6
        self.RANGE = 15
        self.A = 2
        self.S = 5
        self.D = 2
        self.TYPE = 'Heavy'


class WhirlwindCastellanLauncher(Whirlwind, DiceAttackGun):
    def __init__(self):
        super().__init__()
        self.POINTS = 25
        self.RANGE = 72
        self.A = '2D6'
        self.set_attack_dices(dices=2, die_type=6)
        self.S = 6
        self.TYPE = 'Heavy'


class WhirlwindVengeanceLauncher(Whirlwind, DiceAttackGun):
    def __init__(self):
        super().__init__()
        self.POINTS = 34
        self.RANGE = 72
        self.A = '2D3'
        self.set_attack_dices(dices=2, die_type=3)
        self.S = 7
        self.A = -1
        self.D = 2
        self.TYPE = 'Heavy'


class WristMountedGrenadeLauncher(DiceAttackGun):
    def __init__(self):
        super().__init__()
        self.POINTS = 4
        self.RANGE = 12
        self.A = 'D3'
        self.set_attack_dices(dices=1, die_type=3)
        self.AP = -1
        self.TYPE = 'Assault'


class AutoboltStormGauntletsMelee(Gauntlet, DiceDamageGun):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.AP = -3
        self.D = 'D3'
        self.set_damage_dices(dices=1, die_type=3)


class BladeOfCaliban(Melee, DiceDamageGun):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.S += 3
        self.AP = -3
        self.D = 'D3'
        self.set_damage_dices(dices=1, die_type=3)


class BladesOfReason(Melee, DiceDamageGun):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.D = 'D6'


class BoltStormGauntlet(Gauntlet, DiceDamageGun):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.POINTS = 22
        self.AP = -3
        self.D = 'D3'
        self.set_damage_dices(dices=1, die_type=3)


class ChainFist(Gauntlet):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.POINTS = 22
        self.AP = -4
        self.D = 2


class ChainSword(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.ABILITY = 'The bearer can make 1 additional attack with this weapon'


class CloseCombatWeapon(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)


class CombatKnife(ChainSword):
    pass


class CorvusHammer(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.S += 1
        self.AP = -1
        self.ABILITY = 'Each 6 roll for wound causes D3 damage'


class CroziusArcanum(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.S += 1
        self.AP = -1
        self.D = 2


class DreadnoughtCombatWeapon(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.POINTS = 40
        self.S *= 2
        self.AP = -3
        self.D = 3


class Eviscerator(Gauntlet, DiceDamageGun):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.POINTS = 22
        self.AP = -4
        self.D = 'D3'
        self.set_damage_dices(dices=1, die_type=3)


class FlailOfTheUnforgiven(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.S += 2
        self.AP = -3
        self.D = 2
        self.ABILITY = 'The damage is relocated to the target unit. It is not lost'


class FlameStormGauntletsMelee(Gauntlet, DiceDamageGun):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.POINTS = 18
        self.AP = -3
        self.D = 'D3'
        self.set_damage_dices(dices=1, die_type=3)


class ForceAxe(Melee, DiceDamageGun):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.POINTS = 10
        self.S += 1
        self.AP = -2
        self.D = 'D3'
        self.set_damage_dices(dices=1, die_type=3)


class ForceStave(Melee, DiceDamageGun):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.POINTS = 8
        self.S += 2
        self.AP = -1
        self.D = 'D3'
        self.set_damage_dices(dices=1, die_type=3)


class ForceSword(Melee, DiceDamageGun):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.POINTS = 8
        self.AP = -3
        self.D = 'D3'
        self.set_damage_dices(dices=1, die_type=3)


class HalberdOfCaliban(Melee, DiceDamageGun):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.S += 3
        self.AP = -4
        self.D = 'D3'
        self.set_damage_dices(dices=1, die_type=3)
        self.ABILITY = 'D3 additional attacks if the target unit >5 models'


class LightningClaw(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.POINTS = 8
        self.AP = -2
        self.ABILITY = 'Reroll failed wound rolls. If a model is armed with two, +1 attack and 12 points for both'


class MaceOfAbsolution(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.S += 2
        self.AP = -2
        self.D = 3


class MasterCraftedPowerSword(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.POINTS = 10
        self.AP = -3
        self.D = 2


class PowerAxe(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.POINTS = 5
        self.S += 1
        self.AP = -2


class PowerFist(Gauntlet, DiceDamageGun):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.POINTS = 12
        self.AP = -3
        self.D = 'D3'
        self.set_damage_dices(dices=1, die_type=3)


class PowerMaul(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.POINTS = 4
        self.S += 2
        self.AP = -1


class PowerSword(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.POINTS = 4
        self.AP = -3


class RavenSword(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.S += 1
        self.AP = -3
        self.D = 2
        self.ABILITY = 'S = x2 if Sammael charged in the preceding charge phase'


class RedemptorFist(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.S *= 2
        self.AP = -3
        self.D = 'D6'


class RelicBlade(Melee, DiceDamageGun):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.POINTS = 21
        self.S += 2
        self.AP = -3
        self.D = 'D3'
        self.set_damage_dices(dices=1, die_type=3)


class ServoArm(Gauntlet):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.POINTS = 12
        self.AP = -2
        self.D = 3
        self.ABILITY += 'You only can once with this weapon each time the model fights'


class SwordOfSecrets(Melee, DiceDamageGun):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.S = +2
        self.AP = -3
        self.D = 'D3'
        self.set_damage_dices(dices=1, die_type=3)
        self.ABILITY = 'Wound roll of six gives an additional mortal wound'


class SwordOfSilence(Melee):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.S += 1
        self.AP = -3
        self.D = 2
        self.ABILITY = 'Always wounds on 2+ unless the target is a vehicle'


class ThunderHammer(Gauntlet):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.POINTS = 16
        self.AP = -3
        self.D = 3
        self.ABILITY += 'If he bearer is a character, points = 21'


class TraitorsBane(Melee, DiceDamageGun):
    def __init__(self, A=1, S=4):
        super().__init__(A=A, S=S)
        self.S += 1
        self.AP = -3
        self.D = 'D3'
        self.set_damage_dices(dices=1, die_type=3)
        self.ABILITY = 'D += 1 if target is a psyker'
