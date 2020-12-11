from Objects.Factions.Imperium.Common.Armies import Infantry, Vehicle, Sergeant
from . import Mesh, Weapons


class Canoness(Infantry):
    def __init__(self):
        super().__init__(Mesh.Canoness)
        self.Points = 45
        self.WS = 2
        self.BS = 2
        self.S = 3
        self.T = 3
        self.W = 5
        self.A = 4
        self.Ld = 9
        self.Gun.append(Weapons.BoltPistol())
        self.Points += self.Gun[0].Points
        self.Gun.append(Weapons.ChainSword(A=self.A, S=self.S))
        self.Points += self.Gun[1].Points
        self.Gun.append(Weapons.FragGrenade())
        self.Points += self.Gun[2].Points
        self.Gun.append(Weapons.KrakGrenades())
        self.Points += self.Gun[3].Points


class Celestine(Infantry):
    def __init__(self):
        super().__init__()  # TODO Mesh
        self.Points = 160
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
        self.Points += self.Gun[0].Points


class TriumphOfSaintKatherine(Vehicle):
    def __init__(self):
        super().__init__(Mesh.TheTriumphofSaintKatherine)
        self.Points = 185
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
        self.Points += self.Gun[0].Points
        self.Gun.append(Weapons.BoltPistol())
        self.Points += self.Gun[1].Points
        self.Gun.append(Weapons.BoltPistol())
        self.Points += self.Gun[2].Points
        self.Gun.append(Weapons.BoltPistol())
        self.Points += self.Gun[3].Points
        self.Gun.append(Weapons.BoltPistol())
        self.Points += self.Gun[4].Points
        self.Gun.append(Weapons.BoltPistol())
        self.Points += self.Gun[5].Points
        self.Gun.append(Weapons.TheMartyrSword(A=self.A, S=self.S))
        self.Points += self.Gun[6].Points
        self.Gun.append(Weapons.RelicWeapons(A=self.A, S=self.S))
        self.Points += self.Gun[7].Points
        self.Gun.append(Weapons.FragGrenade())
        self.Points += self.Gun[8].Points
        self.Gun.append(Weapons.KrakGrenades())
        self.Points += self.Gun[9].Points


class JunithEruita(Vehicle):
    def __init__(self):
        super().__init__(Mesh.JunithEruita)
        self.Points = 110
        self.M = 10
        self.WS = 2
        self.BS = 2
        self.S = 3
        self.W = 7
        self.A = 4
        self.Ld = 9
        self.Gun.append(Weapons.HeavyFlamer())
        self.Points += self.Gun[0].Points
        self.Gun.append(Weapons.HeavyFlamer())
        self.Points += self.Gun[1].Points
        self.Gun.append(Weapons.TheMaceOfCastigation(A=self.A, S=self.S))
        self.Points += self.Gun[2].Points


class Missionary(Infantry):
    def __init__(self):
        super().__init__(Mesh.Missionary)
        self.Points = 38
        self.WS = 4
        self.BS = 4
        self.S = 3
        self.T = 3
        self.W = 4
        self.A = 3
        self.Sv = 6
        self.Gun.append(Weapons.AutoGun())
        self.Points += self.Gun[0].Points
        self.Gun.append(Weapons.LasPistol())
        self.Points += self.Gun[1].Points
        self.Gun.append(Weapons.ChainSword(A=self.A, S=self.S))
        self.Points += self.Gun[2].Points
        self.Gun.append(Weapons.FragGrenade())
        self.Points += self.Gun[3].Points
        self.Gun.append(Weapons.KrakGrenades())
        self.Points += self.Gun[4].Points


class BattleSister(Infantry):
    def __init__(self):
        super().__init__(Mesh.BattleSisterBoltgunBoltPistol)
        self.Points = 9
        self.WS = 4
        self.S = 3
        self.T = 3
        self.Gun.append(Weapons.BoltPistol())
        self.Points += self.Gun[0].Points
        self.Gun.append(Weapons.Boltgun())
        self.Points += self.Gun[1].Points
        self.Gun.append(Weapons.FragGrenade())
        self.Points += self.Gun[2].Points
        self.Gun.append(Weapons.KrakGrenades())
        self.Points += self.Gun[3].Points


