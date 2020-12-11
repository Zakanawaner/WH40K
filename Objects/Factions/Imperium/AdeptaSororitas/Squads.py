from . import Units, Weapons, Abilities
from Objects.Generic.Models import Unit
from Messages import Messages


class Squad(Unit):
    def __init__(self, Power, MaxUnits, AddedPower, UnitsForIncrement=None):  # TODO terminar la puntuación de poder
        super().__init__(Power, MaxUnits, AddedPower, UnitsForIncrement)
        self.FactionKeywords = ['IMPERIUM', 'ADEPTUS MINISTORUM', 'ADEPTA SORORITAS']


class Canoness(Squad):
    def __init__(self, order):
        super().__init__(Power=3, MaxUnits=1, AddedPower=[0])
        self.FactionKeywords.append(order)
        self.Keywords = ["CHARACTER", "INFANTRY", "CANONESS"]
        self.Abilities = [Abilities.ActsOfFaith,
                          Abilities.SacredRites,
                          Abilities.ShieldOfFaith,
                          Abilities.Rosarius,
                          Abilities.BrazierOfHolyFire,
                          Abilities.LeadTheRighteous,
                          Abilities.RodOfOffice,
                          Abilities.NullRod]
        self.Units.append(Units.Canoness())
        self.HasRodOfOffice = False
        self.HasNullRod = False
        self.HasBrazierOfHolyFire = False
        self.SquadType = 'HQ'
        self.calculate_points()
        self.WargeatOptions = []
        self.WargeatOptions.append('''This model can be equipped with 1 boltgun and 1 power sword instead of 1 bolt 
        pistol and 1 chainsword. If thismodel is equipped with 1 boltgun and 1 power sword, it additionally has a 
        rod of office.''')
        self.WargeatOptions.append('''This model can be equipped with one of the following instead of 1 bolt pistol: 
        1 condemnor boltgun; 1 weaponfrom the Pistols list.''')
        self.WargeatOptions.append('''This model can be equipped with one of the following instead of 1 chainsword: 
        1 power sword; 1 blessed blade.''')
        self.WargeatOptions.append('''If this model is equipped with 1 chainsword, it can have a brazier of holy fire 
        or a null rod.''')

    def replace_pistol_and_sword(self):
        self.Units[0].replace_gun_1(Weapons.Boltgun())
        self.Units[0].replace_gun_2(Weapons.PowerSword(A=self.Units[0].A, S=self.Units[0].S))
        self.HasRodOfOffice = True
        self.Units[0].Points += 5
        self.calculate_points()

    def replace_bolt_pistol(self, weapon=None):
        if weapon.__class__.__name__ == 'CondemnorBoltgun' or weapon.__class__.__name__ in Weapons.WeaponList.Pistols:
            self.Units[0].replace_gun_1(weapon)
            self.calculate_points()
        else:
            print(Messages.IllegalWeapon)

    def replace_chain_sword(self, weapon=None):
        if weapon.__class__.__name__ == 'PowerSword' or weapon.__class__.__name__ == 'BlessedBlade':
            self.Units[0].replace_gun_2(weapon)
            self.calculate_points()
        else:
            print(Messages.IllegalWeapon)

    def select_null_rod(self):
        if self.Units[0].Gun[1].__class__.__name__ == 'ChainSword':
            self.HasNullRod = True
            self.Units[0].Points += 12
            self.calculate_points()
        else:
            print(Messages.IllegalWeapon)

    def select_brazier_of_holy_fire(self):
        if self.Units[0].Gun[1].__class__.__name__ == 'ChainSword':
            self.HasBrazierOfHolyFire = True
            self.Units[0].Points += 8
            self.calculate_points()
        else:
            print(Messages.IllegalWeapon)

        # This model can be equipped with 1 boltgun and 1 power sword instead of 1 bolt pistol and 1 chainsword. If thismodel is equipped with 1 boltgun and 1 power sword, it additionally has a rod of office.
        # This model can be equipped with one of the following instead of 1 bolt pistol: 1 condemnor boltgun; 1 weaponfrom the Pistols list.
        # This model can be equipped with one of the following instead of 1 chainsword: 1 power sword; 1 blessed blade.
        # If this model is equipped with 1 chainsword, it can have a brazier of holy fire or a null rod.


class Celestine(Squad):
    def __init__(self):
        super().__init__(Power=8, MaxUnits=1, AddedPower=[0])
        self.Keywords = ["CHARACTER", "INFANTRY", "JUMP PACK", "FLY", "CELESTINE"]
        self.Abilities = [Abilities.ActsOfFaith,
                          Abilities.SacredRites,
                          Abilities.ShieldOfFaith,
                          Abilities.HealingTears,
                          Abilities.TheArmourOfSaintKatherine,
                          Abilities.SaintlyBlessings,
                          Abilities.MiraculousIntervention]
        self.Units.append(Units.Celestine())
        self.SquadType = 'HQ'
        self.calculate_points()
        self.WargeatOptions = []


class TriumphOfSaintKatherine(Squad):
    def __init__(self):
        super().__init__(Power=9, MaxUnits=1, AddedPower=[0])
        self.Keywords = ["CHARACTER", "INFANTRY", "TRIUMPH OF SAINT KATHERINE"]
        self.Abilities = [Abilities.ActsOfFaith,
                          Abilities.SacredRites,
                          Abilities.ShieldOfFaith,
                          Abilities.PraesidiumProtectiva,
                          Abilities.TheFieryHeart,
                          Abilities.SolemnProcession,
                          Abilities.RelicsOfTheMatriarchs]
        self.Units.append(Units.TriumphOfSaintKatherine())
        self.SquadType = 'HQ'
        self.calculate_points()
        self.WargeatOptions = []


