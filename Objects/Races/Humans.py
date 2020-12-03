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
from Objects.Generic.Models import Model
from Objects.Networks.Evolutionary import EACoherency
from Messages import Messages


# TODO he quitado el brain que habia y lo he guardado en auxoldBrain.py

class Brain:
    def __init__(self):
        self.Coherency = EACoherency()
        self.DecideToMove = None


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


class Human(Brain, Body, Model):
    def __init__(self, meshInfo):
        Brain.__init__(self)
        Body.__init__(self, meshInfo)
        Model.__init__(self)
        self.Position = vector3d.point.Point()
        self.MoveRange = None
        self.PsychicRange = None
        self.Body = Point(self.Position.x, self.Position.y).buffer(self.BodyInfo['radius'])

    @staticmethod
    def throw_die(die=6):
        return random.randint(1, die)

    def set_position(self, x, y, z=0):
        self.Position.x += x
        self.Position.y += y
        self.Position.z += z
        self.Body = Point(self.Position.x, self.Position.y).buffer(self.BodyInfo['radius'])

    def move_range_clean(self):
        self.MoveRange = Point(self.Position.x, self.Position.y).buffer(self.M)
        return self.MoveRange

    def move_range_on_board(self, board):
        pass

    # Action move
    def move(self, objectsBoard, model=None, coherencyRegion=None, newPosition=None, advance=False,
             isSergeant=False, target=None, overlapRange=None):
        if newPosition is not None:
            # M += self.throw_die() if advance else 0
            self.set_position(newPosition[0], newPosition[1])
        elif model is not None and coherencyRegion is not None and objectsBoard is not None and overlapRange is not None:
            M = 0
            direction = 0
            if isSergeant:
                if target is not None:
                    M, direction = self.Coherency.decide(model, coherencyRegion, objectsBoard, overlapRange)
                else:
                    print(Messages.TargetNotDefined)
            else:
                M, direction = self.Coherency.decide(model, coherencyRegion, objectsBoard, overlapRange)
            direction *= math.pi / 180
            self.set_position(M * math.cos(direction), M * math.sin(direction))
            # M += self.throw_die() if advance else 0
        else:
            print(Messages.IllegalArguments)
