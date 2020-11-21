from . import Units, Weapons, Abilities


class Squad:
    def __init__(self, Power, MaxUnits, AddedPower):
        self.Points = 0
        self.Power = Power
        self.Units = []
        self.PowerAdded = AddedPower
        self.MaxUnits = MaxUnits
        self.FactionKeywords = ['IMPERIUM', 'ADEPTUS ASTARTES', 'DARK ANGELS']

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


class TacticalSquad(Squad):
    def __init__(self):
        super().__init__(Power=5, MaxUnits=10, AddedPower=4)
        self.Keywords = ['INFANTRY', 'TACTICAL SQUAD']
        self.ABILITIES = [Abilities.AndTheyShallKnowNoFear,
                          Abilities.CombatSquad]
        self.Units.append(Units.TacticalMarineSergeant())
        self.Units.append(Units.TacticalMarine())
        self.Units.append(Units.TacticalMarine())
        self.Units.append(Units.TacticalMarine())
        self.Units.append(Units.TacticalMarine())
        self.SergeantWithMeltaBombs = False
        self.SoldierWithSpecialWeapon = False
        self.SoldierWithHeavyWeapon = False
        self.calculate_points()

    def sergeant_select_sergeant_weapons(self, sergeant_weapon_1=None, sergeant_weapon_2=None):
        self.Units[0].choose_sergeant_weapon(sergeant_weapon_1, sergeant_weapon_2)
        self.calculate_points()

    def sergeant_take_melta_bombs(self):
        if not self.SergeantWithMeltaBombs:
            self.Units[0].take_melta_bombs()
            self.SergeantWithMeltaBombs = True
            self.calculate_points()
        else:
            print('Already has them')

    def select_special_weapon(self, soldier=1, weapon=None):
        if len(self.Units) < 10:
            if not self.SoldierWithSpecialWeapon and not self.SoldierWithHeavyWeapon:
                self.Units[soldier].replace_gun_2(weapon=weapon)
                self.calculate_points()
                self.SoldierWithSpecialWeapon = True
            else:
                print('Cannot select this')
        elif not self.SoldierWithSpecialWeapon:
            self.Units[soldier].replace_gun_2(weapon=weapon)
            self.calculate_points()
            self.SoldierWithSpecialWeapon = True
        else:
            print('Cannot select this')

    def select_heavy_weapon(self, soldier=2, weapon=None):
        if len(self.Units) < 10:
            if not self.SoldierWithSpecialWeapon and not self.SoldierWithHeavyWeapon:
                self.Units[soldier].replace_gun_2(weapon=weapon)
                self.calculate_points()
                self.SoldierWithHeavyWeapon = True
            else:
                print('Cannot select this')
        elif not self.SoldierWithHeavyWeapon:
            self.Units[soldier].replace_gun_2(weapon=weapon)
            self.calculate_points()
            self.SoldierWithHeavyWeapon = True
        else:
            print('Cannot select this')


class IntercessorSquad(Squad):
    def __init__(self):
        super().__init__(Power=5, MaxUnits=10, AddedPower=5)
        self.Keywords = ['INFANTRY', 'PRIMARIS', 'INTERCESSOR SQUAD']
        self.ABILITIES = [Abilities.AndTheyShallKnowNoFear,
                          Abilities.AuxiliaryGrenadeLauncher,
                          Abilities.CombatSquad]
        self.Units.append(Units.IntercessorSergeant())
        self.Units.append(Units.Intercessor())
        self.Units.append(Units.Intercessor())
        self.Units.append(Units.Intercessor())
        self.Units.append(Units.Intercessor())
        self.SergeantWithMeltaBombs = False
        self.SoldiersWithAuxiliaryGrenadeLauncher = 0
        self.calculate_points()

    def sergeant_replace_bolt_rifle(self):
        self.Units[0].replace_gun_2(weapon=Weapons.PowerSword(A=self.Units[0].A, S=self.Units[0].S))
        self.calculate_points()

    def sergeant_take_power_sword(self):
        self.Units[0].take_power_sword()
        self.calculate_points()

    def replace_bolt_rifle(self, soldier, weapon=None):
        self.Units[soldier].replace_gun_2(weapon=weapon)
        self.calculate_points()

    def take_auxiliary_grenade_launcher(self, soldier=1):
        if len(self.Units) < 10:
            if self.SoldiersWithAuxiliaryGrenadeLauncher < 1:
                self.Units[soldier].Gun3.RANGE = 30
                self.Units[soldier].Gun34RANGE = 30
                self.SoldiersWithAuxiliaryGrenadeLauncher += 1
                self.calculate_points()
            else:
                print('No')
        else:
            if self.SoldiersWithAuxiliaryGrenadeLauncher < 2:
                self.Units[soldier].Gun3.RANGE = 30
                self.Units[soldier].Gun4.RANGE = 30
                self.SoldiersWithAuxiliaryGrenadeLauncher += 1
                self.calculate_points()
            else:
                print('No')


