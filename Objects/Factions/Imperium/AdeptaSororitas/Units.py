from Objects.Common.Armies import Infantry, Vehicle, Sergeant
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
        self.Gun1 = Weapons.BoltPistol()
        self.POINTS += self.Gun1.POINTS
        self.Gun2 = Weapons.ChainSword()
        self.POINTS += self.Gun2.POINTS
        self.Gun3 = Weapons.FragGrenade()
        self.POINTS += self.Gun3.POINTS
        self.Gun4 = Weapons.KrakGrenades()
        self.POINTS += self.Gun4.POINTS


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
        self.Gun1 = Weapons.TheArdentBlade()
        self.POINTS += self.Gun1.POINTS


class TriumphOfSaintKatherine(Vehicle, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.TheTriumphofSaintKatherine)
        self.POINTS = 0
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
        self.Gun1 = Weapons.BoltPistol()
        self.POINTS += self.Gun1.POINTS
        self.Gun2 = Weapons.BoltPistol()
        self.POINTS += self.Gun2.POINTS
        self.Gun3 = Weapons.BoltPistol()
        self.POINTS += self.Gun3.POINTS
        self.Gun4 = Weapons.BoltPistol()
        self.POINTS += self.Gun4.POINTS
        self.Gun5 = Weapons.BoltPistol()
        self.POINTS += self.Gun5.POINTS
        self.Gun6 = Weapons.BoltPistol()
        self.POINTS += self.Gun6.POINTS
        self.Gun7 = Weapons.TheMartyrSword()
        self.POINTS += self.Gun7.POINTS
        self.Gun8 = Weapons.RelicWeapons()
        self.POINTS += self.Gun8.POINTS
        self.Gun9 = Weapons.FragGrenade()
        self.POINTS += self.Gun9.POINTS
        self.Gun10 = Weapons.KrakGrenades()
        self.POINTS += self.Gun10.POINTS


class JunithEruita(Vehicle, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.JunithEruita)
        self.POINTS = 0
        self.M = 10
        self.WS = 2
        self.BS = 2
        self.S = 3
        self.W = 7
        self.A = 4
        self.Ld = 9
        self.Gun1 = Weapons.HeavyFlamer()
        self.POINTS += self.Gun1.POINTS
        self.Gun2 = Weapons.HeavyFlamer()
        self.POINTS += self.Gun2.POINTS
        self.Gun3 = Weapons.TheMaceOfCastigation()
        self.POINTS += self.Gun3.POINTS


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
        self.Gun1 = Weapons.AutoGun()
        self.POINTS += self.Gun1.POINTS
        self.Gun2 = Weapons.LasPistol()
        self.POINTS += self.Gun2.POINTS
        self.Gun3 = Weapons.ChainSword()
        self.POINTS += self.Gun3.POINTS
        self.Gun4 = Weapons.FragGrenade()
        self.POINTS += self.Gun4.POINTS
        self.Gun5 = Weapons.KrakGrenades()
        self.POINTS += self.Gun5.POINTS


class BattleSister(Infantry, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.BattleSisterBoltgunBoltPistol)
        self.POINTS = 0
        self.WS = 4
        self.S = 3
        self.T = 3
        self.Gun1 = Weapons.BoltPistol()
        self.POINTS += self.Gun1.POINTS
        self.Gun2 = Weapons.Boltgun()
        self.POINTS += self.Gun2.POINTS
        self.Gun3 = Weapons.FragGrenade()
        self.POINTS += self.Gun3.POINTS
        self.Gun4 = Weapons.KrakGrenades()
        self.POINTS += self.Gun4.POINTS
        self.HasBoltGun = True
        self.HasSimulacrumImperialis = False


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
        self.Gun1 = Weapons.LasPistol()
        self.POINTS += self.Gun1.POINTS
        self.Gun2 = Weapons.ChainSword()
        self.POINTS += self.Gun2.POINTS


class GeminaeSuperia(Infantry, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.GeminaeSuperiaBoltPistolPowerSword)
        self.POINTS = 0
        self.M = 12
        self.S = 3
        self.T = 3
        self.W = 2
        self.A = 3
        self.Ld = 9
        self.Gun1 = Weapons.BoltPistol()
        self.POINTS += self.Gun1.POINTS
        self.Gun2 = Weapons.PowerSword()
        self.POINTS += self.Gun2.POINTS
        self.Gun3 = Weapons.FragGrenade()
        self.POINTS += self.Gun3.POINTS
        self.Gun4 = Weapons.KrakGrenades()
        self.POINTS += self.Gun4.POINTS