class JunithEruita(Squad):
    def __init__(self):
        super().__init__(Power=6, MaxUnits=1, AddedPower=[0])
        self.FactionKeywords.append('ORDER OF OUR MARTYRED LADY')
        self.Keywords = ["CHARATER", "VEHICLE", "FLY", "CANONESS SUPERIOR", "JUNITH ERUITA"]
        self.Abilities = [Abilities.ActsOfFaith,
                          Abilities.SacredRites,
                          Abilities.ShieldOfFaith,
                          Abilities.Rosarius,
                          Abilities.FieryConviction,
                          Abilities.ThePulpitOfSaintHollinesBasilica,
                          Abilities.Explodes]
        self.Units.append(Units.JunithEruita())
        self.SquadType = 'HQ'
        self.calculate_points()
        self.WargeatOptions = []


class Missionary(Squad):
    def __init__(self):
        super().__init__(Power=2, MaxUnits=1, AddedPower=[0])
        self.FactionKeywords.pop(2)
        self.Keywords = ["CHARACTER", "INFANTRY", "MINISTORUM PRIEST", "MISSIONARY"]
        self.Abilities = [Abilities.Zealot,
                          Abilities.Rosarius,
                          Abilities.WarHymns,
                          Abilities.LoneMission,
                          Abilities.WordOfTheEmperor]
        self.Units.append(Units.Missionary())
        self.SquadType = 'HQ'
        self.calculate_points()
        self.WargeatOptions = []
        self.WargeatOptions.append('''This model can be equipped with 1 bolt pistol and 1 shotgun instead of 1 
        autogun and 1 laspistol.''')

    def replace_autogun_and_laspistol(self):
        self.Units[0].replace_gun_1(Weapons.BoltPistol())
        self.Units[0].replace_gun_2(Weapons.Shotgun())
        self.calculate_points()

        # This model can be equipped with 1 bolt pistol and 1 shotgun instead of 1 autogun and 1 laspistol.


class BattleSistersSquad(Squad):
    def __init__(self, order):
        super().__init__(Power=4, MaxUnits=15, AddedPower=[2, 2], UnitsForIncrement=[5, 10])
        self.FactionKeywords.append(order)
        self.Keywords = ["INFANTRY", "BATTLE SISTERS SQUAD"]
        self.Abilities = [Abilities.ActsOfFaith,
                          Abilities.SacredRites,
                          Abilities.ShieldOfFaith,
                          Abilities.SimulacrumImperialis,
                          Abilities.IncensorCherub]
        self.Units.append(Units.SisterSuperior())
        self.Units.append(Units.BattleSister())
        self.Units.append(Units.BattleSister())
        self.Units.append(Units.BattleSister())
        self.Units.append(Units.BattleSister())
        self.SoldierHasSpecialWeapon = False
        self.SoldierHasHeavyWeapon = False
        self.SoldierWithSimulacrumImperialis = -1
        self.HasIncensorCherub = False
        self.SquadType = 'Troops'
        self.calculate_points()
        self.WargeatOptions = []
        self.WargeatOptions.append('''1 Battle Sister can be equipped with 1 weapon from the Special Weapons list 
        instead of 1 boltgun.''')
        self.WargeatOptions.append('''1 Battle Sister can be equipped with one of the following instead of 1 boltgun: 
        1 weapon from the Heavy Weaponslist; 1 weapon from the Special Weapons list.''')
        self.WargeatOptions.append('''1 Battle Sister equipped with 1 boltgun can have a Simulacrum Imperialis.''')
        self.WargeatOptions.append('''The Sister Superior can additionally be equipped with 1 weapon from the Melee 
        Weapons list, or can be equippedwith 1 weapon from the Melee Weapons list instead of 1 boltgun.''')
        self.WargeatOptions.append('''The Sister Superior can be equipped with 1 weapon from the Ranged Weapons list 
        instead of 1 boltgun.''')
        self.WargeatOptions.append('''The Sister Superior can be equipped with 1 weapon from the Pistols list instead 
        of 1 bolt pistol.''')
        self.WargeatOptions.append('''The unit can have an Incensor Cherub.''')

    def take_incensor_cherub(self):
        if not self.HasIncensorCherub:
            self.HasIncensorCherub = True
            self.Points += 5
        else:
            print(Messages.IllegalWeapon)

    def sergeant_take_melee_weapon(self, weapon=None):
        if weapon.__class__.__name__ in Weapons.WeaponList.MeleeWeapons:
            self.Units[0].replace_gun_5(weapon=weapon)
            self.calculate_points()
        else:
            print(Messages.IllegalWeapon)

    def sergeant_replace_boltgun_with_melee(self, weapon=None):
        if weapon.__class__.__name__ in Weapons.WeaponList.MeleeWeapons:
            self.Units[0].replace_gun_2(weapon=weapon)
            self.calculate_points()
        else:
            print(Messages.IllegalWeapon)

    def sergeant_replace_boltgun_with_ranged(self, weapon=None):
        if weapon.__class__.__name__ in Weapons.WeaponList.RangedWeapons:
            self.Units[0].replace_gun_2(weapon=weapon)
            self.calculate_points()
        else:
            print(Messages.IllegalWeapon)

    def sergeant_replace_bolt_pistol(self, weapon=None):
        if weapon.__class__.__name__ in Weapons.WeaponList.Pistols:
            self.Units[0].replace_gun_1(weapon=weapon)
            self.calculate_points()
        else:
            print(Messages.IllegalWeapon)

    def replace_boltgun_by_special(self, soldier=1, weapon=None):
        if not self.SoldierHasSpecialWeapon and weapon.__class__.__name__ in Weapons.WeaponList.SpecialWeapons:
            self.Units[soldier].replace_gun_2(weapon=weapon)
            self.SoldierHasSpecialWeapon = True
            self.calculate_points()
        else:
            print(Messages.IllegalWeapon)

    def replace_boltgun_by_heavy(self, soldier=1, weapon=None):
        if not self.SoldierHasHeavyWeapon and weapon.__class__.__name__ in Weapons.WeaponList.HeavyWeapons:
            self.Units[soldier].replace_gun_2(weapon=weapon)
            self.SoldierHasHeavyWeapon = True
            self.calculate_points()
        else:
            print(Messages.IllegalWeapon)

    def take_simulacrum_imperialis(self, soldier=1):
        if self.Units[soldier].Gun[1].__class__.__name__ == 'Boltgun':
            self.Units[soldier].HasSimulacrumImperialis = True
            self.SoldierWithSimulacrumImperialis = soldier
            self.Units[soldier].Points += 5
            self.calculate_points()
        else:
            print(Messages.IllegalWeapon)

        # 1 Battle Sister can be equipped with 1 weapon from the Special Weapons list instead of 1 boltgun.
        # 1 Battle Sister can be equipped with one of the following instead of 1 boltgun: 1 weapon from the Heavy Weaponslist; 1 weapon from the Special Weapons list.
        # 1 Battle Sister equipped with 1 boltgun can have a Simulacrum Imperialis.
        # The Sister Superior can additionally be equipped with 1 weapon from the Melee Weapons list, or can be equippedwith 1 weapon from the Melee Weapons list instead of 1 boltgun.
        # The Sister Superior can be equipped with 1 weapon from the Ranged Weapons list instead of 1 boltgun.
        # The Sister Superior can be equipped with 1 weapon from the Pistols list instead of 1 bolt pistol.
        # The unit can have an Incensor Cherub.


