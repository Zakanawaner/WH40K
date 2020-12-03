class Orders:
    OurMartyredLady = 'OUR MARTYRED LADY'
    ValorousHeart = 'VALOROUS HEART'
    BloodyRose = 'BLOODY ROSE'
    EbonChalice = 'EBON CHALICE'
    ArgentShroud = 'ARGENT SHROUD'
    SacredRose = 'SACRED ROSE'


class UnboundArmy:
    def __init__(self):
        self.Points = 0
        self.HQ = 0
        self.Troops = 0
        self.Elites = 0
        self.FastAttack = 0
        self.HeavySupport = 0
        self.DedicatedTransport = 0
        self.Fortification = 0
        self.OrderConviction = ''
        self.Warlord = -1  # Index of the squad that is Warlord
        self.Squads = []

    def calculate_points(self, show=False):
        self.Points = 0
        for squad in self.Squads:
            self.Points += squad.Points
        print(self.Points) if show else None

    def add_squad(self, Squad, isWarlord=False):
        Squad.SquadPosition = len(self.Squads)
        self.Squads.append(Squad)
        self.HQ += 1 if Squad.SquadType == 'HQ' else 0
        self.Troops += 1 if Squad.SquadType == 'Troops' else 0
        self.Elites += 1 if Squad.SquadType == 'Elites' else 0
        self.FastAttack += 1 if Squad.SquadType == 'FastAttack' else 0
        self.HeavySupport += 1 if Squad.SquadType == 'HeavySupport' else 0
        self.DedicatedTransport += 1 if Squad.SquadType == 'DedicatedTransport' else 0
        self.Fortification += 1 if Squad.SquadType == 'Fortification' else 0
        if isWarlord:
            self.Warlord = len(self.Squads) - 1
        self.calculate_points()
