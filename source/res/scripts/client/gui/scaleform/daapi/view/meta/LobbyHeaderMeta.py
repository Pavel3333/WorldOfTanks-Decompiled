# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/LobbyHeaderMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class LobbyHeaderMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def menuItemClick(self, alias):
        self._printOverrideError('menuItemClick')

    def showLobbyMenu(self):
        self._printOverrideError('showLobbyMenu')

    def showExchangeWindow(self):
        self._printOverrideError('showExchangeWindow')

    def showExchangeXPWindow(self):
        self._printOverrideError('showExchangeXPWindow')

    def showPremiumDialog(self):
        self._printOverrideError('showPremiumDialog')

    def onPremShopClick(self):
        self._printOverrideError('onPremShopClick')

    def onPayment(self):
        self._printOverrideError('onPayment')

    def showSquad(self):
        self._printOverrideError('showSquad')

    def fightClick(self, mapID, actionName):
        self._printOverrideError('fightClick')

    def as_setScreenS(self, alias):
        return self.flashObject.as_setScreen(alias) if self._isDAAPIInited() else None

    def as_creditsResponseS(self, credits, btnDoText, tooltip, tooltipType):
        return self.flashObject.as_creditsResponse(credits, btnDoText, tooltip, tooltipType) if self._isDAAPIInited() else None

    def as_goldResponseS(self, gold, btnDoText, tooltip, tooltipType):
        return self.flashObject.as_goldResponse(gold, btnDoText, tooltip, tooltipType) if self._isDAAPIInited() else None

    def as_doDisableNavigationS(self):
        return self.flashObject.as_doDisableNavigation() if self._isDAAPIInited() else None

    def as_doDisableHeaderButtonS(self, btnId, isEnabled):
        return self.flashObject.as_doDisableHeaderButton(btnId, isEnabled) if self._isDAAPIInited() else None

    def as_setGoldFishEnabledS(self, isEnabled, playAnimation, tooltip, tooltipType):
        return self.flashObject.as_setGoldFishEnabled(isEnabled, playAnimation, tooltip, tooltipType) if self._isDAAPIInited() else None

    def as_updateSquadS(self, isInSquad, tooltip, tooltipType, isEvent, icon):
        return self.flashObject.as_updateSquad(isInSquad, tooltip, tooltipType, isEvent, icon) if self._isDAAPIInited() else None

    def as_nameResponseS(self, data):
        """
        :param data: Represented by AccountDataVo (AS)
        """
        return self.flashObject.as_nameResponse(data) if self._isDAAPIInited() else None

    def as_setClanEmblemS(self, tID):
        return self.flashObject.as_setClanEmblem(tID) if self._isDAAPIInited() else None

    def as_setPremiumParamsS(self, btnLabel, doLabel, isHasAction, tooltip, tooltipType):
        return self.flashObject.as_setPremiumParams(btnLabel, doLabel, isHasAction, tooltip, tooltipType) if self._isDAAPIInited() else None

    def as_setPremShopDataS(self, iconSrc, premShopText, tooltip, tooltipType):
        return self.flashObject.as_setPremShopData(iconSrc, premShopText, tooltip, tooltipType) if self._isDAAPIInited() else None

    def as_updateBattleTypeS(self, battleTypeName, battleTypeIcon, isEnabled, tooltip, tooltipType, battleTypeID):
        return self.flashObject.as_updateBattleType(battleTypeName, battleTypeIcon, isEnabled, tooltip, tooltipType, battleTypeID) if self._isDAAPIInited() else None

    def as_setServerS(self, name, tooltip, tooltipType):
        return self.flashObject.as_setServer(name, tooltip, tooltipType) if self._isDAAPIInited() else None

    def as_updatePingStatusS(self, pingStatus, isColorBlind):
        return self.flashObject.as_updatePingStatus(pingStatus, isColorBlind) if self._isDAAPIInited() else None

    def as_setWalletStatusS(self, walletStatus):
        return self.flashObject.as_setWalletStatus(walletStatus) if self._isDAAPIInited() else None

    def as_setFreeXPS(self, freeXP, btnDoText, isHasAction, tooltip, tooltipType):
        return self.flashObject.as_setFreeXP(freeXP, btnDoText, isHasAction, tooltip, tooltipType) if self._isDAAPIInited() else None

    def as_disableFightButtonS(self, isDisabled):
        return self.flashObject.as_disableFightButton(isDisabled) if self._isDAAPIInited() else None

    def as_setFightButtonS(self, label):
        return self.flashObject.as_setFightButton(label) if self._isDAAPIInited() else None

    def as_setCoolDownForReadyS(self, value):
        return self.flashObject.as_setCoolDownForReady(value) if self._isDAAPIInited() else None

    def as_showBubbleTooltipS(self, message, duration):
        return self.flashObject.as_showBubbleTooltip(message, duration) if self._isDAAPIInited() else None

    def as_setFightBtnTooltipS(self, tooltip):
        return self.flashObject.as_setFightBtnTooltip(tooltip) if self._isDAAPIInited() else None

    def as_updateOnlineCounterS(self, clusterStats, regionStats, tooltip, isAvailable):
        return self.flashObject.as_updateOnlineCounter(clusterStats, regionStats, tooltip, isAvailable) if self._isDAAPIInited() else None

    def as_initOnlineCounterS(self, visible):
        return self.flashObject.as_initOnlineCounter(visible) if self._isDAAPIInited() else None

    def as_setHangarMenuDataS(self, data):
        """
        :param data: Represented by HangarMenuVO (AS)
        """
        return self.flashObject.as_setHangarMenuData(data) if self._isDAAPIInited() else None

    def as_setButtonCounterS(self, btnAlias, value):
        return self.flashObject.as_setButtonCounter(btnAlias, value) if self._isDAAPIInited() else None

    def as_removeButtonCounterS(self, btnAlias):
        return self.flashObject.as_removeButtonCounter(btnAlias) if self._isDAAPIInited() else None