class Preacher(Squad):
    def __init__(self):
        super().__init__(Power=1, MaxUnits=1, AddedPower=[0])
        self.FactionKeywords.pop(2)
        self.Keywords = ["CHARACTER", "INFANTRY", "MINISTORUM PRIEST", "PREACHER"]
        self.Abilities = [Abilities.Zealot,
                          Abilities.IconOfTheEcclesiarchy,
                          Abilities.Rosarius,
                          Abilities.WarHymns]
        self.Units.append(Units.Preacher())
        self.SquadType = 'Elites'
        self.calculate_points()
        self.WargeatOptions = []


class GeminaeSuperiaSquad(Squad):
    def __init__(self):
        super().__init__(Power=1, MaxUnits=2, AddedPower=[1], UnitsForIncrement=[2])
        self.Keywords = ["CHARACTER", "INFANTRY", "JUMP PACK", "FLY", "GEMINAE SUPERIA"]
        self.Abilities = [Abilities.ActsOfFaith,
                          Abilities.SacredRites,
                          Abilities.ShieldOfFaith,
                          Abilities.DivineGuardians,
                          Abilities.LifeWards]
        self.Units.append(Units.GeminaeSuperia())
        self.SquadType = 'Elites'
        self.calculate_points()
        self.WargeatOptions = []


class RepentiaSuperior(Squad):
    def __init__(self, order):
        super().__init__(Power=2, MaxUnits=1, AddedPower=[0])
        self.FactionKeywords.append(order)
        self.Keywords = ["CHARACTER", "INFANTRY", "REPENTIA SUPERIOR"]
        self.Abilities = [Abilities.ActsOfFaith,
                          Abilities.SacredRites,
                          Abilities.ShieldOfFaith,
                          Abilities.ScourgeOfThePenitent,
                          Abilities.DrivenOnwards]
        self.Units.append(Units.RepentiaSuperior())
        self.SquadType = ''
        self.calculate_points()
        self.WargeatOptions = []
        self.WargeatOptions.append('''This model can additionally be equipped with 1 bolt pistol.''')

    def take_bolt_pistol(self):
        self.Units[0].replace_gun_4(Weapons.BoltPistol())
        self.calculate_points()

        # This model can additionally be equipped with 1 bolt pistol.


class SisterRepentiaSquad(Squad):
    def __init__(self, order):
        super().__init__(Power=2, MaxUnits=9, AddedPower=[3], UnitsForIncrement=[5])
        self.FactionKeywords.append(order)
        self.Keywords = ["INFANTRY", "SISTERS REPENTIA"]
        self.Abilities = [Abilities.ActsOfFaith,
                          Abilities.SacredRites,
                          Abilities.ShieldOfFaith,
                          Abilities.Zealot,
                          Abilities.Martyrdom,
                          Abilities.SolaceInAnguish]
        self.Units.append(Units.SisterRepentia())
        self.Units.append(Units.SisterRepentia())
        self.Units.append(Units.SisterRepentia())
        self.Units.append(Units.SisterRepentia())
        self.SquadType = 'Elites'
        self.calculate_points()
        self.WargeatOptions = []


