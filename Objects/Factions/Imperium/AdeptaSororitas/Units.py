from Objects.Factions.Imperium.Common.Armies import Infantry, Vehicle, Sergeant
from Objects.Races.Humans import Human
from . import Mesh, Weapons


class Canoness(Infantry, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.Canoness)
        self.POINTS = 45
        self.WS = 2
        self.BS = 2
        self.S = 3
        self.T = 3
        self.W = 5
        self.A = 4
        self.Ld = 9
        self.Gun.append(Weapons.BoltPistol())
        self.POINTS += self.Gun[0].POINTS
        self.Gun.append(Weapons.ChainSword(A=self.A, S=self.S))
        self.POINTS += self.Gun[1].POINTS
        self.Gun.append(Weapons.FragGrenade())
        self.POINTS += self.Gun[2].POINTS
        self.Gun.append(Weapons.KrakGrenades())
        self.POINTS += self.Gun[3].POINTS


class Celestine(Infantry, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self)  # TODO Mesh
        self.POINTS = 160
        self.M = 12
        self.WS = 2
        self.BS = 2
        self.S = 3
        self.T = 3
        self.W = 6
        self.A = 6
        self.Ld = 9
        self.Sv = 2
        self.Gun.append(Weapons.TheArdentBlade(A=self.A, S=self.S))
        self.POINTS += self.Gun[0].POINTS


class TriumphOfSaintKatherine(Vehicle, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.TheTriumphofSaintKatherine)
        self.POINTS = 185
        self.S = 3
        self.T = 3
        self.W = 18
        self.Ld = 9
        self.FirstA = 14
        self.SecondA = 8
        self.ThirdA = 6
        self.FirstW = 10
        self.SecondW = 5
        self.damage_update(A=True)
        self.Gun.append(Weapons.BoltPistol())
        self.POINTS += self.Gun[0].POINTS
        self.Gun.append(Weapons.BoltPistol())
        self.POINTS += self.Gun[1].POINTS
        self.Gun.append(Weapons.BoltPistol())
        self.POINTS += self.Gun[2].POINTS
        self.Gun.append(Weapons.BoltPistol())
        self.POINTS += self.Gun[3].POINTS
        self.Gun.append(Weapons.BoltPistol())
        self.POINTS += self.Gun[4].POINTS
        self.Gun.append(Weapons.BoltPistol())
        self.POINTS += self.Gun[5].POINTS
        self.Gun.append(Weapons.TheMartyrSword(A=self.A, S=self.S))
        self.POINTS += self.Gun[6].POINTS
        self.Gun.append(Weapons.RelicWeapons(A=self.A, S=self.S))
        self.POINTS += self.Gun[7].POINTS
        self.Gun.append(Weapons.FragGrenade())
        self.POINTS += self.Gun[8].POINTS
        self.Gun.append(Weapons.KrakGrenades())
        self.POINTS += self.Gun[9].POINTS


class JunithEruita(Vehicle, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.JunithEruita)
        self.POINTS = 110
        self.M = 10
        self.WS = 2
        self.BS = 2
        self.S = 3
        self.W = 7
        self.A = 4
        self.Ld = 9
        self.Gun.append(Weapons.HeavyFlamer())
        self.POINTS += self.Gun[0].POINTS
        self.Gun.append(Weapons.HeavyFlamer())
        self.POINTS += self.Gun[1].POINTS
        self.Gun.append(Weapons.TheMaceOfCastigation(A=self.A, S=self.S))
        self.POINTS += self.Gun[2].POINTS


class Missionary(Infantry, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.Missionary)
        self.POINTS = 38
        self.WS = 4
        self.BS = 4
        self.S = 3
        self.T = 3
        self.W = 4
        self.A = 3
        self.Sv = 6
        self.Gun.append(Weapons.AutoGun())
        self.POINTS += self.Gun[0].POINTS
        self.Gun.append(Weapons.LasPistol())
        self.POINTS += self.Gun[1].POINTS
        self.Gun.append(Weapons.ChainSword(A=self.A, S=self.S))
        self.POINTS += self.Gun[2].POINTS
        self.Gun.append(Weapons.FragGrenade())
        self.POINTS += self.Gun[3].POINTS
        self.Gun.append(Weapons.KrakGrenades())
        self.POINTS += self.Gun[4].POINTS


