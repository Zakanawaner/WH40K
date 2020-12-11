from shapely.geometry import Point
from Messages import Messages
import numpy


class Model:
    def __init__(self):
        self.SquadPosition = -1
        self.ModelPosition = -1
        self.TeamPosition = -1
        self.Points = 0
        self.M = 0
        self.WS = 0
        self.BS = 0
        self.S = 0
        self.T = 0
        self.W = 0
        self.A = 0
        self.Ld = 0
        self.Sv = 0
        self.InvSv = 0
        self.Gun = []
        self.Psychic = []

    def info(self):
        print('Name: ', self.__class__.__name__)
        print('Points: ', self.Points)
        print('Stats: ',
              'M:' + str(self.M) + '"',
              'WS:' + str(self.WS) + '+',
              'BS:' + str(self.BS) + '+',
              'S:' + str(self.S),
              'T:' + str(self.T),
              'W:' + str(self.W),
              'A:' + str(self.A),
              'Ld:' + str(self.Ld),
              'Sv:' + str(self.Sv) + '+',
              'InvSv:' + str(self.InvSv) + '+')
        print('Weapons: ')
        for gun in self.Gun:
            print('\t' + gun.__class__.__name__ + '->',
                  'Points:' + str(gun.Points),
                  'Range:' + str(gun.RANGE),
                  'A:' + str(gun.A),
                  'S:' + str(gun.S),
                  'AP:' + str(gun.AP),
                  'D:' + str(gun.D),
                  'Ability:' + str(gun.ABILITY),
                  'Type:' + str(gun.TYPE))


class Unit:
    def __init__(self, Power, UnitsForIncrement, AddedPower, MaxUnits):
        self.CoherencyRange = None
        self.Units = []
        self.Abilities = []
        self.Keywords = []
        self.FactionKeywords = []
        self.Points = 0
        self.SquadPosition = -1
        self.TeamPosition = -1
        self.Power = Power
        self.PowerStage = -1
        self.UnitsForIncrement = UnitsForIncrement
        self.PowerAdded = AddedPower
        self.MaxUnits = MaxUnits

    def calculate_points(self):
        self.Points = 0
        for unit in self.Units:
            self.Points += unit.Points

    def add_soldier(self, unit):
        if len(self.Units) < self.MaxUnits:
            self.Units.append(unit)
            if self.UnitsForIncrement is not None:
                for i in range(len(self.UnitsForIncrement)):
                    if len(self.Units) >= self.UnitsForIncrement[i] and i > self.PowerStage:
                        self.Power += self.PowerAdded[i]
                        self.PowerStage = i
                        break
            self.calculate_points()
        else:
            print(Messages.MaxSoldiers)

    def info(self):
        print('Name: ', self.__class__.__name__)
        print('Points: ', self.Points)
        print('Power: ', self.Power)
        print('Models: ')
        [print('\t' + str(i) + ': ' + model.__class__.__name__) for i, model in enumerate(self.Units)]
        print('Abilities: ')
        [print('\t' + str(i) + ': ' + ability) for i, ability in enumerate(self.Abilities)]
        print('FactionKeywords: ')
        [print('\t' + str(i) + ': ' + factionKeyword) for i, factionKeyword in enumerate(self.FactionKeywords)]
        print('Keywords: ')
        [print('\t' + str(i) + ': ' + keyword) for i, keyword in enumerate(self.Keywords)]
        print('Available Methods: ')
        [print('\t' + func + '()') for func in dir(self) if callable(getattr(self, func)) and '__' not in func]

    def init_positions_randomly(self, x, y):
        self.Units[0].set_position(x=0 + x, y=0 + y)
        self.CoherencyRange = Point(self.Units[0].Position.x,
                                    self.Units[0].Position.y).buffer(self.Units[0].BodyInfo['radius'] + 2)
        for index, unit in enumerate(self.Units):
            if index > 0:
                minX, minY, maxX, maxY = self.CoherencyRange.bounds
                ok = False
                overlap = True
                pnt = None
                while not ok or overlap:
                    pnt = Point(numpy.random.uniform(minX, maxX), numpy.random.uniform(minY, maxY))
                    if self.CoherencyRange.contains(pnt):
                        ok = True
                        overlap = False
                        for point in self.Units:
                            if not point.Body.intersection(Point(pnt.x,
                                                                 pnt.y).buffer(self.Units[index].BodyInfo['radius'])).is_empty:
                                overlap = True
                self.Units[index].set_position(x=pnt.x, y=pnt.y)
                auxCohesion = Point(self.Units[index].Position.x,
                                    self.Units[index].Position.y).buffer(self.Units[index].BodyInfo['radius'] + 2)
                self.CoherencyRange = self.CoherencyRange.union(auxCohesion)

    def update_coherency_range(self, index):
        if index == 0:
            self.CoherencyRange = Point(self.Units[0].Position.x,
                                        self.Units[0].Position.y).buffer(self.Units[0].BodyInfo['radius'] + 2)
        else:
            auxCoherency = Point(self.Units[index].Position.x,
                                 self.Units[index].Position.y).buffer(self.Units[index].BodyInfo['radius'] + 2)
            self.CoherencyRange = self.CoherencyRange.union(auxCoherency)

    def move_models(self, board, target):
        self.Units[0].move(model=self.Units[0],
                           objectsBoard=board.Objects,
                           target=target,
                           isSergeant=True)  # For testing
        overlap = []
        for unit in self.Units:
            overlap.append(unit.Body)
        self.update_coherency_range(0)
        if len(self.Units) > 1:
            for i, model in enumerate(self.Units[1:]):
                overlap.pop(i+1)
                model.move(model=model,
                           coherencyRegion=self.CoherencyRange,
                           objectsBoard=board.Objects,
                           overlapRange=overlap,
                           target=target)
                self.update_coherency_range(i+1)
                overlap = []
                for unit in self.Units:
                    overlap.append(unit.Body)


class Army:
    def __init__(self, player):
        self.Points = 0
        self.HQ = 0
        self.Troops = 0
        self.Elites = 0
        self.FastAttack = 0
        self.HeavySupport = 0
        self.DedicatedTransport = 0
        self.Fortification = 0
        self.Squads = []
        self.Player = player

    def calculate_points(self, show=False):
        self.Points = 0
        for squad in self.Squads:
            self.Points += squad.Points
        print(self.Points) if show else None

    def add_squad(self, Squad):
        self.Squads.append(Squad)
        self.HQ += 1 if Squad.SquadType == 'HQ' else 0
        self.Troops += 1 if Squad.SquadType == 'Troops' else 0
        self.Elites += 1 if Squad.SquadType == 'Elites' else 0
        self.FastAttack += 1 if Squad.SquadType == 'FastAttack' else 0
        self.HeavySupport += 1 if Squad.SquadType == 'HeavySupport' else 0
        self.DedicatedTransport += 1 if Squad.SquadType == 'DedicatedTransport' else 0
        self.Fortification += 1 if Squad.SquadType == 'Fortification' else 0
        self.assign_indexes()
        self.calculate_points()

    def assign_indexes(self):
        self.Squads[len(self.Squads)-1].SquadPosition = len(self.Squads) - 1
        self.Squads[len(self.Squads)-1].TeamPosition = self.Player
        for i, model in enumerate(self.Squads[len(self.Squads)-1].Units):
            model.ModelPosition = i
            model.SquadPosition = len(self.Squads) - 1
            model.TeamPosition = self.Player

    def move_squads(self, board, squad, target):
        self.Squads[squad].move_models(board, target)

    def info(self):
        pass  # TODO