class CelestianSquad(Squad):
    def __init__(self, order):
        super().__init__(Power=4, MaxUnits=10, AddedPower=[2], UnitsForIncrement=[6])
        self.FactionKeywords.append(order)
        self.Keywords = ["INFANTRY", "CELESTIAN SQUAD"]
        self.Abilities = [Abilities.ActsOfFaith,
                          Abilities.SacredRites,
                          Abilities.ShieldOfFaith,
                          Abilities.Bodyguard,
                          Abilities.SwornProtectors,
                          Abilities.SimulacrumImperialis,
                          Abilities.IncensorCherub]
        self.Units.append(Units.Celestian())
        self.Units.append(Units.Celestian())
        self.Units.append(Units.Celestian())
        self.Units.append(Units.Celestian())
        self.Units.append(Units.Celestian())
        self.HasSuperior = False
        self.SoldierHasSpecialWeapon = False
        self.SoldierHasHeavyWeapon = False
        self.HasSimulacrumImperialis = False
        self.HasIncensorCherub = False
        self.SquadType = 'Elites'
        self.calculate_points()
        self.WargeatOptions = []
        self.WargeatOptions.append('''1 Celestian can be equipped with 1 weapon from the Special Weapons list instead 
        of 1 boltgun.''')
        self.WargeatOptions.append('''1 Celestian can be equipped with one of the following instead of 1 boltgun: 
        1 weapon from the Heavy Weaponslist; 1 weapon from the Special Weapons list.''')
        self.WargeatOptions.append('''1 Celestian equipped with 1 boltgun can have a Simulacrum Imperialis.''')
        self.WargeatOptions.append('''The Celestian Superior can additionally be equipped with 1 weapon from the 
        Melee Weapons list, or can beequipped with 1 weapon from the Melee Weapons list instead of 1 boltgun.''')
        self.WargeatOptions.append('''The Celestian Superior can be equipped with 1 weapon from the Ranged Weapons 
        list instead of 1 boltgun.''')
        self.WargeatOptions.append('''The Celestian Superior can be equipped with 1 weapon from the Pistols list 
        instead of 1 bolt pistol.''')
        self.WargeatOptions.append('''The unit can have an Incensor Cherub.''')

    def add_superior(self):
        if not self.HasSuperior:
            self.HasSuperior = True
            self.add_soldier(Units.CelestianSuperior())

    def take_incensor_cherub(self):
        self.HasIncensorCherub = True
        self.Points += 5

    def sergeant_take_melee_weapon(self, weapon=None):
        self.Units[0].replace_gun_5(weapon=weapon)
        self.calculate_points()

    def sergeant_replace_boltgun(self, weapon=None):
        self.Units[0].replace_gun_2(weapon=weapon)
        self.calculate_points()

    def sergeant_replace_bolt_pistol(self, weapon=None):
        self.Units[0].replace_gun_1(weapon=weapon)
        self.calculate_points()

    def replace_boltgun_by_special(self, soldier=1, weapon=None):
        if not self.SoldierHasSpecialWeapon:
            self.Units[soldier].replace_gun_2(weapon=weapon)
            self.SoldierHasSpecialWeapon = True
            self.calculate_points()

    def replace_boltgun_by_heavy(self, soldier=1, weapon=None):
        if not self.SoldierHasHeavyWeapon:
            self.Units[soldier].replace_gun_2(weapon=weapon)
            self.SoldierHasHeavyWeapon = True
            self.calculate_points()

    def take_simulacrum_imperialis(self, soldier=1):
        if self.Units[soldier].Gun[1].__class__.__name__ == 'Boltgun':
            self.Units[soldier].HasSimulacrumImperialis = True
            self.HasSimulacrumImperialis = True
            self.Units[soldier].Points += 5
            self.calculate_points()

        # 1 Celestian can be equipped with 1 weapon from the Special Weapons list instead of 1 boltgun.
        # 1 Celestian can be equipped with one of the following instead of 1 boltgun: 1 weapon from the Heavy Weaponslist; 1 weapon from the Special Weapons list.
        # 1 Celestian equipped with 1 boltgun can have a Simulacrum Imperialis.
        # The Celestian Superior can additionally be equipped with 1 weapon from the Melee Weapons list, or can beequipped with 1 weapon from the Melee Weapons list instead of 1 boltgun.
        # The Celestian Superior can be equipped with 1 weapon from the Ranged Weapons list instead of 1 boltgun.
        # The Celestian Superior can be equipped with 1 weapon from the Pistols list instead of 1 bolt pistol.
        # The unit can have an Incensor Cherub.


class ZephyrimSquad(Squad):
    def __init__(self, order):
        super().__init__(Power=5, MaxUnits=10, AddedPower=4)
        self.FactionKeywords.append(order)
        self.Keywords = ["INFANTRY", "JUMP PACK", "FLY", "ZEPHYRIM SQUAD"]
        self.Abilities = [Abilities.ActsOfFaith,
                          Abilities.SacredRites,
                          Abilities.ShieldOfFaith,
                          Abilities.RapturousBlows,
                          Abilities.ZephyrimPennant,
                          Abilities.SkyStrike,
                          Abilities.AngelicVisage]
        self.Units.append(Units.ZephyrimSuperior())
        self.Units.append(Units.Zephyrim())
        self.Units.append(Units.Zephyrim())
        self.Units.append(Units.Zephyrim())
        self.Units.append(Units.Zephyrim())
        self.CanHaveZephyrimPennant = True
        self.HasZephyrimPennant = False
        self.SquadType = 'Elites'
        self.calculate_points()
        self.WargeatOptions = []
        self.WargeatOptions.append('''The Zephyrim Superior can be equipped with 1 plasma pistol instead of 1 
        bolt pistol.''')
        self.WargeatOptions.append('''If the Zephyrim Superior is equipped with 1 bolt pistol, she can have a 
        Zephyrim pennant.''')

    def sergeant_replace_bolt_pistol(self):
        self.Units[0].replace_gun_1(Weapons.PlasmaPistol())
        self.CanHaveZephyrimPennant = False
        self.calculate_points()

    def take_zephyrim_pennant(self):
        if self.CanHaveZephyrimPennant:
            self.CanHaveZephyrimPennant = False
            self.HasZephyrimPennant = True
            self.Units[0].Points += 5
            self.calculate_points()

        # The Zephyrim Superior can be equipped with 1 plasma pistol instead of 1 bolt pistol.
        # If the Zephyrim Superior is equipped with 1 bolt pistol, she can have a Zephyrim pennant.