class RepentiaSuperior(Infantry, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.RepentiaSuperiorNeuralWhips)
        self.POINTS = 0
        self.S = 3
        self.T = 3
        self.W = 4
        self.A = 4
        self.Ld = 8
        self.Gun1 = Weapons.NeuralWhips()
        self.POINTS += self.Gun1.POINTS
        self.Gun2 = Weapons.FragGrenade()
        self.POINTS += self.Gun2.POINTS
        self.Gun3 = Weapons.KrakGrenades()
        self.POINTS += self.Gun3.POINTS


class SisterRepentia(Infantry, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.SisterRepentiaPenitentEviscerator)
        self.POINTS = 0
        self.S = 3
        self.T = 3
        self.A = 2
        self.Ld = 8
        self.Sv = 7
        self.Gun1 = Weapons.PenitentEviscerator()
        self.POINTS += self.Gun1.POINTS


class Celestian(Infantry, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.CelestianBoltgunBoltPistol)
        self.POINTS = 0
        self.S = 3
        self.T = 3
        self.A = 2
        self.Ld = 8
        self.Gun1 = Weapons.BoltPistol()
        self.POINTS += self.Gun1.POINTS
        self.Gun2 = Weapons.Boltgun()
        self.POINTS += self.Gun2.POINTS
        self.Gun3 = Weapons.FragGrenade()
        self.POINTS += self.Gun3.POINTS
        self.Gun4 = Weapons.KrakGrenades()
        self.POINTS += self.Gun4.POINTS


class CelestianSuperior(Celestian, Sergeant):
    def __init__(self):
        super().__init__()


class Zephyrim(Infantry, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.ZephyrimBoltPistolPowerSword)
        self.POINTS = 0
        self.M = 12
        self.S = 3
        self.T = 3
        self.A = 2
        self.Ld = 8
        self.Gun1 = Weapons.BoltPistol()
        self.POINTS += self.Gun1.POINTS
        self.Gun2 = Weapons.PowerSword()
        self.POINTS += self.Gun2.POINTS
        self.Gun3 = Weapons.FragGrenade()
        self.POINTS += self.Gun3.POINTS
        self.Gun4 = Weapons.KrakGrenades()
        self.POINTS += self.Gun4.POINTS


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
        self.Gun1 = Weapons.BoltPistol()
        self.POINTS += self.Gun1.POINTS
        self.Gun2 = Weapons.Dialogusstaff()
        self.POINTS += self.Gun2.POINTS


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
        self.Gun1 = Weapons.BoltPistol()
        self.POINTS += self.Gun1.POINTS
        self.Gun2 = Weapons.ChirurgeonStools()
        self.POINTS += self.Gun2.POINTS


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
        self.Gun1 = Weapons.Boltgun()
        self.POINTS += self.Gun1.POINTS
        self.Gun2 = Weapons.FragGrenade()
        self.POINTS += self.Gun2.POINTS
        self.Gun3 = Weapons.KrakGrenades()
        self.POINTS += self.Gun3.POINTS


class Crusader(Infantry, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.CrusaderPowerSword)
        self.POINTS = 0
        self.BS = 4
        self.S = 3
        self.T = 3
        self.A = 2
        self.Sv = 4
        self.InvSv = 3
        self.Gun1 = Weapons.PowerSword()
        self.POINTS += self.Gun1.POINTS


class DeathCultAssassin(Infantry, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.DeathCultAssassinDeathCultPowerBlades)
        self.POINTS = 0
        self.M = 7
        self.BS = 4
        self.T = 3
        self.A = 4
        self.Sv = 5
        self.Gun1 = Weapons.DeathCultPowerBlades()
        self.POINTS += self.Gun1.POINTS


class ArcoFlagellant(Infantry, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.ArcoflaggellantArcoFlails)
        self.POINTS = 0
        self.M = 7
        self.WS = 4
        self.BS = 7
        self.T = 3
        self.W = 2
        self.A = 2
        self.Sv = 7
        self.Gun1 = Weapons.ArcoFlails()
        self.POINTS += self.Gun1.POINTS


