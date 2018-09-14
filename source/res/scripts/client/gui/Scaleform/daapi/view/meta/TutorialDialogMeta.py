# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/TutorialDialogMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class TutorialDialogMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def submit(self):
        self._printOverrideError('submit')

    def cancel(self):
        self._printOverrideError('cancel')

    def as_setContentS(self, data):
        """
        :param data: Represented by TutorialDialogVO (AS)
        """
        return self.flashObject.as_setContent(data) if self._isDAAPIInited() else None

    def as_updateContentS(self, data):
        """
        :param data: Represented by TutorialDialogVO (AS)
        """
        return self.flashObject.as_updateContent(data) if self._isDAAPIInited() else None