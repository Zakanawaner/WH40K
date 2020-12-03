from shapely.geometry import Polygon, Point
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')


class Board:
    def __init__(self, RedArmy, GreenArmy, x=120, y=60):
        self.Surface = Polygon([(0, 0), (0, y), (x, y), (x, 0)])
        self.Objects = []
        self.update_board(RedArmy, GreenArmy)
        self.PlotIndex = 0

    def add_object(self, obj, objectType, team, squad, model):
        # Object types: Model, Scenography, ShootingRange, MovementRange, PsychicRange
        # Team: 0 -> neutral, 1 -> Army 1 or computer, 2 -> Army 2 or player
        # Squad: squad of the army
        # Model: Model of the squad
        self.Objects.append((obj, objectType, team, squad, model))

    def update_board(self, RedArmy, GreenArmy):
        self.Objects = []
        for squad in RedArmy.Squads:
            for model in squad.Units:
                self.add_object(model.Body, 'Model', 1, squad.SquadPosition, model.ModelPosition)
                self.add_object(model.move_range_clean(), 'MovementRange', 1, squad.SquadPosition, model.ModelPosition)
                for gun in model.Gun:
                    self.add_object(gun.range_clean(model.Body), 'ShootingRange', 1, squad.SquadPosition,
                                    model.ModelPosition)
        for squad in GreenArmy.Squads:
            for model in squad.Units:
                self.add_object(model.Body, 'Model', 2, squad.SquadPosition, model.ModelPosition)
                self.add_object(model.move_range_clean(), 'MovementRange', 2, squad.SquadPosition, model.ModelPosition)
                for gun in model.Gun:
                    self.add_object(gun.range_clean(model.Body), 'ShootingRange', 2,
                                    squad.SquadPosition, model.ModelPosition)

    def plot(self):
        fig = plt.figure()
        ax1 = fig.add_subplot(1, 1, 1)
        ax1.clear()
        ax1.set_aspect(1)
        ax1.set_xlim([self.Surface.bounds[0], self.Surface.bounds[2]])
        ax1.set_ylim([self.Surface.bounds[1], self.Surface.bounds[3]])
        for obj in self.Objects:
            if obj[1] != 'Model' and obj[1] != 'Scenography':
                xs, ys = obj[0].exterior.xy
                fc = '#00000033'
                if obj[1] == 'MovementRange':
                    if obj[2] == 1:
                        fc = '#ff4d0033'
                    if obj[2] == 2:
                        fc = '#00ff8533'
                elif obj[1] == 'ShootingRange':
                    if obj[2] == 1:
                        fc = '#ff8d0033'
                    if obj[2] == 2:
                        fc = '#00f9ff33'
                elif obj[1] == 'PsychicRange':
                    if obj[2] == 1:
                        fc = '#fff40033'
                    if obj[2] == 2:
                        fc = '#00b8ff33'
                ax1.fill(xs, ys, fc=fc, ec='none')
        for obj in self.Objects:
            if obj[1] == 'Model' or obj[1] == 'Scenography':
                xs, ys = obj[0].exterior.xy
                fc = '#00000033'
                if obj[2] == 0:
                    fc = '#000000ff'
                if obj[2] == 1:
                    fc = '#ff0000ff'
                if obj[2] == 2:
                    fc = '#2cbd00ff'
                ax1.fill(xs, ys, fc=fc, ec='none')
                ax1.text(obj[0].centroid.x, obj[0].centroid.y, obj[4])
        plt.axis('off')
        plt.savefig('test{}.png'.format(self.PlotIndex), bbox_inches='tight', pad_inches=0)
        self.PlotIndex += 1
