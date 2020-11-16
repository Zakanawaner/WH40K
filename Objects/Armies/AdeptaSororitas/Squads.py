from Objects.Armies.AdeptaSororitas import Units, Weapons, Abilities


class Squad:
    def __init__(self, Power, MaxUnits, AddedPower):
        self.Points = 0
        self.Power = Power
        self.Units = []
        self.PowerAdded = AddedPower
        self.MaxUnits = MaxUnits
        self.FactionKeywords = ['IMPERIUM', 'ADEPTUS MINISTORUM', 'ADEPTA SORORITAS']

    def calculate_points(self):
        self.Points = 0
        for unit in self.Units:
            self.Points += unit.POINTS

    def add_soldier(self, unit):
        if len(self.Units) < self.MaxUnits:
            self.Power += self.PowerAdded if len(self.Units) == 5 else 0
            self.Units.append(unit)
            self.calculate_points()
        else:
            print('Max units for this squad')


class Canoness(Squad):
    def __init__(self):
        super().__init__(Power=3, MaxUnits=1, AddedPower=0)
        self.FactionKeywords.append('<ORDER>')
        self.Keywords = ["CHARACTER", "INFANTRY", "CANONESS"]
        self.ABILITIES = [Abilities.ActsOfFaith,
                          Abilities.SacredRites,
                          Abilities.ShieldOfFaith,
                          Abilities.Rosarius,
                          Abilities.BrazierOfHolyFire,
                          Abilities.LeadTheRighteous,
                          Abilities.RodOfOffice,
                          Abilities.NullRod]
        self.Units.append(Units.Canoness())
        self.HasChainSword = True
        self.HasRodOfOffice = False
        self.HasNullRod = False
        self.HasBrazierOfHolyFire = False
        self.calculate_points()

    def replace_pistol_and_sword(self):
        self.Units[0].replace_gun_1(Weapons.Boltgun())
        self.Units[0].replace_gun_2(Weapons.PowerSword(A=self.Units[0].A, S=self.Units[0].S))
        self.HasChainSword = False
        self.HasRodOfOffice = True
        self.Units[0].Points += 5
        self.calculate_points()

    def replace_bolt_pistol(self, weapon=None):
        self.Units[0].replace_gun_1(weapon)
        self.calculate_points()

    def replace_chain_sword(self, weapon=None):
        self.Units[0].replace_gun_2(weapon)
        self.HasChainSword = False
        self.calculate_points()

    def select_null_rod(self):
        if self.HasChainSword:
            self.HasNullRod = True
            self.Units[0].POINTS += 12
            self.calculate_points()

    def select_brazier_of_holy_fire(self):
        if self.HasChainSword:
            self.HasBrazierOfHolyFire = True
            self.Units[0].POINTS += 8
            self.calculate_points()


class Celestine(Squad):
    def __init__(self):
        super().__init__(Power=8, MaxUnits=1, AddedPower=0)
        self.Keywords = ["CHARACTER", "INFANTRY", "JUMP PACK", "FLY", "CELESTINE"]
        self.ABILITIES = [Abilities.ActsOfFaith,
                          Abilities.SacredRites,
                          Abilities.ShieldOfFaith,
                          Abilities.HealingTears,
                          Abilities.TheArmourOfSaintKatherine,
                          Abilities.SaintlyBlessings,
                          Abilities.MiraculousIntervention]
        self.Units.append(Units.Celestine())
        self.calculate_points()


class TriumphOfSaintKatherine(Squad):
    def __init__(self):
        super().__init__(Power=9, MaxUnits=1, AddedPower=0)
        self.Keywords = ["CHARACTER", "INFANTRY", "TRIUMPH OF SAINT KATHERINE"]
        self.ABILITIES = [Abilities.ActsOfFaith,
                          Abilities.SacredRites,
                          Abilities.ShieldOfFaith,
                          Abilities.PraesidiumProtectiva,
                          Abilities.TheFieryHeart,
                          Abilities.SolemnProcession,
                          Abilities.RelicsOfTheMatriarchs]
        self.Units.append(Units.TriumphOfSaintKatherine())
        self.calculate_points()


