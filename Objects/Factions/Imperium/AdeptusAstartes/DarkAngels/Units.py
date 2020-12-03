from Objects.Factions.Imperium.Common.Armies import Infantry, Vehicle, Sergeant
from Objects.Races.Humans import Human
from . import Mesh, Weapons as DarkAngelWeapons


class TacticalMarine(Infantry, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.TacticalMarineBolter)
        self.POINTS = 13
        self.Gun.append(DarkAngelWeapons.BoltPistol())
        self.POINTS += self.Gun[0].POINTS
        self.Gun.append(DarkAngelWeapons.Boltgun())
        self.POINTS += self.Gun[1].POINTS
        self.Gun.append(DarkAngelWeapons.FragGrenade())
        self.POINTS += self.Gun[2].POINTS
        self.Gun.append(DarkAngelWeapons.KrakGrenade())
        self.POINTS += self.Gun[3].POINTS


class TacticalMarineSergeant(TacticalMarine, Sergeant):
    def __init__(self):
        super().__init__()

    def take_melta_bombs(self):
        self.Gun.append(DarkAngelWeapons.MeltaBomb())


class Intercessor(Infantry, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.PrimarisIntercessor)
        self.POINTS = 18
        self.W += 1
        self.A += 1
        self.Gun.append(DarkAngelWeapons.BoltPistol())
        self.POINTS += self.Gun[0].POINTS
        self.Gun.append(DarkAngelWeapons.BoltRifle())
        self.POINTS += self.Gun[1].POINTS
        self.Gun.append(DarkAngelWeapons.FragGrenade())
        self.POINTS += self.Gun[2].POINTS
        self.Gun.append(DarkAngelWeapons.KrakGrenade())
        self.POINTS += self.Gun[3].POINTS


class IntercessorSergeant(Intercessor, Sergeant):
    def __init__(self):
        super().__init__()

    def choose_sergeant_weapon(self, sergeant_weapon_1=None, sergeant_weapon_2=None):
        pass

    def take_power_sword(self):
        self.Gun.append(DarkAngelWeapons.PowerSword(A=self.A, S=self.S))
        self.POINTS += self.Gun[4].POINTS


class Scout(Infantry, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.ScoutBolter)
        self.POINTS = 11
        self.Sv += 1
        self.Gun.append(DarkAngelWeapons.BoltPistol())
        self.POINTS += self.Gun[0].POINTS
        self.Gun.append(DarkAngelWeapons.Boltgun())
        self.POINTS += self.Gun[1].POINTS
        self.Gun.append(DarkAngelWeapons.FragGrenade())
        self.POINTS += self.Gun[2].POINTS
        self.Gun.append(DarkAngelWeapons.KrakGrenade())
        self.POINTS += self.Gun[3].POINTS
        self.camo_cloak = False

    def take_camo_cloak(self):
        self.camo_cloak = True
        self.POINTS += 3


class ScoutSergeant(Scout, Sergeant):
    def __init__(self):
        super().__init__()

    def choose_sergeant_weapon(self, sergeant_weapon_1=None, sergeant_weapon_2=None):
        pass


class Veteran(Infantry, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.VanguardVeteranBoltPistol_ChainSword)
        self.POINTS = 16
        self.A += 1
        self.Ld += 1
        self.Gun.append(DarkAngelWeapons.BoltPistol())
        self.POINTS += self.Gun[0].POINTS
        self.Gun.append(DarkAngelWeapons.ChainSword(A=self.A, S=self.S))
        self.POINTS += self.Gun[1].POINTS
        self.Gun.append(DarkAngelWeapons.FragGrenade())
        self.POINTS += self.Gun[2].POINTS
        self.Gun.append(DarkAngelWeapons.KrakGrenade())
        self.POINTS += self.Gun[3].POINTS

    # Storm Shield or Melee weapons or Pistols List
    def replace_gun_1(self, weapon=None):
        self.POINTS -= self.Gun[0].POINTS
        self.Gun[0] = weapon
        if weapon is not None:
            self.POINTS += self.Gun[0].POINTS
        else:
            self.InvSv = 3
            self.POINTS += 5

    # Storm Shield (weapon=None) or BoltGun or Melee weapons or Pistols list or Combi weapons or Special Weapons
    def replace_gun_2(self, weapon=None):
        self.POINTS -= self.Gun[1].POINTS
        self.Gun[1] = weapon
        if weapon is not None:
            self.POINTS += self.Gun[1].POINTS
        else:
            self.InvSv = 3
            self.POINTS += 5

    def take_combat_shield(self):
        self.InvSv = 5
        self.POINTS += 4


