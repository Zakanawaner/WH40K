import numpy
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon
import copy


class Environment:
    def __init__(self):
        # Create armies
        self.RedArmyUnits = []
        self.RedArmyBodies = []
        self.GreenArmyUnits = []
        self.GreenArmyBodies = []
        self.redArmyWins = False
        self.greenArmyWins = False
        # Create board
        self.minX = 0.0
        self.maxX = 120.0
        self.minY = 0.0
        self.maxY = 60.0
        self.targetX = 0.
        self.targetY = 0.
        self.targetRadius = 10
        self.TargetShape = None
        # broken rules punishment
        self.BoundaryPunishment = 0
        # Rewards
        self.WinningReward = 1

    def start(self, RedArmy, GreenArmy):
        # self.i = 0
        self.redArmyWins = False
        self.greenArmyWins = False
        self.init_positions(RedArmy, GreenArmy)
        return self.get_state()

    def init_positions(self, RedArmy, GreenArmy):
        self.RedArmyBodies = []
        self.GreenArmyBodies = []
        for index, unit in enumerate(RedArmy.Units):
            RedArmy.Units[index].set_position(x=numpy.random.uniform(0, 30), y=numpy.random.uniform(0, 60))
            body = Point(RedArmy.Units[index].Position.x,
                         RedArmy.Units[index].Position.y).buffer(RedArmy.Units[index].BodyInfo['radius'])
            self.RedArmyBodies.append(body)
        for index, unit in enumerate(GreenArmy.Units):
            GreenArmy.Units[index].set_position(x=numpy.random.uniform(90, 120), y=numpy.random.uniform(0, 60))
            body = Point(GreenArmy.Units[index].Position.x,
                         GreenArmy.Units[index].Position.y).buffer(GreenArmy.Units[index].BodyInfo['radius'])
            self.GreenArmyBodies.append(body)
        self.targetX = numpy.random.uniform(30, 90)
        self.targetY = numpy.random.uniform(0, 60)
        self.TargetShape = Point(self.targetX, self.targetY).buffer(self.targetRadius)

    def step(self, Action, soldier, Army, redTurn):
        direction = 15 * Action
        Army.Units[soldier].move(6, direction=direction)
        reward = self.check_boundaries(soldier, Army, redTurn)
        if reward == 0:
            reward, done = self.calculate_r(Army, redTurn)
            if redTurn:
                self.redArmyWins = done
            else:
                self.greenArmyWins = done
        else:
            done = False
        return self.get_state(), reward, done

    def update_board(self, soldier, Army, redTurn):
        body = Point(Army.Units[soldier].Position.x,
                     Army.Units[soldier].Position.y).buffer(Army.Units[soldier].BodyInfo['radius'])
        if redTurn:
            self.RedArmyBodies[soldier] = body
        else:
            self.GreenArmyBodies[soldier] = body

    def get_state(self):
        state = []
        for body in self.RedArmyBodies:
            state.append(body.centroid.x)
            state.append(body.centroid.y)
        for body in self.GreenArmyBodies:
            state.append(body.centroid.x)
            state.append(body.centroid.y)
        state.append(self.targetX)
        state.append(self.targetY)
        return state

    def calculate_r(self, Army, redTurn):
        count = 0
        for index, unit in enumerate(Army.Units):
            if redTurn:
                count += 1 if not self.RedArmyBodies[index].intersection(self.TargetShape).is_empty else 0
            else:
                count += 1 if not self.GreenArmyBodies[index].intersection(self.TargetShape).is_empty else 0
        if count == len(Army.Units):
            done = True
            reward = self.WinningReward
        else:
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

    def plot(self, RedArmy, GreenArmy, Episode, Movement):
        fig = plt.figure()
        ax1 = fig.add_subplot(1, 1, 1)
        ax1.clear()
        ax1.set_aspect(1)
        ax1.set_title('Episode: {}, Movement: {}'.format(Episode, Movement))
        ax1.set_xlim([0, 120])
        ax1.set_ylim([0, 60])
        ax1.add_patch(plt.Circle((self.targetX, self.targetY), self.targetRadius, color='y', alpha=0.3))
        for unit in RedArmy.Units:
            ax1.add_patch(plt.Circle((unit.Position.x, unit.Position.y), unit.BodyInfo['radius'], color='r', alpha=0.3))
        for unit in GreenArmy.Units:
            ax1.add_patch(plt.Circle((unit.Position.x, unit.Position.y), unit.BodyInfo['radius'], color='g', alpha=0.3))
        plt.savefig('./Images/FirstApproach/GameHistory/{}_{}.png'.format(Episode, Movement))
        plt.close(fig)