class Dialogus(Squad):
    def __init__(self):
        super().__init__(Power=2, MaxUnits=1, AddedPower=0)
        self.Keywords = ["CHARACTER", "INFANTRY", "DIALOGUS"]
        self.Abilities = [Abilities.ActsOfFaith,
                          Abilities.SacredRites,
                          Abilities.ShieldOfFaith,
                          Abilities.LaudHailer,
                          Abilities.SpiritualFortitude,
                          Abilities.StirringRhetoric]
        self.Units.append(Units.Dialogus())
        self.SquadType = 'Elites'
        self.calculate_points()
        self.WargeatOptions = []


class Hospitaller(Squad):
    def __init__(self):
        super().__init__(Power=2, MaxUnits=1, AddedPower=0)
        self.Keywords = ["CHARACTER", "INFANTRY", "HOSPITALLER"]
        self.Abilities = [Abilities.ActsOfFaith,
                          Abilities.SacredRites,
                          Abilities.ShieldOfFaith,
                          Abilities.MedicusMinistorum]
        self.Units.append(Units.Hospitaller())
        self.SquadType = 'Elites'
        self.calculate_points()
        self.WargeatOptions = []


class Imagifier(Squad):
    def __init__(self, order):
        super().__init__(Power=2, MaxUnits=1, AddedPower=0)
        self.FactionKeywords.append(order)
        self.Keywords = ["CHARACTER", "INFANTRY", "IMAGIFIER"]
        self.Abilities = [Abilities.ActsOfFaith,
                          Abilities.SacredRites,
                          Abilities.ShieldOfFaith,
                          Abilities.LitanyOfDeeds]
        self.Units.append(Units.Imagifier())
        self.SquadType = 'Elites'
        self.calculate_points()
        self.WargeatOptions = []


class CrusaderSquad(Squad):
    def __init__(self):
        super().__init__(Power=1, MaxUnits=6, AddedPower=2)
        self.FactionKeywords.pop(2)
        self.FactionKeywords.append('ASTRA MILITARUM')
        self.Keywords = ["INFANTRY", "ECCLESIARCHY BATTLE CONCLAVE", "CRUSADERS"]
        self.Abilities = [Abilities.Zealot,
                          Abilities.EcclesiarchyBattleConclave,
                          Abilities.StormShield,
                          Abilities.SpiritualFortitude]
        self.Units.append(Units.Crusader())
        self.Units.append(Units.Crusader())
        self.SquadType = 'Elites'
        self.calculate_points()
        self.WargeatOptions = []


class DeathCultAssassinSquad(Squad):
    def __init__(self):
        super().__init__(Power=1, MaxUnits=6, AddedPower=2)
        self.FactionKeywords.pop(2)
        self.Keywords = ["INFANTRY", "ECCLESIARCHY BATTLE CONCLAVE", "DEATH CULT ASSASSINS"]
        self.Abilities = [Abilities.Zealot,
                          Abilities.UncannyReflexes,
                          Abilities.EcclesiarchyBattleConclave]
        self.Units.append(Units.DeathCultAssassin())
        self.Units.append(Units.DeathCultAssassin())
        self.SquadType = 'Elites'
        self.calculate_points()
        self.WargeatOptions = []


class ArcoFlagellantSquad(Squad):
    def __init__(self):
        super().__init__(Power=2, MaxUnits=10, AddedPower=4)
        self.FactionKeywords.pop(2)
        self.Keywords = ["INFANTRY", "ECCLESIARCHY BATTLE CONCLAVE", "ARCO-FLAGELLANTS"]
        self.Abilities = [Abilities.Zealot,
                          Abilities.BerserkKillingMachines,
                          Abilities.EcclesiarchyBattleConclave]
        self.Units.append(Units.ArcoFlagellant())
        self.Units.append(Units.ArcoFlagellant())
        self.Units.append(Units.ArcoFlagellant())
        self.HasEndurant = False
        self.SquadType = 'Elites'
        self.calculate_points()
        self.WargeatOptions = []

    def take_endurant(self):
        if not self.HasEndurant:
            self.Units[0] = Units.Endurant()
            self.HasEndurant = True


