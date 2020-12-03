from shapely.geometry import Polygon, Point
import numpy


class Model:
    def __init__(self):
        self.SquadPosition = -1
        self.ModelPosition = -1

    def info(self):
        print('Name: ', self.__class__.__name__)
        print('Points: ', self.POINTS)
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
                  'Points:' + str(gun.POINTS),
                  'Range:' + str(gun.RANGE),
                  'A:' + str(gun.A),
                  'S:' + str(gun.S),
                  'AP:' + str(gun.AP),
                  'D:' + str(gun.D),
                  'Ability:' + str(gun.ABILITY),
                  'Type:' + str(gun.TYPE))


class Unit:
    def __init__(self):
        self.CoherencyRange = None
        self.Units = []
        self.Points = 0
        self.SquadPosition = -1

    def info(self):
        print('Name: ', self.__class__.__name__)
        print('Points: ', self.Points)
        print('Power: ', self.Power)
        print('Models: ')
        [print('\t' + str(i) + ': ' + model.__class__.__name__) for i, model in enumerate(self.Units)]
        print('Abilities: ')
        [print('\t' + str(i) + ': ' + ability) for i, ability in enumerate(self.ABILITIES)]
        print('FactionKeywords: ')
        [print('\t' + str(i) + ': ' + factionKeyword) for i, factionKeyword in enumerate(self.FactionKeywords)]
        print('Keywords: ')
        [print('\t' + str(i) + ': ' + keyword) for i, keyword in enumerate(self.Keywords)]
        print('Available Methods: ')
        [print('\t' + func + '()') for func in dir(self) if callable(getattr(self, func)) and '__' not in func]

    def init_positions_randomly(self, offset):
        self.Units[0].set_position(x=0 + offset, y=0 + offset)
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

    def move_models(self, board):
        self.Units[0].move(newPosition=(6, 0), objectsBoard=board.Objects)  # For testing
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
                           overlapRange=overlap)
                self.update_coherency_range(i+1)
                overlap = []
                for unit in self.Units:
                    overlap.append(unit.Body)
