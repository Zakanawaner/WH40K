import numpy
import torch
import torch.nn as nn
import torch.nn.functional as fun
import torch.optim as optim


class MoveHyperParameters:
    def __init__(self):
        self.MoveLearningRate = 0.005
        self.MoveBatchSize = 32
        self.MoveGamma = 0.2
        self.MoveEpsilonDec = 0.9995
        self.MoveEpsilonInc = 0.9999
        self.MoveEpsilonMax = 0.3
        self.MoveEpsilonMin = 0.2
        self.MoveEpsilon = self.MoveEpsilonMax
        self.MoveInputDims = 6
        self.MoveFirstLayerDims = 64
        self.MoveSecondLayerDims = 32
        self.MoveThirdLayerDims = 64
        self.MoveFourthLayerDims = 32
        self.MoveActionDims = 24
        self.MoveActionSpace = numpy.arange(self.MoveActionDims)
        self.MoveMaximalMemory = 100000
        self.MoveTargetCopyValue = 20

        self.CoherencyLearningRate = 0.005
        self.CoherencyBatchSize = 32
        self.CoherencyGamma = 0.2
        self.CoherencyEpsilonDec = 0.9995
        self.CoherencyEpsilonInc = 0.9999
        self.CoherencyEpsilonMax = 0.3
        self.CoherencyEpsilonMin = 0.2
        self.CoherencyEpsilon = self.CoherencyEpsilonMax
        self.CoherencyInputDims = 4
        self.CoherencyFirstLayerDims = 4
        self.CoherencySecondLayerDims = 4
        self.CoherencyActionDims = 2
        self.CoherencyActionSpace = numpy.arange(self.CoherencyActionDims)
        self.CoherencyMaximalMemory = 100000
        self.CoherencyTargetCopyValue = 20


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
        # self.fc2 = nn.Linear(self.FirstLayerDims, self.SecondLayerDims)
        # self.fc3 = nn.Linear(self.SecondLayerDims, self.ThirdLayerDims)
        # self.fc4 = nn.Linear(self.ThirdLayerDims, self.FourthLayerDims)
        self.fc5 = nn.Linear(self.FirstLayerDims, self.ActionDims)
        self.Optimizer = optim.Adam(self.parameters(), lr=self.LearningRate)
        self.Loss = nn.MSELoss()
        self.Device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
        self.to(self.Device)

    def forward(self, state):
        x = fun.relu(self.fc1(state))
        # x = fun.relu(self.fc2(x))
        # x = fun.relu(self.fc3(x))
        # x = fun.relu(self.fc4(x))
        outputs = self.fc5(x)
        return outputs


# This network will manage the unit coherency. Will make the model to move within 3" horizontally or 5"
# vertically from any of the other models of the squad.
# INPUTS : the x and y from the unit before the model
# OUTPUTS: x and y of the model
class CoherencyNetwork(nn.Module):
    def __init__(self,
                 InputDims,
                 FirstLayerDims,
                 SecondLayerDims,
                 ActionDims,
                 LearningRate):
        super(CoherencyNetwork, self).__init__()
        self.InputDims = InputDims
        self.FirstLayerDims = FirstLayerDims
        self.SecondLayerDims = SecondLayerDims
        self.ActionDims = ActionDims
        self.LearningRate = LearningRate
        self.fc1 = nn.Linear(self.InputDims, self.FirstLayerDims)
        # self.fc2 = nn.Linear(self.FirstLayerDims, self.SecondLayerDims)
        self.fc5 = nn.Linear(self.FirstLayerDims, self.ActionDims)
        self.Optimizer = optim.Adam(self.parameters(), lr=self.LearningRate)
        self.Loss = nn.MSELoss()
        self.Device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
        self.to(self.Device)

    def forward(self, state):
        x = fun.relu(self.fc1(state))
        # x = fun.relu(self.fc2(x))
        return self.fc5(x)