class DominionSquad(Squad):
    def __init__(self, order):
        super().__init__(Power=5, MaxUnits=10, AddedPower=2)
        self.FactionKeywords.append(order)
        self.Keywords = ["INFANTRY", " DOMINION SQUAD"]
        self.Abilities = [Abilities.ActsOfFaith,
                          Abilities.SacredRites,
                          Abilities.ShieldOfFaith,
                          Abilities.Vanguard,
                          Abilities.SimulacrumImperialis,
                          Abilities.IncensorCherub]
        self.Units.append(Units.DominionSuperior())
        self.Units.append(Units.Dominion())
        self.Units.append(Units.Dominion())
        self.Units.append(Units.Dominion())
        self.Units.append(Units.Dominion())
        self.SoldiersWithSpecialWeapon = 0
        self.SoldierWithSimulacrumImperialis = -1
        self.HasIncensorCherub = False
        self.SquadType = 'FastAttack'
        self.calculate_points()
        self.WargeatOptions = []
        self.WargeatOptions.append('''Up to 4 Dominions can be equipped with 1 weapon from the Special Weapons list 
        instead of 1 boltgun.''')
        self.WargeatOptions.append('''1 Dominion equipped with 1 boltgun can have a Simulacrum Imperialis.''')
        self.WargeatOptions.append('''The Dominion Superior can additionally be equipped with 1 weapon from the Melee 
        Weapons list, or can beequipped with 1 weapon from the Melee Weapons list instead of 1 boltgun.''')
        self.WargeatOptions.append('''The Dominion Superior can be equipped with 1 weapon from the Ranged Weapons list 
        instead of 1 boltgun.''')
        self.WargeatOptions.append('''The Dominion Superior can be equipped with 1 weapon from the Pistols list instead 
        of 1 bolt pistol.''')
        self.WargeatOptions.append('''The unit can have an Incensor Cherub.''')

    def sergeant_take_melee_weapon(self, weapon=None):
        self.Units[0].Gun[4] = weapon
        self.calculate_points()

    def sergeant_replace_boltgun_with_melee(self, weapon=None):
        self.Units[0].replace_gun_2(weapon=weapon)
        self.calculate_points()

    def sergeant_replace_boltgun_with_ranged(self, weapon=None):
        self.Units[0].replace_gun_2(weapon=weapon)
        self.calculate_points()

    def sergeant_replace_pistol(self, weapon=None):
        self.Units[0].replace_gun_1(weapon=weapon)
        self.calculate_points()

    def replace_boltgun(self, soldier, weapon=None):
        if self.SoldiersWithSpecialWeapon < 4:
            self.SoldiersWithSpecialWeapon += 1
            self.Units[soldier].replace_gun_2(weapon=weapon)
            self.calculate_points()

    def take_simulacrum_imperialis(self, soldier):
        if self.Units[soldier].Gun[1].__class__.__name__ == 'Boltgun' and self.SoldierWithSimulacrumImperialis < 0:
            self.SoldierWithSimulacrumImperialis = soldier
            self.Points += 5

    def take_incestor_cherub(self):
        if not self.HasIncensorCherub:
            self.HasIncensorCherub = True
            self.Points += 5

        # Up to 4 Dominions can be equipped with 1 weapon from the Special Weapons list instead of 1 boltgun.
        # 1 Dominion equipped with 1 boltgun can have a Simulacrum Imperialis.
        # The Dominion Superior can additionally be equipped with 1 weapon from the Melee Weapons list, or can beequipped with 1 weapon from the Melee Weapons list instead of 1 boltgun.
        # The Dominion Superior can be equipped with 1 weapon from the Ranged Weapons list instead of 1 boltgun.
        # The Dominion Superior can be equipped with 1 weapon from the Pistols list instead of 1 bolt pistol.
        # The unit can have an Incensor Cherub.


class SeraphimSquad(Squad):
    def __init__(self, order):
        super().__init__(Power=4, MaxUnits=5, AddedPower=3)
        self.FactionKeywords.append(order)
        self.Keywords = ["INFANTRY", "JUMP PACK", "FLY", "SERAPHIM SQUAD"]
        self.Abilities = [Abilities.ActsOfFaith,
                          Abilities.SacredRites,
                          Abilities.ShieldOfFaith,
                          Abilities.AngelicVisage,
                          Abilities.SkyStrike]
        self.Units.append(Units.SeraphimSuperior())
        self.Units.append(Units.Seraphim())
        self.Units.append(Units.Seraphim())
        self.Units.append(Units.Seraphim())
        self.Units.append(Units.Seraphim())
        self.SoldiersWithoutPistols = 0
        self.SquadType = 'FastAttack'
        self.calculate_points()
        self.WargeatOptions = []
        self.WargeatOptions.append('''Up to 2 Seraphim can be equipped with one of the following instead of 2 bolt 
        pistols: 2 hand flamers; 2inferno pistols.''')
        self.WargeatOptions.append('''The Seraphim Superior can be equipped with one of the following instead of 1 
        bolt pistol: 1 chainsword; 1power sword.''')
        self.WargeatOptions.append('''The Seraphim Superior can be equipped with 1 plasma pistol instead of 1 bolt 
        pistol.''')

    def sergeant_replace_pistol_by_sword(self, weapon=None):
        self.Units[0].replace_gun_1(weapon=weapon)
        self.calculate_points()

    def sergeant_replace_pistol_by_plasma_pistol(self):
        self.Units[0].replace_gun_2(weapon=Weapons.PlasmaPistol())
        self.calculate_points()

    def replace_pistols(self, soldier, weapon=None):
        if self.SoldiersWithoutPistols > 2:
            self.Units[soldier].replace_gun_1(weapon=weapon)
            self.Units[soldier].replace_gun_2(weapon=weapon)
            self.SoldiersWithoutPistols += 1
            self.calculate_points()

        # Up to 2 Seraphim can be equipped with one of the following instead of 2 bolt pistols: 2 hand flamers; 2inferno pistols.
        # The Seraphim Superior can be equipped with one of the following instead of 1 bolt pistol: 1 chainsword; 1power sword.
        # The Seraphim Superior can be equipped with 1 plasma pistol instead of 1 bolt pistol.


class ExorcistSquad(Squad):
    def __init__(self, order):
        super().__init__(Power=8, MaxUnits=0, AddedPower=0)
        self.FactionKeywords.append(order)
        self.Keywords = ["VEHICLE", "EXORCIST"]
        self.Abilities = [Abilities.ActsOfFaith,
                          Abilities.SacredRites,
                          Abilities.ShieldOfFaith,
                          Abilities.Explodes,
                          Abilities.SmokeLaunchers]
        self.Units.append(Units.Exorcist())
        self.SquadType = 'HeavySupport'
        self.calculate_points()
        self.WargeatOptions = []
        self.WargeatOptions.append('''This model can be equipped with Exorcist conflagration rockets instead of 1 
        Exorcist missile launcher.''')
        self.WargeatOptions.append('''This model can additionally be equipped with 1 hunter-killer missile.''')

    def replace_missile_launcher(self):
        self.Units[0].replace_gun_1(Weapons.ExorcistConflagrationRockets())

    def take_hunter_killer_missile(self):
        self.Units[0].replace_gun_3(Weapons.HunterKillerMissile())

        # This model can be equipped with Exorcist conflagration rockets instead of 1 Exorcist missile launcher.
        # This model can additionally be equipped with 1 hunter-killer missile.


