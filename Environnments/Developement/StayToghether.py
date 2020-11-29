# Environments for learning to move on the board keeping the unit coherency.
#   -StayTogether: Board 120 x 60. Only for one Squad, that will be deployed in the center of the board.
#                  The squad doesnt win, only moves and receives the reward after the movement
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
        # Broken rules punishment
        self.BoundaryPunishment = -1
        self.BadPunishment = -10
        # Rewards
        self.WinningReward = 10

    # Start the game
    def start(self, RedArmy):
        self.i = 0
        self.init_positions(RedArmy)
        return [self.get_state(i) for i in range(len(RedArmy.Units))]

    # The environment deploys the squad in the center of the board, keeping the unit coherency
    def init_positions(self, RedArmy):
        self.RedArmyBodies = []
        RedArmy.Units[0].set_position(x=self.maxX / 2, y=self.maxY / 2)
        cohesion = Polygon([[RedArmy.Units[0].Position.x - 3, RedArmy.Units[0].Position.y - 3],
                            [RedArmy.Units[0].Position.x - 3, RedArmy.Units[0].Position.y + 3],
                            [RedArmy.Units[0].Position.x + 3, RedArmy.Units[0].Position.y + 3],
                            [RedArmy.Units[0].Position.x + 3, RedArmy.Units[0].Position.y + 3]])
        for index, unit in enumerate(RedArmy.Units):
            if index > 0:
                minX, minY, maxX, maxY = cohesion.bounds
                ok = False
                overlap = True
                pnt = None
                while not ok or overlap:
                    pnt = Point(numpy.random.uniform(minX, maxX), numpy.random.uniform(minY, maxY))
                    if cohesion.contains(pnt):
                        ok = True
                        overlap = False
                        for point in self.RedArmyBodies:
                            if not point.intersection(Point(pnt.x,
                                                            pnt.y).buffer(RedArmy.Units[index].BodyInfo['radius'])).is_empty:
                                overlap = True
                RedArmy.Units[index].set_position(x=pnt.x, y=pnt.y)
                auxCohesion = Polygon([[RedArmy.Units[index].Position.x - 3, RedArmy.Units[index].Position.y - 3],
                                       [RedArmy.Units[index].Position.x - 3, RedArmy.Units[index].Position.y + 3],
                                       [RedArmy.Units[index].Position.x + 3, RedArmy.Units[index].Position.y + 3],
                                       [RedArmy.Units[index].Position.x + 3, RedArmy.Units[index].Position.y + 3]])
                cohesion = cohesion.union(auxCohesion)
            self.RedArmyBodies.append(RedArmy.Units[index].Body)

    # For every new position, the environment checks if it respects the coherency rule. If not, it applies a punishment.
    # This method is called when the training loop calls the step()
    def check_new_position(self, RedArmy, Coordinates, index):
        overlap = False
        ok = False
        SoldierPosition = Point(RedArmy.Units[index].Position.x,
                                RedArmy.Units[index].Position.y).buffer(RedArmy.Units[index].BodyInfo['radius'])
        NewPosition = Point(Coordinates.tolist()[0][0],
                            Coordinates.tolist()[0][1]).buffer(RedArmy.Units[index].BodyInfo['radius'])
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
                    if cohesion.contains(NewPosition) \
                            and (SoldierPosition.distance(NewPosition) <= RedArmy.Units[index].M):
                        ok = True
                        break
        if ok and not overlap:
            reward = self.WinningReward
            RedArmy.Units[index].set_position(x=NewPosition.x, y=NewPosition.y)
            self.RedArmyBodies[index] = RedArmy.Units[index].Body
        else:
            reward = self.BadPunishment
        return reward

    # Called to make a movement from an agent in the environment
    def step(self, Coordinates, index, Army):
        Army.Units[index].Position.x = Coordinates.tolist()[0][0]
        Army.Units[index].Position.y = Coordinates.tolist()[0][1]
        reward = self.check_boundaries(index, Army)
        reward += self.check_new_position(Army, Coordinates, index)
        return self.get_state(index), reward

    # Returns the state for the agent
    def get_state(self, index):
        return [self.RedArmyBodies[index - 1].centroid.x, self.RedArmyBodies[index - 1].centroid.y,
                self.RedArmyBodies[index].centroid.x, self.RedArmyBodies[index].centroid.y]

    # Check the board bounds to ensure that no illegal movement is made. And if it is,
    # it applies the correction and the punishment to the agent
    def check_boundaries(self, index, Army):
        reward = 0
        if Army.Units[index].Position.x > self.maxX:
            Army.Units[index].Position.x = self.maxX
            reward = self.BoundaryPunishment
        if Army.Units[index].Position.x < self.minX:
            Army.Units[index].Position.x = self.minX
            reward = self.BoundaryPunishment
        if Army.Units[index].Position.y > self.maxY:
            Army.Units[index].Position.y = self.maxY
            reward = self.BoundaryPunishment
        if Army.Units[index].Position.y < self.minY:
            Army.Units[index].Position.y = self.minY
            reward = self.BoundaryPunishment
        return reward

    # If plot is called in the training loop, the environment will save the game state in a graph.
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
        plt.savefig('./Images/FirstApproach/GameHistory/StayTogether{}.png'.format(self.i))
        plt.close(fig)