class SisterSuperior(BattleSister, Sergeant):
    def __init__(self):
        super().__init__()


class Preacher(Infantry):
    def __init__(self):
        super().__init__(Mesh.PreacherLaspistolChainsword)
        self.Points = 30
        self.WS = 4
        self.BS = 4
        self.S = 3
        self.T = 3
        self.W = 4
        self.A = 3
        self.Sv = 6
        self.Gun.append(Weapons.LasPistol())
        self.Points += self.Gun[0].Points
        self.Gun.append(Weapons.ChainSword(A=self.A, S=self.S))
        self.Points += self.Gun[1].Points


class GeminaeSuperia(Infantry):
    def __init__(self):
        super().__init__(Mesh.GeminaeSuperiaBoltPistolPowerSword)
        self.Points = 16
        self.M = 12
        self.S = 3
        self.T = 3
        self.W = 2
        self.A = 3
        self.Ld = 9
        self.Gun.append(Weapons.BoltPistol())
        self.Points += self.Gun[0].Points
        self.Gun.append(Weapons.PowerSword(A=self.A, S=self.S))
        self.Points += self.Gun[1].Points
        self.Gun.append(Weapons.FragGrenade())
        self.Points += self.Gun[2].Points
        self.Gun.append(Weapons.KrakGrenades())
        self.Points += self.Gun[3].Points


class RepentiaSuperior(Infantry):
    def __init__(self):
        super().__init__(Mesh.RepentiaSuperiorNeuralWhips)
        self.Points = 35
        self.S = 3
        self.T = 3
        self.W = 4
        self.A = 4
        self.Ld = 8
        self.Gun.append(Weapons.NeuralWhips(A=self.A, S=self.S))
        self.Points += self.Gun[0].Points
        self.Gun.append(Weapons.FragGrenade())
        self.Points += self.Gun[1].Points
        self.Gun.append(Weapons.KrakGrenades())
        self.Points += self.Gun[2].Points


class SisterRepentia(Infantry):
    def __init__(self):
        super().__init__(Mesh.SisterRepentiaPenitentEviscerator)
        self.Points = 13
        self.S = 3
        self.T = 3
        self.A = 2
        self.Ld = 8
        self.Sv = 7
        self.Gun.append(Weapons.PenitentEviscerator(A=self.A, S=self.S))
        self.Points += self.Gun[0].Points


class Celestian(Infantry):
    def __init__(self):
        super().__init__(Mesh.CelestianBoltgunBoltPistol)
        self.Points = 10
        self.S = 3
        self.T = 3
        self.A = 2
        self.Ld = 8
        self.Gun.append(Weapons.BoltPistol())
        self.Points += self.Gun[0].Points
        self.Gun.append(Weapons.Boltgun())
        self.Points += self.Gun[1].Points
        self.Gun.append(Weapons.FragGrenade())
        self.Points += self.Gun[2].Points
        self.Gun.append(Weapons.KrakGrenades())
        self.Points += self.Gun[3].Points


class CelestianSuperior(Celestian, Sergeant):
    def __init__(self):
        super().__init__()


class Zephyrim(Infantry):
    def __init__(self):
        super().__init__(Mesh.ZephyrimBoltPistolPowerSword)
        self.Points = 13
        self.M = 12
        self.S = 3
        self.T = 3
        self.A = 2
        self.Ld = 8
        self.Gun.append(Weapons.BoltPistol())
        self.Points += self.Gun[0].Points
        self.Gun.append(Weapons.PowerSword(A=self.A, S=self.S))
        self.Points += self.Gun[1].Points
        self.Gun.append(Weapons.FragGrenade())
        self.Points += self.Gun[2].Points
        self.Gun.append(Weapons.KrakGrenades())
        self.Points += self.Gun[3].Points


