import numpy
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon


class StayTogether:
    def __init__(self):
        # Create armies
        self.RedArmyUnits = []
        self.RedArmyBodies = []
        # Create board
        self.minX = 0.0
        self.maxX = 120.0
        self.minY = 0.0
        self.maxY = 60.0
        self.i = 0
        # broken rules punishment
        self.BoundaryPunishment = -1
        self.BadPunishment = -10
        # Rewards
        self.WinningReward = 10

    def start(self, RedArmy):
        self.i = 0
        self.init_positions(RedArmy)
        return [self.get_state(i) for i in range(len(RedArmy.Units))]

    def init_positions(self, RedArmy):
        self.RedArmyBodies = []
        RedArmy.Units[0].set_position(x=self.maxX/2, y=self.maxY/2)
        cohesion = Polygon([[RedArmy.Units[0].Position.x - 3, RedArmy.Units[0].Position.y - 3],
                            [RedArmy.Units[0].Position.x - 3, RedArmy.Units[0].Position.y + 3],
                            [RedArmy.Units[0].Position.x + 3, RedArmy.Units[0].Position.y + 3],
                            [RedArmy.Units[0].Position.x + 3, RedArmy.Units[0].Position.y + 3]])
        for index, unit in enumerate(RedArmy.Units):
            if index > 0:
                minX, minY, maxX, maxY = cohesion.bounds
                ok = False
                overlap = True
                while not ok or overlap:
                    pnt = Point(numpy.random.uniform(minX, maxX), numpy.random.uniform(minY, maxY))
                    if cohesion.contains(pnt):
                        ok = True
                        overlap = False
                        for point in self.RedArmyBodies:
                            if not point.intersection(Point(pnt.x, pnt.y).buffer(RedArmy.Units[index].BodyInfo['radius'])).is_empty:
                                overlap = True
                RedArmy.Units[index].set_position(x=pnt.x, y=pnt.y)
                auxCohesion = Polygon([[RedArmy.Units[index].Position.x - 3, RedArmy.Units[index].Position.y - 3],
                                       [RedArmy.Units[index].Position.x - 3, RedArmy.Units[index].Position.y + 3],
                                       [RedArmy.Units[index].Position.x + 3, RedArmy.Units[index].Position.y + 3],
                                       [RedArmy.Units[index].Position.x + 3, RedArmy.Units[index].Position.y + 3]])
                cohesion = cohesion.union(auxCohesion)
            body = Point(RedArmy.Units[index].Position.x,
                         RedArmy.Units[index].Position.y).buffer(RedArmy.Units[index].BodyInfo['radius'])
            self.RedArmyBodies.append(body)

    def check_new_position(self, RedArmy, Coordinates, index):
        overlap = False
        ok = False
        SoldierPosition = Point(RedArmy.Units[index].Position.x, RedArmy.Units[index].Position.y).buffer(RedArmy.Units[index].BodyInfo['radius'])
        NewPosition = Point(Coordinates.tolist()[0][0], Coordinates.tolist()[0][1]).buffer(RedArmy.Units[index].BodyInfo['radius'])
        for i, point in enumerate(self.RedArmyBodies):
            if not point.intersection(NewPosition).is_empty and i != index:
                overlap = True
                break
        if not overlap:
            cohesion = Polygon([[RedArmy.Units[0].Position.x - 3, RedArmy.Units[0].Position.y - 3],
                                [RedArmy.Units[0].Position.x - 3, RedArmy.Units[0].Position.y + 3],
                                [RedArmy.Units[0].Position.x + 3, RedArmy.Units[0].Position.y + 3],
                                [RedArmy.Units[0].Position.x + 3, RedArmy.Units[0].Position.y + 3]])
            for index, unit in enumerate(RedArmy.Units):
                if index > 0:
                    if cohesion.contains(NewPosition) and (SoldierPosition.distance(NewPosition) <= RedArmy.Units[index].M):
                        ok = True
                        break
        if ok and not overlap:
            reward = self.WinningReward
            RedArmy.Units[index].set_position(x=NewPosition.x, y=NewPosition.y)
            body = Point(RedArmy.Units[index].Position.x,
                         RedArmy.Units[index].Position.y).buffer(RedArmy.Units[index].BodyInfo['radius'])
            self.RedArmyBodies.append(body)
            self.update_board(index, RedArmy)
        else:
            reward = self.BadPunishment
        return reward

    def step(self, Coordinates, index, Army):
        Army.Units[index].Position.x = Coordinates.tolist()[0][0]
        Army.Units[index].Position.y = Coordinates.tolist()[0][1]
        reward = self.check_boundaries(index, Army)
        reward += self.check_new_position(Army, Coordinates, index)
        return self.get_state(index), reward

    def update_board(self, index, Army):
        body = Point(Army.Units[index].Position.x,
                     Army.Units[index].Position.y).buffer(Army.Units[index].BodyInfo['radius'])
        self.RedArmyBodies[index] = body

    def get_state(self, index):
        return [self.RedArmyBodies[index-1].centroid.x, self.RedArmyBodies[index-1].centroid.y,
                self.RedArmyBodies[index].centroid.x, self.RedArmyBodies[index].centroid.y]

    def check_boundaries(self, index, Army):
        reward = 0
        if Army.Units[index].Position.x > 120.0:
            Army.Units[index].Position.x = 120.0
            reward = self.BoundaryPunishment
        if Army.Units[index].Position.x < 0.0:
            Army.Units[index].Position.x = 0.0
            reward = self.BoundaryPunishment
        if Army.Units[index].Position.y > 60.0:
            Army.Units[index].Position.y = 60.0
            reward = self.BoundaryPunishment
        if Army.Units[index].Position.y < 0.0:
            Army.Units[index].Position.y = 0.0
            reward = self.BoundaryPunishment
        return reward

    def plot(self, RedArmy):
        self.i += 1
        fig = plt.figure()
        ax1 = fig.add_subplot(1, 1, 1)
        ax1.clear()
        ax1.set_aspect(1)
        ax1.set_xlim([0, 120])
        ax1.set_ylim([0, 60])
        for unit in RedArmy.Units:
            ax1.add_patch(plt.Circle((unit.Position.x, unit.Position.y), unit.BodyInfo['radius'], color='r', alpha=0.3))
        plt.savefig('./Images/FirstApproach/GameHistory/{}.png'.format(self.i))
        plt.close(fig)
