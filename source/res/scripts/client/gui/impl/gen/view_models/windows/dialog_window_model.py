# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/impl/gen/view_models/windows/dialog_window_model.py
import typing
from frameworks.wulf import Resource
from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from gui.impl.gen.view_models.ui_kit.list_model import ListModel

class DialogWindowModel(ViewModel):
    __slots__ = ('onClosed', 'onBtnClicked')

    @property
    def buttons(self):
        return self._getViewModel(0)

    @property
    def currency(self):
        return self._getViewModel(1)

    def getHasCloseBtn(self):
        return self._getBool(2)

    def setHasCloseBtn(self, value):
        self._setBool(2, value)

    def getHasCurrencyBlock(self):
        return self._getBool(3)

    def setHasCurrencyBlock(self, value):
        self._setBool(3, value)

    def getContent(self):
        return self._getView(4)

    def setContent(self, value):
        self._setView(4, value)

    def getBottomContent(self):
        return self._getView(5)

    def setBottomContent(self, value):
        self._setView(5, value)

    def getBackgroundShineImage(self):
        return self._getResource(6)

    def setBackgroundShineImage(self, value):
        self._setResource(6, value)

    def getBackgroundImage(self):
        return self._getResource(7)

    def setBackgroundImage(self, value):
        self._setResource(7, value)

    def _initialize(self):
        super(DialogWindowModel, self)._initialize()
        self._addViewModelProperty('buttons', UserListModel())
        self._addViewModelProperty('currency', ListModel())
        self._addBoolProperty('hasCloseBtn', True)
        self._addBoolProperty('hasCurrencyBlock', False)
        self._addViewProperty('content')
        self._addViewProperty('bottomContent')
        self._addResourceProperty('backgroundShineImage', Resource.INVALID)
        self._addResourceProperty('backgroundImage', Resource.INVALID)
        self.onClosed = self._addCommand('onClosed')
        self.onBtnClicked = self._addCommand('onBtnClicked')
