import trimesh
import vector3d
import numpy
import requests
import math
import random
import io
import torch
from torchvision import transforms
from PIL import Image
from operator import itemgetter
from shapely.geometry import Point
from Objects.Networks.MovementNetworks import MoveHyperParameters, MoveNetwork, CoherencyNetwork
from Objects.Networks.TestMovementCNN import MoveHyperParametersCNN, MoveNetworkCNN


# TODO The coherency part is horseshit
class Brain(MoveHyperParameters):
    def __init__(self):
        super().__init__()
        # Define the Neural Networks
        self.MoveNetwork = MoveNetwork(InputDims=self.MoveInputDims,
                                       FirstLayerDims=self.MoveFirstLayerDims,
                                       SecondLayerDims=self.MoveSecondLayerDims,
                                       ThirdLayerDims=self.MoveThirdLayerDims,
                                       FourthLayerDims=self.MoveFourthLayerDims,
                                       ActionDims=self.MoveActionDims,
                                       LearningRate=self.MoveLearningRate)
        self.MoveTargetNetwork = MoveNetwork(InputDims=self.MoveInputDims,
                                             FirstLayerDims=self.MoveFirstLayerDims,
                                             SecondLayerDims=self.MoveSecondLayerDims,
                                             ThirdLayerDims=self.MoveThirdLayerDims,
                                             FourthLayerDims=self.MoveFourthLayerDims,
                                             ActionDims=self.MoveActionDims,
                                             LearningRate=self.MoveLearningRate)
        # self.CoherencyNetwork = CoherencyNetwork(InputDims=self.CoherencyInputDims,
        #                                         FirstLayerDims=self.CoherencyFirstLayerDims,
        #                                         SecondLayerDims=self.CoherencySecondLayerDims,
        #                                         ActionDims=self.CoherencyActionDims,
        #                                         LearningRate=self.CoherencyLearningRate)
        # self.CoherencyTargetNetwork = CoherencyNetwork(InputDims=self.CoherencyInputDims,
        #                                               FirstLayerDims=self.CoherencyFirstLayerDims,
        #                                               SecondLayerDims=self.CoherencySecondLayerDims,
        #                                               ActionDims=self.CoherencyActionDims,
        #                                               LearningRate=self.CoherencyLearningRate)
        # self.MoveNetworkCNN = MoveNetworkCNN(InputDims=self.CNNInputDims,
        #                                     FirstLayerDims=self.CNNFirstLayerDims,
        #                                     SecondLayerDims=self.CNNSecondLayerDims,
        #                                     ThirdLayerDims=self.CNNThirdLayerDims,
        #                                     FourthLayerDims=self.CNNFourthLayerDims,
        #                                     ActionDims=self.CNNActionDims,
        #                                     LearningRate=self.CNNLearningRate)
        # self.MoveTargetNetworkCNN = MoveNetworkCNN(InputDims=self.CNNInputDims,
        #                                           FirstLayerDims=self.CNNFirstLayerDims,
        #                                           SecondLayerDims=self.CNNSecondLayerDims,
        #                                           ThirdLayerDims=self.CNNThirdLayerDims,
        #                                           FourthLayerDims=self.CNNFourthLayerDims,
        #                                           ActionDims=self.CNNActionDims,
        #                                           LearningRate=self.CNNLearningRate)
        # Define the coherency training parameters
        # self.CNNMemoryCounter = 0
        # self.CNNPreviousMemoryCounter = 0
        # self.CNNTargetCopyCounter = 0
        # self.CNNStateMemory = []
        # self.CNNNewStateMemory = []
        # self.CNNActionMemory = [[float] * self.CNNActionDims] * self.CNNMaximalMemory
        # self.CNNRewardMemory = [float] * self.CNNMaximalMemory
        # self.CNNTerminalMemory = [bool] * self.CNNMaximalMemory
        # Define the move training parameters
        self.MoveMemoryCounter = 0
        self.MovePreviousMemoryCounter = 0
        self.MoveTargetCopyCounter = 0
        self.MoveStateMemory = numpy.zeros((self.MoveMaximalMemory, self.MoveInputDims), dtype=numpy.float32)
        self.MoveNewStateMemory = numpy.zeros((self.MoveMaximalMemory, self.MoveInputDims), dtype=numpy.float32)
        self.MoveActionMemory = numpy.zeros(self.MoveMaximalMemory, dtype=numpy.int32)
        self.MoveRewardMemory = numpy.zeros(self.MoveMaximalMemory, dtype=numpy.float32)
        self.MoveTerminalMemory = numpy.zeros(self.MoveMaximalMemory, dtype=numpy.bool)
        # Define the coherency training parameters
        self.CoherencyMemoryCounter = 0
        self.CoherencyPreviousMemoryCounter = 0
        self.CoherencyTargetCopyCounter = 0
        self.CoherencyStateMemory = numpy.zeros((self.CoherencyMaximalMemory, self.CoherencyInputDims), dtype=numpy.float32)
        self.CoherencyNewStateMemory = numpy.zeros((self.CoherencyMaximalMemory, self.CoherencyInputDims), dtype=numpy.float32)
        self.CoherencyActionMemory = numpy.zeros((self.CoherencyMaximalMemory, self.CoherencyActionDims), dtype=numpy.float32)
        self.CoherencyRewardMemory = numpy.zeros(self.CoherencyMaximalMemory, dtype=numpy.float32)
        self.CoherencyTerminalMemory = numpy.zeros(self.CoherencyMaximalMemory, dtype=numpy.bool)

    def store_transition(self, model, s_0, action, reward, s_1, done):
        if model == 'Move':
            index = self.MoveMemoryCounter % self.MoveMaximalMemory
            self.MoveStateMemory[index] = s_0
            self.MoveNewStateMemory[index] = s_1
            self.MoveRewardMemory[index] = reward
            self.MoveActionMemory[index] = action
            self.MoveTerminalMemory[index] = done
            self.MoveMemoryCounter += 1
        if model == 'Coherency':
            index = self.CoherencyMemoryCounter % self.CoherencyMaximalMemory
            self.CoherencyStateMemory[index] = s_0
            self.CoherencyNewStateMemory[index] = s_1
            self.CoherencyRewardMemory[index] = reward
            self.CoherencyActionMemory[index] = action.detach().numpy()
            self.CoherencyTerminalMemory[index] = done
            self.CoherencyMemoryCounter += 1
        if model == 'CNN':
            index = self.CNNMemoryCounter % self.CNNMaximalMemory
            self.CNNStateMemory.append(s_0)
            self.CNNNewStateMemory.append(s_1)
            self.CNNRewardMemory[index] = reward
            self.CNNActionMemory[index] = action
            self.CNNTerminalMemory[index] = done
            self.CNNMemoryCounter += 1

    def choose(self, model, observation):
        if model == 'Move':
            if numpy.random.random() > self.MoveEpsilon:
                state = torch.tensor([observation]).to(self.MoveNetwork.Device)
                actions = self.MoveNetwork.forward(state)
                direction = torch.argmax(actions).item()
            else:
                direction = numpy.random.choice(self.MoveActionSpace)
            return direction
        if model == 'Coherency':
            state = torch.tensor([observation]).to(self.CoherencyNetwork.Device)
            coordinates = self.CoherencyNetwork.forward(state)
            return coordinates
        if model == 'CNN':
            if numpy.random.random() > self.CNNEpsilon:
                state = transforms.ToTensor()(observation).unsqueeze_(0).to(self.MoveNetworkCNN.Device)
                actions = self.MoveNetworkCNN.forward(state)
                action = torch.argmax(actions).item()
            else:
                action = numpy.random.choice(self.CNNActionSpace)
            return action, action % 24, numpy.round(action / 24)

    def learn(self, model):
        if model == 'Move':
            if self.MoveMemoryCounter < self.MoveBatchSize:
                return
            self.MoveNetwork.Optimizer.zero_grad()
            max_mem = min(self.MoveMemoryCounter, self.MoveMaximalMemory)
            batch = numpy.random.choice(max_mem, self.MoveBatchSize, replace=False)
            batch_index = numpy.arange(self.MoveBatchSize, dtype=numpy.int32)
            state_batch = torch.tensor(self.MoveStateMemory[batch]).to(self.MoveNetwork.Device)
            new_state_batch = torch.tensor(self.MoveNewStateMemory[batch]).to(self.MoveNetwork.Device)
            reward_batch = torch.tensor(self.MoveRewardMemory[batch]).to(self.MoveNetwork.Device)
            terminal_batch = torch.tensor(self.MoveTerminalMemory[batch]).to(self.MoveNetwork.Device)
            action_batch = self.MoveActionMemory[batch]

            evaluation = self.MoveNetwork.forward(state_batch)[batch_index, action_batch]
            evaluation_next = self.MoveTargetNetwork.forward(new_state_batch)
            evaluation_next[terminal_batch] = 0.0

            evaluation_target = reward_batch + self.MoveGamma * torch.max(evaluation_next, dim=1)[0]

            loss = self.MoveNetwork.Loss(evaluation_target, evaluation).to(self.MoveNetwork.Device)
            loss.backward()
            self.MoveNetwork.Optimizer.step()
            self.MoveTargetCopyCounter += 1
            if self.MoveTargetCopyCounter == self.MoveTargetCopyValue:
                self.MoveTargetCopyCounter = 0
                self.update_target_network('Move')

        if model == 'Coherency':
            if self.CoherencyMemoryCounter < self.CoherencyBatchSize:
                return
            self.CoherencyNetwork.Optimizer.zero_grad()
            max_mem = min(self.CoherencyMemoryCounter, self.CoherencyMaximalMemory)
            batch = numpy.random.choice(max_mem, self.CoherencyBatchSize, replace=False)
            batch_index = numpy.arange(self.CoherencyBatchSize, dtype=numpy.int32)
            state_batch = torch.tensor(self.CoherencyStateMemory[batch]).to(self.CoherencyNetwork.Device)
            new_state_batch = torch.tensor(self.CoherencyNewStateMemory[batch]).to(self.CoherencyNetwork.Device)
            reward_batch = torch.tensor(self.CoherencyRewardMemory[batch]).to(self.CoherencyNetwork.Device)
            terminal_batch = torch.tensor(self.CoherencyTerminalMemory[batch]).to(self.CoherencyNetwork.Device)
            action_batch = self.CoherencyActionMemory[batch]

            evaluation = self.CoherencyNetwork.forward(state_batch)
            evaluation_next = self.CoherencyTargetNetwork.forward(new_state_batch)
            evaluation_next[terminal_batch] = 0.0

            evaluation_target = torch.stack([reward_batch, reward_batch], dim=1) + self.CoherencyGamma * evaluation_next

            loss = self.CoherencyNetwork.Loss(evaluation_target, evaluation).to(self.CoherencyNetwork.Device)
            loss.backward()
            self.CoherencyNetwork.Optimizer.step()
            self.CoherencyTargetCopyCounter += 1
            if self.CoherencyTargetCopyCounter == self.CoherencyTargetCopyValue:
                self.CoherencyTargetCopyCounter = 0
                self.update_target_network('Coherency')

        if model == 'CNN':
            if self.CNNMemoryCounter < self.CNNBatchSize:
                return
            self.MoveNetworkCNN.Optimizer.zero_grad()
            max_mem = min(self.CNNMemoryCounter, self.CNNMaximalMemory)
            batch = numpy.random.choice(max_mem, self.CNNBatchSize, replace=False).tolist()
            batch_index = numpy.arange(self.CNNBatchSize)
            for i, image in enumerate(list(itemgetter(*batch)(self.CNNStateMemory))):
                if i == 0:
                    state_batch = transforms.ToTensor()(image).unsqueeze_(0).to(self.MoveNetworkCNN.Device)
                else:
                    state_batch = torch.cat((state_batch, transforms.ToTensor()(image).unsqueeze_(0).to(self.MoveNetworkCNN.Device)), dim=0)
            for i, image in enumerate(list(itemgetter(*batch)(self.CNNNewStateMemory))):
                if i == 0:
                    new_state_batch = transforms.ToTensor()(image).unsqueeze_(0).to(self.MoveNetworkCNN.Device)
                else:
                    new_state_batch = torch.cat((new_state_batch, transforms.ToTensor()(image).unsqueeze_(0).to(self.MoveNetworkCNN.Device)), dim=0)
            reward_batch = torch.tensor(itemgetter(*batch)(self.CNNRewardMemory)).to(self.MoveNetworkCNN.Device)
            terminal_batch = torch.tensor(itemgetter(*batch)(self.CNNTerminalMemory)).to(self.MoveNetworkCNN.Device)
            action_batch = itemgetter(*batch)(self.CNNActionMemory)

            evaluation = self.MoveNetworkCNN.forward(state_batch)[batch_index, action_batch]
            evaluation_next = self.MoveTargetNetworkCNN.forward(new_state_batch)
            evaluation_next[terminal_batch] = 0.0

            evaluation_target = reward_batch + self.CNNGamma * torch.max(evaluation_next, dim=1)[0]

            loss = self.MoveNetworkCNN.Loss(evaluation_target, evaluation).to(self.MoveNetworkCNN.Device)
            loss.backward()
            self.MoveNetworkCNN.Optimizer.step()
            self.CNNTargetCopyCounter += 1
            if self.CNNTargetCopyCounter == self.CNNTargetCopyValue:
                self.CNNTargetCopyCounter = 0
                self.update_target_network('CNN')

    def epsilon_increase(self, model):
        if model == 'Move':
            self.MoveEpsilon = self.MoveEpsilon / self.MoveEpsilonInc if self.MoveEpsilon < self.MoveEpsilonMax else self.MoveEpsilonMax
        if model == 'Coherency':
            self.CoherencyEpsilon = self.CoherencyEpsilon / self.CoherencyEpsilonInc if self.CoherencyEpsilon < self.CoherencyEpsilonMax else self.CoherencyEpsilonMax
        if model == 'CNN':
            self.CNNEpsilon = self.CNNEpsilon / self.CNNEpsilonInc if self.CNNEpsilon < self.CNNEpsilonMax else self.CNNEpsilonMax

    def epsilon_decrease(self, model):
        if model == 'Move':
            self.MoveEpsilon = self.MoveEpsilon * self.MoveEpsilonDec if self.MoveEpsilon > self.MoveEpsilonMin else self.MoveEpsilonMin
        if model == 'Coherency':
            self.CoherencyEpsilon = self.CoherencyEpsilon * self.CoherencyEpsilonDec if self.CoherencyEpsilon > self.CoherencyEpsilonMin else self.CoherencyEpsilonMin
        if model == 'CNN':
            self.CNNEpsilon = self.CNNEpsilon * self.CNNEpsilonDec if self.CNNEpsilon > self.CNNEpsilonMin else self.CNNEpsilonMin

    def update_target_network(self, model):
        if model == 'Move':
            self.MoveTargetNetwork.load_state_dict(self.MoveNetwork.state_dict())
        if model == 'Coherency':
            self.CoherencyTargetNetwork.load_state_dict(self.CoherencyNetwork.state_dict())
        if model == 'CNN':
            self.MoveTargetNetworkCNN.load_state_dict(self.MoveNetworkCNN.state_dict())

    def save_model(self, model):
        if model == 'Move':
            torch.save(self.MoveNetwork.state_dict(), 'Objects/Networks/Models/MoveNetwork.pt')
        if model == 'Coherency':
            torch.save(self.CoherencyNetwork.state_dict(), 'Objects/Networks/Models/CoherencyNetwork.pt')
        if model == 'CNN':
            torch.save(self.MoveNetworkCNN.state_dict(), 'Objects/Networks/Models/MoveNetworkCNN.pt')

    def load_model(self, model):
        if model == 'Move':
            self.MoveNetwork.load_state_dict(torch.load('Objects/Networks/Models/MoveNetwork.pt'))
        if model == 'Coherency':
            self.CoherencyNetwork.load_state_dict(torch.load('Objects/Networks/Models/CoherencyNetwork.pt'))
        if model == 'CNN':
            self.MoveNetworkCNN.load_state_dict(torch.load('Objects/Networks/Models/MoveNetworkCNN.pt'))


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
        self.Body = Point(self.Position.x, self.Position.y).buffer(self.BodyInfo['radius'])

    @staticmethod
    def throw_die(die=6):
        return random.randint(1, die)

    def set_position(self, x, y, z=0):
        self.Position.x += x
        self.Position.y += y
        self.Position.z += z
        self.Body = Point(self.Position.x, self.Position.y).buffer(self.BodyInfo['radius'])

    # Action move
    def move(self, M, target=None, direction=0, advance=False):
        M += self.throw_die() if advance else 0
        if target is not None:
            vector = vector3d.vector.from_points(self.Position, target.position)
            direction = math.atan(vector.y/vector.x)
        else:
            direction *= math.pi / 180
        self.set_position(M * math.cos(direction), M * math.sin(direction))