class JunithEruita(Squad):
    def __init__(self):
        super().__init__(Power=6, MaxUnits=1, AddedPower=0)
        self.FactionKeywords.append('ORDER OF OUR MARTYRED LADY')
        self.Keywords = ["CHARATER", "VEHICLE", "FLY", "CANONESS SUPERIOR", "JUNITH ERUITA"]
        self.ABILITIES = [Abilities.ActsOfFaith,
                          Abilities.SacredRites,
                          Abilities.ShieldOfFaith,
                          Abilities.Rosarius,
                          Abilities.FieryConviction,
                          Abilities.ThePulpitOfSaintHollinesBasilica,
                          Abilities.Explodes]
        self.Units.append(Units.JunithEruita())
        self.calculate_points()


class Missionary(Squad):
    def __init__(self):
        super().__init__(Power=2, MaxUnits=1, AddedPower=0)
        self.FactionKeywords.pop(2)
        self.Keywords = ["CHARACTER", "INFANTRY", "MINISTORUM PRIEST", "MISSIONARY"]
        self.ABILITIES = [Abilities.Zealot,
                          Abilities.Rosarius,
                          Abilities.WarHymns,
                          Abilities.LoneMission,
                          Abilities.WordOfTheEmperor]
        self.Units.append(Units.Missionary())
        self.calculate_points()

    def replace_autogun_and_laspistol(self):
        self.Units[0].replace_gun_1(Weapons.BoltPistol())
        self.Units[0].replace_gun_2(Weapons.Shotgun())
        self.calculate_points()


