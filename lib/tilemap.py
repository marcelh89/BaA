__author__ = 'marcman'

from lib.sprites.player import Player
from lib.sprites.paper import Paper
from lib.stages import Stages


class Tilemap(object):

    def __init__(self):

        self.player = Player()
        self.paper = Paper()
        self.stages = Stages(self.player)
        self.status = 0

    def render(self, event, screen):

        stat = self.status

        if stat == 1:
            print "render gameover"
            self.paper.render(stat, screen)
        elif stat == 2:
            print "render stagecomplete"
            self.paper.render(stat, screen)
        else:
            #render player
            arrows = self.player.render(event, screen)

            #render stage
            self.status = self.stages.render(event, screen, arrows)

    def handle_input(self, event):
        self.player.handle_input(event)