from Objects.Generic.Models import Army


class Orders:
    OurMartyredLady = 'OUR MARTYRED LADY'
    ValorousHeart = 'VALOROUS HEART'
    BloodyRose = 'BLOODY ROSE'
    EbonChalice = 'EBON CHALICE'
    ArgentShroud = 'ARGENT SHROUD'
    SacredRose = 'SACRED ROSE'


class UnboundArmy(Army):
    def __init__(self, player):
        super().__init__(player)
        self.OrderConviction = ''
        self.Warlord = -1  # Index of the squad that is Warlord

    def assign_warlord(self, index):
        self.Warlord = index