class ScoutSquad(Squad):
    def __init__(self):
        super().__init__(Power=4, MaxUnits=10, AddedPower=4)
        self.Keywords = ['INFANTRY', 'SCOUT', 'SCOUT SQUAD']
        self.ABILITIES = [Abilities.AndTheyShallKnowNoFear,
                          Abilities.ConcealedPositions,
                          Abilities.CombatSquad,
                          Abilities.CamoCloaks]
        self.Units.append(Units.ScoutSergeant())
        self.Units.append(Units.Scout())
        self.Units.append(Units.Scout())
        self.Units.append(Units.Scout())
        self.Units.append(Units.Scout())
        self.SoldiersWithHeavyBolterOrMissileLauncher = False
        self.calculate_points()

    def sergeant_replace_bolt_pistol(self, weapon=None):
        self.Units[0].replace_gun_1(weapon)
        self.calculate_points()

    def sergeant_replace_boltgun(self, weapon=None):
        self.Units[0].replace_gun_2(weapon)
        self.calculate_points()

    def replace_boltgun_heavy(self, soldier=1, weapon=None):
        self.Units[soldier].replace_gun_2(weapon)
        self.SoldiersWithHeavyBolterOrMissileLauncher = False
        self.calculate_points()

    def replace_boltgun(self, soldier, weapon=None):
        self.Units[soldier].replace_gun_2(weapon)
        self.calculate_points()

    def take_camo_cloak(self, soldier):
        self.Units[soldier].take_camo_cloak()
        self.calculate_points()


class CompanyVeterans(Squad):
    def __init__(self):
        super().__init__(Power=3, MaxUnits=5, AddedPower=5)
        self.Keywords = ['INFANTRY', 'COMPANY VETERANS']
        self.ABILITIES = [Abilities.AndTheyShallKnowNoFear,
                          Abilities.StormShield,
                          Abilities.CombatShield,
                          Abilities.CommandSquadBodyGuard]
        self.Units.append(Units.VeteranSergeant())
        self.Units.append(Units.Veteran())
        self.SoldierWithHeavyWeapon = False
        self.calculate_points()

    def sergeant_select_sergeant_weapons(self, sergeant_weapon_1=None, sergeant_weapon_2=None):
        self.Units[0].choose_sergeant_weapon(sergeant_weapon_1, sergeant_weapon_2)
        self.calculate_points()

    def replace_bolt_pistol(self, soldier, weapon=None):
        self.Units[soldier].replace_gun_1(weapon)
        self.calculate_points()

    def replace_chain_sword(self, soldier, weapon=None):
        self.Units[soldier].replace_gun_2(weapon)
        self.calculate_points()

    def take_combat_shield(self, soldier):
        self.Units[soldier].take_combat_shield()
        self.calculate_points()

    def replace_chain_sword_heavy(self, soldier=1, weapon=None):
        if not self.SoldierWithHeavyWeapon:
            self.Units[soldier].replace_chain_sword_heavy(weapon)
            self.SoldierWithHeavyWeapon = True
            self.calculate_points()