class ZephyrimSuperior(Zephyrim, Sergeant):
    def __init__(self):
        super().__init__()


class Dialogus(Infantry):
    def __init__(self):
        super().__init__(Mesh.DialogusBoltPistolDialogusStaff)
        self.Points = 35
        self.WS = 4
        self.S = 3
        self.T = 3
        self.W = 4
        self.A = 3
        self.Ld = 8
        self.Gun.append(Weapons.BoltPistol())
        self.Points += self.Gun[0].Points
        self.Gun.append(Weapons.Dialogusstaff(A=self.A, S=self.S))
        self.Points += self.Gun[1].Points


class Hospitaller(Infantry):
    def __init__(self):
        super().__init__(Mesh.HospitallerBoltPistolChirurgeonsTools)
        self.Points = 35
        self.WS = 4
        self.S = 3
        self.T = 3
        self.W = 4
        self.A = 3
        self.Ld = 8
        self.Gun.append(Weapons.BoltPistol())
        self.Points += self.Gun[0].Points
        self.Gun.append(Weapons.ChirurgeonStools(A=self.A, S=self.S))
        self.Points += self.Gun[1].Points


class Imagifier(Infantry):
    def __init__(self):
        super().__init__(Mesh.ImagifierBoltgun)
        self.Points = 45
        self.S = 3
        self.T = 3
        self.W = 4
        self.A = 3
        self.Ld = 8
        self.Gun.append(Weapons.Boltgun())
        self.Points += self.Gun[0].Points
        self.Gun.append(Weapons.FragGrenade())
        self.Points += self.Gun[1].Points
        self.Gun.append(Weapons.KrakGrenades())
        self.Points += self.Gun[2].Points


class Crusader(Infantry):
    def __init__(self):
        super().__init__(Mesh.CrusaderPowerSword)
        self.Points = 9
        self.BS = 4
        self.S = 3
        self.T = 3
        self.A = 2
        self.Sv = 4
        self.InvSv = 3
        self.Gun.append(Weapons.PowerSword(A=self.A, S=self.S))
        self.Points += self.Gun[0].Points


class DeathCultAssassin(Infantry):
    def __init__(self):
        super().__init__(Mesh.DeathCultAssassinDeathCultPowerBlades)
        self.Points = 13
        self.M = 7
        self.BS = 4
        self.T = 3
        self.A = 4
        self.Sv = 5
        self.Gun.append(Weapons.DeathCultPowerBlades(A=self.A, S=self.S))
        self.Points += self.Gun[0].Points


class ArcoFlagellant(Infantry):
    def __init__(self):
        super().__init__(Mesh.ArcoflaggellantArcoFlails)
        self.Points = 13
        self.M = 7
        self.WS = 4
        self.BS = 7
        self.T = 3
        self.W = 2
        self.A = 2
        self.Sv = 7
        self.Gun.append(Weapons.ArcoFlails(A=self.A, S=self.S))
        self.Points += self.Gun[0].Points


class Endurant(ArcoFlagellant, Sergeant):
    def __init__(self):
        super().__init__()
        self.A = 3


class Dominion(Infantry):
    def __init__(self):
        super().__init__(Mesh.DominionBoltgunBoltPistol)
        self.Points = 10
        self.WS = 4
        self.S = 3
        self.T = 3
        self.Gun.append(Weapons.BoltPistol())
        self.Points += self.Gun[0].Points
        self.Gun.append(Weapons.Boltgun())
        self.Points += self.Gun[1].Points
        self.Gun.append(Weapons.FragGrenade())
        self.Points += self.Gun[2].Points
        self.Gun.append(Weapons.KrakGrenades())
        self.Points += self.Gun[3].Points


class DominionSuperior(Dominion, Sergeant):
    def __init__(self):
        super().__init__()


