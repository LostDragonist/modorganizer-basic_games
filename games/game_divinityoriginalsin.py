# -*- encoding: utf-8 -*-

import mobase

from ..basic_game import BasicGame
from ..basic_features import BasicGameSaveGameInfo


class DivinityOriginalSinGame(BasicGame):
    Name = "Divinity Original Sin Support Plugin"
    Author = "LostDragonist"
    Version = "1.0.0"

    GameName = "Divinity: Original Sin (Classic)"
    GameShortName = "divinityoriginalsin"
    GameNexusName = "divinityoriginalsin"
    GameValidShortNames = ["divinityoriginalsin"]
    GameNexusId = 573
    GameSteamId = [230230]
    GameBinary = "Shipping/EoCApp.exe"
    GameDataPath = "Data"
    GameSaveExtension = "lsv"  # Not confirmed
    GameDocumentsDirectory = (
        "%USERPROFILE%/Documents/Larian Studios/Divinity Original Sin/PlayerProfiles"
    )
    GameSavesDirectory = (
        "%USERPROFILE%/Documents/Larian Studios/Divinity Original Sin/PlayerProfiles"
    )

    def init(self, organizer: mobase.IOrganizer):
        super().init(organizer)
        self._featureMap[mobase.SaveGameInfo] = BasicGameSaveGameInfo(
            lambda s: s.replace(".lsv", ".png")  # Not confirmed
        )
        return True