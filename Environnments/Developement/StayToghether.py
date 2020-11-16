import numpy
import matplotlib.pyplot as plt
from shapely.geometry import Point


class Environment:
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
        self.BoundaryPunishment = 0
        # Rewards
        self.WinningReward = 1

    def start(self, RedArmy):
        self.i = 0
        self.init_positions(RedArmy)
        return self.get_state()

    def init_positions(self, RedArmy):
        self.RedArmyBodies = []
        for index, unit in enumerate(RedArmy.Units):
            RedArmy.Units[index].set_position(x=numpy.random.uniform(0, 30), y=numpy.random.uniform(0, 60))
            body = Point(RedArmy.Units[index].Position.x,
                         RedArmy.Units[index].Position.y).buffer(RedArmy.Units[index].BodyInfo['radius'])
            self.RedArmyBodies.append(body)

    def step(self, Action, soldier, Army, redTurn):
        direction = 15 * Action
        Army.Units[soldier].move(6, direction=direction)
        reward = self.check_boundaries(soldier, Army, redTurn)
        return self.get_state(), reward

    def update_board(self, soldier, Army, redTurn):
        body = Point(Army.Units[soldier].Position.x,
                     Army.Units[soldier].Position.y).buffer(Army.Units[soldier].BodyInfo['radius'])
        if redTurn:
            self.RedArmyBodies[soldier] = body

    def get_state(self):
        state = []
        for body in self.RedArmyBodies:
            state.append(body.centroid.x)
            state.append(body.centroid.y)
        return state

    def calculate_r(self, Army, redTurn):
        done = False
        reward = 0
        return reward, done

    def check_boundaries(self, soldier, Army, redTurn):
        reward = 0
        if Army.Units[soldier].Position.x > 120.0:
            Army.Units[soldier].Position.x = 120.0
            reward = self.BoundaryPunishment
        if Army.Units[soldier].Position.x < 0.0:
            Army.Units[soldier].Position.x = 0.0
            reward = self.BoundaryPunishment
        if Army.Units[soldier].Position.y > 60.0:
            Army.Units[soldier].Position.y = 60.0
            reward = self.BoundaryPunishment
        if Army.Units[soldier].Position.y < 0.0:
            Army.Units[soldier].Position.y = 0.0
            reward = self.BoundaryPunishment
        self.update_board(soldier, Army, redTurn)
        return reward

    def plot(self, RedArmy, GreenArmy):
        self.i += 1
        fig = plt.figure()
        ax1 = fig.add_subplot(1, 1, 1)
        ax1.clear()
        ax1.set_aspect(1)
        ax1.set_xlim([0, 120])
        ax1.set_ylim([0, 60])
        ax1.add_patch(plt.Circle((60.0, 30.0), 10.0, color='y', alpha=0.3))
        for unit in RedArmy.Units:
            ax1.add_patch(plt.Circle((unit.Position.x, unit.Position.y), unit.BodyInfo['radius'], color='r', alpha=0.3))
        for unit in GreenArmy.Units:
            ax1.add_patch(plt.Circle((unit.Position.x, unit.Position.y), unit.BodyInfo['radius'], color='g', alpha=0.3))
        plt.savefig('./Images/FirstApproach/GameHistory/{}.png'.format(self.i))
        plt.close(fig)


class StayTogether(Environment):
    def __init__(self):
        super().__init__()