class Seraphim(Infantry):
    def __init__(self):
        super().__init__(Mesh.Seraphim2xBoltPistols)
        self.Points = 11
        self.M = 12
        self.S = 3
        self.T = 3
        self.Gun.append(Weapons.BoltPistol())
        self.Points += self.Gun[0].Points
        self.Gun.append(Weapons.BoltPistol())
        self.Points += self.Gun[1].Points
        self.Gun.append(Weapons.FragGrenade())
        self.Points += self.Gun[2].Points
        self.Gun.append(Weapons.KrakGrenades())
        self.Points += self.Gun[3].Points


class SeraphimSuperior(Seraphim, Sergeant):
    def __init__(self):
        super().__init__()


class Exorcist(Vehicle):
    def __init__(self):
        super().__init__(Mesh.ExorcistMissileLauncherHeavyBolter)
        self.Points = 90
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
        self.Points += self.Gun[0].Points
        self.Gun.append(Weapons.HeavyBolter())
        self.Points += self.Gun[1].Points


class Mortifier(Vehicle):
    def __init__(self):
        super().__init__(Mesh.Mortifier2xHeavyBolters2xPenitentFlails)
        self.Points = 36
        self.M = 9
        self.S = 5
        self.T = 5
        self.W = 5
        self.Sv = 4
        self.Gun.append(Weapons.HeavyBolter())
        self.Points += self.Gun[0].Points
        self.Gun.append(Weapons.HeavyBolter())
        self.Points += self.Gun[1].Points
        self.Gun.append(Weapons.PenitentFlail(A=self.A, S=self.S))
        self.Points += self.Gun[2].Points
        self.Gun.append(Weapons.PenitentFlail(A=self.A, S=self.S))
        self.Points += self.Gun[3].Points


class Anchorite(Mortifier, Sergeant):
    def __init__(self):
        super().__init__()
        self.Points = 42
        self.Sv = 3
        self.update_body(Mesh.Anchorite2xHeavyBolters2xPenitentFlails)


class Retributor(Infantry):
    def __init__(self):
        super().__init__(Mesh.RetributorBoltgunBoltPistol)
        self.Points = 10
        self.WS = 4
        self.S = 3
        self.T = 3
        self.Gun.append(Weapons.BoltPistol())
        self.Points += self.Gun[0].Points
        self.Gun.append(Weapons.Boltgun())
        self.Points += self.Gun[1].Points
        self.Gun.append(Weapons.FragGrenade())
        self.Points += self.Gun[2].Points
        self.Gun.append(Weapons.KrakGrenades())
        self.Points += self.Gun[3].Points


class RetributorSuperior(Retributor, Sergeant):
    def __init__(self):
        super().__init__()  # TODO Mesh info


class PenitentEngine(Vehicle):
    def __init__(self):
        super().__init__(Mesh.PenitentEngine2xHeavyFlamers)
        self.Points = 28
        self.M = 7
        self.WS = 4
        self.BS = 5
        self.S = 5
        self.T = 5
        self.W = 5
        self.Sv = 4
        self.Gun.append(Weapons.HeavyFlamer())
        self.Points += self.Gun[0].Points
        self.Gun.append(Weapons.HeavyFlamer())
        self.Points += self.Gun[1].Points
        self.Gun.append(Weapons.PenitentFlail())
        self.Points += self.Gun[2].Points
        self.Gun.append(Weapons.PenitentFlail())
        self.Points += self.Gun[3].Points


class SororitasRhino(Vehicle):
    def __init__(self):
        super().__init__(Mesh.SororitasRhinoStormBolter)
        self.Points = 65
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
        self.Points += self.Gun[0].Points


class Immolator(Vehicle):
    def __init__(self):
        super().__init__(Mesh.ImmolatorImmolationFlamersHeavyBolter)
        self.Points = 70
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
        self.Points += self.Gun[0].Points
        self.Gun.append(Weapons.HeavyBolter())
        self.Points += self.Gun[1].Points
