# Environments for learning to get to a position on the board the fastest way.
#   -Environment: Father class. Board 120 x 60. Each army deploys on a side of the board.
#                 On the middle randomly the target. Army wins when all of its units are inside the target
#   -GetToTheTargetIndividually: Only for one army that is deployed in any part of the board.
#   -GetToTheTargetWithDistanceInformation: We add the distance between the agent and the target as an input
#                                           to the network
#   -GetToTheTargetCNN: Environment for the CNN version of the MoveNetwork
import numpy
import matplotlib
import matplotlib.pyplot as plt
from shapely.geometry import Point
from PIL import Image
import copy
import io

matplotlib.use('Agg')


class Environment:
    def __init__(self):
        # Create armies
        self.RedArmyBodies = []
        self.GreenArmyBodies = []
        self.redArmyWins = False
        self.greenArmyWins = False
        # Create board
        self.minX = 0.0
        self.maxX = 120.0
        self.minY = 0.0
        self.maxY = 60.0
        self.redDeployLimit = 30.0
        self.greenDeployLimit = 90.0
        self.targetX = 0.
        self.targetY = 0.
        self.targetRadius = 10
        self.TargetShape = None
        # Broken rules punishment
        self.BoundaryPunishment = 0
        # Rewards
        self.WinningReward = 1

    # Start the game
    def start(self, RedArmy, GreenArmy):
        self.redArmyWins = False
        self.greenArmyWins = False
        self.init_positions(RedArmy, GreenArmy)
        return self.get_state()

    # Called when game started. Deploys all units randomly within the corresponding zone for each army, and also saves
    # the images of the unis in the shapely list "...ArmyBodies".
    def init_positions(self, RedArmy, GreenArmy):
        self.RedArmyBodies = []
        self.GreenArmyBodies = []
        for index, unit in enumerate(RedArmy.Units):
            RedArmy.Units[index].set_position(x=numpy.random.uniform(self.minX, self.redDeployLimit),
                                              y=numpy.random.uniform(self.minY, self.maxY))
            self.RedArmyBodies.append(RedArmy.Units[index].Body)
        for index, unit in enumerate(GreenArmy.Units):
            GreenArmy.Units[index].set_position(x=numpy.random.uniform(self.greenDeployLimit, self.maxX),
                                                y=numpy.random.uniform(self.minY, self.maxY))
            self.GreenArmyBodies.append(GreenArmy.Units[index].Body)
        self.targetX = numpy.random.uniform(self.redDeployLimit, self.greenDeployLimit)
        self.targetY = numpy.random.uniform(self.minY, self.maxY)
        self.TargetShape = Point(self.targetX, self.targetY).buffer(self.targetRadius)

    # Performs a movement of the agent given the action ans the agent that chose it
    def step(self, ActionDirection, soldier, Army, redTurn, ActionDistance=6):
        direction = 15 * ActionDirection
        Army.Units[soldier].move(ActionDistance, direction=direction)
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

    # Called in the function 'check_boundaries' for checking the illegal movements and making the necessary corrections
    def update_board(self, soldier, Army, redTurn):
        if redTurn:
            self.RedArmyBodies[soldier] = Army.Units[soldier].Body
        else:
            self.GreenArmyBodies[soldier] = Army.Units[soldier].Body

    # Method that returns the state for the training loop
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

    # Method that checks if an army has won the game. Decides if the game is over and the reward.
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

    # Check the board bounds to ensure that no illegal movement is made. And if it is,
    # it applies the correction and the punishment to the agent
    def check_boundaries(self, soldier, Army, redTurn):
        reward = 0
        if Army.Units[soldier].Position.x > self.maxX:
            Army.Units[soldier].Position.x = self.maxX
            Army.Units[soldier].Body = Point(Army.Units[soldier].Position.x,
                                             Army.Units[soldier].Position.y).buffer(Army.Units[soldier].BodyInfo['radius'])
            reward = self.BoundaryPunishment
        if Army.Units[soldier].Position.x < self.minX:
            Army.Units[soldier].Position.x = self.minX
            Army.Units[soldier].Body = Point(Army.Units[soldier].Position.x,
                                             Army.Units[soldier].Position.y).buffer(Army.Units[soldier].BodyInfo['radius'])
            reward = self.BoundaryPunishment
        if Army.Units[soldier].Position.y > self.maxY:
            Army.Units[soldier].Position.y = self.maxY
            Army.Units[soldier].Body = Point(Army.Units[soldier].Position.x,
                                             Army.Units[soldier].Position.y).buffer(Army.Units[soldier].BodyInfo['radius'])
            reward = self.BoundaryPunishment
        if Army.Units[soldier].Position.y < self.minY:
            Army.Units[soldier].Position.y = self.minY
            Army.Units[soldier].Body = Point(Army.Units[soldier].Position.x,
                                             Army.Units[soldier].Position.y).buffer(Army.Units[soldier].BodyInfo['radius'])
            reward = self.BoundaryPunishment
        self.update_board(soldier, Army, redTurn)
        return reward

    # If plot is called in the training loop, the environment will save the game state in a graph.
    def plot(self, RedArmy, GreenArmy, Episode, Movement):
        fig = plt.figure()
        ax1 = fig.add_subplot(1, 1, 1)
        ax1.clear()
        ax1.set_aspect(1)
        ax1.set_title('Episode: {}, Movement: {}'.format(Episode, Movement))
        ax1.set_xlim([self.minX, self.maxX])
        ax1.set_ylim([self.minY, self.maxY])
        ax1.add_patch(plt.Circle((self.targetX, self.targetY), self.targetRadius, color='y', alpha=0.3))
        for unit in RedArmy.Units:
            ax1.add_patch(plt.Circle((unit.Position.x, unit.Position.y), unit.BodyInfo['radius'], color='r', alpha=0.3))
        for unit in GreenArmy.Units:
            ax1.add_patch(plt.Circle((unit.Position.x, unit.Position.y), unit.BodyInfo['radius'], color='g', alpha=0.3))
        plt.savefig('./Images/FirstApproach/GameHistory/GetToTheTarget{}_{}.png'.format(Episode, Movement))
        plt.close(fig)