class BattleSistersSquad(Squad):
    def __init__(self):
        super().__init__(Power=4, MaxUnits=15, AddedPower=4)
        self.FactionKeywords.append('<ORDER>')
        self.Keywords = ["INFANTRY", "BATTLE SISTERS SQUAD"]
        self.ABILITIES = [Abilities.ActsOfFaith,
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
        self.SoldierHasSimulacrumImperialis = False
        self.HasIncensorCherub = False
        self.calculate_points()

    def take_incensor_cherub(self):
        self.HasIncensorCherub = True
        self.Points += 5

    def sergeant_take_melee_weapon(self, weapon=None):
        self.Units[0].replace_gun_5(weapon=weapon)
        self.calculate_points()

    def sergeant_replace_boltgun(self, weapon=None):
        self.Units[0].replace_gun_2(weapon=weapon)
        self.Units[0].HasBoltGun = False
        self.calculate_points()

    def sergeant_replace_bolt_pistol(self, weapon=None):
        self.Units[0].replace_gun_1(weapon=weapon)
        self.calculate_points()

    def replace_boltgun_by_special(self, soldier=1, weapon=None):
        if not self.SoldierHasSpecialWeapon:
            self.Units[soldier].replace_gun_2(weapon=weapon)
            self.Units[soldier].HasBoltGun = False
            self.SoldierHasSpecialWeapon = True
            self.calculate_points()

    def replace_boltgun_by_heavy(self, soldier=1, weapon=None):
        if not self.SoldierHasHeavyWeapon:
            self.Units[soldier].replace_gun_2(weapon=weapon)
            self.Units[soldier].HasBoltGun = False
            self.SoldierHasHeavyWeapon = True
            self.calculate_points()

    def take_simulacrum_imperialis(self, soldier=1):
        if self.Units[soldier].HasBoltGun:
            self.Units[soldier].HasSimulacrumImperialis = True
            self.SoldierHasSimulacrumImperialis = True
            self.Units[soldier].POINTS += 5
            self.calculate_points()


class Preacher(Squad):
    def __init__(self):
        super().__init__(Power=1, MaxUnits=1, AddedPower=0)
        self.FactionKeywords.pop(2)
        self.Keywords = ["CHARACTER", "INFANTRY", "MINISTORUM PRIEST", "PREACHER"]
        self.ABILITIES = [Abilities.Zealot,
                          Abilities.IconOfTheEcclesiarchy,
                          Abilities.Rosarius,
                          Abilities.WarHymns]
        self.Units.append(Units.Preacher())
        self.calculate_points()


class GeminaeSuperiaSquad(Squad):
    def __init__(self):
        super().__init__(Power=1, MaxUnits=2, AddedPower=1)
        self.Keywords = ["CHARACTER", "INFANTRY", "JUMP PACK", "FLY", "GEMINAE SUPERIA"]
        self.ABILITIES = [Abilities.ActsOfFaith,
                          Abilities.SacredRites,
                          Abilities.ShieldOfFaith,
                          Abilities.DivineGuardians,
                          Abilities.LifeWards]
        self.Units.append(Units.GeminaeSuperia())
        self.calculate_points()


class RepentiaSuperior(Squad):
    def __init__(self):
        super().__init__(Power=2, MaxUnits=1, AddedPower=0)
        self.FactionKeywords.append('<ORDER>')
        self.Keywords = ["CHARACTER", "INFANTRY", "REPENTIA SUPERIOR"]
        self.ABILITIES = [Abilities.ActsOfFaith,
                          Abilities.SacredRites,
                          Abilities.ShieldOfFaith,
                          Abilities.ScourgeOfThePenitent,
                          Abilities.DrivenOnwards]
        self.Units.append(Units.RepentiaSuperior())
        self.calculate_points()

    def take_bolt_pistol(self):
        self.Units[0].replace_gun_4(Weapons.BoltPistol())
        self.calculate_points()


class SisterRepentiaSquad(Squad):
    def __init__(self):
        super().__init__(Power=2, MaxUnits=5, AddedPower=3)
        self.Keywords = ["INFANTRY", " SISTERS REPENTIA"]
        self.ABILITIES = [Abilities.ActsOfFaith,
                          Abilities.SacredRites,
                          Abilities.ShieldOfFaith,
                          Abilities.Zealot,
                          Abilities.Martyrdom,
                          Abilities.SolaceInAnguish]
        self.Units.append(Units.SisterRepentia())
        self.Units.append(Units.SisterRepentia())
        self.Units.append(Units.SisterRepentia())
        self.Units.append(Units.SisterRepentia())
        self.calculate_points()


class CelestianSquad(Squad):
    def __init__(self):
        super().__init__(Power=, MaxUnits=, AddedPower=)
        self.Keywords = ["INFANTRY", " CELESTIAN SQUAD"]
        self.ABILITIES = []
        self.Units.append(Units. )
        self.Units.append(Units. )
        self.Units.append(Units. )
        self.Units.append(Units. )
        self.Units.append(Units. )
        # TODO Equipment singularities
        self.calculate_points()

        # 1 Celestian can be equipped with 1 weapon from the Special Weapons list instead of 1 boltgun.
        # 1 Celestian can be equipped with one of the following instead of 1 boltgun: 1 weapon from the Heavy Weaponslist; 1 weapon from the Special Weapons list.
        # 1 Celestian equipped with 1 boltgun can have a Simulacrum Imperialis.
        # The Celestian Superior can additionally be equipped with 1 weapon from the Melee Weapons list, or can beequipped with 1 weapon from the Melee Weapons list instead of 1 boltgun.
        # The Celestian Superior can be equipped with 1 weapon from the Ranged Weapons list instead of 1 boltgun.
        # The Celestian Superior can be equipped with 1 weapon from the Pistols list instead of 1 bolt pistol.
        # The unit can have an Incensor Cherub.


class ZephyrimSquad(Squad):
    def __init__(self):
        super().__init__(Power=, MaxUnits=, AddedPower=)
        self.Keywords = ["INFANTRY", " JUMP PACK", " FLY", " ZEPHYRIM SQUAD"]
        self.ABILITIES = []
        self.Units.append(Units. )
        self.Units.append(Units. )
        self.Units.append(Units. )
        self.Units.append(Units. )
        self.Units.append(Units. )
        # TODO Equipment singularities
        self.calculate_points()

        # The Zephyrim Superior can be equipped with 1 plasma pistol instead of 1 bolt pistol.
        # If the Zephyrim Superior is equipped with 1 bolt pistol, she can have a Zephyrim pennant.


class DialogusSquad(Squad):
    def __init__(self):
        super().__init__(Power=, MaxUnits=, AddedPower=)
        self.Keywords = ["CHARACTER", " INFANTRY", " DIALOGUS"]
        self.ABILITIES = []
        self.Units.append(Units. )
        self.Units.append(Units. )
        self.Units.append(Units. )
        self.Units.append(Units. )
        self.Units.append(Units. )
        # TODO Equipment singularities
        self.calculate_points()



class HospitallerSquad(Squad):
    def __init__(self):
        super().__init__(Power=, MaxUnits=, AddedPower=)
        self.Keywords = ["CHARACTER", " INFANTRY", " HOSPITALLER"]
        self.ABILITIES = []
        self.Units.append(Units. )
        self.Units.append(Units. )
        self.Units.append(Units. )
        self.Units.append(Units. )
        self.Units.append(Units. )
        # TODO Equipment singularities
        self.calculate_points()



class ImagifierSquad(Squad):
    def __init__(self):
        super().__init__(Power=, MaxUnits=, AddedPower=)
        self.Keywords = ["CHARACTER", " INFANTRY", " IMAGIFIER"]
        self.ABILITIES = []
        self.Units.append(Units. )
        self.Units.append(Units. )
        self.Units.append(Units. )
        self.Units.append(Units. )
        self.Units.append(Units. )
        # TODO Equipment singularities
        self.calculate_points()



class CrusaderSquad(Squad):
    def __init__(self):
        super().__init__(Power=, MaxUnits=, AddedPower=)
        self.Keywords = ["INFANTRY", " ECCLESIARCHY BATTLE CONCLAVE", " CRUSADERS"]
        self.ABILITIES = []
        self.Units.append(Units. )
        self.Units.append(Units. )
        self.Units.append(Units. )
        self.Units.append(Units. )
        self.Units.append(Units. )
        # TODO Equipment singularities
        self.calculate_points()



class Death Cult AssassinSquad(Squad):
    def __init__(self):
        super().__init__(Power=, MaxUnits=, AddedPower=)
        self.Keywords = ["INFANTRY", " ECCLESIARCHY BATTLE CONCLAVE", " DEATH CULT ASSASSINS"]
        self.ABILITIES = []
        self.Units.append(Units. )
        self.Units.append(Units. )
        self.Units.append(Units. )
        self.Units.append(Units. )
        self.Units.append(Units. )
        # TODO Equipment singularities
        self.calculate_points()



class Arco-flagellantSquad(Squad):
    def __init__(self):
        super().__init__(Power=, MaxUnits=, AddedPower=)
        self.Keywords = ["INFANTRY", " ECCLESIARCHY BATTLE CONCLAVE", " ARCO-FLAGELLANTS"]
        self.ABILITIES = []
        self.Units.append(Units. )
        self.Units.append(Units. )
        self.Units.append(Units. )
        self.Units.append(Units. )
        self.Units.append(Units. )
        # TODO Equipment singularities
        self.calculate_points()



class DominionSquad(Squad):
    def __init__(self):
        super().__init__(Power=, MaxUnits=, AddedPower=)
        self.Keywords = ["INFANTRY", " DOMINION SQUAD"]
        self.ABILITIES = []
        self.Units.append(Units. )
        self.Units.append(Units. )
        self.Units.append(Units. )
        self.Units.append(Units. )
        self.Units.append(Units. )
        # TODO Equipment singularities
        self.calculate_points()

        # Up to 4 Dominions can be equipped with 1 weapon from the Special Weapons list instead of 1 boltgun.
        # 1 Dominion equipped with 1 boltgun can have a Simulacrum Imperialis.
        # The Dominion Superior can additionally be equipped with 1 weapon from the Melee Weapons list, or can beequipped with 1 weapon from the Melee Weapons list instead of 1 boltgun.
        # The Dominion Superior can be equipped with 1 weapon from the Ranged Weapons list instead of 1 boltgun.
        # The Dominion Superior can be equipped with 1 weapon from the Pistols list instead of 1 bolt pistol.
        # The unit can have an Incensor Cherub.


class SeraphimSquad(Squad):
    def __init__(self):
        super().__init__(Power=, MaxUnits=, AddedPower=)
        self.Keywords = ["INFANTRY", " JUMP PACK", " FLY", " SERAPHIM SQUAD"]
        self.ABILITIES = []
        self.Units.append(Units. )
        self.Units.append(Units. )
        self.Units.append(Units. )
        self.Units.append(Units. )
        self.Units.append(Units. )
        # TODO Equipment singularities
        self.calculate_points()

        # Up to 2 Seraphim can be equipped with one of the following instead of 2 bolt pistols: 2 hand flamers; 2inferno pistols.
        # The Seraphim Superior can be equipped with one of the following instead of 1 bolt pistol: 1 chainsword; 1power sword.
        # The Seraphim Superior can be equipped with 1 plasma pistol instead of 1 bolt pistol.


class ExorcistSquad(Squad):
    def __init__(self):
        super().__init__(Power=, MaxUnits=, AddedPower=)
        self.Keywords = ["VEHICLE", " EXORCIST"]
        self.ABILITIES = []
        self.Units.append(Units. )
        self.Units.append(Units. )
        self.Units.append(Units. )
        self.Units.append(Units. )
        self.Units.append(Units. )
        # TODO Equipment singularities
        self.calculate_points()

        # This model can be equipped with Exorcist conflagration rockets instead of 1 Exorcist missile launcher.
        # This model can additionally be equipped with 1 hunter-killer missile.


class MortifierSquad(Squad):
    def __init__(self):
        super().__init__(Power=, MaxUnits=, AddedPower=)
        self.Keywords = ["VEHICLE", " MORTIFIERS"]
        self.ABILITIES = []
        self.Units.append(Units. )
        self.Units.append(Units. )
        self.Units.append(Units. )
        self.Units.append(Units. )
        self.Units.append(Units. )
        # TODO Equipment singularities
        self.calculate_points()

        # Any model can be equipped with 1 heavy flamer instead of 1 heavy bolter.
        # Any model can be equipped with 2 heavy flamers instead of 2 heavy bolters.
        # Any model can be equipped with 1 penitent buzz-blade instead of 1 penitent flail.
        # Any model can be equipped with 2 penitent buzz-blades instead of 2 penitent flails.


class RetributorSquad(Squad):
    def __init__(self):
        super().__init__(Power=, MaxUnits=, AddedPower=)
        self.Keywords = ["INFANTRY", " RETRIBUTOR SQUAD"]
        self.ABILITIES = []
        self.Units.append(Units. )
        self.Units.append(Units. )
        self.Units.append(Units. )
        self.Units.append(Units. )
        self.Units.append(Units. )
        # TODO Equipment singularities
        self.calculate_points()

        # Up to 4 Retributors can be equipped with 1 weapon from the Heavy Weapons list instead of 1 boltgun.
        # 1 Retributor equipped with 1 boltgun can have a Simulacrum Imperialis.
        # The Retributor Superior can additionally be equipped with 1 weapon from the Melee Weapons list, or can beequipped with 1 weapon from the Melee Weapons list instead of 1 boltgun.
        # The Retributor Superior can be equipped with 1 weapon from the Ranged Weapons list instead of 1 boltgun.
        # The Retributor Superior can be equipped with 1 weapon from the Pistols list instead of 1 bolt pistol.
        # This unit can have an Armorium Cherub, or it can have two Armorium Cherubs.


class Penitent EngineSquad(Squad):
    def __init__(self):
        super().__init__(Power=, MaxUnits=, AddedPower=)
        self.Keywords = ["VEHICLE", " PENITENT ENGINES"]
        self.ABILITIES = []
        self.Units.append(Units. )
        self.Units.append(Units. )
        self.Units.append(Units. )
        self.Units.append(Units. )
        self.Units.append(Units. )
        # TODO Equipment singularities
        self.calculate_points()

        # Any model can be equipped with 1 penitent buzz-blade instead of 1 penitent flail.
        # Any model can be equipped with 2 penitent buzz-blades instead of 2 penitent flails.


class Sororitas RhinoSquad(Squad):
    def __init__(self):
        super().__init__(Power=, MaxUnits=, AddedPower=)
        self.Keywords = ["VEHICLE", " TRANSPORT", " RHINO", " SORORITAS RHINO"]
        self.ABILITIES = []
        self.Units.append(Units. )
        self.Units.append(Units. )
        self.Units.append(Units. )
        self.Units.append(Units. )
        self.Units.append(Units. )
        # TODO Equipment singularities
        self.calculate_points()

        # This model can additionally be equipped with 1 hunter-killer missile.


class ImmolatorSquad(Squad):
    def __init__(self):
        super().__init__(Power=, MaxUnits=, AddedPower=)
        self.Keywords = ["VEHICLE", " TRANSPORT", " IMMOLATOR"]
        self.ABILITIES = []
        self.Units.append(Units. )
        self.Units.append(Units. )
        self.Units.append(Units. )
        self.Units.append(Units. )
        self.Units.append(Units. )
        # TODO Equipment singularities
        self.calculate_points()

        # This model can be equipped with one of the following instead of immolation flamers: 1 twin heavy bolter; 1twin multi-melta.
        # This model can additionally be equipped with 1 hunter-killer missile.



