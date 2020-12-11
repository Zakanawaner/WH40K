from shapely.geometry import Polygon, Point
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')


class Board:
    def __init__(self, RedArmy, GreenArmy, x=120, y=60):
        self.Surface = Polygon([(0, 0), (0, y), (x, y), (x, 0)])
        self.Objects = []
        self.PlotIndex = 0
        self.ObjectIndex = 0
        self.update_board(RedArmy, GreenArmy)

    def add_object(self, obj, objectType, team, squad, model):
        # Object types: Model, Scenography, ShootingRange, MovementRange, PsychicRange
        # Team: 0 -> neutral, 1 -> Army 1 or computer, 2 -> Army 2 or player
        # Squad: squad of the army
        # Model: Model of the squad
        self.Objects.append((self.ObjectIndex, obj, objectType, team, squad, model))
        self.ObjectIndex += 1

    def update_board(self, RedArmy, GreenArmy):
        self.Objects = []
        for squad in RedArmy.Squads:
            for model in squad.Units:
                self.add_object(model.Body, 'Model', RedArmy.Player, squad.SquadPosition, model.ModelPosition)
                self.add_object(model.move_range_on_board(self), 'MovementRange', RedArmy.Player, squad.SquadPosition,
                                model.ModelPosition)
                for gun in model.Gun:
                    if gun.TYPE != 'Melee':
                        self.add_object(gun.range_clean(model.Body), 'ShootingRange', RedArmy.Player, squad.SquadPosition,
                                        model.ModelPosition)
        for squad in GreenArmy.Squads:
            for model in squad.Units:
                self.add_object(model.Body, 'Model', GreenArmy.Player, squad.SquadPosition, model.ModelPosition)
                self.add_object(model.move_range_on_board(self), 'MovementRange', GreenArmy.Player, squad.SquadPosition,
                                model.ModelPosition)
                for gun in model.Gun:
                    if gun.TYPE != 'Melee':
                        self.add_object(gun.range_clean(model.Body), 'ShootingRange', GreenArmy.Player,
                                        squad.SquadPosition,
                                        model.ModelPosition)

    def plot(self):
        fig = plt.figure()
        ax1 = fig.add_subplot(1, 1, 1)
        ax1.clear()
        ax1.set_aspect(1)
        ax1.set_xlim([self.Surface.bounds[0], self.Surface.bounds[2]])
        ax1.set_ylim([self.Surface.bounds[1], self.Surface.bounds[3]])
        for obj in self.Objects:
            if obj[2] != 'Model' and obj[2] != 'Scenography':
                xs, ys = obj[1].exterior.xy
                fc = '#00000033'
                if obj[2] == 'MovementRange':
                    if obj[3] == 1:
                        fc = '#ff4d0033'
                    if obj[3] == 2:
                        fc = '#00ff8533'
                elif obj[2] == 'ShootingRange':
                    if obj[3] == 1:
                        fc = '#ff8d0033'
                    if obj[3] == 2:
                        fc = '#00f9ff33'
                elif obj[2] == 'PsychicRange':
                    if obj[3] == 1:
                        fc = '#fff40033'
                    if obj[3] == 2:
                        fc = '#00b8ff33'
                ax1.fill(xs, ys, fc=fc, ec='none')
        for obj in self.Objects:
            if obj[2] == 'Model' or obj[2] == 'Scenography':
                xs, ys = obj[1].exterior.xy
                fc = '#00000033'
                if obj[3] == 0:
                    fc = '#000000ff'
                if obj[3] == 1:
                    fc = '#ff0000ff'
                if obj[3] == 2:
                    fc = '#2cbd00ff'
                ax1.fill(xs, ys, fc=fc, ec='none')
                # ax1.text(obj[1].centroid.x, obj[1].centroid.y, obj[5])
        plt.axis('off')
        plt.savefig('test{}.png'.format(self.PlotIndex), bbox_inches='tight', pad_inches=0)
        self.PlotIndex += 1
