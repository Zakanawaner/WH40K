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
from Objects.Networks.Evolutionary import EAMove
from Messages import Messages


# TODO he quitado el brain que habia y lo he guardado en auxoldBrain.py

class Brain:
    def __init__(self):
        # Assign Movement Cerebral Regions
        self.Move = EAMove()
        # Assign Shooting Cerebral Regions
        # Assign Psychic Cerebral Regions
        # Assign Charge Cerebral Regions
        # Assign Combat Cerebral Regions
        # ...


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
        self.move_range_clean()

    def move_range_clean(self):
        self.MoveRange = Point(self.Position.x, self.Position.y).buffer(self.M)

    def move_range_on_board(self, board):
        pass
        # return self.MoveRange

    # Action move
    def move(self, objectsBoard=None, model=None, coherencyRegion=None, newPosition=None, advance=False,
             isSergeant=False, target=None, overlapRange=None):
        if newPosition is not None:
            # M += self.throw_die() if advance else 0
            self.set_position(newPosition[0], newPosition[1])
        elif objectsBoard is not None:
            if model is not None:
                M = 0
                direction = 0
                if isSergeant:
                    if target is not None:
                        M, direction = self.Move.decide(model=model,
                                                        target=target,
                                                        objects=objectsBoard,
                                                        isSergeant=True)
                    else:
                        print(Messages.TargetNotDefined)
                elif coherencyRegion is not None and overlapRange is not None and target is not None:
                    M, direction = self.Move.decide(model=model,
                                                    target=target,
                                                    objects=objectsBoard,
                                                    region=coherencyRegion,
                                                    overlapRange=overlapRange,
                                                    isSergeant=False)
                else:
                    print(Messages.IllegalArguments)
                direction *= math.pi / 180
                self.set_position(M * math.cos(direction), M * math.sin(direction))
        else:
            print(Messages.IllegalArguments)