class MortifierSquad(Squad):
    def __init__(self):
        super().__init__(Power=3, MaxUnits=5, AddedPower=3)
        self.Keywords = ["VEHICLE", "MORTIFIERS"]
        self.Abilities = [Abilities.AnguishOfTheUnredeemed,
                          Abilities.NoReprieve,
                          Abilities.BlazeOfAgony]
        self.Units.append(Units.Mortifier())
        self.HasAnchorite = False
        self.SquadType = 'HeavySupport'
        self.calculate_points()
        self.WargeatOptions = []
        self.WargeatOptions.append('''Any model can be equipped with 1 heavy flamer instead of 1 heavy bolter.''')
        self.WargeatOptions.append('''Any model can be equipped with 2 heavy flamers instead of 2 heavy bolters.''')
        self.WargeatOptions.append('''Any model can be equipped with 1 penitent buzz-blade instead of 1 penitent 
        flail.''')
        self.WargeatOptions.append('''Any model can be equipped with 2 penitent buzz-blades instead of 2 penitent 
        flails.''')

    def take_endurant(self):
        if not self.HasAnchorite:
            self.Units[0] = Units.Endurant()
            self.HasAnchorite = True
            self.calculate_points()

    def choose_heavy_flamer(self, soldier):
        self.Units[soldier].replace_gun_1(Weapons.HeavyFlamer())
        self.calculate_points()

    def choose_two_heavy_flamer(self, soldier):
        self.Units[soldier].replace_gun_1(Weapons.HeavyFlamer())
        self.Units[soldier].replace_gun_2(Weapons.HeavyFlamer())
        self.calculate_points()

    def choose_penitent_buss_blade(self, soldier):
        self.Units[soldier].replace_gun_3(Weapons.PenitentBuzzBlade(A=self.Units[soldier].A, S=self.Units[soldier].S))
        self.calculate_points()

    def choose_two_penitent_buss_blade(self, soldier):
        self.Units[soldier].replace_gun_3(Weapons.PenitentBuzzBlade(A=self.Units[soldier].A, S=self.Units[soldier].S))
        self.Units[soldier].replace_gun_4(Weapons.PenitentBuzzBlade(A=self.Units[soldier].A, S=self.Units[soldier].S))
        self.calculate_points()

        # Any model can be equipped with 1 heavy flamer instead of 1 heavy bolter.
        # Any model can be equipped with 2 heavy flamers instead of 2 heavy bolters.
        # Any model can be equipped with 1 penitent buzz-blade instead of 1 penitent flail.
        # Any model can be equipped with 2 penitent buzz-blades instead of 2 penitent flails.


class RetributorSquad(Squad):
    def __init__(self, order):
        super().__init__(Power=6, MaxUnits=10, AddedPower=2)
        self.FactionKeywords.append(order)
        self.Keywords = ["INFANTRY", "RETRIBUTOR SQUAD"]
        self.Abilities = [Abilities.ActsOfFaith,
                          Abilities.SacredRites,
                          Abilities.ShieldOfFaith,
                          Abilities.SimulacrumImperialis,
                          Abilities.FaithfulAdvance,
                          Abilities.RitesOfFire,
                          Abilities.ArmoriumCherub]
        self.Units.append(Units.RetriibutorSuperior())
        self.Units.append(Units.Retributor())
        self.Units.append(Units.Retributor())
        self.Units.append(Units.Retributor())
        self.Units.append(Units.Retributor())
        self.RetributorsWithHeavy = 0
        self.SoldierWithSimulacrumImperialis = -1
        self.HasIncensorCherub = False
        self.SquadType = 'HeavySupport'
        self.calculate_points()
        self.WargeatOptions = []
        self.WargeatOptions.append('''Up to 4 Retributors can be equipped with 1 weapon from the Heavy Weapons list 
        instead of 1 boltgun.''')
        self.WargeatOptions.append('''1 Retributor equipped with 1 boltgun can have a Simulacrum Imperialis.''')
        self.WargeatOptions.append('''The Retributor Superior can additionally be equipped with 1 weapon from the 
        Melee Weapons list, or can beequipped with 1 weapon from the Melee Weapons list instead of 1 boltgun.''')
        self.WargeatOptions.append('''The Retributor Superior can be equipped with 1 weapon from the Ranged Weapons 
        list instead of 1 boltgun.''')
        self.WargeatOptions.append('''The Retributor Superior can be equipped with 1 weapon from the Pistols list 
        instead of 1 bolt pistol.''')
        self.WargeatOptions.append('''This unit can have an Armorium Cherub, or it can have two Armorium Cherubs.''')

    def sergeant_take_melee_weapon(self, weapon=None):
        self.Units[0].Gun[4] = weapon
        self.calculate_points()

    def sergeant_replace_boltgun_with_melee(self, weapon=None):
        self.Units[0].replace_gun_2(weapon=weapon)
        self.calculate_points()

    def sergeant_replace_boltgun_with_ranged(self, weapon=None):
        self.Units[0].replace_gun_2(weapon=weapon)
        self.calculate_points()

    def sergeant_replace_pistol(self, weapon=None):
        self.Units[0].replace_gun_1(weapon=weapon)
        self.calculate_points()

    def replace_boltgun_with_heavy(self, soldier, weapon=None):
        if weapon.__class__.__name__ in Weapons.WeaponList.HeavyWeapons and self.RetributorsWithHeavy < 4:
            self.Units[soldier].replace_gun_2(weapon=weapon)
            self.RetributorsWithHeavy += 1
            self.calculate_points()

    def take_simulacrum_imperialis(self, soldier):
        if self.Units[soldier].Gun[1].__class__.__name__ == 'Boltgun' and self.SoldierWithSimulacrumImperialis < 0:
            self.SoldierWithSimulacrumImperialis = soldier
            self.Points += 5

    def take_incestor_cherub(self):
        if not self.HasIncensorCherub:
            self.HasIncensorCherub = True
            self.Points += 5

        # Up to 4 Retributors can be equipped with 1 weapon from the Heavy Weapons list instead of 1 boltgun.
        # 1 Retributor equipped with 1 boltgun can have a Simulacrum Imperialis.
        # The Retributor Superior can additionally be equipped with 1 weapon from the Melee Weapons list, or can beequipped with 1 weapon from the Melee Weapons list instead of 1 boltgun.
        # The Retributor Superior can be equipped with 1 weapon from the Ranged Weapons list instead of 1 boltgun.
        # The Retributor Superior can be equipped with 1 weapon from the Pistols list instead of 1 bolt pistol.
        # This unit can have an Armorium Cherub, or it can have two Armorium Cherubs.