class VeteranSergeant(Veteran, Sergeant):
    def __init__(self):
        super().__init__()


class DeathWingTerminator(Infantry, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.TerminatorPowerfist_Stormbolter)
        self.POINTS = 26
        self.M -= 1
        self.W += 1
        self.A += 1
        self.Ld += 1
        self.Sv -= 1
        self.Gun.append(DarkAngelWeapons.PowerFist(A=self.A, S=self.S))
        self.POINTS += self.Gun[0].POINTS
        self.Gun.append(DarkAngelWeapons.StormBolter())
        self.POINTS += self.Gun[1].POINTS


class DeathWingTerminatorSergeant(DeathWingTerminator, Sergeant):
    def __init__(self):
        super().__init__()

    def choose_sergeant_weapon(self, sergeant_weapon_1=None, sergeant_weapon_2=None):
        pass


class DeathWingKnight(Infantry, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.DeathwingKnightMace)
        self.POINTS = 45
        self.M -= 1
        self.W += 1
        self.A += 1
        self.Ld += 1
        self.Sv -= 1
        self.Gun.append(DarkAngelWeapons.MaceOfAbsolution(A=self.A, S=self.S))
        self.POINTS += self.Gun[0].POINTS
        self.InvSv = 3
        self.POINTS += 5


class DeathWingKnightMaster(DeathWingKnight, Sergeant):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.DeathingKnightFlail)
        self.POINTS += self.Gun[0].POINTS
        self.Gun.append(DarkAngelWeapons.FlailOfTheUnforgiven(A=self.A, S=self.S))
        self.POINTS += self.Gun[0].POINTS

    def choose_sergeant_weapon(self, sergeant_weapon_1=None, sergeant_weapon_2=None):
        pass


class DeathWingCataphractiiTerminator(Infantry, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self)  # TODO Not Mesh
        self.POINTS = 30
        self.M -= 2
        self.W += 1
        self.A += 1
        self.Ld += 1
        self.Sv -= 1
        self.Gun.append(DarkAngelWeapons.CombiBolter())
        self.POINTS += self.Gun[0].POINTS
        self.Gun.append(DarkAngelWeapons.PowerFist(A=self.A, S=self.S))
        self.POINTS += self.Gun[1].POINTS


class DeathWingCataphractiiTerminatorSergeant(DeathWingCataphractiiTerminator, Sergeant):
    def __init__(self):
        DeathWingCataphractiiTerminator.__init__(self)
        Sergeant.__init__(self)
        self.POINTS += self.Gun[1].POINTS
        self.Gun.append(DarkAngelWeapons.PowerSword(A=self.A, S=self.S))
        self.POINTS += self.Gun[1].POINTS

    def choose_sergeant_weapon(self, sergeant_weapon_1=None, sergeant_weapon_2=None):
        pass

    def take_grenade_harness(self):
        self.Gun.append(DarkAngelWeapons.GrenadeHarness())
        self.POINTS += self.Gun[2].POINTS


class DeathWingTartarosTerminator(Infantry, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self)  # TODO Not Mesh
        self.POINTS = 26
        self.W += 1
        self.A += 1
        self.Ld += 1
        self.Sv -= 1
        self.Gun.append(DarkAngelWeapons.CombiBolter())
        self.POINTS += self.Gun[0].POINTS
        self.Gun.append(DarkAngelWeapons.PowerFist(A=self.A, S=self.S))
        self.POINTS += self.Gun[1].POINTS

    def take_grenade_harness(self):
        self.Gun.append(DarkAngelWeapons.GrenadeHarness())
        self.POINTS += self.Gun[2].POINTS


class DeathWingTartarosTerminatorSergeant(DeathWingTartarosTerminator, Sergeant):
    def __init__(self):
        DeathWingTartarosTerminator.__init__(self)
        Sergeant.__init__(self)
        self.POINTS += self.Gun[1].POINTS
        self.Gun.append(DarkAngelWeapons.PowerSword(A=self.A, S=self.S))
        self.POINTS += self.Gun[1].POINTS

    def choose_sergeant_weapon(self, sergeant_weapon_1=None, sergeant_weapon_2=None):
        pass