class DeathWingTerminatorSquad(Squad):
    def __init__(self):
        super().__init__(Power=13, MaxUnits=10, AddedPower=12)
        self.FactionKeywords.append('DEATHWING')
        self.Keywords = ['INFANTRY', 'TERMINATOR', 'DEATHWING TERMINATOR SQUAD']
        self.ABILITIES = [Abilities.InnerCircle,
                          Abilities.WatcherInTheDark,
                          Abilities.CruxTerminatus,
                          Abilities.TeleportStrike,
                          Abilities.CombatSquad,
                          Abilities.StormShield]
        self.Units.append(Units.DeathWingTerminatorSergeant())
        self.Units.append(Units.DeathWingTerminator())
        self.Units.append(Units.DeathWingTerminator())
        self.Units.append(Units.DeathWingTerminator())
        self.Units.append(Units.DeathWingTerminator())
        self.SoldiersWithHeavyWeapon = 0
        self.WatcherInTheDark = False
        self.calculate_points()

    def replace_all_weapons(self, soldier, weapon_1=None, weapon_2=None):
        self.Units[soldier].replace_gun_1(weapon=weapon_1)
        self.Units[soldier].replace_gun_2(weapon=weapon_2)
        self.calculate_points()

    def replace_power_fist(self, soldier, weapon=None):
        self.Units[soldier].replace_gun_1(weapon=weapon)
        self.calculate_points()

    def replace_storm_bolter(self, soldier=1, weapon=None):
        if len(self.Units) < 10:
            if self.SoldiersWithHeavyWeapon < 1:
                self.Units[soldier].replace_gun_2(weapon)
                self.SoldiersWithHeavyWeapon += 1
                self.calculate_points()
            else:
                print('No')
        else:
            if self.SoldiersWithHeavyWeapon < 2:
                self.Units[soldier].replace_gun_2(weapon)
                self.SoldiersWithHeavyWeapon += 1
                self.calculate_points()
            else:
                print('No')

    def take_cyclone_missile_launcher(self, soldier=1):
        if len(self.Units) < 10:
            if self.SoldiersWithHeavyWeapon < 1:
                self.Units[soldier].replace_gun_3(weapon=Weapons.CycloneMissileLauncher())
                self.SoldiersWithHeavyWeapon += 1
                self.calculate_points()
            else:
                print('No')
        else:
            if self.SoldiersWithHeavyWeapon < 2:
                self.Units[soldier].replace_gun_3(weapon=Weapons.CycloneMissileLauncher())
                self.SoldiersWithHeavyWeapon += 1
                self.calculate_points()
            else:
                print('No')

    def get_watcher_in_the_dark(self):
        if not self.WatcherInTheDark:
            self.WatcherInTheDark = True
            self.Points += 5


class DeathWingKnightSquad(Squad):
    def __init__(self):
        super().__init__(Power=12, MaxUnits=10, AddedPower=12)
        self.FactionKeywords.append('DEATHWING')
        self.Keywords = ['INFANTRY', 'TERMINATOR', 'DEATHWING KNIGHTS']
        self.ABILITIES = [Abilities.InnerCircle,
                          Abilities.WatcherInTheDark,
                          Abilities.TeleportStrike,
                          Abilities.CombatSquad,
                          Abilities.StormShield]
        self.Units.append(Units.DeathWingKnightMaster())
        self.Units.append(Units.DeathWingKnight())
        self.Units.append(Units.DeathWingKnight())
        self.Units.append(Units.DeathWingKnight())
        self.Units.append(Units.DeathWingKnight())
        self.WatcherInTheDark = False
        self.calculate_points()

    def get_watcher_in_the_dark(self):
        if not self.WatcherInTheDark:
            self.WatcherInTheDark = True
            self.Points += 5


class DeathWingCataphractiiTerminatorSquad(Squad):
    def __init__(self):
        super().__init__(Power=12, MaxUnits=10, AddedPower=12)
        self.FactionKeywords.append('DEATHWING')
        self.Keywords = ['INFANTRY', 'TERMINATOR', 'DEATHWING CATAPHRACTII TERMINATOR SQUAD']
        self.ABILITIES = [Abilities.InnerCircle,
                          Abilities.TeleportStrike,
                          Abilities.CombatSquad,
                          Abilities.CataphractiiArmour]
        self.Units.append(Units.DeathWingCataphractiiTerminatorSergeant())
        self.Units.append(Units.DeathWingCataphractiiTerminator())
        self.Units.append(Units.DeathWingCataphractiiTerminator())
        self.Units.append(Units.DeathWingCataphractiiTerminator())
        self.Units.append(Units.DeathWingCataphractiiTerminator())
        self.SoldiersWithHeavyFlamer = 0
        self.SergeantWithGrenadeHarness = False
        self.calculate_points()

    def sergeant_replace_power_sword(self, weapon=None):
        self.Units[0].replace_gun_2(weapon=weapon)
        self.calculate_points()

    def sergeant_take_grenade_harness(self):
        self.Units[0].take_grenade_harness()
        self.SergeantWithGrenadeHarness = True
        self.calculate_points()

    def replace_combi_bolter_heavy(self, soldier=1):
        if len(self.Units) < 10:
            if self.SoldiersWithHeavyFlamer < 1:
                self.Units[soldier].replace_gun_1(weapon=Weapons.HeavyFlamer())
                self.SoldiersWithHeavyFlamer += 1
                self.calculate_points()
            else:
                print('No')
        else:
            if self.SoldiersWithHeavyFlamer < 2:
                self.Units[soldier].replace_gun_1(weapon=Weapons.HeavyFlamer())
                self.SoldiersWithHeavyFlamer += 1
                self.calculate_points()
            else:
                print('No')

    def replace_combi_bolter(self, soldier=1):
        self.Units[soldier].replace_gun_1(weapon=Weapons.LightningClaw(A=self.Units[soldier].A,
                                                                       S=self.Units[soldier].S))
        self.calculate_points()

    def replace_power_fist(self, soldier=1, weapon=None):
        self.Units[soldier].replace_gun_2(weapon=weapon)
        self.calculate_points()