class PenitentEngineSquad(Squad):
    def __init__(self):
        super().__init__(Power=3, MaxUnits=3, AddedPower=3)
        self.FactionKeywords.pop(2)
        self.Keywords = ["VEHICLE", "PENITENT ENGINES"]
        self.Abilities = [Abilities.Zealot,
                          Abilities.BerserkKillingMachines]
        self.Units.append(Units.PenitentEngine())
        self.SquadType = 'HeavySupport'
        self.calculate_points()
        self.WargeatOptions = []
        self.WargeatOptions.append('''Any model can be equipped with 1 penitent buzz-blade instead of 1 penitent 
        flail.''')
        self.WargeatOptions.append('''Any model can be equipped with 2 penitent buzz-blades instead of 2 penitent 
        flails.''')

    def choose_penitent_buzz_blade(self, soldier):
        self.Units[soldier].replace_gun_3(Weapons.PenitentBuzzBlade(A=self.Units[soldier].A, S=self.Units[soldier].S))
        self.calculate_points()

    def choose_two_penitent_buzz_blade(self, soldier):
        self.Units[soldier].replace_gun_3(Weapons.PenitentBuzzBlade(A=self.Units[soldier].A, S=self.Units[soldier].S))
        self.Units[soldier].replace_gun_4(Weapons.PenitentBuzzBlade(A=self.Units[soldier].A, S=self.Units[soldier].S))
        self.calculate_points()

        # Any model can be equipped with 1 penitent buzz-blade instead of 1 penitent flail.
        # Any model can be equipped with 2 penitent buzz-blades instead of 2 penitent flails.


class SororitasRhinoSquad(Squad):
    def __init__(self, order):
        super().__init__(Power=3, MaxUnits=1, AddedPower=0)
        self.FactionKeywords.append(order)
        self.Keywords = ["VEHICLE", "TRANSPORT", "RHINO", "SORORITAS RHINO"]
        self.Abilities = [Abilities.ActsOfFaith,
                          Abilities.SacredRites,
                          Abilities.ShieldOfFaith,
                          Abilities.SmokeLaunchers,
                          Abilities.Explodes,
                          Abilities.SelfRepair]
        self.Units.append(Units.SororitasRhino())
        self.SquadType = 'DedicatedTransport'
        self.calculate_points()
        self.WargeatOptions = []
        self.WargeatOptions.append('''This model can additionally be equipped with 1 hunter-killer missile.''')

    def take_hunter_killer_missile(self):
        self.Units[0].replace_gun_2(Weapons.HunterKillerMissile())
        self.calculate_points()

        # This model can additionally be equipped with 1 hunter-killer missile.


class ImmolatorSquad(Squad):
    def __init__(self, order):
        super().__init__(Power=5, MaxUnits=1, AddedPower=0)
        self.FactionKeywords.append(order)
        self.Keywords = ["VEHICLE", "TRANSPORT", "IMMOLATOR"]
        self.Abilities = [Abilities.ActsOfFaith,
                          Abilities.SacredRites,
                          Abilities.ShieldOfFaith,
                          Abilities.SmokeLaunchers,
                          Abilities.Explodes]
        self.Units.append(Units.Immolator())
        self.SquadType = 'DedicatedTransport'
        self.calculate_points()
        self.WargeatOptions = []
        self.WargeatOptions.append('''This model can be equipped with one of the following instead of immolation 
        flamers: 1 twin heavy bolter; 1twin multi-melta.''')
        self.WargeatOptions.append('''This model can additionally be equipped with 1 hunter-killer missile.''')

    def replace_immolation_flamers(self, weapon=None):
        if weapon.__class__.__name__ == 'TwinHeavyBolter' or weapon.__class__.__name__ == 'TwinMultiMelta':
            self.Units[0].replace_gun_1(weapon)
            self.calculate_points()

    def take_hunter_killer_missile(self):
        self.Units[0].replace_gun_3(Weapons.HunterKillerMissile())
        self.calculate_points()

        # This model can be equipped with one of the following instead of immolation flamers: 1 twin heavy bolter; 1twin multi-melta.
        # This model can additionally be equipped with 1 hunter-killer missile.