class GetToTheTargetIndividually(Environment):
    def __init__(self):
        super().__init__()
        self.BoundaryPunishment = -1
        self.WinningReward = 10

    def init_positions(self, RedArmy, GreenArmy):
        self.RedArmyBodies = []
        self.GreenArmyBodies = []
        for index, unit in enumerate(RedArmy.Units):
            x_position = numpy.random.uniform(0, 30), numpy.random.uniform(90, 120)
            RedArmy.Units[index].set_position(x=numpy.random.choice(x_position), y=numpy.random.uniform(0, 60))
            body = Point(RedArmy.Units[index].Position.x,
                         RedArmy.Units[index].Position.y).buffer(RedArmy.Units[index].BodyInfo['radius'])
            self.RedArmyBodies.append(body)
        for index, unit in enumerate(GreenArmy.Units):
            GreenArmy.Units[index].set_position(x=0, y=0)
            body = Point(GreenArmy.Units[index].Position.x,
                         GreenArmy.Units[index].Position.y).buffer(GreenArmy.Units[index].BodyInfo['radius'])
            self.GreenArmyBodies.append(body)
        self.targetX = numpy.random.uniform(30, 90)
        self.targetY = numpy.random.uniform(0, 60)
        self.TargetShape = Point(self.targetX, self.targetY).buffer(self.targetRadius)

    def get_state(self):
        state = []
        for body in self.RedArmyBodies:
            state.append(body.centroid.x)
            state.append(body.centroid.y)
        for body in self.GreenArmyBodies:
            state.append(0)
            state.append(0)
        state.append(self.targetX)
        state.append(self.targetY)
        return state


class GetToTheTargetWithDistanceInformation(Environment):
    def __init__(self):
        super().__init__()
        self.BoundaryPunishment = -1
        # Rewards
        self.WinningReward = 10
        self.DistanceFromTargetRed = []
        self.DistanceFromTargetGreen = []
        self.PreviousDistanceFromTargetRed = []
        self.PreviousDistanceFromTargetGreen = []
        self.Initialisation = True

    def calculate_r(self, Army, redTurn):
        count = 0
        reward = 0
        for index, unit in enumerate(Army.Units):
            if redTurn:
                count += 1 if not self.RedArmyBodies[index].intersection(self.TargetShape).is_empty else 0
                reward = (self.PreviousDistanceFromTargetRed[index] - self.DistanceFromTargetRed[index]) / 3
            else:
                count += 1 if not self.GreenArmyBodies[index].intersection(self.TargetShape).is_empty else 0
                reward = (self.PreviousDistanceFromTargetGreen[index] - self.DistanceFromTargetGreen[index]) / 3
        if count == len(Army.Units):
            done = True
            reward = self.WinningReward
        else:
            done = False
        return reward, done

    def get_state(self):
        state = []
        self.PreviousDistanceFromTargetRed = copy.deepcopy(self.DistanceFromTargetRed)
        self.PreviousDistanceFromTargetGreen = copy.deepcopy(self.DistanceFromTargetGreen)
        for i, body in enumerate(self.RedArmyBodies):
            if self.Initialisation:
                self.DistanceFromTargetRed.append(body.distance(self.TargetShape))
                self.PreviousDistanceFromTargetRed.append(body.distance(self.TargetShape))
            else:
                self.DistanceFromTargetRed[i] = body.distance(self.TargetShape)
            state.append(body.centroid.x)
            state.append(body.centroid.y)
        for i, body in enumerate(self.GreenArmyBodies):
            if self.Initialisation:
                self.DistanceFromTargetGreen.append(body.distance(self.TargetShape))
                self.PreviousDistanceFromTargetGreen.append(body.distance(self.TargetShape))
            else:
                self.DistanceFromTargetGreen[i] = body.distance(self.TargetShape)
            state.append(body.centroid.x)
            state.append(body.centroid.y)
        state.append(self.targetX)
        state.append(self.targetY)
        self.Initialisation = False
        return state

    def step(self, Action, soldier, Army, redTurn):
        direction = 15 * Action
        Army.Units[soldier].move(6, direction=direction)
        reward = self.check_boundaries(soldier, Army, redTurn)
        s_1 = self.get_state()
        if reward == 0:
            reward, done = self.calculate_r(Army, redTurn)
            if redTurn:
                self.redArmyWins = done
            else:
                self.greenArmyWins = done
        else:
            done = False
        return s_1, reward, done