class Dreadnought(Vehicle, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.Dreadnought_CombatWeapon_AssaultCannon)
        self.POINTS = 70
        self.Gun.append(DarkAngelWeapons.AssaultCannon())
        self.POINTS += self.Gun[0].POINTS
        self.Gun.append(DarkAngelWeapons.StormBolter())
        self.POINTS += self.Gun[1].POINTS
        self.Gun.append(DarkAngelWeapons.DreadnoughtCombatWeapon(A=self.A, S=self.S))
        self.POINTS += self.Gun[2].POINTS


class VenerableDreadnought(Dreadnought):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.VenerableDreadnought3_3Autocannon_Assaultcannon)
        self.POINTS = 90
        self.WS = 2
        self.BS = 2


class ContemptorDreadnought(Vehicle, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self)  # TODO Not Mesh
        self.POINTS = 98
        self.T = 7
        self.W = 10
        self.InvSv = 5
        self.FirstM = 9
        self.SecondM = 6
        self.ThirdM = 4
        self.FirstWS = 2
        self.SecondWS = 3
        self.ThirdWS = 4
        self.FirstBS = 2
        self.SecondBS = 3
        self.ThirdBS = 4
        self.FirstW = 6
        self.SecondW = 3
        self.damage_update(M=True, WS=True, BS=True)
        self.Gun.append(DarkAngelWeapons.MultiMelta())
        self.POINTS += self.Gun[0].POINTS
        self.Gun.append(DarkAngelWeapons.CombiBolter())
        self.POINTS += self.Gun[1].POINTS
        self.Gun.append(DarkAngelWeapons.DreadnoughtCombatWeapon(A=self.A, S=self.S))
        self.POINTS += self.Gun[2].POINTS


class RedemptorDreadnought(Vehicle, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.RedemptorDreadnought)
        self.POINTS = 140
        self.T = 7
        self.W = 13
        self.InvSv = 5
        self.FirstM = 8
        self.SecondM = 6
        self.ThirdM = 4
        self.FirstWS = 3
        self.SecondWS = 4
        self.ThirdWS = 5
        self.FirstBS = 3
        self.SecondBS = 4
        self.ThirdBS = 5
        self.FirstW = 7
        self.SecondW = 4
        self.damage_update(M=True, WS=True, BS=True)
        self.Gun.append(DarkAngelWeapons.HeavyOnslaughtGatlingCannon())
        self.POINTS += self.Gun[0].POINTS
        self.Gun.append(DarkAngelWeapons.HeavyFlamer())
        self.POINTS += self.Gun[1].POINTS
        self.Gun.append(DarkAngelWeapons.FragStormGrenadeLauncher())
        self.POINTS += self.Gun[2].POINTS
        self.Gun.append(DarkAngelWeapons.FragStormGrenadeLauncher())
        self.POINTS += self.Gun[3].POINTS
        self.Gun.append(DarkAngelWeapons.RedemptorFist(A=self.A, S=self.S))
        self.POINTS += self.Gun[4].POINTS


class Aggressor(Infantry, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.PrimarisAggressor)
        self.POINTS = 21
        self.M = 5
        self.T = 5
        self.W = 2
        self.A = 2
        self.Gun.append(DarkAngelWeapons.AutoboltStormGauntlets())
        self.POINTS += self.Gun[0].POINTS
        self.Gun.append(DarkAngelWeapons.AutoboltStormGauntletsMelee(A=self.A, S=self.S))
        self.POINTS += self.Gun[1].POINTS
        self.Gun.append(DarkAngelWeapons.FragStormGrenadeLauncher())
        self.POINTS += self.Gun[2].POINTS


class AggressorSergeant(Aggressor, Sergeant):
    def __init__(self):
        Aggressor.__init__(self)
        Sergeant.__init__(self)

    def choose_sergeant_weapon(self, sergeant_weapon_1=None, sergeant_weapon_2=None):
        pass


class Servitor(Infantry, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self)  # TODO not mesh
        self.POINTS = 2
        self.M = 5
        self.WS = 5
        self.BS = 5
        self.S = 3
        self.T = 3
        self.Ld = 6
        self.Sv = 4
        self.Gun.append(DarkAngelWeapons.ServoArm(A=self.A, S=self.S))
        self.POINTS += self.Gun[0].POINTS