class BattleSister(Infantry, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.BattleSisterBoltgunBoltPistol)
        self.POINTS = 9
        self.WS = 4
        self.S = 3
        self.T = 3
        self.Gun.append(Weapons.BoltPistol())
        self.POINTS += self.Gun[0].POINTS
        self.Gun.append(Weapons.Boltgun())
        self.POINTS += self.Gun[1].POINTS
        self.Gun.append(Weapons.FragGrenade())
        self.POINTS += self.Gun[2].POINTS
        self.Gun.append(Weapons.KrakGrenades())
        self.POINTS += self.Gun[3].POINTS


class SisterSuperior(BattleSister, Sergeant):
    def __init__(self):
        super().__init__()


class Preacher(Infantry, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.PreacherLaspistolChainsword)
        self.POINTS = 30
        self.WS = 4
        self.BS = 4
        self.S = 3
        self.T = 3
        self.W = 4
        self.A = 3
        self.Sv = 6
        self.Gun.append(Weapons.LasPistol())
        self.POINTS += self.Gun[0].POINTS
        self.Gun.append(Weapons.ChainSword(A=self.A, S=self.S))
        self.POINTS += self.Gun[1].POINTS


class GeminaeSuperia(Infantry, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.GeminaeSuperiaBoltPistolPowerSword)
        self.POINTS = 16
        self.M = 12
        self.S = 3
        self.T = 3
        self.W = 2
        self.A = 3
        self.Ld = 9
        self.Gun.append(Weapons.BoltPistol())
        self.POINTS += self.Gun[0].POINTS
        self.Gun.append(Weapons.PowerSword(A=self.A, S=self.S))
        self.POINTS += self.Gun[1].POINTS
        self.Gun.append(Weapons.FragGrenade())
        self.POINTS += self.Gun[2].POINTS
        self.Gun.append(Weapons.KrakGrenades())
        self.POINTS += self.Gun[3].POINTS


class RepentiaSuperior(Infantry, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.RepentiaSuperiorNeuralWhips)
        self.POINTS = 35
        self.S = 3
        self.T = 3
        self.W = 4
        self.A = 4
        self.Ld = 8
        self.Gun.append(Weapons.NeuralWhips(A=self.A, S=self.S))
        self.POINTS += self.Gun[0].POINTS
        self.Gun.append(Weapons.FragGrenade())
        self.POINTS += self.Gun[1].POINTS
        self.Gun.append(Weapons.KrakGrenades())
        self.POINTS += self.Gun[2].POINTS


class SisterRepentia(Infantry, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.SisterRepentiaPenitentEviscerator)
        self.POINTS = 13
        self.S = 3
        self.T = 3
        self.A = 2
        self.Ld = 8
        self.Sv = 7
        self.Gun.append(Weapons.PenitentEviscerator(A=self.A, S=self.S))
        self.POINTS += self.Gun[0].POINTS


class Celestian(Infantry, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.CelestianBoltgunBoltPistol)
        self.POINTS = 10
        self.S = 3
        self.T = 3
        self.A = 2
        self.Ld = 8
        self.Gun.append(Weapons.BoltPistol())
        self.POINTS += self.Gun[0].POINTS
        self.Gun.append(Weapons.Boltgun())
        self.POINTS += self.Gun[1].POINTS
        self.Gun.append(Weapons.FragGrenade())
        self.POINTS += self.Gun[2].POINTS
        self.Gun.append(Weapons.KrakGrenades())
        self.POINTS += self.Gun[3].POINTS


class CelestianSuperior(Celestian, Sergeant):
    def __init__(self):
        super().__init__()


class Zephyrim(Infantry, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.ZephyrimBoltPistolPowerSword)
        self.POINTS = 13
        self.M = 12
        self.S = 3
        self.T = 3
        self.A = 2
        self.Ld = 8
        self.Gun.append(Weapons.BoltPistol())
        self.POINTS += self.Gun[0].POINTS
        self.Gun.append(Weapons.PowerSword(A=self.A, S=self.S))
        self.POINTS += self.Gun[1].POINTS
        self.Gun.append(Weapons.FragGrenade())
        self.POINTS += self.Gun[2].POINTS
        self.Gun.append(Weapons.KrakGrenades())
        self.POINTS += self.Gun[3].POINTS


class ZephyrimSuperior(Zephyrim, Sergeant):
    def __init__(self):
        super().__init__()


