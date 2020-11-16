import trimesh
import vector3d
import numpy
import requests
import math
import random
import io
import torch
import torch.nn as nn
import torch.nn.functional as fun
import torch.optim as optim


class HyperParameters:
    def __init__(self):
        self.LearningRate = 0.001
        self.BatchSize = 32
        self.Gamma = 0.8
        self.Epsilon = 0.8
        self.EpsilonDec = 0.999
        self.EpsilonInc = 0.9999
        self.EpsilonMax = 0.8
        self.EpsilonMin = 0.1
        self.Epsilon = self.EpsilonMax
        self.InputDims = 10
        self.FirstLayerDims = 16
        self.SecondLayerDims = 24
        self.ThirdLayerDims = 0
        self.FourthLayerDims = 0
        self.ActionDims = 24
        self.ActionSpace = numpy.arange(self.ActionDims)
        self.MaximalMemory = 100000
        self.TargetCopyValue = 20


class MoveNetwork(nn.Module):
    def __init__(self,
                 InputDims,
                 FirstLayerDims,
                 SecondLayerDims,
                 ThirdLayerDims,
                 FourthLayerDims,
                 ActionDims,
                 LearningRate):
        super(MoveNetwork, self).__init__()
        self.InputDims = InputDims
        self.FirstLayerDims = FirstLayerDims
        self.SecondLayerDims = SecondLayerDims
        self.ThirdLayerDims = ThirdLayerDims
        self.FourthLayerDims = FourthLayerDims
        self.ActionDims = ActionDims
        self.LearningRate = LearningRate
        self.fc1 = nn.Linear(self.InputDims, self.FirstLayerDims)
        self.fc2 = nn.Linear(self.FirstLayerDims, self.SecondLayerDims)
        # self.fc3 = nn.Linear(self.SecondLayerDims, self.ThirdLayerDims)
        # self.fc4 = nn.Linear(self.ThirdLayerDims, self.FourthLayerDims)
        self.fc5 = nn.Linear(self.SecondLayerDims, self.ActionDims)
        self.Optimizer = optim.Adam(self.parameters(), lr=self.LearningRate)
        self.Loss = nn.MSELoss()
        self.Device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
        self.to(self.Device)

    def forward(self, state):
        x = fun.relu(self.fc1(state))
        x = fun.relu(self.fc2(x))
        # x = fun.relu(self.fc3(x))
        # x = fun.relu(self.fc4(x))
        outputs = self.fc5(x)
        return outputs


