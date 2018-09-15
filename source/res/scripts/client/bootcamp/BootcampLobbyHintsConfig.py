# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/bootcamp/BootcampLobbyHintsConfig.py
from gui.Scaleform.framework import ViewTypes
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS

class BootcampLobbyHintsConfig():
    objects = {'ResearchButton': {'viewAlias': VIEW_ALIAS.LOBBY_HANGAR,
                        'path': 'vehResearchPanel.button'},
     'FightButton': {'viewAlias': VIEW_ALIAS.LOBBY,
                     'path': 'header.fightBtn'},
     'ResearchNode': {'viewAlias': VIEW_ALIAS.BOOTCAMP_LOBBY_RESEARCH,
                      'path': 'researchItems:id=asInt.button',
                      'asInt': 0},
     'ResearchNodeTankII': {'viewAlias': VIEW_ALIAS.BOOTCAMP_LOBBY_RESEARCH,
                            'path': 'researchItems:id=asInt.button',
                            'asInt': 0},
     'DialogAccept': {'viewAlias': VIEW_ALIAS.SIMPLE_DIALOG,
                      'path': 'secondBtn'},
     'VehicleBuyAccept': {'viewAlias': VIEW_ALIAS.BOOTCAMP_VEHICLE_BUY_WINDOW,
                          'path': 'submitBtn'},
     'VehicleBuyAcademy': {'viewAlias': VIEW_ALIAS.BOOTCAMP_VEHICLE_BUY_WINDOW,
                           'path': 'content.academyBtn'},
     'HangarButton': {'viewAlias': VIEW_ALIAS.LOBBY,
                      'path': 'header.mainMenuButtonBar:value=ButtonID',
                      'ButtonID': 'hangar',
                      'padding': {'left': -50,
                                  'right': 50},
                      'hideBorder': True},
     'TechTreeButton': {'viewAlias': VIEW_ALIAS.LOBBY,
                        'path': 'header.mainMenuButtonBar:value=ButtonID',
                        'ButtonID': 'bootcampLobbyTechTree',
                        'padding': {'left': -50,
                                    'right': 50},
                        'hideBorder': True},
     'TechNodeUsa': {'viewAlias': VIEW_ALIAS.BOOTCAMP_LOBBY_TECHTREE,
                     'path': 'nationTree:id=asInt.hit',
                     'asInt': 0},
     'VehiclePreviewUnlockButton': {'viewAlias': VIEW_ALIAS.BOOTCAMP_VEHICLE_PREVIEW,
                                    'path': 'bottomPanel.buyingPanel.buyBtn'},
     'AmmunitionOptionalDevices': {'viewAlias': VIEW_ALIAS.LOBBY_HANGAR,
                                   'path': 'ammunitionPanel.optionalDevice1',
                                   'padding': {'left': 0,
                                               'right': 98,
                                               'top': 0,
                                               'bottom': -3}},
     'AmmunitionEquipment': {'viewAlias': VIEW_ALIAS.LOBBY_HANGAR,
                             'path': 'ammunitionPanel.equipment1',
                             'padding': {'left': 0,
                                         'right': 98,
                                         'top': 0,
                                         'bottom': -3}},
     'ServiceSlot': {'viewAlias': VIEW_ALIAS.BOOTCAMP_TECHNICAL_MAINTENANCE,
                     'path': 'eqItem1.slotBg'},
     'ServiceSlotRepairOption': {'viewAlias': VIEW_ALIAS.BOOTCAMP_TECHNICAL_MAINTENANCE,
                                 'path': 'eqItem1.select:id=asInt',
                                 'asInt': 0,
                                 'padding': {'bottom': -2,
                                             'right': -4}},
     'ServiceAccept': {'viewAlias': VIEW_ALIAS.BOOTCAMP_TECHNICAL_MAINTENANCE,
                       'path': 'applyBtn'},
     'FirstTankman': {'viewAlias': VIEW_ALIAS.LOBBY_HANGAR,
                      'path': 'crew.list:slot=indexId',
                      'indexId': 0,
                      'hideBorder': True},
     'PersonalCaseOption': {'viewAlias': VIEW_ALIAS.LOBBY_HANGAR,
                            'path': 'crew.list:slot=indexId.:personalCase=bool',
                            'indexId': 0,
                            'bool': True},
     'PersonalCaseSkill': {'viewAlias': VIEW_ALIAS.BOOTCAMP_PERSONAL_CASE,
                           'path': 'view.currentView.modifiers:title=skillId',
                           'skillId': '',
                           'padding': {'right': -1,
                                       'bottom': -1}},
     'PersonalCaseSkillSelect': {'viewAlias': VIEW_ALIAS.BOOTCAMP_PERSONAL_CASE,
                                 'path': 'view.currentView.selectBtn'},
     'PersonalCaseClose': {'viewAlias': VIEW_ALIAS.BOOTCAMP_PERSONAL_CASE,
                           'path': 'closeBtn'},
     'OptionalDevice': {'viewAlias': VIEW_ALIAS.BOOTCAMP_FITTING_SELECT_POPOVER,
                        'path': 'itemsList:id=asInt',
                        'asInt': 249,
                        'padding': {'bottom': -8}},
     'OptionalDeviceSmall': {'viewAlias': VIEW_ALIAS.BOOTCAMP_FITTING_SELECT_POPOVER,
                             'path': 'itemsList:id=asInt',
                             'asInt': 249,
                             'padding': {'right': -24,
                                         'bottom': -8}},
     'QuestsControl': {'viewAlias': VIEW_ALIAS.LOBBY_HANGAR,
                       'path': 'header.btnCommonQuests',
                       'padding': {'left': 0,
                                   'right': 0},
                       'customHint': 'BCLobbyHintMissionUI'},
     'HangarHeader': {'viewAlias': VIEW_ALIAS.LOBBY_HANGAR,
                      'path': 'header',
                      'padding': {'left': 0,
                                  'right': 0}},
     'BattleType': {'viewAlias': VIEW_ALIAS.LOBBY,
                    'path': 'header.headerButtonBar:id=ButtonID',
                    'ButtonID': 'battleSelector',
                    'padding': {'left': 8,
                                'right': 0}},
     'RandomBattle': {'viewAlias': VIEW_ALIAS.BOOTCAMP_BATTLE_TYPE_SELECT_POPOVER,
                      'path': 'list:data=ButtonID',
                      'ButtonID': 'random',
                      'padding': {'left': 0,
                                  'right': 0}},
     'SecondTank': {'viewAlias': VIEW_ALIAS.LOBBY_HANGAR,
                    'path': 'carouselContainer.carousel.scrollList:id=TankIndex',
                    'TankIndex': '2'},
     'AmmunitionSlot': {'viewAlias': VIEW_ALIAS.LOBBY_HANGAR,
                        'path': 'ammunitionPanel.engine',
                        'customHint': 'BCLobbySlotUI'},
     'SkillSlot': {'viewAlias': VIEW_ALIAS.BOOTCAMP_PERSONAL_CASE,
                   'path': 'skills_mc:name=skillId',
                   'skillId': '',
                   'customHint': 'BCLobbySlotUI'},
     'InBattleRepairKit': {'viewAlias': VIEW_ALIAS.BOOTCAMP_BATTLE_PAGE,
                           'path': 'consumablesPanel:index=slotIndex',
                           'slotIndex': 3,
                           'padding': {'left': 6,
                                       'right': -6,
                                       'top': 28,
                                       'bottom': -6}},
     'InBattleHealKit': {'viewAlias': VIEW_ALIAS.BOOTCAMP_BATTLE_PAGE,
                         'path': 'consumablesPanel:index=slotIndex',
                         'slotIndex': 4,
                         'padding': {'left': 6,
                                     'right': -6,
                                     'top': 28,
                                     'bottom': -6}},
     'InBattleExtinguisher': {'viewAlias': VIEW_ALIAS.BOOTCAMP_BATTLE_PAGE,
                              'path': 'consumablesPanel:index=slotIndex',
                              'slotIndex': 5,
                              'padding': {'left': 6,
                                          'right': -6,
                                          'top': 28,
                                          'bottom': -6}},
     'Consumables': {'viewAlias': VIEW_ALIAS.BOOTCAMP_BATTLE_PAGE,
                     'path': 'consumablesPanel',
                     'padding': {'left': 7,
                                 'right': -7,
                                 'top': 16,
                                 'bottom': -8},
                     'customHint': 'BCHudHintUI'},
     'FragCorrelationBar': {'viewAlias': VIEW_ALIAS.BOOTCAMP_BATTLE_PAGE,
                            'path': 'fragCorrelationBar',
                            'padding': {'left': 310,
                                        'right': -310,
                                        'bottom': -4},
                            'customHint': 'BCHudHintUI',
                            'hideBorder': True},
     'Minimap': {'viewAlias': VIEW_ALIAS.BOOTCAMP_BATTLE_PAGE,
                 'path': 'minimap.mapHit',
                 'padding': {'left': -15,
                             'top': -15,
                             'right': 2,
                             'bottom': 2},
                 'customHint': 'BCHudHintUI'},
     'FragCorrelationBarAppear': {'viewAlias': VIEW_ALIAS.BOOTCAMP_BATTLE_PAGE,
                                  'path': 'fragCorrelationBar',
                                  'padding': {'left': 340,
                                              'right': -340,
                                              'bottom': -4},
                                  'customHint': 'BCAppearHintUI'},
     'ConsumablesAppear': {'viewAlias': VIEW_ALIAS.BOOTCAMP_BATTLE_PAGE,
                           'path': 'consumablesPanel',
                           'padding': {'left': 7,
                                       'right': -7,
                                       'top': 16,
                                       'bottom': -8},
                           'customHint': 'BCAppearHintUI'},
     'MinimapAppear': {'viewAlias': VIEW_ALIAS.BOOTCAMP_BATTLE_PAGE,
                       'path': 'minimap.background',
                       'padding': {'left': 7,
                                   'right': -7,
                                   'top': 16,
                                   'bottom': -8},
                       'customHint': 'BCAppearHintUI'},
     'ConsumableSlot1': {'viewAlias': VIEW_ALIAS.BOOTCAMP_BATTLE_PAGE,
                         'path': 'consumablesPanel:index=slotIndex.iconLoader',
                         'slotIndex': 0},
     'ConsumableSlot4': {'viewAlias': VIEW_ALIAS.BOOTCAMP_BATTLE_PAGE,
                         'path': 'consumablesPanel:index=slotIndex.iconLoader',
                         'slotIndex': 3,
                         'customHint': 'BCHudHintUI'},
     'ConsumableSlot5': {'viewAlias': VIEW_ALIAS.BOOTCAMP_BATTLE_PAGE,
                         'path': 'consumablesPanel:index=slotIndex.iconLoader',
                         'slotIndex': 4,
                         'customHint': 'BCHudHintUI'},
     'ConsumableSlot6': {'viewAlias': VIEW_ALIAS.BOOTCAMP_BATTLE_PAGE,
                         'path': 'consumablesPanel:index=slotIndex.iconLoader',
                         'slotIndex': 5,
                         'customHint': 'BCHudHintUI'},
     'DamagePanelHealthbar': {'viewAlias': VIEW_ALIAS.BOOTCAMP_BATTLE_PAGE,
                              'path': 'damagePanel.healthBar'},
     'LoadingRightButton': {'viewAlias': VIEW_ALIAS.BOOTCAMP_INTRO_VIDEO,
                            'path': 'btnRight',
                            'padding': {'left': 10,
                                        'right': -10,
                                        'top': 10,
                                        'bottom': -11},
                            'customHint': 'BCHudHintUI'},
     'LoadingLeftButton': {'viewAlias': VIEW_ALIAS.BOOTCAMP_INTRO_VIDEO,
                           'path': 'btnLeft',
                           'padding': {'left': 10,
                                       'right': -10,
                                       'top': 10,
                                       'bottom': -11},
                           'customHint': 'BCHudHintUI'},
     'StartBattleButton': {'viewAlias': VIEW_ALIAS.BOOTCAMP_INTRO_VIDEO,
                           'path': 'loadingProgress.btnSelect',
                           'padding': {'left': 13,
                                       'right': -13,
                                       'top': 13,
                                       'bottom': -13},
                           'hideBorder': True}}

    def getItems(self):
        return self.objects


g_bootcampHintsConfig = BootcampLobbyHintsConfig()