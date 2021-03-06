# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/WarriorAchievement.py
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from abstract import RegularExtAchievement
from abstract.mixins import NoProgressBar
from arena_achievements import ACHIEVEMENT_CONDITIONS, ACHIEVEMENT_CONDITIONS_EXT

class WarriorAchievement(NoProgressBar, RegularExtAchievement):

    def __init__(self, dossier, value=None):
        RegularExtAchievement.__init__(self, 'warrior', _AB.TOTAL, dossier, value)

    def _getStandardValues(self):
        return ACHIEVEMENT_CONDITIONS[self._getActualName()]['minFrags']

    def _getExtValues(self):
        return ACHIEVEMENT_CONDITIONS_EXT[self._getActualName()]['minFrags']