class DeathWingTartarosTerminatorSquad(Squad):
    def __init__(self):
        super().__init__(Power=12, MaxUnits=10, AddedPower=12)
        self.FactionKeywords.append('DEATHWING')
        self.Keywords = ['INFANTRY', 'TERMINATOR', 'TARTAROS TERMINATOR SQUAD']
        self.ABILITIES = [Abilities.InnerCircle,
                          Abilities.TeleportStrike,
                          Abilities.CombatSquad,
                          Abilities.TartarosArmour]
        self.Units.append(Units.DeathWingTartarosTerminatorSergeant())
        self.Units.append(Units.DeathWingTartarosTerminator())
        self.Units.append(Units.DeathWingTartarosTerminator())
        self.Units.append(Units.DeathWingTartarosTerminator())
        self.Units.append(Units.DeathWingTartarosTerminator())
        self.SoldiersWithHeavy = 0
        self.SoldierstWithGrenadeHarness = 0
        self.calculate_points()

    def sergeant_replace_all_weapons(self):
        self.Units[0].replace_gun_1(Weapons.LightningClaw(A=self.Units[0].A, S=self.Units[0].S))
        self.Units[0].replace_gun_2(Weapons.LightningClaw(A=self.Units[0].A, S=self.Units[0].S))
        self.calculate_points()

    def sergeant_replace_power_sword(self, weapon=None):
        self.Units[0].replace_gun_2(weapon=weapon)
        self.calculate_points()

    def sergeant_replace_combi_bolter(self, weapon=None):
        self.Units[0].replace_gun_1(weapon=weapon)
        self.calculate_points()

    def replace_combi_bolter_heavy(self, soldier=1, weapon=None):
        if len(self.Units) < 10:
            if self.SoldiersWithHeavy < 1 and weapon is not None:
                self.Units[soldier].replace_gun_1(weapon=weapon)
                self.SoldiersWithHeavy += 1
                self.calculate_points()
            else:
                print('No')
        else:
            if self.SoldiersWithHeavy < 2 and weapon is not None:
                self.Units[soldier].replace_gun_1(weapon=weapon)
                self.SoldiersWithHeavy += 1
                self.calculate_points()
            else:
                print('No')

    def replace_all_weapons(self, soldier=1):
        self.Units[soldier].replace_gun_1(Weapons.LightningClaw(A=self.Units[0].A, S=self.Units[0].S))
        self.Units[soldier].replace_gun_2(Weapons.LightningClaw(A=self.Units[0].A, S=self.Units[0].S))
        self.calculate_points()

    def replace_power_fist(self, soldier=1):
        self.Units[soldier].replace_gun_2(weapon=Weapons.ChainFist(A=self.Units[soldier].A, S=self.Units[soldier].S))
        self.calculate_points()

    def take_grenade_harness(self, soldier=1):
        if len(self.Units) < 10:
            if self.SoldierstWithGrenadeHarness < 1:
                self.Units[soldier].take_grenade_harness()
                self.SoldierstWithGrenadeHarness += 1
                self.calculate_points()
            else:
                print('No')
        else:
            if self.SoldierstWithGrenadeHarness < 2:
                self.Units[soldier].take_grenade_harness()
                self.SoldierstWithGrenadeHarness += 1
                self.calculate_points()
            else:
                print('No')