class Dialogus(Infantry, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.DialogusBoltPistolDialogusStaff)
        self.POINTS = 35
        self.WS = 4
        self.S = 3
        self.T = 3
        self.W = 4
        self.A = 3
        self.Ld = 8
        self.Gun.append(Weapons.BoltPistol())
        self.POINTS += self.Gun[0].POINTS
        self.Gun.append(Weapons.Dialogusstaff(A=self.A, S=self.S))
        self.POINTS += self.Gun[1].POINTS


class Hospitaller(Infantry, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.HospitallerBoltPistolChirurgeonsTools)
        self.POINTS = 35
        self.WS = 4
        self.S = 3
        self.T = 3
        self.W = 4
        self.A = 3
        self.Ld = 8
        self.Gun.append(Weapons.BoltPistol())
        self.POINTS += self.Gun[0].POINTS
        self.Gun.append(Weapons.ChirurgeonStools(A=self.A, S=self.S))
        self.POINTS += self.Gun[1].POINTS


class Imagifier(Infantry, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.ImagifierBoltgun)
        self.POINTS = 45
        self.S = 3
        self.T = 3
        self.W = 4
        self.A = 3
        self.Ld = 8
        self.Gun.append(Weapons.Boltgun())
        self.POINTS += self.Gun[0].POINTS
        self.Gun.append(Weapons.FragGrenade())
        self.POINTS += self.Gun[1].POINTS
        self.Gun.append(Weapons.KrakGrenades())
        self.POINTS += self.Gun[2].POINTS


class Crusader(Infantry, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.CrusaderPowerSword)
        self.POINTS = 9
        self.BS = 4
        self.S = 3
        self.T = 3
        self.A = 2
        self.Sv = 4
        self.InvSv = 3
        self.Gun.append(Weapons.PowerSword(A=self.A, S=self.S))
        self.POINTS += self.Gun[0].POINTS


class DeathCultAssassin(Infantry, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.DeathCultAssassinDeathCultPowerBlades)
        self.POINTS = 13
        self.M = 7
        self.BS = 4
        self.T = 3
        self.A = 4
        self.Sv = 5
        self.Gun.append(Weapons.DeathCultPowerBlades(A=self.A, S=self.S))
        self.POINTS += self.Gun[0].POINTS


class ArcoFlagellant(Infantry, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.ArcoflaggellantArcoFlails)
        self.POINTS = 13
        self.M = 7
        self.WS = 4
        self.BS = 7
        self.T = 3
        self.W = 2
        self.A = 2
        self.Sv = 7
        self.Gun.append(Weapons.ArcoFlails(A=self.A, S=self.S))
        self.POINTS += self.Gun[0].POINTS


class Endurant(ArcoFlagellant):
    def __init__(self):
        super().__init__()
        self.A = 3


class Dominion(Infantry, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.DominionBoltgunBoltPistol)
        self.POINTS = 10
        self.WS = 4
        self.S = 3
        self.T = 3
        self.Gun.append(Weapons.BoltPistol())
        self.POINTS += self.Gun[0].POINTS
        self.Gun.append(Weapons.Boltgun())
        self.POINTS += self.Gun[1].POINTS
        self.Gun.append(Weapons.FragGrenade())
        self.POINTS += self.Gun[2].POINTS
        self.Gun.append(Weapons.KrakGrenades())
        self.POINTS += self.Gun[3].POINTS


class DominionSuperior(Dominion, Sergeant):
    def __init__(self):
        super().__init__()


class Seraphim(Infantry, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.Seraphim2xBoltPistols)
        self.POINTS = 11
        self.M = 12
        self.S = 3
        self.T = 3
        self.Gun.append(Weapons.BoltPistol())
        self.POINTS += self.Gun[0].POINTS
        self.Gun.append(Weapons.BoltPistol())
        self.POINTS += self.Gun[1].POINTS
        self.Gun.append(Weapons.FragGrenade())
        self.POINTS += self.Gun[2].POINTS
        self.Gun.append(Weapons.KrakGrenades())
        self.POINTS += self.Gun[3].POINTS


class SeraphimSuperior(Seraphim, Sergeant):
    def __init__(self):
        super().__init__()