class Brain(HyperParameters):
    def __init__(self):
        super().__init__()
        # Define the Neural Networks
        self.MoveNetwork = MoveNetwork(InputDims=self.InputDims,
                                       FirstLayerDims=self.FirstLayerDims,
                                       SecondLayerDims=self.SecondLayerDims,
                                       ThirdLayerDims=self.ThirdLayerDims,
                                       FourthLayerDims=self.FourthLayerDims,
                                       ActionDims=self.ActionDims,
                                       LearningRate=self.LearningRate)
        self.MoveTargetNetwork = MoveNetwork(InputDims=self.InputDims,
                                             FirstLayerDims=self.FirstLayerDims,
                                             SecondLayerDims=self.SecondLayerDims,
                                             ThirdLayerDims=self.ThirdLayerDims,
                                             FourthLayerDims=self.FourthLayerDims,
                                             ActionDims=self.ActionDims,
                                             LearningRate=self.LearningRate)
        # Define the training parameters
        self.MemoryCounter = 0
        self.PreviousMemoryCounter = 0
        self.TargetCopyCounter = 0
        self.StateMemory = numpy.zeros((self.MaximalMemory, self.InputDims), dtype=numpy.float32)
        self.NewStateMemory = numpy.zeros((self.MaximalMemory, self.InputDims), dtype=numpy.float32)
        self.ActionMemory = numpy.zeros(self.MaximalMemory, dtype=numpy.int32)
        self.RewardMemory = numpy.zeros(self.MaximalMemory, dtype=numpy.float32)
        self.TerminalMemory = numpy.zeros(self.MaximalMemory, dtype=numpy.bool)

    def store_transition(self, s_0, action, reward, s_1, done):
        index = self.MemoryCounter % self.MaximalMemory
        self.StateMemory[index] = s_0
        self.NewStateMemory[index] = s_1
        self.RewardMemory[index] = reward
        self.ActionMemory[index] = action
        self.TerminalMemory[index] = done
        self.MemoryCounter += 1

    def choose(self, observation):
        if numpy.random.random() > self.Epsilon:
            state = torch.tensor([observation]).to(self.MoveNetwork.Device)
            actions = self.MoveNetwork.forward(state)
            direction = torch.argmax(actions).item()
        else:
            direction = numpy.random.choice(self.ActionSpace)
        return direction

    def learn(self):
        if self.MemoryCounter < self.BatchSize:
            return
        self.MoveNetwork.Optimizer.zero_grad()
        max_mem = min(self.MemoryCounter, self.MaximalMemory)
        batch = numpy.random.choice(max_mem, self.BatchSize, replace=False)
        batch_index = numpy.arange(self.BatchSize, dtype=numpy.int32)
        state_batch = torch.tensor(self.StateMemory[batch]).to(self.MoveNetwork.Device)
        new_state_batch = torch.tensor(self.NewStateMemory[batch]).to(self.MoveNetwork.Device)
        reward_batch = torch.tensor(self.RewardMemory[batch]).to(self.MoveNetwork.Device)
        terminal_batch = torch.tensor(self.TerminalMemory[batch]).to(self.MoveNetwork.Device)
        action_batch = self.ActionMemory[batch]

        evaluation = self.MoveNetwork.forward(state_batch)[batch_index, action_batch]
        evaluation_next = self.MoveTargetNetwork.forward(new_state_batch)
        evaluation_next[terminal_batch] = 0.0

        evaluation_target = reward_batch + self.Gamma * torch.max(evaluation_next, dim=1)[0]

        loss = self.MoveNetwork.Loss(evaluation_target, evaluation).to(self.MoveNetwork.Device)
        loss.backward()
        self.MoveNetwork.Optimizer.step()
        self.TargetCopyCounter += 1
        if self.TargetCopyCounter == self.TargetCopyValue:
            self.TargetCopyCounter = 0
            self.update_target_network()

    def epsilon_increase(self):
        self.Epsilon = self.Epsilon / self.EpsilonInc if self.Epsilon < self.EpsilonMax else self.EpsilonMax

    def epsilon_decrease(self):
        self.Epsilon = self.Epsilon * self.EpsilonDec if self.Epsilon > self.EpsilonMin else self.EpsilonMin

    def update_target_network(self):
        self.MoveTargetNetwork.load_state_dict(self.MoveNetwork.state_dict())


class Body:
    def __init__(self, meshInfo):
        mesh = trimesh.load_mesh(file_obj=io.StringIO(requests.get(meshInfo['MeshURL']).content.decode('utf-8')),
                                 file_type='obj')
        self.BodyInfo = {'radius': trimesh.base.bounds.minimum_cylinder(mesh).get('radius') * meshInfo['scaleX'],
                         'height': trimesh.base.bounds.minimum_cylinder(mesh).get('height') * meshInfo['scaleX']}

    def update_body(self, meshInfo):
        mesh = trimesh.load_mesh(file_obj=io.StringIO(requests.get(meshInfo['MeshURL']).content.decode('utf-8')),
                                 file_type='obj')
        self.BodyInfo = {'radius': trimesh.base.bounds.minimum_cylinder(mesh).get('radius') * meshInfo['scaleX'],
                         'height': trimesh.base.bounds.minimum_cylinder(mesh).get('height') * meshInfo['scaleX']}


class Human(Brain, Body):
    def __init__(self, meshInfo):
        Brain.__init__(self)
        Body.__init__(self, meshInfo)
        self.Position = vector3d.point.Point()

    @staticmethod
    def throw_die(die=6):
        return random.randint(1, die)

    def set_position(self, x, y, z=0):
        self.Position.x += x
        self.Position.y += y
        self.Position.z += z

    # Action move
    def move(self, M, target=None, direction=0, advance=False):
        M += self.throw_die() if advance else 0
        if target is not None:
            vector = vector3d.vector.from_points(self.Position, target.position)
            direction = math.atan(vector.y/vector.x)
        else:
            direction *= math.pi / 180
        self.set_position(M * math.cos(direction), M * math.sin(direction))