class DreadnoughtUnit(Squad):
    def __init__(self, Power=7, MaxUnits=1, AddedPower=0):
        super().__init__(Power=Power, MaxUnits=MaxUnits, AddedPower=AddedPower)
        self.Keywords = ['VEHICLE', 'DREADNOUGHT']
        self.ABILITIES = [Abilities.SmokeLaunchers,
                          Abilities.Explodes]
        self.Units.append(Units.Dreadnought())
        self.HasMissileLauncher = False

    def replace_assault_cannon(self, weapon=None):
        self.Units[0].replace_gun_1(weapon=weapon)
        self.calculate_points()

    def replace_combat_weapon_and_storm_bolter(self):
        self.Units[0].replace_gun_1(weapon=Weapons.MissileLauncher())
        self.Units[0].gun2 = None
        self.HasMissileLauncher = True
        self.calculate_points()

    def replace_storm_bolter(self):
        if not self.HasMissileLauncher:
            self.Units[0].replace_gun_2(weapon=Weapons.HeavyFlamer())


class VenerableDreadnoughtUnit(DreadnoughtUnit):
    def __init__(self):
        super().__init__(Power=8, MaxUnits=1, AddedPower=0)
        self.Keywords.append('VENERABLE DREADNOUGHT')
        self.ABILITIES.append(Abilities.UnyieldingAncient)
        self.Units[0] = Units.VenerableDreadnought()


class ContemptorDreagnouht(Squad):
    def __init__(self):
        super().__init__(Power=8, MaxUnits=1, AddedPower=0)
        self.Keywords = ['VEHICLE', 'DREADNOUGHT', 'CONTEMPTOR DREADNOUGHT']
        self.ABILITIES = [Abilities.AtomanticShielding,
                          Abilities.Explodes]
        self.Units.append(Units.ContemptorDreadnought())

    def replace_multi_melta(self):
        self.Units[0].replace_gun_1(weapon=Weapons.KheresPatternAssault())
        self.calculate_points()


class RedemptorDreadnought(Squad):
    def __init__(self):
        super().__init__(Power=10, MaxUnits=1, AddedPower=0)
        self.Keywords = ['VEHICLE', 'DREADNOUGHT', 'REDEMPTOR DREADNOUGHT']
        self.ABILITIES = [Abilities.Explodes]
        self.Units.append(Units.ContemptorDreadnought())

    def replace_heavy_flamer(self):
        self.Units[0].replace_gun_2(weapon=Weapons.OnslaughtGatlingCannon())
        self.calculate_points()

    def replace_gatling_cannon(self):
        self.Units[0].replace_gun_1(weapon=Weapons.MacroPlasmaIncinerator())
        self.calculate_points()

    def replace_fragstorm_launcher(self):
        self.Units[0].replace_gun_3(weapon=Weapons.StormBolter())
        self.Units[0].replace_gun_4(weapon=Weapons.StormBolter())
        self.calculate_points()

    def take_icarus_rocket(self):
        self.Units[0].replace_gun_6(weapon=Weapons.IcarusRocketPod())
        self.calculate_points()


class AggressorSquad(Squad):
    def __init__(self):
        super().__init__(Power=6, MaxUnits=6, AddedPower=6)
        self.FactionKeywords.append('DEATHWING')
        self.Keywords = ['INFANTRY', 'MK X GRAVIS', 'PRIMARIS', 'AGGRESSOR SQUAD']
        self.ABILITIES = [Abilities.AndTheyShallKnowNoFear,
                          Abilities.CombatSquad,
                          Abilities.FireStorm,
                          Abilities.RelentlessAdvance]
        self.Units.append(Units.AggressorSergeant())
        self.Units.append(Units.Aggressor())
        self.Units.append(Units.Aggressor())
        self.calculate_points()

    def replace_boltstorm_gauntlets_and_launcher(self, soldier=1):
        self.Units[soldier].replace_gun_1(Weapons.FlameStormGauntlets())
        self.Units[soldier].replace_gun_2(Weapons.FlameStormGauntletsMelee(A=self.Units[soldier].A,
                                                                           S=self.Units[soldier].S))
        self.calculate_points()


class ServitorSquad(Squad):
    def __init__(self):
        super().__init__(Power=3, MaxUnits=4, AddedPower=0)
        self.Keywords = ['INFANTRY', 'SERVITORS']
        self.ABILITIES = [Abilities.Mindlock]
        self.Units.append(Units.Servitor())
        self.Units.append(Units.Servitor())
        self.Units.append(Units.Servitor())
        self.Units.append(Units.Servitor())
        self.SoldiersWithServoArmReplaced = 0
        self.calculate_points()

    def replace_servo_amr(self, soldier=1, weapon=None):
        if self.SoldiersWithServoArmReplaced < 2:
            self.Units[soldier].replace_gun_1(weapon=weapon)
