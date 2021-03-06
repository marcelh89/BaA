__author__ = 'marcman'

from data.stage.stage import Stage
from data.components.balloon import Balloon


class Stage01Training(Stage):
    def __init__(self, description):
        Stage.__init__(self, description)
        self.targets = (Balloon('RED', x * 30 + 300, 600) for x in range(15))

    def get_targets(self):
        return self.targets