class Exorcist(Vehicle, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.ExorcistMissileLauncherHeavyBolter)
        self.POINTS = 90
        self.WS = 6
        self.S = 7
        self.T = 8
        self.W = 12
        self.Ld = 7
        self.FirstM = 12
        self.SecondM = 6
        self.ThirdM = 4
        self.FirstBS = 3
        self.SecondBS = 4
        self.ThirdBS = 5
        self.FirstA = 3
        self.SecondA = 'D3'
        self.ThirdA = 1
        self.FirstW = 7
        self.SecondW = 4
        self.damage_update(M=True, A=True, BS=True)
        self.Gun.append(Weapons.ExorcistMissileLauncher())
        self.POINTS += self.Gun[0].POINTS
        self.Gun.append(Weapons.HeavyBolter())
        self.POINTS += self.Gun[1].POINTS


class Mortifier(Vehicle, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.Mortifier2xHeavyBolters2xPenitentFlails)
        self.POINTS = 36
        self.M = 9
        self.S = 5
        self.T = 5
        self.W = 5
        self.Sv = 4
        self.Gun.append(Weapons.HeavyBolter())
        self.POINTS += self.Gun[0].POINTS
        self.Gun.append(Weapons.HeavyBolter())
        self.POINTS += self.Gun[1].POINTS
        self.Gun.append(Weapons.PenitentFlail(A=self.A, S=self.S))
        self.POINTS += self.Gun[2].POINTS
        self.Gun.append(Weapons.PenitentFlail(A=self.A, S=self.S))
        self.POINTS += self.Gun[3].POINTS


class Anchorite(Mortifier):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.Anchorite2xHeavyBolters2xPenitentFlails)
        self.POINTS = 42
        self.Sv = 3


class Retributor(Infantry, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.RetributorBoltgunBoltPistol)
        self.POINTS = 10
        self.WS = 4
        self.S = 3
        self.T = 3
        self.Gun.append(Weapons.BoltPistol())
        self.POINTS += self.Gun[0].POINTS
        self.Gun.append(Weapons.Boltgun())
        self.POINTS += self.Gun[1].POINTS
        self.Gun.append(Weapons.FragGrenade())
        self.POINTS += self.Gun[2].POINTS
        self.Gun.append(Weapons.KrakGrenades())
        self.POINTS += self.Gun[3].POINTS


class RetriibutorSuperior(Retributor, Sergeant):
    def __init__(self):
        super().__init__()


class PenitentEngine(Vehicle, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.PenitentEngine2xHeavyFlamers)
        self.POINTS = 28
        self.M = 7
        self.WS = 4
        self.BS = 5
        self.S = 5
        self.T = 5
        self.W = 5
        self.Sv = 4
        self.Gun.append(Weapons.HeavyFlamer())
        self.POINTS += self.Gun[0].POINTS
        self.Gun.append(Weapons.HeavyFlamer())
        self.POINTS += self.Gun[1].POINTS
        self.Gun.append(Weapons.PenitentFlail())
        self.POINTS += self.Gun[2].POINTS
        self.Gun.append(Weapons.PenitentFlail())
        self.POINTS += self.Gun[3].POINTS


class SororitasRhino(Vehicle, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.SororitasRhinoStormBolter)
        self.POINTS = 65
        self.WS = 6
        self.W = 10
        self.FirstM = 12
        self.SecondM = 6
        self.ThirdM = 3
        self.FirstBS = 3
        self.SecondBS = 4
        self.ThirdBS = 5
        self.FirstA = 3
        self.SecondA = 'D3'
        self.ThirdA = 1
        self.FirstW = 6
        self.SecondW = 3
        self.damage_update(M=True, A=True, BS=True)
        self.Gun.append(Weapons.StormBolter())
        self.POINTS += self.Gun[0].POINTS


class Immolator(Vehicle, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.ImmolatorImmolationFlamersHeavyBolter)
        self.POINTS = 70
        self.WS = 6
        self.W = 10
        self.FirstM = 12
        self.SecondM = 6
        self.ThirdM = 3
        self.FirstBS = 3
        self.SecondBS = 4
        self.ThirdBS = 5
        self.FirstA = 3
        self.SecondA = 'D3'
        self.ThirdA = 1
        self.FirstW = 6
        self.SecondW = 3
        self.damage_update(M=True, A=True, BS=True)
        self.Gun.append(Weapons.ImmolationFlamers())
        self.POINTS += self.Gun[0].POINTS
        self.Gun.append(Weapons.HeavyBolter())
        self.POINTS += self.Gun[1].POINTS