class GetToTheTargetIndividually(Environment):
    def __init__(self):
        super().__init__()
        self.BoundaryPunishment = -1
        self.WinningReward = 10

    # Overrides the Environment in that red army can deploy in any side of the board
    def init_positions(self, RedArmy, GreenArmy):
        self.RedArmyBodies = []
        self.GreenArmyBodies = []
        for index, unit in enumerate(RedArmy.Units):
            x_position = [numpy.random.uniform(self.minX, self.redDeployLimit),
                          numpy.random.uniform(self.greenDeployLimit, self.maxX)]
            RedArmy.Units[index].set_position(x=numpy.random.choice(x_position),
                                              y=numpy.random.uniform(self.minY, self.maxY))
            self.RedArmyBodies.append(RedArmy.Units[index].Body)
        for index, unit in enumerate(GreenArmy.Units):
            GreenArmy.Units[index].set_position(x=0, y=0)
            self.GreenArmyBodies.append(GreenArmy.Units[index].Body)
        self.targetX = numpy.random.uniform(self.redDeployLimit, self.greenDeployLimit)
        self.targetY = numpy.random.uniform(self.minY, self.maxY)
        self.TargetShape = Point(self.targetX, self.targetY).buffer(self.targetRadius)

    # We keep the state of the father but green armies will give no information (value 0)
    def get_state(self):
        state = []
        for body in self.RedArmyBodies:
            state.append(body.centroid.x)
            state.append(body.centroid.y)
        for _ in self.GreenArmyBodies:
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

    # We override the reward function by adding in each movement a reward connected to
    # the difference in distance between the previous position and the new one
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

    # For the state we added the information of the distance between the agent and the target
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

    # We only override this one because we need to call get_state() before calculate r
    # to update the new distance from the target to de agent
    def step(self, ActionDirection, soldier, Army, redTurn, ActionDistance=6):
        direction = 15 * ActionDirection
        Army.Units[soldier].move(ActionDistance, direction=direction)
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


class GetToTheTargetCNN(Environment):
    def __init__(self):
        super().__init__()

    # Overrides father method by getting the images of the board fot the CNN inputs
    def get_state(self):
        fig = plt.figure()
        ax1 = fig.add_subplot(1, 1, 1)
        ax1.clear()
        ax1.set_aspect(1)
        ax1.set_xlim([self.minX, self.maxX])
        ax1.set_ylim([self.minY, self.maxY])
        # objects map
        for body in self.RedArmyBodies:
            ax1.add_patch(plt.Circle((body.centroid.x, body.centroid.y), body.centroid.x - body.bounds[0], color='r'))
        for body in self.GreenArmyBodies:
            ax1.add_patch(plt.Circle((body.centroid.x, body.centroid.y), body.centroid.x - body.bounds[0], color='b'))
        ax1.add_patch(plt.Circle((self.TargetShape.centroid.x, self.TargetShape.centroid.y),
                                 self.targetRadius, color='g'))
        plt.axis('off')
        buf = io.BytesIO()
        plt.savefig(buf, bbox_inches='tight', pad_inches=0, format='png')
        plt.close()
        return Image.open(buf).convert('RGB').resize((100, 50))

    # Overrides father method by saving the images of the board
    def plot(self, RedArmy, GreenArmy, Episode, Movement):
        fig = plt.figure()
        ax1 = fig.add_subplot(1, 1, 1)
        ax1.clear()
        ax1.set_aspect(1)
        ax1.set_xlim([self.minX, self.maxX])
        ax1.set_ylim([self.minY, self.maxY])
        # objects map
        for body in self.RedArmyBodies:
            ax1.add_patch(plt.Circle((body.centroid.x, body.centroid.y), body.centroid.x - body.bounds[0], color='r'))
        for body in self.GreenArmyBodies:
            ax1.add_patch(plt.Circle((body.centroid.x, body.centroid.y), body.centroid.x - body.bounds[0], color='b'))
        ax1.add_patch(plt.Circle((self.TargetShape.centroid.x, self.TargetShape.centroid.y),
                                 self.targetRadius, color='g'))
        plt.axis('off')
        buf = io.BytesIO()
        plt.savefig('./Images/FirstApproach/GameHistory/GetToTheTargetCNN_{}_{}.png'.format(Episode, Movement),
                    bbox_inches='tight', pad_inches=0, format='png')
        plt.close()