class Endurant(ArcoFlagellant):
    def __init__(self):
        super().__init__()
        self.A = 3


class Dominion(Infantry, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.DominionBoltgunBoltPistol)
        self.POINTS = 0
        self.WS = 4
        self.S = 3
        self.T = 3
        self.Gun1 = Weapons.BoltPistol()
        self.POINTS += self.Gun1.POINTS
        self.Gun2 = Weapons.Boltgun()
        self.POINTS += self.Gun2.POINTS
        self.Gun3 = Weapons.FragGrenade()
        self.POINTS += self.Gun3.POINTS
        self.Gun4 = Weapons.KrakGrenades()
        self.POINTS += self.Gun4.POINTS


class DominionSuperior(Dominion, Sergeant):
    def __init__(self):
        super().__init__()


class Seraphim(Infantry, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.Seraphim2xBoltPistols)
        self.POINTS = 0
        self.M = 12
        self.S = 3
        self.T = 3
        self.Gun1 = Weapons.BoltPistol()
        self.POINTS += self.Gun1.POINTS
        self.Gun2 = Weapons.BoltPistol()
        self.POINTS += self.Gun2.POINTS
        self.Gun3 = Weapons.FragGrenade()
        self.POINTS += self.Gun3.POINTS
        self.Gun4 = Weapons.KrakGrenades()
        self.POINTS += self.Gun4.POINTS


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
        self.Gun1 = Weapons.ExorcistMissileLauncher()
        self.POINTS += self.Gun1.POINTS
        self.Gun2 = Weapons.HeavyBolter()
        self.POINTS += self.Gun2.POINTS


class Mortifier(Vehicle, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.Mortifier2xHeavyBolters2xPenitentFlails)
        self.POINTS = 0
        self.M = 9
        self.S = 5
        self.T = 5
        self.W = 5
        self.Sv = 4
        self.Gun1 = Weapons.HeavyBolter()
        self.POINTS += self.Gun1.POINTS
        self.Gun2 = Weapons.HeavyBolter()
        self.POINTS += self.Gun2.POINTS
        self.Gun3 = Weapons.PenitentFlail()
        self.POINTS += self.Gun3.POINTS
        self.Gun4 = Weapons.PenitentFlail()
        self.POINTS += self.Gun4.POINTS


class Anchorite(Mortifier):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.Anchorite2xHeavyBolters2xPenitentFlails)
        self.Sv = 3


class Retributor(Infantry, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.RetributorBoltgunBoltPistol)
        self.POINTS = 0
        self.WS = 4
        self.S = 3
        self.T = 3
        self.Gun1 = Weapons.BoltPistol()
        self.POINTS += self.Gun1.POINTS
        self.Gun2 = Weapons.Boltgun()
        self.POINTS += self.Gun2.POINTS
        self.Gun3 = Weapons.FragGrenade()
        self.POINTS += self.Gun3.POINTS
        self.Gun4 = Weapons.KrakGrenades()
        self.POINTS += self.Gun4.POINTS


class RetriibutorSuperior(Retributor, Sergeant):
    def __init__(self):
        super().__init__()


class PenitentEngine(Vehicle, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.PenitentEngine2xHeavyFlamers)
        self.POINTS = 0
        self.M = 7
        self.WS = 4
        self.BS = 5
        self.S = 5
        self.T = 5
        self.W = 5
        self.Sv = 4
        self.Gun1 = Weapons.HeavyFlamer()
        self.POINTS += self.Gun1.POINTS
        self.Gun2 = Weapons.HeavyFlamer()
        self.POINTS += self.Gun2.POINTS
        self.Gun3 = Weapons.PenitentFlail()
        self.POINTS += self.Gun3.POINTS
        self.Gun4 = Weapons.PenitentFlail()
        self.POINTS += self.Gun4.POINTS


class SororitasRhino(Vehicle, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.SororitasRhinoStormBolter)
        self.POINTS = 0
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
        self.Gun1 = Weapons.StormBolter()
        self.POINTS += self.Gun1.POINTS


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
        self.Gun1 = Weapons.ImmolationFlamers()
        self.POINTS += self.Gun1.POINTS
        self.Gun2 = Weapons.HeavyBolter()
        self.POINTS += self.Gun2.POINTS
