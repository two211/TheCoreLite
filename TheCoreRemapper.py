##################################################
#
# Filename: TheCoreRemapper.py
# Author: Jonny Weiss
# Description: Script to take the LM layouts of TheCore and generate the other 44 layouts.
# Change Log:
#   9/25/12 - Created
#   9/26/12 - Finished initial functionality
#
################################################## 
from configparser import SafeConfigParser
import os, sys

TRANSLATE = not "US" in sys.argv
ONLY_SEED = "LM" in sys.argv

GLOBAL = -1
LMM = 0
RMM = 1
RM = 2

SHOW_HOTS_MISSING = True
SHOW_DUPLICATES = False
VERIFY_ALL = False

CAMERA_KEYS = ['CameraSave0', 'CameraSave1', 'CameraSave2', 'CameraSave3', 'CameraSave4', 'CameraSave5', 'CameraSave6', 'CameraSave7',
               'CameraView0', 'CameraView1', 'CameraView2', 'CameraView3', 'CameraView4', 'CameraView5', 'CameraView6', 'CameraView7']

# ZERG_CONTROL_GROUP_SPECIAL = ['ControlGroupAssign7']

CONTROL_GROUP_KEYS = ['ControlGroupAppend0', 'ControlGroupAppend1', 'ControlGroupAppend2', 'ControlGroupAppend3', 'ControlGroupAppend4', 'ControlGroupAppend5', 'ControlGroupAppend6', 'ControlGroupAppend7', 'ControlGroupAppend8', 'ControlGroupAppend9',
                      'ControlGroupAssign0', 'ControlGroupAssign1', 'ControlGroupAssign2', 'ControlGroupAssign3', 'ControlGroupAssign4', 'ControlGroupAssign5', 'ControlGroupAssign6', 'ControlGroupAssign7', 'ControlGroupAssign8', 'ControlGroupAssign9',
                      'ControlGroupRecall0', 'ControlGroupRecall1', 'ControlGroupRecall2', 'ControlGroupRecall3', 'ControlGroupRecall4', 'ControlGroupRecall5', 'ControlGroupRecall6', 'ControlGroupRecall7', 'ControlGroupRecall8', 'ControlGroupRecall9',
                      'ControlGroupAppendAndSteal0', 'ControlGroupAppendAndSteal1', 'ControlGroupAppendAndSteal2', 'ControlGroupAppendAndSteal3', 'ControlGroupAppendAndSteal4', 'ControlGroupAppendAndSteal5', 'ControlGroupAppendAndSteal6', 'ControlGroupAppendAndSteal7', 'ControlGroupAppendAndSteal8', 'ControlGroupAppendAndSteal9',
                      'ControlGroupAssignAndSteal0', 'ControlGroupAssignAndSteal1', 'ControlGroupAssignAndSteal2', 'ControlGroupAssignAndSteal3', 'ControlGroupAssignAndSteal4', 'ControlGroupAssignAndSteal5', 'ControlGroupAssignAndSteal6', 'ControlGroupAssignAndSteal7', 'ControlGroupAssignAndSteal8', 'ControlGroupAssignAndSteal9', ]


# Add to this please.
GENERAL_KEYS = ['FPS', 'Music', 'Sound', 'PTT', 'DialogDismiss', 'MenuAchievements', 'MenuGame', 'MenuMessages', 'MenuSocial',
                'LeaderResources', 'LeaderIncome', 'LeaderSpending', 'LeaderUnits', 'LeaderUnitsLost', 'LeaderProduction', 'LeaderArmy',
                'LeaderAPM', 'LeaderCPM', 'ObserveAllPlayers', 'ObserveAutoCamera', 'ObserveClearSelection', 'ObservePlayer0', 'ObservePlayer1',
                'ObservePlayer2', 'ObservePlayer3', 'ObservePlayer4', 'ObservePlayer5', 'ObservePlayer6', 'ObservePlayer7', 'ObservePlayer8',
                'ObservePlayer9', 'ObservePlayer10', 'ObservePlayer11', 'ObservePlayer12', 'ObservePlayer13', 'ObservePlayer14', 'ObservePlayer15',
                'ObserveSelected', 'ObservePreview', 'ObserveStatusBars', 'StatPanelResources', 'StatPanelArmySupply', 'StatPanelUnitsLost', 'StatPanelAPM', 'StatPanelCPM',
                'ToggleWorldPanel', 'CinematicSkip', 'AlertRecall', 'CameraFollow', 'GameTooltipsOn', 'IdleWorker', 'MinimapColors', 'MinimapPing',
                'MinimapTerrain', 'PauseGame', 'QuickPing', 'QuickSave', 'ReplayPlayPause', 'ReplayRestart', 'ReplaySkipBack', 'ReplaySkipNext', 'ReplaySpeedDec',
                'ReplaySpeedInc', 'ReplayStop', 'ReplayHide', 'SelectionCancelDrag', 'SubgroupNext', 'SubgroupPrev', 'TeamResources', 'TownCamera', 'WarpIn',
                'Cancel', 'CancelCocoon', 'CancelMutateMorph', 'CancelUpgradeMorph', 'ChatCancel',
                'ChatAll', 'ChatDefault', 'ChatIndividual', 'ChatRecipient', 'ChatAllies',
                'CameraTurnLeft', 'CameraTurnRight', 'CameraCenter',
                'StatusAll', 'StatusOwner', 'StatusEnemy', 'StatusAlly', 'MenuHelp', 'NamePanel', 'ArmySelect', 'SelectBuilder', 'ToggleVersusModeSides']

EXCLUDE_MAPPING = ['AllowSetConflicts']

SAME_CHECKS = [['Pylon/Probe', 'SupplyDepot/SCV', 'SupplyDepotDrop/SCV'],
               ['Assimilator/Probe', 'Extractor/Drone', 'Refinery/SCV', 'AutomatedRefinery/SCV', 'AutomatedExtractor/Drone'],
               ['Gateway/Probe', 'Barracks/SCV'],
               ['Nexus/Probe', 'Hatchery/Drone', 'CommandCenter/SCV', 'CommandCenterOrbRelay/SCV'],
               ['Forge/Probe', 'EvolutionChamber/Drone', 'EngineeringBay/SCV'],
               ['RoboticsFacility/Probe', 'Factory/SCV'],
               ['Stargate/Probe', 'Spire/Drone', 'Starport/SCV'],
               ['TwilightCouncil/Probe', 'Armory/SCV'],
               ['FleetBeacon/Probe', 'FusionCore/SCV'],
               ['ProtossGroundWeaponsLevel1/Forge', 'TerranInfantryWeaponsLevel1/EngineeringBay', 'TerranInfantryWeaponsUltraCapacitorsLevel1/EngineeringBay', 'TerranInfantryWeaponsUltraCapacitorsLevel2/EngineeringBay', 'TerranInfantryWeaponsUltraCapacitorsLevel3/EngineeringBay'],
               ['ProtossGroundArmorLevel1/Forge', 'TerranInfantryArmorLevel1/EngineeringBay', 'zerggroundarmor1/EvolutionChamber', 'TerranInfantryArmorVanadiumPlatingLevel1/EngineeringBay', 'TerranInfantryArmorVanadiumPlatingLevel2/EngineeringBay', 'TerranInfantryArmorVanadiumPlatingLevel3/EngineeringBay'],
               ['ProtossAirWeaponsLevel1/CyberneticsCore', 'TerranShipWeaponsLevel1/Armory', 'zergflyerattack1'],
               ['TerranShipWeaponsLevel1/Armory', 'TerranShipWeaponsUltraCapacitorsLevel1/Armory', 'TerranShipWeaponsUltraCapacitorsLevel2/Armory', 'TerranShipWeaponsUltraCapacitorsLevel3/Armory'],
               ['ProtossAirArmorLevel1/CyberneticsCore', 'TerranShipPlatingLevel1/Armory', 'zergflyerarmor1'],
               ['TerranShipPlatingLevel1/Armory', 'TerranShipPlatingVanadiumPlatingLevel1/Armory', 'TerranShipPlatingVanadiumPlatingLevel2/Armory', 'TerranShipPlatingVanadiumPlatingLevel3/Armory'],
               ['Stim', 'StimFirebat/Firebat', 'StimFirebat/DevilDog'],
               ['Heal/Medivac', 'BonesHeal/Stetmann', 'NanoRepair/ScienceVessel', 'MedicHeal/Medic', 'MercMedicHeal/MercMedic'],
               ['CloakOnBanshee', 'RogueGhostCloak/Spectre', 'WraithCloakOn/Wraith'],
               ['CloakOff', 'WraithCloakOff/Wraith'],
#               ['WeaponsFree/Ghost','SpectreWeaponsFree/Spectre'], thanks to HotS Spectre key now unbinds if set to same as HoldFire, Ghost HoldFire & weapons free toggle works correctly
               ['GhostHoldFire/Ghost', 'SpectreHoldFire/Spectre'],
               ['NukeArm/GhostAcademy', 'SpectreNukeArm/GhostAcademy'],
               ['NukeCalldown/Ghost', 'SpectreNukeCalldown/Spectre', 'HeroNukeCalldown/Nova', 'HeroNukeCalldown/Tosh', 'OdinNukeCalldown/Odin'],
               ['BunkerLoad', 'HerculesLoad/Hercules'],
               ['BunkerUnloadAll', 'HerculesUnloadAll/Hercules'],
               ['Reactor/Barracks', 'Reactor/BarracksFlying', 'Reactor/Factory', 'Reactor/FactoryFlying', 'Reactor/Starport', 'Reactor/StarportFlying'],
               ['TechLabBarracks/Barracks', 'TechLabBarracks/BarracksFlying', 'TechReactor/Barracks', 'TechReactor/BarracksFlying', 'TechLabFactory/Factory', 'BuildTechLabFactory/FactoryFlying', 'TechReactor/Factory', 'TechReactor/FactoryFlying', 'TechLabStarport/Starport', 'BuildTechLabStarport/StarportFlying', 'TechReactor/Starport', 'TechReactor/StarportFlying'],
#               ['Ghost/Barracks','Spectre/Barracks'], thanks to HotS campaign these can no longer be on the same key
               ['Raven/Starport', 'BuildScienceVessel/Starport'],
               ['EMP/Ghost', 'UltrasonicPulse/Spectre'],
               ['Snipe/Ghost', 'NovaSnipe/Nova', 'Obliterate/Spectre'],
               ['Lair/Hatchery', 'Hive/Lair', 'LurkerDen/HydraliskDen', 'ImpalerDen/HydraliskDen'],
               ['MassRecall/Mothership', 'MassRecall/Artanis', 'MothershipMassRecall/Mothership', 'MothershipCoreMassRecall/MothershipCore'],
               ['Vortex/Mothership', 'Vortex/Artanis'],
               ['Mothership/Nexus', 'MothershipCore/Nexus'],
               ['AutoTurret/Raven', 'BuildAutoTurret/Raven'],
               ['PointDefenseDrone/Raven', 'BuildPointDefenseDrone/Raven'],
               ['ResearchShieldWall/BarracksTechLab', 'ResearchShieldWall/BarracksTechReactor'],
               ['Stimpack/BarracksTechLab', 'Stimpack/BarracksTechReactor'],
               ['ResearchPunisherGrenades/BarracksTechLab', 'ResearchPunisherGrenades/BarracksTechReactor', 'ResearchJackhammerConcussionGrenade/BarracksTechLab', 'ResearchJackhammerConcussionGrenade/BarracksTechReactor'],
               ['ReaperSpeed/BarracksTechLab', 'ReaperSpeed/BarracksTechReactor', 'ResearchG4Charge/BarracksTechLab', 'ResearchG4Charge/BarracksTechReactor'],
               ['ResearchIncineratorNozzles/BarracksTechLab', 'ResearchIncineratorNozzles/BarracksTechReactor'],
               ['ResearchStabilizerMedPacks/BarracksTechLab', 'ResearchStabilizerMedPacks/BarracksTechReactor'],
               ['ResearchCerberusMines/FactoryTechLab', 'ResearchCerberusMines/FactoryTechReactor'],
               ['ResearchHighCapacityBarrels/FactoryTechLab', 'ResearchHighCapacityBarrels/FactoryTechReactor'],
               ['ResearchMultiLockTargetingSystem/FactoryTechLab', 'ResearchMultiLockTargetingSystem/FactoryTechReactor'],
               ['ResearchRegenerativeBioSteel/FactoryTechLab', 'ResearchRegenerativeBioSteel/FactoryTechReactor'],
               ['ResearchStrikeCannons/FactoryTechLab', 'ResearchStrikeCannons/FactoryTechReactor'],
               ['ResearchSiegeTech/FactoryTechLab', 'ResearchSiegeTech/FactoryTechReactor', 'ResearchShapedBlast/FactoryTechLab', 'ResearchShapedBlast/FactoryTechReactor'],
               ['ResearchMedivacEnergyUpgrade/StarportTechLab', 'ResearchMedivacEnergyUpgrade/StarportTechReactor'],
               ['ResearchBansheeCloak/StarportTechLab', 'ResearchBansheeCloak/StarportTechReactor'],
               ['ResearchDurableMaterials/StarportTechLab', 'ResearchDurableMaterials/StarportTechReactor'],
               ['ResearchSeekerMissile/StarportTechLab', 'ResearchSeekerMissile/StarportTechReactor'],
               ['ResearchRavenEnergyUpgrade/StarportTechLab', 'ResearchRavenEnergyUpgrade/StarportTechReactor'],
               ['WraithCloak/StarportTechLab', 'WraithCloak/StarportTechReactor'],
               ['Baneling/Zergling', 'Baneling/Zergling2', 'Baneling/HotSRaptor', 'Baneling/HotSSwarmling', 'MorphtoHunter/HotSRaptor', 'MorphtoHunter/HotSSwarmling', 'MorphtoSplitterling/HotSRaptor', 'MorphtoSplitterling/HotSSwarmling'],
               ['DisableBuildingAttack/Baneling', 'DisableBuildingAttack/baneling', 'DisableBuildingAttack/baneling2', 'DisableBuildingAttack/HotSHunter', 'DisableBuildingAttack/HotSSplitterlingBig'],
               ['EnableBuildingAttack/Baneling', 'EnableBuildingAttack/baneling', 'EnableBuildingAttack/baneling2', 'EnableBuildingAttack/HotSHunter', 'EnableBuildingAttack/HotSSplitterlingBig'],
               ['Explode/Baneling', 'Explode/BanelingBurrowed', 'Explode/baneling', 'Explode/baneling2', 'Explode/HotSSplitterlingBig', 'Explode/HotSSplitterlingBigBurrowed', 'Explode/HotSHunter', 'Explode/HotSHunterBurrowed'],
               ['ForceField/Sentry', 'ForceField2/Sentry2'],
               ['FungalGrowth/Infestor', 'FungalGrowth/Infestor2'],
               ['GuardianShield/Sentry', 'GuardianShield/Sentry2'],
               ['Hallucination/Sentry', 'Hallucination/Sentry2'],
               ['Heal/Medivac', 'Heal/Medivac2'],
               ['InfestedTerrans/Infestor', 'InfestedTerrans/Infestor2'],
               ['NeuralParasite/Infestor', 'NeuralParasite/Infestor2', 'NPSwarm/Infestor'],
               ['Baneling/Zergling', 'Baneling/Zergling2', 'Baneling/HotSRaptor', 'Baneling/HotSSwarmling'],
               ['Apocalypse/K5Kerrigan', 'K5DropPods/K5Kerrigan', 'K5Leviathan/K5Kerrigan'],
               ['MindBolt/K5Kerrigan', 'MindBolt/KerriganGhostLab', 'PrimalSlash/K5Kerrigan'],
               ['PrimalHeal/K5Kerrigan', 'SpawnBanelings/K5Kerrigan', 'WildMutation/K5Kerrigan'],
               ['PsiStrike/K5Kerrigan', 'PsionicLift/K5Kerrigan', 'PsionicLift/KerriganGhostLab'],
               ['YamatoGun', 'SJHyperionYamato/SJHyperion','HyperionVoidCoopYamatoCannon/HyperionVoidCoop'],
               ['Hydralisk/Larva', 'MorphToHydraliskImpaler/Larva', 'MorphToHydraliskLurker/Larva'],
               ['Infestor/Larva', 'MorphtoDefiler/Larva'],
               ['Mutalisk/Larva', 'MorphToMutaliskBroodlord/Larva', 'MorphToMutaliskViper/Larva'],
               ['Roach/Larva', 'MorphToVile/Larva', 'MorphToCorpser/Larva'],
               ['SwarmHostMP/Larva', 'MorphToSwarmHostSplitA/Larva', 'MorphToSwarmHostSplitB/Larva'],
               ['Ultralisk/Larva', 'MorphToHotSNoxious/Larva', 'MorphToHotSTorrasque/Larva'],
               ['Viper/Larva', 'Aberration/Larva'],
               ['Zergling/Larva', 'MorphToSwarmling/Larva', 'MorphToRaptor/Larva'],
               ['LocustLaunch/SwarmHostBurrowed', 'LocustFlyingLaunch/SwarmHostSplitABurrowed', 'LocustFlyingLaunch/SwarmHostSplitARooted', 'LocustLaunch/SwarmHostRooted', 'LocustLaunchCreeper/SwarmHostSplitBBurrowed', 'LocustLaunchCreeper/SwarmHostSplitBRooted'],
               ['BurrowDown', 'BurrowHydraliskImpalerDown', 'BurrowHydraliskLurkerDown', 'ImpalerBurrowDown', 'LurkerBurrowDown'],
               ['BurrowUp', 'BurrowHydraliskImpalerUp', 'BurrowHydraliskLurkerUp', 'ImpalerBurrowUp', 'LurkerBurrowUp'],  # 'SwarmHostUprootUnburrow/SwarmHostBurrowed','SwarmHostUprootUnburrow/SwarmHostSplitABurrowed','SwarmHostUprootUnburrow/SwarmHostSplitBBurrowed'
               ['SwarmHostDeepBurrow/SwarmHostSplitB', 'SwarmHostDeepBurrow/SwarmHostSplitBBurrowed', 'SwarmHostDeepBurrow/SwarmHostSplitBRooted'],
               ['SwarmHostRoot/SwarmHost', 'SwarmHostRoot/SwarmHostSplitA', 'SwarmHostRoot/SwarmHostSplitB'],
               ['SwarmHostUproot/SwarmHostRooted', 'SwarmHostUproot/SwarmHostSplitARooted', 'SwarmHostUproot/SwarmHostSplitBRooted'],
               ['HydraliskFrenzy/Hydralisk', 'HydraliskFrenzy/HydraliskImpaler', 'HydraliskFrenzy/HydraliskLurker'],
               ['Impaler/HydraliskImpaler', 'Lurker/HydraliskLurker'],
               ['BroodLord/Corruptor', 'BroodLord/MutaliskBroodlord', 'Viper/MutaliskViper'],
               ['BlindingCloud/Viper', 'DisablingCloud/Viper'],
               ['ViperConsume/Viper', 'ViperConsumption/Viper'],
               ['BurrowChargeMP/Ultralisk', 'BurrowChargeCampaign/Ultralisk', 'BurrowChargeCampaign/HotSTorrasque', 'BurrowChargeCampaignNoxious/HotSNoxious'],
               ['Transfusion/Queen', 'Transfusion/Queen2', 'QueenBurstHeal/Queen'],
               ['GrowHugeQueen/LargeSwarmQueen', 'GrowLargeQueen/SwarmQueen', 'GrowSwarmQueen/LarvalQueen'],
               ['SwarmQueenHydralisk/HugeSwarmQueen', 'SwarmQueenHydralisk/SwarmQueenEgg', 'SwarmQueenHydraliskImpaler/HugeSwarmQueen', 'SwarmQueenHydraliskImpaler/LargeSwarmQueen', 'SwarmQueenHydraliskImpaler/SwarmQueen', 'SwarmQueenHydraliskLurker/HugeSwarmQueen', 'SwarmQueenHydraliskLurker/LargeSwarmQueen', 'SwarmQueenHydraliskLurker/SwarmQueen'],
               ['ParasiticInvasion/LarvalQueen', 'SwarmQueenParasiticInvasion/HugeSwarmQueen', 'SwarmQueenParasiticInvasion/LargeSwarmQueen', 'SwarmQueenParasiticInvasion/SwarmQueen'],
               ['SwarmQueenCorpser/LargeSwarmQueen', 'SwarmQueenCorpser/HugeSwarmQueen', 'SwarmQueenCorpser/SwarmQueen', 'SwarmQueenRoach/HugeSwarmQueen', 'SwarmQueenRoach/LargeSwarmQueen', 'SwarmQueenRoach/SwarmQueenEgg', 'SwarmQueenVile/HugeSwarmQueen', 'SwarmQueenVile/LargeSwarmQueen', 'SwarmQueenVile/SwarmQueen'],
               ['SwarmQueenRaptor/HugeSwarmQueen', 'SwarmQueenRaptor/LargeSwarmQueen', 'SwarmQueenRaptor/SwarmQueen', 'SwarmQueenSwarmling/HugeSwarmQueen', 'SwarmQueenSwarmling/LargeSwarmQueen', 'SwarmQueenSwarmling/SwarmQueen', 'SwarmQueenZergling/HugeSwarmQueen', 'SwarmQueenZergling/LargeSwarmQueen', 'SwarmQueenZergling/SwarmQueen', 'SwarmQueenZergling/SwarmQueenEgg'],
               ['GreaterSpire/Spire', 'GreaterSpireBroodlord/Spire'],
               ['RespawnZergling/Hatchery', 'RespawnZergling/Hive', 'RespawnZergling/Lair'],
               # ['GenerateCreep/Overlord','StopGenerateCreep/Overlord']]
               ['VoidSentryShieldRepair/Sentry','VoidSentryShieldRepairDouble/SentryAiur'],
               ['UpgradeToWarpGate/Gateway','UpgradeToRoboticsFacilityWarp/RoboticsFacility','UpgradeToStargateWarp/Stargate'],
               ['MorphBackToGateway/WarpGate','MorphBackToRoboticsFacility/RoboticsFacilityWarp',],
               ['Vortex/Mothership','Vortex/Artanis','VoidSentryBlackHole/SOAMothershipv4','TemporalField/Mothership','TemporalField/MothershipCore'],
               ['250mmStrikeCannons/Thor','250mmStrikeCannons/ThorWreckageSwann'],
               ['SelfRepair/Thor','SelfRepair/ThorWreckageSwann'],
               ['StopPlanetaryFortress/PlanetaryFortress','Stop'],
               ['Salvage/Bunker','Salvage/MissileTurret','Salvage/KelMorianGrenadeTurret','Salvage/PerditionTurret','Salvage/KelMorianMissileTurret'],
               ['Hyperjump/Battlecruiser','HyperionVoidCoopHyperjump/HyperionVoidCoop','HyperjumpHercules/Hercules'],
               ['Charge/Zealot','Charge/ZealotAiur','Charge/ZealotPurifier','VoidZealotShadowCharge/ZealotShakuras'],
               ['ResearchIncineratorGauntlets/BarracksTechLab','ResearchIncineratorGauntlets/BarracksTechReactor'],
               ['ResearchJuggernautPlating/BarracksTechLab','ResearchJuggernautPlating/BarracksTechReactor'],['ResearchStabilizerMedpacks/BarracksTechLab','ResearchStabilizerMedpacks/BarracksTechReactor'],
               ['ResearchHellbatHellArmor/FactoryTechLab','ResearchHellbatHellArmor/FactoryTechReactor'],
               ['ResearchAresClassTargetingSystem/FactoryTechLab','ResearchAresClassTargetingSystem/FactoryTechReactor'],
               ['ResearchMultiLockWeaponsSystem/FactoryTechLab','ResearchMultiLockWeaponsSystem/FactoryTechReactor'],
               ['ResearchMaelstromRounds/FactoryTechLab','ResearchMaelstromRounds/FactoryTechReactor'],
               ['ResearchLockOnRangeUpgrade/FactoryTechLab','ResearchLockOnRangeUpgrade/FactoryTechReactor'],
               ['ResearchCycloneLockOnDamageUpgrade/FactoryTechLab','ResearchCycloneLockOnDamageUpgrade/FactoryTechReactor'],
               ['Research330mmBarrageCannon/FactoryTechLab','Research330mmBarrageCannon/FactoryTechReactor'],
               ['ResearchShockwaveMissileBattery/StarportTechLab','ResearchShockwaveMissileBattery/StarportTechReactor'],
               ['ResearchPhobosClassWeaponsSystem/StarportTechLab','ResearchPhobosClassWeaponsSystem/StarportTechReactor'],
               ['ResearchRipwaveMissiles/StarportTechLab','ResearchRipwaveMissiles/StarportTechReactor'],
               ['SummonNydusWorm/NydusNetwork','ZagaraVoidCoopNydusWorm/NydusNetwork'],
               ['Queen','QueenCoop'],
               ['BuildCreepTumor/Queen',CBuildCreepTumor/QueenCoop'],
               ['MorphMorphalisk/Queen','MorphMorphalisk/QueenCoop'],
               ['Transfusion/QueenCoop','Transfusion/QueenCoop'],
               ['Immortal/RoboticsFacility','Immortal/RoboticsFacilityWarp'],
               ['Colossus/RoboticsFacility','Colossus/RoboticsFacilityWarp'],
               ['Observer/RoboticsFacility','Observer/RoboticsFacilityWarp']]
               
CONFLICT_CHECKS = [['Cancel', 'Stop', 'Rally', 'Probe/Nexus', 'TimeWarp/Nexus', 'Mothership/Nexus'],
                   ['Cancel', 'Stop', 'Attack', 'Rally', 'Probe/Nexus', 'TimeWarp/Nexus', 'MothershipCore/Nexus'],  # Nexus HotS
                   ['SelectBuilder', 'Cancel', 'Lift', 'Rally', 'CommandCenterLoad', 'CommandCenterUnloadAll', 'SCV', 'OrbitalCommand/CommandCenter', 'UpgradeToPlanetaryFortress/CommandCenter'],  # CC
                   ['Cancel', 'Lift', 'Rally', 'SCV', 'CalldownMULE/OrbitalCommand', 'SupplyDrop/OrbitalCommand', 'Scan/OrbitalCommand'],  # OC
                   ['Cancel', 'Rally', 'CommandCenterLoad', 'CommandCenterUnloadAll', 'Attack', 'StopPlanetaryFortress/PlanetaryFortress', 'SCV'],  # PF
                   ['EvolveVentralSacks', 'Lair/Hatchery', 'Larva', 'overlordspeed', 'Queen', 'Rally', 'RallyEgg', 'ResearchBurrow'],  # Hatch/Lair/Hive
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'GatherProt', 'ReturnCargo', 'ProtossBuild/Probe', 'ProtossBuildAdvanced/Probe'],  # __Harvesters__ #Probe
                   ['Assimilator/Probe', 'CyberneticsCore/Probe', 'Forge/Probe', 'Gateway/Probe', 'Nexus/Probe', 'PhotonCannon/Probe', 'Pylon/Probe'],
                   ['DarkShrine/Probe', 'FleetBeacon/Probe', 'RoboticsBay/Probe', 'RoboticsFacility/Probe', 'Stargate/Probe', 'TemplarArchive/Probe', 'TwilightCouncil/Probe'],
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'Repair', 'GatherProt', 'ReturnCargo', 'TerranBuild/SCV', 'TerranBuildAdvanced/SCV'],  # SCV
                   ['Barracks/SCV', 'Bunker/SCV', 'CommandCenter/SCV', 'EngineeringBay/SCV', 'HiveMindEmulator/SCV', 'MissileTurret/SCV', 'PerditionTurret/SCV', 'Refinery/SCV', 'SensorTower/SCV', 'SupplyDepot/SCV'],
                   ['Armory/SCV', 'Factory/SCV', 'FusionCore/SCV', 'GhostAcademy/SCV', 'MercCompound/SCV', 'Starport/SCV'],
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'GatherProt', 'ReturnCargo', 'BurrowDown', 'ZergBuild/Drone', 'ZergBuildAdvanced/Drone'],  # Drone
                   ['BanelingNest/Drone', 'EvolutionChamber/Drone', 'Extractor/Drone', 'Hatchery/Drone', 'RoachWarren/Drone', 'SpawningPool/Drone', 'SporeCrawler/Drone', 'SpineCrawler/Drone'],
                   ['HydraliskDen/Drone', 'InfestationPit/Drone', 'NydusNetwork/Drone', 'Spire/Drone', 'UltraliskCavern/Drone'],
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'Rally', 'Interceptor/Carrier', 'ReleaseInterceptors/Carrier'],  # __Protoss Units__ #Carrier
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'Rally', 'PsiStorm/HighTemplar', 'Feedback/HighTemplar', 'AWrp'],  # High Templar
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'MassRecall/Mothership', 'Vortex/Mothership'],  # Mothership WoL
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'MothershipMassRecall/Mothership', 'TemporalField/Mothership'],  # Mothership HotS
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'MothershipCoreWeapon/MothershipCore', 'MothershipCoreMassRecall/MothershipCore', 'TemporalField/MothershipCore', 'MorphToMothership/MothershipCore'],  # Mothership Core
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'OracleRevelation/Oracle', 'OracleWeaponOff/Oracle', 'OracleWeaponOn/Oracle', 'LightofAiur/Oracle'],  # Oracle HotS
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'OracleAttack', 'OracleRevelation/Oracle', 'OracleWeaponOff/Oracle', 'OracleWeaponOn/Oracle', 'OracleBuildStasisTrap/Oracle'],  # Oracle LotV
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'GravitonBeam/Phoenix'],  # Phoenix
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'Rally', 'ForceField/Sentry', 'GuardianShield/Sentry', 'Hallucination/Sentry'],  # Sentry
                   ['DisruptorHallucination/Sentry', 'AdeptHallucination/Sentry', 'ArchonHallucination/Sentry', 'ColossusHallucination/Sentry', 'HighTemplarHallucination/Sentry', 'ImmortalHallucination/Sentry', 'OracleHallucination/Sentry', 'PhoenixHallucination/Sentry', 'ProbeHallucination/Sentry', 'StalkerHallucination/Sentry', 'VoidRayHallucination/Sentry', 'WarpPrismHallucination/Sentry', 'ZealotHallucination/Sentry'],
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'Rally', 'Blink/Stalker'],  # Stalker
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'Rally', 'VoidRaySwarmDamageBoost/VoidRay'],  # VoidRay
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'BunkerLoad', 'BunkerUnloadAll', 'PhasingMode/WarpPrism', 'TransportMode/WarpPrism'],  # Warp Prism
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'ImmortalOverload/Immortal'],  # Immortal
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'PurificationNovaTargeted/Disruptor'],  # Disruptor
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'Rally', 'Charge/Zealot'],  # Zealot
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'Rally', 'AdeptPhaseShift/Adept'],  # Adept
                   ['ProtossAirWeaponsLevel1/CyberneticsCore', 'ProtossAirArmorLevel1/CyberneticsCore', 'ResearchWarpGate/CyberneticsCore', 'ResearchHallucination/CyberneticsCore'],  # __Protoss Buildings__ #Cybernetics Core
                   ['AnionPulseCrystals/FleetBeacon', 'ResearchInterceptorLaunchSpeedUpgrade/FleetBeacon', 'ResearchVoidRaySpeedUpgrade/FleetBeacon'],  # Fleet Beacon
                   ['ProtossGroundWeaponsLevel1/Forge', 'ProtossGroundArmorLevel1/Forge', 'ProtossShieldsLevel1/Forge'],  # Forge
                   ['Rally', 'Zealot', 'Stalker', 'Sentry', 'HighTemplar', 'DarkTemplar', 'WarpInAdept/Gateway', 'UpgradeToWarpGate/Gateway'],  # Gateway
                   ['Rally', 'Zealot', 'Stalker', 'Sentry', 'HighTemplar', 'DarkTemplar', 'WarpInAdept/WarpGate', 'MorphBackToGateway/WarpGate'],  # Warpgate
                   ['ResearchGraviticDrive/RoboticsBay', 'ResearchExtendedThermalLance/RoboticsBay', 'ResearchGraviticBooster/RoboticsBay'],  # Robotics Bay
                   ['Rally', 'Immortal/RoboticsFacility', 'Colossus/RoboticsFacility', 'Observer/RoboticsFacility', 'WarpinDisruptor/RoboticsFacility', 'WarpPrism/RoboticsFacility'],  # Robotics Facility
                   ['Rally', 'Tempest/Stargate', 'VoidRay/Stargate', 'Phoenix/Stargate', 'Oracle/Stargate', 'Carrier/Stargate', 'WarpInScout/Stargate'],  # Stargate
                   ['ResearchHighTemplarEnergyUpgrade/TemplarArchive', 'ResearchPsiStorm/TemplarArchive'],  # Templar Archives
                   ['AdeptResearchPiercingUpgrade/TwilightCouncil', 'ResearchCharge/TwilightCouncil', 'ResearchStalkerTeleport/TwilightCouncil'],  # TwilightCouncil
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'CloakOnBanshee', 'CloakOff'],  # __Terran Units__ #Banshee
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'LiberatorAAMode/Liberator', 'LiberatorAGMode/Liberator'],  # Liberator
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'YamatoGun', 'Hyperjump/Battlecruiser', 'MissilePods/Battlecruiser', 'DefensiveMatrix/Battlecruiser'],  # Battlecruiser
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'StimFirebat/Firebat', 'IncineratorNozzles/Firebat'],  # Firebat
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'ChannelSnipe/Ghost', 'CloakOnBanshee', 'CloakOff', 'EMP/Ghost', 'Snipe/Ghost', 'NukeCalldown/Ghost', 'GhostHoldFire/Ghost'],  # Ghost
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'MorphToHellionTank/Hellion', 'MorphToHellion/Hellion'],  # Hellion
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'LockOn/Cyclone'],  # Cyclone
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'HerculesLoad/Hercules', 'HerculesUnloadAll/Hercules'],  # Hercules
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'Stim'],  # Marine
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'MedicHeal/Medic'],  # Medic
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'Heal/Medivac', 'MedivacSpeedBoost/Medivac', 'BunkerLoad', 'BunkerUnloadAll'],  # Medivac
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'AutoTurret/Raven', 'PointDefenseDrone/Raven', 'HunterSeekerMissile/Raven'],  # Raven
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'D8Charge/Reaper'],  # Reaper
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'KD8Charge/Reaper'],  # Reaper LotV
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'NanoRepair/ScienceVessel', 'Irradiate/ScienceVessel'],  # Science Vessel
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'SiegeMode', 'Unsiege'],  # Siege Tank
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'RogueGhostCloak/Spectre', 'CloakOff', 'Obliterate/Spectre', 'UltrasonicPulse/Spectre', 'SpectreNukeCalldown/Spectre', 'SpectreHoldFire/Spectre'],  # Spectre
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', '250mmStrikeCannons/Thor'],  # Thor
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'ExplosiveMode', 'ArmorpiercingMode'],  # Thor HotS
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'AssaultMode', 'FighterMode'],  # Viking
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'SpiderMine/Vulture', 'SpiderMineReplenish/Vulture'],  # Vulture
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'WidowMineBurrow/WidowMine', 'WidowMineUnburrow/WidowMine'],  # Widow Mine                   
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'WraithCloakOn/Wraith', 'WraithCloakOff/Wraith'],  # Wraith
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'Cancel', 'NovaSnipe/Nova', 'Domination/Nova', 'ReleaseMinion/Nova', 'HeroNukeCalldown/Nova'],  # __Heroes__ #Nova
                   ['SJHyperionBlink/SJHyperion', 'SJHyperionFighters/SJHyperion', 'SJHyperionFightersRecall/SJHyperion', 'SJHyperionLightningStorm/SJHyperion', 'SJHyperionYamato/SJHyperion'],  # Hyperion HotS
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'Cancel', 'OdinBarrage/Odin', 'OdinNukeCalldown/Odin'],  # Odin
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'ExperimentalPlasmaGun/Raynor', 'PlantC4Charge/Raynor', 'TheMorosDevice/Raynor', 'TossGrenade/Raynor'],  # Raynor
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'RaynorSnipe/RaynorCommando'],
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'BonesHeal/Stetmann'],  # Stetmann
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'DutchPlaceTurret/Swann'],  # Swann
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'MindBlast/Tosh', 'VoodooShield/Tosh', 'Consumption/Tosh', 'HeroNukeCalldown/Tosh'],  # Tosh
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'TossGrenadeTychus/TychusCommando'],  # Tychus
                   ['SelectBuilder', 'Halt', 'Cancel', 'TerranShipPlatingLevel1/Armory', 'TerranShipWeaponsLevel1/Armory', 'TerranVehiclePlatingLevel1/Armory', 'TerranVehicleWeaponsLevel1/Armory'],  # __Terran Buildings__ #Armory WoL
                   ['SelectBuilder', 'Halt', 'Cancel', 'TerranShipWeaponsLevel1/Armory', 'TerranVehicleAndShipPlatingLevel1/Armory', 'TerranVehicleWeaponsLevel1/Armory'],  # Armory HotS
                   ['SelectBuilder', 'Cancel', 'Lift', 'Rally', 'Marine/Barracks', 'Marauder/Barracks', 'Reaper/Barracks', 'Ghost/Barracks', 'Medic/Barracks', 'Firebat/Barracks', 'TechLabBarracks/Barracks', 'Reactor/Barracks', 'TechReactorAI/Barracks'],  # Barracks WoL
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Land', 'TechLabBarracks/BarracksFlying', 'Reactor/BarracksFlying'],
                   ['SelectBuilder', 'Cancel', 'Lift', 'Rally', 'Marine/Barracks', 'Marauder/Barracks', 'Reaper/Barracks', 'Ghost/Barracks', 'Medic/Barracks', 'Firebat/Barracks', 'Spectre/Barracks', 'MengskUnits/Barracks', 'TechLabBarracks/Barracks', 'Reactor/Barracks', 'TechReactorAI/Barracks'],  # Barracks HotS Campaign
                   ['SelectBuilder', 'Cancel', 'Lift', 'Rally', 'Marine/Barracks', 'Marauder/Barracks', 'Reaper/Barracks', 'Medic/Barracks', 'Firebat/Barracks', 'HireKelmorianMiners/Barracks', 'HireHammerSecurities/Barracks', 'HireDevilDogs/Barracks', 'MercReaper/Barracks', 'MercMedic/Barracks'],  # Barracks HotS Campaign 2
                   ['SelectBuilder', 'Cancel', 'Salvage/Bunker', 'SetBunkerRallyPoint/Bunker', 'BunkerLoad', 'BunkerUnloadAll', 'Stim', 'Stop', 'Attack'],  # Bunker
                   ['SelectBuilder', 'Halt', 'Cancel', 'TerranInfantryArmorLevel1/EngineeringBay', 'TerranInfantryWeaponsLevel1/EngineeringBay', 'ResearchHiSecAutoTracking/EngineeringBay', 'ResearchNeosteelFrame/EngineeringBay', 'UpgradeBuildingArmorLevel1/EngineeringBay'],  # Engineering Bay
                   ['SelectBuilder', 'Cancel', 'Lift', 'Rally', 'Hellion/Factory', 'WidowMine/Factory', 'SiegeTank/Factory', 'HellionTank/Factory', 'Thor/Factory', 'TechLabFactory/Factory', 'Reactor/Factory', 'BuildCyclone/Factory'],  # Factory
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Land', 'BuildTechLabFactory/FactoryFlying', 'Reactor/FactoryFlying'],
                   ['SelectBuilder', 'Cancel', 'Lift', 'Rally', 'Hellion/Factory', 'SiegeTank/Factory', 'Thor/Factory', 'Vulture/Factory', 'Goliath/Factory', 'Diamondback/Factory', 'Predator/Factory', 'TechLabFactory/Factory', 'Reactor/Factory', 'TechReactorAI/Factory'],  # Factory WoL Campaign
                   ['SelectBuilder', 'Cancel', 'Lift', 'Rally', 'Hellion/Factory', 'SiegeTank/Factory', 'WarHound/Factory', 'CampaignVehicles/Factory', 'TechLabFactory/Factory', 'Reactor/Factory', 'TechReactorAI/Factory'],  # Factory HotS Campaign
                   ['SelectBuilder', 'Cancel', 'Lift', 'Rally', 'Vulture/Factory', 'Predator/Factory', 'Diamondback/Factory', 'Goliath/Factory', 'MicroBot/Factory', 'Thor/Factory', 'Hellion/Factory'],  # Factory HotS Campaign 2
                   ['SelectBuilder', 'Cancel', 'Lift', 'Rally', 'Hellion/Factory', 'Goliath/Factory', 'SiegeTank/Factory', 'Diamondback/Factory', 'Thor/Factory', 'MercHellion/Factory', 'HireSpartanCompany/Factory', 'HireSiegeBreakers/Factory'],  # Factory HotS Campaign 3
                   ['ResearchBattlecruiserEnergyUpgrade/FusionCore', 'ResearchBattlecruiserSpecializations/FusionCore'],  # Fusion Core
                   ['NukeArm/GhostAcademy', 'ResearchGhostEnergyUpgrade/GhostAcademy', 'ResearchPersonalCloaking/GhostAcademy'],  # Ghost Academy
                   ['SelectBuilder', 'Halt', 'Cancel', 'Rally', 'HireKelmorianMiners/MercCompound', 'HireDevilDogs/MercCompound', 'HireHammerSecurities/MercCompound', 'HireSpartanCompany/MercCompound', 'HireSiegeBreakers/MercCompound', 'HireHelsAngels/MercCompound', 'HireDuskWing/MercCompound', 'HireDukesRevenge/MercCompound', 'ReaperSpeed/MercCompound', 'MercHellion/MercCompound', 'MercMedic/MercCompound', 'MercReaper/MercCompound'],  # Merc Compound
                   ['ResearchHellion/ScienceFacility', 'ResearchSiegeTank/ScienceFacility', 'ResearchReaper/ScienceFacility', 'ResearchMedic/ScienceFacility', 'ResearchFirebat/ScienceFacility', 'ResearchGoliath/ScienceFacility', 'ResearchBunkerUpgrade/ScienceFacility', 'ResearchPerditionTurret/ScienceFacility', 'ResearchFireSuppression/ScienceFacility', 'ResearchTechReactor/ScienceFacility'],  # Science Facility
                   ['SelectBuilder', 'Cancel', 'Lift', 'Rally', 'VikingFighter/Starport', 'Medivac/Starport', 'Raven/Starport', 'Banshee/Starport', 'Battlecruiser/Starport', 'Wraith/Starport', 'BuildHercules/Starport', 'TechLabStarport/Starport', 'Reactor/Starport', 'TechReactorAI/Starport'],  # Starport WoL Campaign
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Land', 'BuildTechLabStarport/StarportFlying', 'Reactor/StarportFlying'],
                   ['SelectBuilder', 'Cancel', 'Lift', 'Rally', 'VikingFighter/Starport', 'Medivac/Starport', 'Liberator/Starport', 'Raven/Starport', 'Banshee/Starport', 'Battlecruiser/Starport', 'TechLabStarport/Starport', 'Reactor/Starport'],  # Starport
                   ['SelectBuilder', 'Cancel', 'Lift', 'Rally', 'VikingFighter/Starport', 'Medivac/Starport', 'Raven/Starport', 'Banshee/Starport', 'Battlecruiser/Starport', 'CampaignVehicles/Starport', 'TechLabStarport/Starport', 'Reactor/Starport', 'TechReactorAI/Starport'],  # Starport HotS Campaign
                   ['SelectBuilder', 'Cancel', 'Lift', 'Rally', 'Wraith/Starport', 'BuildHercules/Starport', 'BuildScienceVessel/Starport', 'Battlecruiser/Starport'],  # Starport HotS Campaign 2
                   ['SelectBuilder', 'Cancel', 'Lift', 'Rally', 'VikingFighter/Starport', 'Banshee/Starport', 'Wraith/Starport', 'Battlecruiser/Starport', 'HireDuskWing/Starport', 'HireHelsAngels/Starport', 'HireDukesRevenge/Starport'],  # Starport HotS Campaign 3
                   ['SelectBuilder', 'Halt', 'Cancel', 'Lower/SupplyDepot'],  # Supply Depot
                   ['ResearchShieldWall/BarracksTechLab', 'Stimpack/BarracksTechLab', 'ResearchPunisherGrenades/BarracksTechLab', 'ReaperSpeed/BarracksTechLab'],  # TechLab Barracks WoL
                   ['Stimpack/BarracksTechLab', 'ResearchJackhammerConcussionGrenade/BarracksTechLab', 'ResearchG4Charge/BarracksTechLab', 'ResearchStabilizerMedPacks/BarracksTechLab', 'ResearchIncineratorNozzles/BarracksTechLab'],  # TechLab Barracks Left2Die
                   ['ResearchHighCapacityBarrels/FactoryTechLab', 'ResearchSiegeTech/FactoryTechLab', 'ResearchStrikeCannons/FactoryTechLab'],  # TechLab Factory WoL
                   ['ResearchHighCapacityBarrels/FactoryTechLab', 'ResearchDrillClaws/FactoryTechLab', 'ResearchTransformationServos/FactoryTechLab'],  # TechLab Factory HotS
                   ['ResearchHighCapacityBarrels/FactoryTechLab', 'ResearchDrillClaws/FactoryTechLab', 'CycloneResearchLockOnDamageUpgrade/FactoryTechLab'],  # TechLab Factory LotV
                   ['ResearchHighCapacityBarrels/FactoryTechLab', 'ResearchShapedBlast/FactoryTechLab', 'ResearchCerberusMines/FactoryTechLab', 'ResearchMultiLockTargetingSystem/FactoryTechLab', 'ResearchRegenerativeBioSteel/FactoryTechLab'],  # TechLab Factory Left2Die
                   ['ResearchMedivacEnergyUpgrade/StarportTechLab', 'ResearchBansheeCloak/StarportTechLab', 'ResearchDurableMaterials/StarportTechLab', 'ResearchSeekerMissile/StarportTechLab', 'ResearchRavenEnergyUpgrade/StarportTechLab', 'WraithCloak/StarportTechLab'],  # TechLab Starport WoL
                   ['ResearchMedivacEnergyUpgrade/StarportTechLab', 'ResearchBansheeCloak/StarportTechLab', 'ResearchDurableMaterials/StarportTechLab', 'ResearchRavenEnergyUpgrade/StarportTechLab', 'WraithCloak/StarportTechLab'],  # TechLab Starport HotS
                   ['ResearchBansheeCloak/StarportTechLab', 'ResearchRavenEnergyUpgrade/StarportTechLab', 'WraithCloak/StarportTechLab', 'BansheeSpeed/StarportTechLab', 'ResearchExplosiveShrapnelShells/StarportTechLab', 'ResearchHighCapacityFuelTanks/StarportTechLab', 'ResearchBallisticRange/StarportTechLab'],  # TechLab Starport LotV
                   ['Corruptor/Larva', 'Drone/Larva', 'Hydralisk/Larva', 'Infestor/Larva', 'Mutalisk/Larva', 'Overlord/Larva', 'Roach/Larva', 'SwarmHostMP/Larva', 'Ultralisk/Larva', 'Viper/Larva', 'Zergling/Larva'],  # __Zerg Units__ #Larva
                   ['Aberration/Larva', 'Drone/Larva', 'Hydralisk/Larva', 'Infestor/Larva', 'Mutalisk/Larva', 'Overlord/Larva', 'Roach/Larva', 'MorphToSwarmHostSplitA/Larva', 'Ultralisk/Larva', 'Zergling/Larva'],  # Larva HotS Campaign
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'BurrowDown', 'DisableBuildingAttack/Baneling', 'EnableBuildingAttack/Baneling', 'Explode/Baneling'],  # Baneling
                   ['Attack', 'Explode/BanelingBurrowed', 'BurrowUp'],
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'CausticSpray/Corruptor', 'BroodLord/Corruptor', 'CorruptionAbility/Corruptor'],  # Corruptor
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'BurrowDown', 'NeuralParasite/Infestor', 'FungalGrowth/Infestor', 'InfestedTerrans/Infestor'],  # Infestor
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'BurrowDown', 'NPSwarm/Infestor', 'FungalGrowth/Infestor', 'InfestorConsumption/Infestor'],  # Infestor HotS Campaign
                   ['Attack', 'InfestedTerrans/InfestorBurrowed', 'BurrowUp'],
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'BunkerLoad', 'BunkerUnloadAll', 'GenerateCreep/Overlord', 'MorphToOverseer/Overlord', 'MorphtoOverlordTransport/Overlord'],  # Overlord
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'SpawnChangeling/Overseer', 'Contaminate/Overseer'],  # Overseer
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'BurrowDown', 'MorphMorphalisk/Queen', 'BuildCreepTumor/Queen', 'Transfusion/Queen'],  # Queen
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'BurrowDown', 'Ravager/Roach'],  # Roach
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'BurrowDown', 'RavagerCorrosiveBile/Ravager'],  # Ravager
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'SwarmHost/SwarmHostMP', 'SwarmHostBurrowDown'],  # Swarm Host
                   ['Attack', 'VoidSwarmHostSpawnLocust/SwarmHostBurrowedMP', 'SwarmHostBurrowUp'],  # Swarm Host Burrowed
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'LocustMPFlyingSwoop/LocustMPFlying'],  # Locust
                   ['Attack', 'SetRallyPointSwarmHost/SwarmHostBurrowedMP', 'SwarmHost/SwarmHostBurrowedMP', 'SwarmHostBurrowUp'],  # Swarm Host Burrowed
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'SwarmHostDeepBurrow/SwarmHostSplitB', 'SwarmHostBurrowDown'],  # Swarm Host HotS Campaign
                   ['Stop', 'Attack', 'SwarmHostDeepBurrow/SwarmHostSplitB', 'SwarmHostBurrowUp', 'LocustLaunchCreeper/SwarmHostSplitBBurrowed'],  # Swarm Host HotS Campaign Burrowed
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'BlindingCloud/Viper', 'FaceEmbrace/Viper', 'ViperConsume/Viper', 'ParasiticBomb/Viper'],  # Viper
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'BurrowDown', 'Baneling/Zergling'],  # Zergling
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'LurkerMP/Hydralisk'],  # Hydralisk
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'BurrowLurkerMP'],  # Lurker Burrowed
                   ['Attack', 'Stop', 'LurkerBurrowUp', 'LurkerCancelHoldFire/LurkerMPBurrowed', 'LurkerHoldFire/LurkerMPBurrowed'],  # Lurker UnBurrowed
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'BurrowDown', 'K5Leviathan/K5Kerrigan', 'MindBolt/K5Kerrigan', 'PsionicLift/K5Kerrigan', 'WildMutation/K5Kerrigan'],  # __Zerg Heroes Kerrigan
                   ['K5Leviathan/K5KerriganBurrowed', 'MindBolt/K5KerriganBurrowed', 'PsionicLift/K5KerriganBurrowed', 'WildMutation/K5KerriganBurrowed', 'BurrowUp'],
                   ['SwarmQueenParasiticInvasion/LargeSwarmQueen', 'SwarmQueenZergling/LargeSwarmQueen', 'SwarmQueenRoach/LargeSwarmQueen', 'GrowHugeQueen/LargeSwarmQueen'],  # Niadra
                   ['SwarmQueenParasiticInvasion/HugeSwarmQueen', 'SwarmQueenZergling/HugeSwarmQueen', 'SwarmQueenRoach/HugeSwarmQueen', 'SwarmQueenHydralisk/HugeSwarmQueen'],
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'BurrowDown', 'Drag/Dehaka', 'DehakaHeal/Dehaka', 'DehakaMirrorImage/Dehaka'],  # Dehaka
                   ['zerggroundarmor1/EvolutionChamber', 'zergmeleeweapons1/EvolutionChamber', 'zergmissileweapons1/EvolutionChamber'],  # __Zerg Buildings__ #Evolution Chamber
                   ['hydraliskspeed/HydraliskDen', 'MutateintoLurkerDen/HydraliskDen'],  # Hydralisk Den LotV
                   ['MuscularAugments/HydraliskDen', 'hydraliskspeed/HydraliskDen', 'LurkerDen/HydraliskDen'],  # Hydralisk Den HotS
                   ['hydraliskspeed/LurkerDenMP'],  # Lurker Den
                   ['ResearchLocustLifetimeIncrease/InfestationPit', 'EvolveInfestorEnergyUpgrade/InfestationPit', 'ResearchNeuralParasite/InfestationPit'],  # Infestation Pit
                   ['Stop', 'BunkerLoad', 'BunkerUnloadAll', 'Rally', 'SummonNydusWorm/NydusNetwork'],  # Nydus Network
                   ['EvolveTunnelingClaws/RoachWarren', 'EvolveGlialRegeneration/RoachWarren'],  # Roach Warren
                   ['zerglingattackspeed/SpawningPool', 'zerglingmovementspeed/SpawningPool'],  # Spawning Pool
                   ['Stop', 'Attack', 'SpineCrawlerUproot/SpineCrawler'],  # Spine Crawler
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'SpineCrawlerRoot/SpineCrawlerUprooted'],
                   ['zergflyerattack1', 'zergflyerarmor1', 'GreaterSpire/Spire'],  # Spire
                   ['Stop', 'Attack', 'SporeCrawlerUproot/SporeCrawler'],  # Spore Crawler
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'SporeCrawlerRoot/SporeCrawlerUprooted'],
                   ['Cancel', 'EvolveChitinousPlating/UltraliskCavern'],  # Ultralisk Cavern
                   ['Stop', 'Attack', 'SelectBuilder', 'SetBunkerRallyPoint/Bunker', 'Stim', 'BunkerLoad', 'BunkerUnloadAll', 'Salvage/Bunker', 'Cancel'], #LotV Multiplayer/Terran/Structures/Bunker/General
				   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'Baneling/Zergling', 'BurrowDown'], #LotV Multiplayer/Zerg/Units/Zergling
                   ['Attack', 'Explode/BanelingBurrowed', 'BurrowUp'], #LotV Multiplayer/Zerg/Units/Baneling/Burrowed
                   ['SCV', 'OrbitalCommand/CommandCenter', 'UpgradeToPlanetaryFortress/CommandCenter', 'SelectBuilder', 'Rally', 'CommandCenterLoad', 'CommandCenterUnloadAll', 'Lift', 'Halt', 'Cancel'], #LotV Multiplayer/Terran/Structures/Command Center/General
                   ['Marine/Barracks', 'Reaper/Barracks', 'Marauder/Barracks', 'Ghost/Barracks', 'SelectBuilder', 'Rally', 'TechLabBarracks/Barracks', 'Reactor/Barracks', 'Lift', 'Halt', 'Cancel'], #LotV Multiplayer/Terran/Structures/Barracks/General
                   ['Stop', 'Attack', 'SporeCrawlerUproot/SporeCrawler', 'Cancel'], #LotV Multiplayer/Zerg/Structures/Spore Crawler/General
                   ['ResearchHighCapacityFuelTanks/StarportTechLab', 'ResearchExplosiveShrapnelShells/StarportTechLab', 'ResearchRavenEnergyUpgrade/StarportTechLab', 'ResearchBansheeCloak/StarportTechLab', 'BansheeSpeed/StarportTechLab', 'ResearchBallisticRange/StarportTechLab', 'Cancel'], #LotV Multiplayer/Terran/Structures/Tech Lab/Attached to Starport
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'Ravager/Roach', 'BurrowDown'], #LotV Multiplayer/Zerg/Units/Roach
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'MorphToOverseer/Overlord', 'GenerateCreep/Overlord', 'BunkerLoad', 'BunkerUnloadAll', 'Cancel'], #LotV Multiplayer/Zerg/Units/Droplord/General
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'GatherProt', 'ReturnCargo', 'ZergBuild/Drone', 'ZergBuildAdvanced/Drone', 'BurrowDown'], #LotV Multiplayer/Zerg/Units/Drone/General
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'MorphToOverseer/Overlord', 'GenerateCreep/Overlord', 'MorphtoOverlordTransport/Overlord', 'BunkerUnloadAll', 'Cancel'], #LotV Multiplayer/Zerg/Units/Overlord/General (BunkerUnloadAll shouldn't be here)
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'AutoTurret/Raven', 'PointDefenseDrone/Raven', 'HunterSeekerMissile/Raven'], #LotV Multiplayer/Terran/Units/Raven
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'BuildTechLabStarport/StarportFlying', 'Reactor/StarportFlying', 'Land'], #LotV Multiplayer/Terran/Structures/Starport/Flying
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'CloakOnBanshee', 'CloakOff', 'GhostHoldFire/Ghost', 'WeaponsFree/Ghost', 'ChannelSnipe/Ghost', 'EMP/Ghost', 'NukeCalldown/Ghost', 'Cancel'], #LotV Multiplayer/Terran/Units/Ghost
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'OracleAttack', 'OracleRevelation/Oracle', 'OracleBuildStasisTrap/Oracle', 'OracleWeaponOn/Oracle', 'OracleWeaponOff/Oracle', 'Cancel'], #LotV Multiplayer/Protoss/Units/Oracle
                   ['Phoenix/Stargate', 'Oracle/Stargate', 'VoidRay/Stargate', 'Tempest/Stargate', 'Carrier/Stargate', 'Rally', 'Cancel'], #LotV Multiplayer/Protoss/Structures/Stargate
                   ['Stop', 'SummonNydusWorm/NydusNetwork', 'Rally', 'BunkerLoad', 'BunkerUnloadAll', 'Cancel'], #LotV Multiplayer/Zerg/Structures/Nydus Network
                   ['TwilightCouncil/Probe', 'Stargate/Probe', 'RoboticsFacility/Probe', 'TemplarArchive/Probe', 'FleetBeacon/Probe', 'RoboticsBay/Probe', 'DarkShrine/Probe', 'Cancel'], #LotV Multiplayer/Protoss/Units/Probe/ProbeAdvanced Structures
                   ['ResearchBattlecruiserSpecializations/FusionCore', 'ResearchBattlecruiserEnergyUpgrade/FusionCore', 'SelectBuilder', 'Halt', 'Cancel'], #LotV Multiplayer/Terran/Structures/Fusion Core
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'RavagerCorrosiveBile/Ravager', 'BurrowDown'], #LotV Multiplayer/Zerg/Units/Ravager
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'MothershipCoreWeapon/Mothership', 'MothershipMassRecall/Mothership', 'TemporalField/Mothership'], #LotV Multiplayer/Protoss/Units/Mothership
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'AdeptPhaseShift/Adept', 'Rally'], #LotV Multiplayer/Protoss/Units/Adept
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'CommandCenterLoad', 'CommandCenterUnloadAll', 'Land'], #LotV Multiplayer/Terran/Structures/Command Center/Flying
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'Interceptor/Carrier', 'ReleaseInterceptors/Carrier', 'Cancel'], #LotV Multiplayer/Protoss/Units/Carrier
                   ['VikingFighter/Starport', 'Medivac/Starport', 'Liberator/Starport', 'Raven/Starport', 'Banshee/Starport', 'Battlecruiser/Starport', 'SelectBuilder', 'Rally', 'TechLabStarport/Starport', 'Reactor/Starport', 'Lift', 'Cancel'], #LotV Multiplayer/Terran/Structures/Starport/General
                   ['ResearchGraviticBooster/RoboticsBay', 'ResearchGraviticDrive/RoboticsBay', 'ResearchExtendedThermalLance/RoboticsBay', 'Cancel'], #LotV Multiplayer/Protoss/Structures/Robotics Bay
                   ['ResearchHighCapacityBarrels/FactoryTechLab', 'ResearchDrillClaws/FactoryTechLab', 'CycloneResearchLockOnDamageUpgrade/FactoryTechLab', 'Cancel'], #LotV Multiplayer/Terran/Structures/Tech Lab/Attached to Factory
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'SporeCrawlerRoot/SporeCrawlerUprooted', 'Cancel'], #LotV Multiplayer/Zerg/Structures/Spore Crawler/Uprooted
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'GatherProt', 'ReturnCargo', 'ProtossBuild/Probe', 'ProtossBuildAdvanced/Probe'], #LotV Multiplayer/Protoss/Units/Probe/General
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'GravitonBeam/Phoenix', 'Cancel'], #LotV Multiplayer/Protoss/Units/Phoenix
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'PhasingMode/WarpPrism', 'TransportMode/WarpPrism', 'BunkerLoad', 'BunkerUnloadAll'], #LotV Multiplayer/Protoss/Units/Warp Prism
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'ImmortalOverload/Immortal'], #LotV Multiplayer/Protoss/Units/Immortal
                   ['EvolveInfestorEnergyUpgrade/InfestationPit', 'ResearchNeuralParasite/InfestationPit', 'Cancel'], #LotV Multiplayer/Zerg/Structures/Infestation Pit
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'GatherProt', 'ReturnCargo', 'TerranBuild/SCV', 'TerranBuildAdvanced/SCV', 'Repair', 'Halt'], #LotV Multiplayer/Terran/Units/SCV/General
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'MorphToMothership/MothershipCore', 'MothershipCoreWeapon/MothershipCore', 'MothershipCoreMassRecall/MothershipCore', 'TemporalField/MothershipCore', 'Cancel'], #LotV Multiplayer/Protoss/Units/Mothership Core
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'InfestedTerrans/InfestorBurrowed', 'BurrowUp'], #LotV Multiplayer/Zerg/Units/Infestor/Burrowed
                   ['Stop', 'Attack', 'SpineCrawlerUproot/SpineCrawler', 'Cancel'], #LotV Multiplayer/Zerg/Structures/Spine Crawler/General
                   ['Attack', 'VoidSwarmHostSpawnLocust/SwarmHostBurrowedMP', 'SwarmHostBurrowUp'], #LotV Multiplayer/Zerg/Units/Swarm Host/Burrowed
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'VoidRaySwarmDamageBoost/VoidRay'], #LotV Multiplayer/Protoss/Units/Void Ray
                   ['TerranVehicleWeaponsLevel1/Armory', 'TerranVehicleAndShipPlatingLevel1/Armory', 'TerranShipWeaponsLevel1/Armory', 'SelectBuilder', 'Halt', 'Cancel'], #LotV Multiplayer/Terran/Structures/Armory
                   ['Larva', 'Queen', 'ResearchBurrow', 'overlordspeed', 'RallyEgg', 'Rally', 'Hive/Lair', 'Cancel'], #LotV Multiplayer/Zerg/Structures/Lair
                   ['Drone/Larva', 'Overlord/Larva', 'Zergling/Larva', 'Roach/Larva', 'Hydralisk/Larva', 'Mutalisk/Larva', 'Corruptor/Larva', 'Infestor/Larva', 'SwarmHostMP/Larva', 'Viper/Larva', 'Ultralisk/Larva', 'Cancel'], #LotV Multiplayer/Zerg/Units/Larva/General
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'Charge/Zealot', 'Rally'], #LotV Multiplayer/Protoss/Units/Zealot
                   ['TerranInfantryWeaponsLevel1/EngineeringBay', 'TerranInfantryArmorLevel1/EngineeringBay', 'ResearchHiSecAutoTracking/EngineeringBay', 'ResearchNeosteelFrame/EngineeringBay', 'UpgradeBuildingArmorLevel1/EngineeringBay', 'SelectBuilder', 'Halt', 'Cancel'], #LotV Multiplayer/Terran/Structures/Barracks/Engineering BayGeneral
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'MorphToOverseer/Overlord', 'StopGenerateCreep', 'MorphtoOverlordTransport/Overlord', 'BunkerUnloadAll', 'Cancel'], #LotV Multiplayer/Zerg/Units/Overlord/Creeping (BunkerUnloadAll shouldn't be here)
                   ['SCV', 'Rally', 'CalldownMULE/OrbitalCommand', 'SupplyDrop/OrbitalCommand', 'Scan/OrbitalCommand', 'Lift', 'Cancel'], #LotV Multiplayer/Terran/Structures/Orbital Command
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'SwarmHost/SwarmHostMP', 'SwarmHostBurrowDown'], #LotV Multiplayer/Zerg/Units/Swarm Host/General
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'Heal/Medivac', 'MedivacSpeedBoost/Medivac', 'BunkerLoad', 'BunkerUnloadAll'], #LotV Multiplayer/Terran/Units/Medivac
                   ['Zealot', 'Sentry', 'Stalker', 'WarpInAdept/WarpGate', 'HighTemplar', 'DarkTemplar', 'Rally', 'MorphBackToGateway/WarpGate'], #LotV Multiplayer/Protoss/Structures/Gateway/Warp Gate
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'WidowMineBurrow/WidowMine', 'WidowMineUnburrow/WidowMine'], #LotV Multiplayer/Terran/Units/Widow Mine
                   ['Zealot', 'Sentry', 'Stalker', 'WarpInAdept/Gateway', 'HighTemplar', 'DarkTemplar', 'Rally', 'UpgradeToWarpGate/Gateway', 'Cancel'], #LotV Multiplayer/Protoss/Structures/Gateway/General
                   ['ProtossAirWeaponsLevel1/CyberneticsCore', 'ProtossAirArmorLevel1/CyberneticsCore', 'ResearchWarpGate/CyberneticsCore', 'Cancel'], #LotV Multiplayer/Protoss/Structures/Cybernetics Core
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'LurkerMP/Hydralisk', 'BurrowDown'], #LotV Multiplayer/Zerg/Units/Hydralisk
                   ['Observer/RoboticsFacility', 'WarpPrism/RoboticsFacility', 'Immortal/RoboticsFacility', 'Colossus/RoboticsFacility', 'WarpinDisruptor/RoboticsFacility', 'Rally', 'Cancel'], #LotV Multiplayer/Protoss/Structures/Robotics Facility
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'TechLabBarracks/BarracksFlying', 'Reactor/BarracksFlying', 'Land'], #LotV Multiplayer/Terran/Structures/Barracks/Flying
                   ['ResearchCharge/TwilightCouncil', 'ResearchStalkerTeleport/TwilightCouncil', 'AdeptResearchPiercingUpgrade/TwilightCouncil', 'Cancel'], #LotV Multiplayer/Protoss/Structures/Twilight Council
                   ['Larva', 'Queen', 'ResearchBurrow', 'overlordspeed', 'RallyEgg', 'Rally', 'Lair/Hatchery', 'Cancel'], #LotV Multiplayer/Zerg/Structures/Hatchery
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'Feedback/HighTemplar', 'PsiStorm/HighTemplar', 'AWrp', 'Rally'], #LotV Multiplayer/Protoss/Units/High Templar
                   ['hydraliskspeed/LurkerDenMP', 'Cancel'], #LotV Multiplayer/Zerg/Structures/Lurker Den
                   ['ProbeHallucination/Sentry', 'ZealotHallucination/Sentry', 'AdeptHallucination/Sentry', 'StalkerHallucination/Sentry', 'ImmortalHallucination/Sentry', 'HighTemplarHallucination/Sentry', 'ArchonHallucination/Sentry', 'VoidRayHallucination/Sentry', 'PhoenixHallucination/Sentry', 'WarpPrismHallucination/Sentry', 'OracleHallucination/Sentry', 'ColossusHallucination/Sentry', 'DisruptorHallucination/Sentry', 'Cancel'], #LotV Multiplayer/Protoss/Units/Sentry/Hallucinations
                   ['Probe/Nexus', 'MothershipCore/Nexus', 'Stop', 'Attack', 'Rally', 'TimeWarp/Nexus', 'Cancel'], #LotV Multiplayer/Protoss/Structures/Nexus
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'SpineCrawlerRoot/SpineCrawlerUprooted', 'Cancel'], #LotV Multiplayer/Zerg/Structures/Spine Crawler/Uprooted
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'LiberatorAGMode/Liberator', 'LiberatorAAMode/Liberator'], #LotV Multiplayer/Terran/Units/Liberator
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'Stim'], #LotV Multiplayer/Terran/Units/Marine
                   ['Hellion/Factory', 'WidowMine/Factory', 'SiegeTank/Factory', 'BuildCyclone/Factory', 'HellionTank/Factory', 'Thor/Factory', 'SelectBuilder', 'Rally', 'TechLabFactory/Factory', 'Reactor/Factory', 'Lift', 'Cancel'], #LotV Multiplayer/Terran/Structures/Factory/General
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'PurificationNovaTargeted/Disruptor', 'Rally'], #LotV Multiplayer/Protoss/Units/Disruptor
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'GuardianShield/Sentry', 'ForceField/Sentry', 'Hallucination/Sentry', 'Rally'], #LotV Multiplayer/Protoss/Units/Sentry/General
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'Explode/Baneling', 'EnableBuildingAttack/Baneling', 'DisableBuildingAttack/Baneling', 'BurrowDown'], #LotV Multiplayer/Zerg/Units/Baneling/General
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'InfestedTerrans/Infestor', 'FungalGrowth/Infestor', 'NeuralParasite/Infestor', 'Cancel', 'BurrowDown'], #LotV Multiplayer/Zerg/Units/Infestor/General
                   ['hydraliskspeed/HydraliskDen', 'MutateintoLurkerDen/HydraliskDen', 'Cancel'], #LotV Multiplayer/Zerg/Structures/Hydralisk Den
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'BurrowLurkerMP'], #LotV Multiplayer/Zerg/Units/Lurker/General
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'BuildTechLabFactory/FactoryFlying', 'Reactor/FactoryFlying', 'Land'], #LotV Multiplayer/Terran/Structures/Factory/Flying
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'ViperConsume/Viper', 'FaceEmbrace/Viper', 'BlindingCloud/Viper', 'ParasiticBomb/Viper'], #LotV Multiplayer/Zerg/Units/Viper
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'Blink/Stalker', 'Rally'], #LotV Multiplayer/Protoss/Units/Stalker
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'MorphToOverseer/Overlord', 'StopGenerateCreep', 'BunkerLoad', 'BunkerUnloadAll', 'Cancel'], #LotV Multiplayer/Zerg/Units/Droplord/Creeping
                   ['SelectBuilder', 'SetBunkerRallyPoint/Bunker', 'Halt', 'Cancel'], #LotV Multiplayer/Terran/Structures/Bunker/Construction
                   ['zergflyerattack1', 'zergflyerarmor1', 'GreaterSpire/Spire', 'Cancel'], #LotV Multiplayer/Zerg/Structures/Spire
                   ['Stop', 'Attack', 'LurkerHoldFire/LurkerMPBurrowed', 'LurkerCancelHoldFire/LurkerMPBurrowed', 'LurkerBurrowUp'], #LotV Multiplayer/Zerg/Units/Lurker/Burrowed
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'LocustMPFlyingSwoop/LocustMPFlying'], #LotV Multiplayer/Zerg/Units/Locust (Flying)
                   ['BuildCreepTumorPropagate/CreepTumorBurrowed', 'Cancel'], #LotV Multiplayer/Zerg/Structures/Creep Tumor
                   ['AnionPulseCrystals/FleetBeacon', 'ResearchInterceptorLaunchSpeedUpgrade/FleetBeacon', 'Cancel'], #LotV Multiplayer/Protoss/Structures/Fleet Beacon
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'CausticSpray/Corruptor', 'BroodLord/Corruptor', 'Cancel'], #LotV Multiplayer/Zerg/Units/Corruptor
                   ['CommandCenter/SCV', 'Refinery/SCV', 'SupplyDepot/SCV', 'Barracks/SCV', 'EngineeringBay/SCV', 'Bunker/SCV', 'MissileTurret/SCV', 'SensorTower/SCV', 'Cancel'], #LotV Multiplayer/Terran/Units/SCV/Basic Structures
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'KD8Charge/Reaper'], #LotV Multiplayer/Terran/Units/Reaper
                   ['SelectBuilder', 'Lower/SupplyDepot', 'Halt', 'Cancel', 'Raise/SupplyDepotLowered'], #LotV Multiplayer/Terran/Structures/Supply Depot
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'SpawnChangeling/Overseer', 'Contaminate/Overseer'], #LotV Multiplayer/Zerg/Units/Overseer
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'BuildCreepTumor/Queen', 'MorphMorphalisk/Queen', 'Transfusion/Queen', 'BurrowDown'], #LotV Multiplayer/Zerg/Units/Queen
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'MorphtoObserverSiege/Observer', 'MorphtoObserver/Observer'], #Coop/Protoss/Units/Observer
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'LockOn/Cyclone', 'SwannCommanderRebuild', 'Cancel'], #Coop/Terran/Units/Cyclone
                   ['Marine/Barracks', 'Marauder/Barracks', 'Reaper/Barracks', 'Firebat/Barracks', 'Medic/Barracks', 'HireKelmorianMiners/Barracks', 'HireHammerSecurities/Barracks', 'HireDevilDogs/Barracks', 'MercReaper/Barracks', 'MercMedic/Barracks', 'Cancel'], #Coop/Terran/Structures/Barracks (kinda Raynor Commander)/General (AI)
                   ['GhostAcademy/SCV', 'MercCompound/SCV', 'Factory/SCV', 'Armory/SCV', 'Starport/SCV', 'FusionCore/SCV', 'Cancel'], #Coop/Terran/Units/SCV/Advanced Structures
                   ['Hatchery/Drone', 'Extractor/Drone', 'SpawningPool/Drone', 'EvolutionChamber/Drone', 'BanelingNest/Drone', 'RoachWarren/Drone', 'SpineCrawler/Drone', 'SporeCrawler/Drone', 'ZagaraBileLauncher/Drone', 'Cancel'], #Coop/Zerg/Units/Drone/Basic Structures (Zagara+Kerrigan Commander)
                   ['Larva', 'QueenCoop', 'RespawnZergling/Lair', 'overlordspeed', 'EvolveVentralSacks', 'RallyEgg', 'Rally', 'Hive/Lair', 'Cancel'], #Coop/Zerg/Structures/Lair
                   ['HellionTank/Factory', 'Goliath/Factory', 'SiegeTank/Factory', 'BuildCyclone/Factory', 'Thor/Factory', 'SelectBuilder', 'Rally', 'TechLabFactory/Factory', 'Reactor/Factory', 'Lift', 'Cancel'], #Coop/Terran/Structures/Factory/General (kinda Swann Commander)
                   ['ResearchShieldWall/BarracksTechReactor', 'Stimpack/BarracksTechReactor', 'ResearchPunisherGrenades/BarracksTechReactor', 'ResearchIncineratorGauntlets/BarracksTechReactor', 'ResearchJuggernautPlating/BarracksTechReactor', 'ResearchStabilizerMedpacks/BarracksTechReactor', 'Cancel'], #Coop/Terran Story/Structures/Tech Reactor/Attached to Barracks (Raynor Commander, notAvailable)
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'LightningBomb/Tempest', 'Rally'], #Coop/Protoss/Units/TempestGeneral
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'Impaler/HydraliskImpaler', 'HydraliskFrenzy/HydraliskImpaler', 'BurrowDown'], #Coop/Zerg Story/Units/Hydralisk (Impaler Strain)
                   ['ResearchBansheeCloak/StarportTechLab', 'ResearchShockwaveMissileBattery/StarportTechLab', 'ResearchPhobosClassWeaponsSystem/StarportTechLab', 'ResearchRipwaveMissiles/StarportTechLab', 'Cancel'], #Coop/Terran/Structures/Tech Lab/Attached to Starport (Raynor(+Swann) Commander)
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'DarkArchonConfusion/DarkArchon', 'DarkArchonMindControl/DarkArchon', 'Rally'], #Coop/Protoss/Units/Dark Archon
                   ['ShieldBatteryRecharge/ShieldBattery', 'ShieldBatteryStructureBarrier/ShieldBattery', 'Cancel'], #Coop/Protoss Story/Structures/Shield Battery
                   ['Immortal/RoboticsFacility', 'Colossus/RoboticsFacility', 'Observer/RoboticsFacility', 'Rally', 'UpgradeToRoboticsFacilityWarp/RoboticsFacility', 'Cancel'], #Coop/Protoss/Structures/Robotics Facility
                   ['Larva', 'QueenCoop', 'RespawnZergling/Hive', 'overlordspeed', 'EvolveVentralSacks', 'RallyEgg', 'Rally', 'Cancel'], #Coop/Zerg/Structures/Hive
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'FaceEmbrace/Viper', 'DisablingCloud/Viper', 'ViperConsumption/Viper'], #Coop/Zerg/Units/Viper
                   ['Stop', 'ZagaraVoidCoopNydusWorm/NydusNetwork', 'Rally', 'BunkerLoad', 'BunkerUnloadAll', 'Cancel'], #Coop/Zerg/Structures/Nydus Network (Kerrigan Commander)
                   ['BrokenSolarForge/SolarForge'], #Coop/Protoss Story/Structures/Solar Forge (Karax Commander)/General (Broken)
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'Charge/ZealotAiur', 'VoidZealotWhirlwind/ZealotAiur', 'Rally'], #Coop/Protoss Story/Units/Zealot (Artanis Commander)
                   ['ResearchCharge/TwilightCouncil', 'ResearchDragoonRange/TwilightCouncil', 'ResearchWhirlwind/TwilightCouncil', 'ResearchDragoonChassis/TwilightCouncil', 'Cancel'], #Coop/Protoss/Structures/Twilight Council (Artanis commander)
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'CloakOnBanshee', 'CloakOff', 'IgniteAfterburners/Banshee'], #Coop/Terran/Units/Banshee (Raynor Commander)
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'VoidZealotShadowCharge/ZealotShakuras', 'VoidZealotShadowChargeStun/ZealotShakuras', 'Rally'], #Coop/Protoss Story/Units/Centurion (Vorazun Commander)
                   ['ResearchGraviticBooster/RoboticsBay', 'ResearchBarrier/RoboticsBay', 'ResearchReaverIncreasedScarabCount/RoboticsBay', 'ResearchReaverIncreasedScarabSplashRadius/RoboticsBay', 'Cancel'], #Coop/Protoss/Structures/Robotics Bay (Artanis Commander)
                   ['Attack', 'Explode/HotSSplitterlingBigBurrowed', 'BurrowUp', 'Attack', 'Explode/HotSHunterBurrowed', 'BurrowUp'], #Coop/Zerg Story/Units/Baneling/Burrowed
                   ['ResearchSolarEfficiencyLevel1/SolarForge', 'ResearchSOARepairBeamExtraTarget/SolarForge', 'ResearchSOAOrbitalStrikeUpgrade/SolarForge', 'ResearchSOASolarLanceUpgrade/SolarForge', 'Cancel'], #Coop/Protoss Story/Structures/Solar Forge (Karax Commander)/General
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'VoidSentryChronoBeam/SentryPurifier', 'EnergizerReclamation/SentryPurifier', 'VoidSentryPhasingMode/SentryPurifier', 'VoidSentryMobileMode/SentryPurifier', 'Rally'], #Coop/Protoss Story/Units/Energizer (Karax Commander)
                   ['ResearchHighCapacityBarrels/FactoryTechLab', 'ResearchHellbatHellArmor/FactoryTechLab', 'ResearchAresClassTargetingSystem/FactoryTechLab', 'ResearchMultiLockWeaponsSystem/FactoryTechLab', 'ResearchMaelstromRounds/FactoryTechLab', 'ResearchLockOnRangeUpgrade/FactoryTechLab', 'ResearchCycloneLockOnDamageUpgrade/FactoryTechLab', 'Research330mmBarrageCannon/FactoryTechLab', 'Cancel'], #Coop/Terran/Structures/Tech Lab/Attached to Factory (Swann(+Raynor) Commander)
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'AutoTurret/Raven', 'PointDefenseDrone/Raven', 'InstantHunterSeekerMissile/Raven'], #Coop/Terran/Units/Raven
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'VoidSentryShieldRepairDouble/SentryAiur', 'GuardianShield/SentryAiur', 'Rally'], #Coop/Protoss Story/Units/Sentry
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'MindBolt/K5KerriganBurrowed', 'PsionicLift/K5KerriganBurrowed', 'KerriganVoidCoopEconDrop/K5KerriganBurrowed', 'KerriganVoidCoopCrushingGripWave/K5KerriganBurrowed', 'BurrowUp'], #Coop/Zerg Story/Units/Kerrigan/Burrowed
                   ['Drone/Larva', 'Overlord/Larva', 'Zergling/Larva', 'Aberration/Larva', 'Roach/Larva', 'Hydralisk/Larva', 'Infestor/Larva', 'Ultralisk/Larva', 'SwarmHostMP/Larva', 'Mutalisk/Larva', 'Brutalisk/Larva', 'Cancel', 'SwarmQueenZergling/SwarmQueenEgg', 'SwarmQueenRoach/SwarmQueenEgg', 'SwarmQueenHydralisk/SwarmQueenEgg', 'Cancel'], #Coop/Zerg/Units/Larva/General
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'CorsairMPDisruptionWeb/CorsairMP', 'Rally'], #Coop/Protoss Story/Units/Corsair
                   ['HellionTank/Factory', 'Goliath/Factory', 'SiegeTank/Factory', 'WidowMine/Factory', 'Thor/Factory', 'MercHellion/Factory', 'HireSpartanCompany/Factory', 'HireSiegeBreakers/Factory', 'Cancel'], #Coop/Terran/Structures/Factory/General3
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'MedicHeal/Medic'], #Coop/Terran Story/Units/Medic
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'D8Charge/Reaper'], #Coop/Terran/Units/Reaper (WoL Campaign?)
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'CloakOnBanshee', 'CloakOff', 'GhostHoldFire/Ghost', 'WeaponsFree/Ghost', 'Snipe/Ghost', 'EMP/Ghost', 'NukeCalldown/Ghost', 'Cancel'], #Coop/Terran/Units/Ghost
                   ['Zealot', 'Sentry', 'Stalker', 'HighTemplar', 'DarkTemplar', 'DarkArchon/WarpGate', 'Rally', 'MorphBackToGateway/WarpGate', 'Cancel'], #Coop/Protoss/Structures/Gateway/Warp Gate
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'VoidStasis/DarkTemplarTaldarim', 'Rally'], #Coop/Protoss Story/Units/Blood Hunter
                   ['Probe/Nexus', 'Mothership/Nexus', 'Stop', 'Attack', 'Rally', 'TimeWarp/Nexus', 'Cancel'], #Coop/Protoss/Structures/Nexus
                   ['ResearchShadowFury/DarkShrine', 'ResearchShadowDash/DarkShrine', 'ResearchVoidStasis/DarkShrine', 'ResearchDarkArchonFullStartingEnergy/DarkShrine', 'ResearchDarkArchonMindControl/DarkShrine', 'Cancel'], #Coop/Protoss/Structures/Dark Shrine (Vorazun Commander)
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'ArbiterMPStasisField/ArbiterMP', 'ArbiterMPRecall/ArbiterMP', 'Rally'], #Coop/Protoss/Units/Arbiter
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'Interceptor/CarrierAiur', 'Cancel'], #Coop/Protoss Story/Units/Carrier
                   ['BileLauncherBombardment/BileLauncherZagara', 'Cancel'], #Coop/Zerg Story/Structures/Bile Launcher (Zagara Commander)
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'MindBolt/K5Kerrigan', 'PsionicLift/K5Kerrigan', 'KerriganVoidCoopEconDrop/K5Kerrigan', 'KerriganVoidCoopCrushingGripWave/K5Kerrigan', 'BurrowDown'], #Coop/Zerg Story/Units/Kerrigan/General
                   ['zergmeleeweapons1/EvolutionChamber', 'zergmissileweapons1/EvolutionChamber', 'zerggroundarmor1/EvolutionChamber', 'EvolveKerriganHeroicFortitude/EvolutionChamber', 'EvolveK5ChainLightning/EvolutionChamber', 'EvolveK5Cooldowns/EvolutionChamber', 'Cancel'], #Coop/Zerg/Structures/Evolution Chamber (Kerrigan+Zagara Commander)
                   ['SCV', 'VespeneDrone/PlanetaryFortress', 'StopPlanetaryFortress/PlanetaryFortress', 'Attack', 'Rally', 'CommandCenterLoad', 'CommandCenterUnloadAll', 'Cancel'], #Coop/Terran/Structures/Planetary Fortress
                   ['CommandCenter/SCV', 'Refinery/SCV', 'SupplyDepot/SCV', 'Barracks/SCV', 'EngineeringBay/SCV', 'Bunker/SCV', 'MissileTurret/SCV', 'BuildKelMorianRocketTurret/SCV', 'HiveMindEmulator/SCV', 'Cancel'], #Coop/Terran/Units/SCV/Basic Structures
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'LiberatorAGMode/Liberator', 'IgniteAfterburners/Liberator'], #Coop/Terran/Units/Liberator
                   ['ImmortalityProtocol/ThorWreckage', 'Cancel'], #Coop/Terran/Units/Thor (Swann Commander)/Front 02
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'Feedback/Archon', 'PsiStorm/Archon', 'Rally'], #Coop/Protoss/Units/Archon
                   ['EvolveMuscularAugments/ImpalerDen', 'EvolveAncillaryCarapace/ImpalerDen', 'EvolveFrenzy/ImpalerDen', 'Cancel'], #Coop/Zerg Story/Structures/Impaler Den
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'VoidSentryBlackHole/SOAMothershipv4', 'SOAMothershipLineAttack/SOAMothershipv4', 'SOAMothershipBlink/SOAMothershipv4'], #Coop/Protoss Story/Units/Mothership
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'VoidDarkTemplarShadowFury/DarkTemplarShakuras', 'DarkTemplarShadowDash/DarkTemplarShakuras', 'VoidStasis/DarkTemplarShakuras', 'Rally'], #Coop/Protoss Story/Units/Dark Templar (Vorazun Commander)
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'PoisonNova/HotSNoxious', 'BurrowChargeCampaignNoxious/HotSNoxious', 'BurrowDown'], #Coop/Zerg Story/Units/Ultralisk (Noxious Strain)
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'TargetLock/Monitor', 'SentryTaldarimForceField/Monitor', 'Rally'], #Coop/Protoss Story/Units/Havoc
                   ['Phoenix/Stargate', 'VoidRay/Stargate', 'Oracle/Stargate', 'Arbiter/Stargate', 'Rally', 'UpgradeToStargateWarp/Stargate', 'Cancel'], #Coop/Protoss/Structures/Stargate
                   ['zergflyerattack1', 'zergflyerarmor1', 'EvolveMutaliskRapidRegeneration/Spire', 'EvolveViciousGlaive/Spire', 'EvolveSunderingGlave/Spire', 'EvolveBroodLordSpeed/Spire', 'GreaterSpireBroodlord/Spire', 'Cancel'], #Coop/Zerg/Structures/Spire
                   ['EvolveInfestorEnergyUpgrade/InfestationPit', 'RapidIncubation/InfestationPit', 'HotSPressurizedGlands/InfestationPit', 'Cancel'], #Coop/Zerg/Structures/Infestation Pit
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'HydraliskFrenzy/Hydralisk', 'BurrowDown'], #Coop/Zerg/Units/Hydralisk
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'Feedback/HighArchonTemplar', 'HighArchonPsiStorm/HighArchonTemplar', 'ArchonAdvancedMergeSelection', 'Rally'], #Coop/Protoss Story/Units/High Templar
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'Baneling/HotSSwarmling', 'BurrowDown'], #Coop/Zerg Story/Units/Zergling (Swarmling Strain)
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'Baneling/HotSRaptor', 'BurrowDown'], #Coop/Zerg Story/Units/Zergling (Raptor Strain)
                   ['EvolveChitinousPlating/UltraliskCavern', 'EvolveBurrowCharge/UltraliskCavern', 'EvolveTissueAssimilation/UltraliskCavern', 'Cancel'], #Coop/Zerg/Structures/Ultralisk Cavern (Kerrigan Commander)
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'StalkerBlinkShieldRestoreBase/StalkerShakuras', 'Rally'], #Coop/Protoss Story/Units/Stalker
                   ['EvolveCentrificalHooks/BanelingNest', 'EvolveBanelingCorrosiveBile/BanelingNest', 'EvolveBanelingRupture/BanelingNest', 'EvolveBanelingHeal/BanelingNest', 'Rally', 'ZagaraVoidCoopBanelingSpawner/BanelingNest', 'Cancel'], #Coop/Zerg/Structures/Baneling Nest (Zagara Commander)
                   ['Nexus/Probe', 'Assimilator/Probe', 'Pylon/Probe', 'Gateway/Probe', 'Forge/Probe', 'ShieldBattery/Probe', 'CyberneticsCore/Probe', 'PhotonCannon/Probe', 'KhaydarinMonolith/Probe', 'Cancel'], #Coop/Protoss/Units/Probe/Basic Structures
                   ['Stop', 'Attack', 'SelectBuilder', 'Salvage/PerditionTurret', 'Halt', 'Cancel'], #Coop/Terran Story/Structures/Perdition Turret
                   ['zerglingmovementspeed/SpawningPool', 'EvolveHardenedCarapace/SpawningPool', 'zerglingattackspeed/SpawningPool', 'EvolveZerglingArmorShred/SpawningPool', 'EvolveBileLauncherIncreasedRange/SpawningPool', 'EvolveBileLauncherBombardmentCooldown/SpawningPool', 'Cancel'], #Coop/Zerg/Structures/Spawning Pool (Zagara Commander)
                   ['HydraliskDen/Drone', 'InfestationPit/Drone', 'Spire/Drone', 'NydusNetwork/Drone', 'UltraliskCavern/Drone', 'ScourgeNest/Drone', 'Cancel'], #Coop/Zerg/Units/Drone/Advanced Structures (Zagara+Kerrigan Commander)
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'YamatoGun', 'Hyperjump/Battlecruiser', 'IgniteAfterburners/Battlecruiser'], #Coop/Terran/Units/Battlecruiser (Raynor Commander)
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'GravitonBeamVoidCampaign/PhoenixPurifier', 'Cancel'], #Coop/Protoss Story/Units/Mirage
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', '250mmStrikeCannons/Thor', 'ThorDefensiveMatrix/Thor', 'SelfRepair/Thor', 'Cancel'], #Coop/Terran/Units/Thor (Swann Commander)/Front 01
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'DetonateScourge/Scourge', 'EnableBuildingAttackScourge/Scourge'], #Coop/Zerg Story/Units/General
                   ['HireKelmorianMiners/MercCompound', 'HireDevilDogs/MercCompound', 'HireHammerSecurities/MercCompound', 'HireSpartanCompany/MercCompound', 'HireSiegeBreakers/MercCompound', 'HireHelsAngels/MercCompound', 'HireDuskWing/MercCompound', 'HireDukesRevenge/MercCompound', 'Rally', 'Halt', 'Cancel'], #Coop/Terran Story/Structures/Merc Compound
                   ['Zealot', 'Sentry', 'Stalker', 'HighTemplar', 'DarkTemplar', 'DarkArchon/Gateway', 'Rally', 'UpgradeToWarpGate/Gateway', 'Cancel'], #Coop/Protoss/Structures/Gateway/General (Gateway)
                   ['SCV', 'VespeneDrone/CommandCenter', 'OrbitalCommand/CommandCenter', 'SelectBuilder', 'Rally', 'CommandCenterLoad', 'CommandCenterUnloadAll', 'Lift', 'Cancel'], #Coop/Terran/Structures/Command Center/General
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'Charge/ZealotPurifier', 'Rally'], #Coop/Protoss Story/Units/Sentinel (Karax Commander)
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'LightningBomb/TempestPurifier', 'Rally'], #Coop/Protoss Story/Units/Tempest
                   ['Stop', 'Attack', 'LocustLaunch/SwarmHostRooted', 'SwarmHostUproot', 'Stop', 'Attack', 'LocustFlyingLaunch/SwarmHostSplitARooted', 'SwarmHostUproot', 'Stop', 'Attack', 'LocustLaunchCreeper/SwarmHostSplitBRooted', 'SwarmHostDeepBurrow/SwarmHostSplitBRooted', 'SwarmHostUproot'], #Coop/Zerg Story/Units/Swarm Host/Rooted
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'FighterMode', 'AssaultMode', 'IgniteAfterburners/VikingAssault'], #Coop/Terran/Units/Viking (Raynor Commander)
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'BroodLord/MutaliskBroodlord'], #Coop/Zerg Story/Units/Mutalisk (Brood Lord Strain)
                   ['ProtossGroundWeaponsLevel1/Forge', 'ProtossGroundArmorLevel1/Forge', 'ProtossShieldsLevel1/Forge', 'ResearchKaraxTurretRange/Forge', 'ResearchKaraxTurretAttackSpeed/Forge', 'ResearchStructureBarrier/Forge', 'Cancel'], #Coop/Protoss/Structures/Forge (Karax Commander)
                   ['Stop', 'Attack', 'DarkPylonRecall/DarkPylon', 'Cancel'], #Coop/Protoss Story/Structures/Dark Pylon
                   ['VikingFighter/Starport', 'Banshee/Starport', 'Wraith/Starport', 'Battlecruiser/Starport', 'HireDuskWing/Starport', 'HireHelsAngels/Starport', 'HireDukesRevenge/Starport', 'Cancel'], #Coop/Terran/Structures/Starport/General3
                   ['Stop', 'Attack', 'LurkerHoldFire/LurkerBurrowed', 'LurkerCancelHoldFire/LurkerBurrowed', 'LurkerBurrowUp'], #Coop/Zerg Story/Units/Lurker (Burrowed)
                   ['TerranVehicleAndShipWeaponsLevel1/Armory', 'TerranVehicleAndShipPlatingLevel1/Armory', 'ResearchVehicleWeaponRange/Armory', 'ResearchRegenerativeBioSteel/Armory', 'SelectBuilder', 'Halt', 'Cancel'], #Coop/Terran/Structures/Armory
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'MorphtoOverseerSiege/Overseer', 'MorphtoOverseer/Overseer'], #Coop/Zerg/Units/Overseer
                   ['Immortal/RoboticsFacilityWarp', 'Colossus/RoboticsFacilityWarp', 'Observer/RoboticsFacilityWarp', 'MorphBackToRoboticsFacility/RoboticsFacilityWarp', 'Cancel'], #Coop/Protoss Story/Structures/Warp Robotics Facility
                   ['Phoenix/StargateWarp', 'VoidRay/StargateWarp', 'Oracle/StargateWarp', 'Arbiter/StargateWarp', 'MorphBackToStargate/StargateWarp', 'Cancel'], #Coop/Protoss Story/Structures/Warp Stargate
                   ['Stop', 'Attack', 'SelectBuilder', 'Salvage/KelMorianGrenadeTurret', 'Halt', 'Cancel'], #Coop/Terran Story/Structures/Devastation Turret (Swann Commander)
                   ['ResearchPsiStorm/TemplarArchive', 'ResearchHighTemplarEnergyUpgrade/TemplarArchive', 'ResearchHealingPsionicStorm/TemplarArchive', 'Cancel'], #Coop/Protoss/Structures/Templar Archives (Artanis Commander)
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'MorphToOverseer/Overlord', 'StopGenerateCreep/Overlord', 'BunkerLoad', 'BunkerUnloadAll', 'Cancel'], #Coop/Zerg/Units/Overlord/General (Creeping)
                   ['TerranInfantryWeaponsLevel1/EngineeringBay', 'TerranInfantryArmorLevel1/EngineeringBay', 'ResearchNeosteelFrame/EngineeringBay', 'UpgradeBuildingArmorLevel1/EngineeringBay', 'SelectBuilder', 'ResearchFireSuppressionSystems/EngineeringBay', 'ResearchImprovedTurretAttackSpeed/EngineeringBay', 'Halt', 'Cancel'], #Coop/Terran/Structures/Engineering Bay (Raynor Commander)
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'CorruptionAbility/Corruptor', 'BroodLord/Corruptor', 'Cancel'], #Coop/Zerg/Units/Corruptor
                   ['Attack', 'ResearchDrakkenLaserDrillBFG/DrakkenLaserDrillCoop', 'Cancel'], #Coop/Terran Story/Structures/Drakken Laser Drill
                   ['AnionPulseCrystals/FleetBeacon', 'ResearchDoubleGravitonBeam/FleetBeacon', 'ResearchTempestDisintegration/FleetBeacon', 'ResearchOracleStasisWardUpgrade/FleetBeacon', 'Cancel'], #Coop/Protoss/Structures/Fleet Beacon (Artanis+Vorazun Commander)
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'ReaverScarabs/Reaver', 'Rally'], #Coop/Protoss/Units/Reaver
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'BurrowChargeCampaign/Ultralisk', 'BurrowDown'], #Coop/Zerg/Units/Ultralisk
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'VoidShadowGuardShadowFury/VorazunShadowGuard', 'ShadowGuardBlink/VorazunShadowGuard', 'VoidStasis/VorazunShadowGuard'], #Coop/Protoss Story/Units/Shadow Guard
                   ['Stop', 'Attack', 'SelectBuilder', 'Salvage/KelMorianMissileTurret', 'Halt', 'Cancel'], #Coop/Terran Story/Structures/Spinning Dizzy
                   ['EvolveMuscularAugments/LurkerDen', 'EvolveAncillaryCarapace/LurkerDen', 'EvolveFrenzy/LurkerDen', 'ResearchLurkerRange/LurkerDen', 'Cancel'], #Coop/Zerg Story/Structures/Lurker Den
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'ZagaraVoidCoopBanelingBarrage/ZagaraVoidCoopBurrowed', 'ZagaraVoidCoopSpawnHunterKillers/ZagaraVoidCoopBurrowed', 'ZagaraVoidCoopMassFrenzy/ZagaraVoidCoopBurrowed', 'MassRoachDrop/ZagaraVoidCoopBurrowed', 'BurrowUp'], #Coop/Zerg Story/Units/Zagara/Burrowed
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'SiegeMode', 'Unsiege', 'IgniteAfterburners/SiegeTank'], #Coop/Terran/Units/Siege Tank/General (Raynor Commander)
                   ['Stop', 'Attack', 'SelectBuilder', 'Salvage/MissileTurret', 'Halt', 'Cancel'], #Coop/Terran/Structures/Missile Turret
                   ['Predator/Factory', 'MicroBot/Factory', 'Cancel'], #Coop/Terran/Structures/Factory/General2
                   ['zergflyerattack1', 'zergflyerarmor1', 'EvolveScourgeSplashDamage/ScourgeNest', 'EvolveScourgeGasCostReduction/ScourgeNest'], #Coop/Zerg Story/Structures/Scourge Nest
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'NanoRepair/ScienceVessel', 'Irradiate/ScienceVessel', 'DefensiveMatrixTarget/ScienceVessel'], #Coop/Terran Story/Units/Science Vessel (Swann Commander)
                   ['Larva', 'QueenCoop', 'RespawnZergling/Hatchery', 'overlordspeed', 'EvolveVentralSacks', 'RallyEgg', 'Rally', 'Lair/Hatchery', 'Cancel'], #Coop/Zerg/Structures/Hatchery
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'VoidHighTemplarPsiOrb/HighTemplarTaldarim', 'VoidHighTemplarMindBlast/HighTemplarTaldarim', 'AscendantSacrifice/HighTemplarTaldarim', 'Rally'], #Coop/Protoss Story/Units/Ascendant
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'Viper/MutaliskViper'], #Coop/Zerg Story/Units/Mutalisk (Viper Strain)
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'WraithCloakOn/Wraith', 'WraithCloakOff/Wraith'], #Coop/Terran Story/Units/Wraith (Swann Commander)
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'SwarmHostDeepBurrow/SwarmHostSplitB', 'SwarmHostRoot'], #Coop/Zerg Story/Units/Swarm Host/Creeper Strain
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'MorphToHellion/Hellion', 'MorphToHellionTank/Hellion', 'SwannCommanderRebuild'], #Coop/Terran/Units/Hellion (Swann Commander)
                   ['ResearchPersonalCloaking/GhostAcademy', 'ResearchGhostEnergyUpgrade/GhostAcademy', 'SelectBuilder', 'NukeArm/GhostAcademy', 'Halt', 'Cancel'], #Coop/Terran/Structures/Ghost Academy
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', '250mmStrikeCannons/ThorWreckageSwann', 'ThorDefensiveMatrix/ThorWreckageSwann', 'SelfRepair/ThorWreckageSwann', 'Cancel'], #Coop/Terran/Units/Thor (Swann Commander)/Front 03
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'ZagaraVoidCoopBanelingBarrage/ZagaraVoidCoop', 'ZagaraVoidCoopSpawnHunterKillers/ZagaraVoidCoop', 'ZagaraVoidCoopMassFrenzy/ZagaraVoidCoop', 'MassRoachDrop/ZagaraVoidCoop', 'BurrowDown'], #Coop/Zerg Story/Units/Zagara/General
                   ['ResearchBansheeCloak/StarportTechReactor', 'ResearchShockwaveMissileBattery/StarportTechReactor', 'ResearchPhobosClassWeaponsSystem/StarportTechReactor', 'ResearchRipwaveMissiles/StarportTechReactor', 'Cancel'], #Coop/Terran Story/Structures/Tech Reactor/Attached to Starport (Raynor(+Swann) Commander)
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'VoidSentryShieldRepair/Sentry', 'GuardianShield/Sentry', 'ForceField/Sentry', 'Rally'], #Coop/Protoss/Units/Sentry/General
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'DetonateScourge/Scourge', 'DisableBuildingAttackScourge/Scourge'], #Coop/Zerg Story/Units/Building Attack Enabled
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'HerculesLoad/Hercules', 'HerculesUnloadAll/Hercules', 'HyperjumpHercules/Hercules'], #Coop/Terran Story/Units/Hercules (Swann Commander)
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'SpectreHoldFire/Spectre', 'SpectreWeaponsFree/Spectre', 'MindBlast/Spectre', 'VoodooShield/Spectre', 'SpectreDomination/Spectre', 'NukeCalldown/Spectre', 'Cancel'], #Coop/Terran Story/Units/Spectre (Tosh framework, AI)
                   ['Attack', 'SetRallyPointSwarmHost/SwarmHostBurrowedMP', 'SwarmHost/SwarmHostBurrowedMP', 'SwarmHostBurrowUp'], #Coop/Zerg/Units/Swarm Host/Burrowed
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'ImmortalShakurasShadowCannon/ImmortalShakuras'], #Coop/Protoss Story/Units/Annihilator
                   ['ResearchGraviticBooster/RoboticsBay', 'ResearchExtendedThermalLance/RoboticsBay', 'ResearchReaverIncreasedScarabSplashRadius/RoboticsBay', 'ResearchBarrier/RoboticsBay', 'Cancel'], #Coop/Protoss/Structures/Robotics Bay (Karax Commander)(not tested)
                   ['zergflyerattack1', 'zergflyerarmor1', 'EvolveMutaliskRapidRegeneration/GreaterSpire', 'EvolveViciousGlaive/GreaterSpire', 'EvolveSunderingGlave/GreaterSpire', 'EvolveBroodLordSpeed/GreaterSpire', 'Cancel'], #Coop/Zerg/Structures/Greater Spire
                   ['ResearchShieldWall/BarracksTechLab', 'Stimpack/BarracksTechLab', 'ResearchPunisherGrenades/BarracksTechLab', 'ResearchIncineratorGauntlets/BarracksTechLab', 'ResearchJuggernautPlating/BarracksTechLab', 'ResearchStabilizerMedpacks/BarracksTechLab', 'Cancel'], #Coop/Terran/Structures/Tech Lab/Attached to Barracks (Raynor Commander)
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'Lurker/HydraliskLurker', 'HydraliskFrenzy/HydraliskLurker', 'BurrowDown'], #Coop/Zerg Story/Units/Hydralisk (Lurker Strain)
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'ImmortalOverload/ImmortalAiur', 'ImmortalShakurasShadowCannon/ImmortalAiur'], #Coop/Protoss Story/Units/Immortal
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'SiegeMode', 'SwannCommanderRebuild'], #Coop/Terran/Units/Siege Tank/General (Wreckage,Swann Commander)
                   ['EvolveGlialRegeneration/RoachWarren', 'EvolveTunnelingClaws/RoachWarren', 'EvolveHydriodicBile/RoachWarren', 'EvolveAdaptivePlating/RoachWarren', 'Cancel'], #Coop/Zerg/Structures/Roach Warren (Kerrigan Commander)
                   ['EvolveMuscularAugments/HydraliskDen', 'EvolveAncillaryCarapace/HydraliskDen', 'EvolveFrenzy/HydraliskDen', 'ResearchLurkerRange/HydraliskDen', 'LurkerDen/HydraliskDen', 'Cancel'], #Coop/Zerg/Structures/Hydralisk Den (Kerrigan Commander)
                   ['ResearchHighCapacityBarrels/FactoryTechReactor', 'ResearchHellbatHellArmor/FactoryTechReactor', 'ResearchAresClassTargetingSystem/FactoryTechReactor', 'ResearchMultiLockWeaponsSystem/FactoryTechReactor', 'ResearchMaelstromRounds/FactoryTechReactor', 'ResearchLockOnRangeUpgrade/FactoryTechReactor', 'ResearchCycloneLockOnDamageUpgrade/FactoryTechReactor', 'Research330mmBarrageCannon/FactoryTechReactor', 'Cancel'], #Coop/Terran Story/Structures/Tech Reactor/Attached to Factory (Swann Commander)
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'SpiderMine/Vulture', 'SpiderMineReplenish/Vulture', 'IgniteAfterburners/Vulture', 'Cancel'], #Coop/Terran Story/Units/Vulture (Raynor Commander)
                   ['Marine/Barracks', 'Marauder/Barracks', 'Firebat/Barracks', 'Medic/Barracks', 'SelectBuilder', 'Rally', 'TechLabBarracks/Barracks', 'Reactor/Barracks', 'TechReactorAI/Barracks', 'Lift', 'Cancel'], #Coop/Terran/Structures/Barracks (kinda Raynor Commander)/General
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'HyperionVoidCoopHyperjump/HyperionVoidCoop', 'HyperionVoidCoopYamatoCannon/HyperionVoidCoop', 'HyperionAdvancedPDD/HyperionVoidCoop'], #Coop/Terran Story/Units/Hyperion (Raynor Commander)
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'BuildCreepTumor/QueenCoop', 'MorphMorphalisk/QueenCoop', 'Transfusion/QueenCoop', 'BurrowDown'], #Coop/Zerg/Units/Queen
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'Explode/HotSHunter', 'EnableBuildingAttack/HotSHunter', 'BurrowDown'], #Coop/Zerg Story/Units/Baneling/Hunter Strain
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'MindBolt/K5KerriganBurrowed', 'PsionicLift/K5KerriganBurrowed', 'WildMutation/K5KerriganBurrowed', 'K5Leviathan/K5KerriganBurrowed', 'BurrowUp'], #LotV Campaign/Zerg Story/Units/Kerrigan/Burrowed
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'DutchPlaceTurret/Swann'], #LotV Campaign/Terran Story/Units/Rory Swann
                   ['ResearchShieldWall/BarracksTechReactor', 'Stimpack/BarracksTechReactor', 'ReaperSpeed/BarracksTechReactor', 'Cancel'], #LotV Campaign/Terran Story/Units/Tech Reactor/Attached to Barracks
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'StukovBossBlast/InfestedStukov', 'DevastatingShot/InfestedStukov', 'StukovInfestedTerrans/InfestedStukov', 'StukovCrystalChannel/InfestedStukov'], #LotV Campaign/Zerg Story/Units/Alexei Stukov
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'OdinBarrage/Odin', 'Cancel'], #LotV Campaign/Terran Story/Units/Odin
                   ['Larva', 'Queen', 'RespawnZergling/Hive', 'overlordspeed', 'EvolveVentralSacks', 'RallyEgg', 'Rally', 'Cancel'], #LotV Campaign/Zerg/Structures/Hive
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'ArtanisLightningDash/ArtanisVoid', 'ArtanisAstralWind/ArtanisVoid', 'Rally'], #LotV Campaign/Protoss Story/Units/Artanis/Hero Zealot
                   ['Marine/Barracks', 'Marauder/Barracks', 'Reaper/Barracks', 'Ghost/Barracks', 'Medic/Barracks', 'Firebat/Barracks', 'Spectre/Barracks', 'SelectBuilder', 'Rally', 'TechLabBarracks/Barracks', 'Reactor/Barracks', 'Lift', 'Cancel'], #LotV Campaign/Protoss Story/Structures/Barracks/General
                   ['ResearchCharge/TwilightCouncil', 'ResearchStalkerTeleport/TwilightCouncil', 'WarpInVulcanChampion/TwilightCouncil', 'WarpInReaverChampion/TwilightCouncil', 'WarpInFenixChampion/TwilightCouncil', 'WarpInDarkArchonChampion/TwilightCouncil'], #LotV Campaign/Protoss/Structues/Twilight Council
                   ['ResearchHighCapacityBarrels/FactoryTechLab', 'ResearchSiegeTech/FactoryTechLab', 'ResearchStrikeCannons/FactoryTechLab', 'Cancel'], #LotV Campaign/Protoss Story/Structures/Attached to Factory
                   ['Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'ImpalerBurrowUp'], #LotV Campaign/Zerg Story/Units/Impaler/Burrowed
                   ['Larva', 'Queen', 'RespawnZergling/Hatchery', 'overlordspeed', 'EvolveVentralSacks', 'RallyEgg', 'Rally', 'Lair/Hatchery', 'Cancel'], #LotV Campaign/Zerg/Structures/Hatchery
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'SpectreHoldFire/Spectre', 'SpectreWeaponsFree/Spectre', 'UltrasonicPulse/Spectre', 'Obliterate/Spectre', 'CloakOnBanshee', 'SpectreNukeCalldown/Spectre', 'Cancel'], #LotV Campaign/Terran Story/Units/Spectre/General
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'SJHyperionFightersRecall/SJHyperion', 'SJHyperionBlink/SJHyperion', 'SJHyperionFighters/SJHyperion', 'SJHyperionYamato/SJHyperion', 'SJHyperionLightningStorm/SJHyperion'], #LotV Campaign/Terran Story/Units/Hyperion
                   ['VikingFighter/Starport', 'Medivac/Starport', 'Raven/Starport', 'Banshee/Starport', 'Battlecruiser/Starport', 'Wraith/Starport', 'SelectBuilder', 'Rally', 'TechLabStarport/Starport', 'Reactor/Starport', 'Lift', 'Cancel'], #LotV Campaign/Protoss Story/Structures/Starport/General
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'QueenClassicParasite/QueenClassic', 'QueenMPEnsnare/QueenClassic', 'QueenMPSpawnBroodlings/QueenClassic', 'CreepTumor/QueenClassic'], #LotV Campaign/Zerg Story/Units/Queen
                   ['ResearchMedivacEnergyUpgrade/StarportTechReactor', 'ResearchBansheeCloak/StarportTechReactor', 'ResearchRavenEnergyUpgrade/StarportTechReactor', 'WraithCloak/StarportTechReactor', 'ResearchDurableMaterials/StarportTechReactor', 'ResearchSeekerMissile/StarportTechReactor', 'Cancel'], #LotV Campaign/Terran Story/Units/Tech Reactor/Attached to Starport
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'FenixSOACharge/FenixChampion', 'FenixWhirlwind/FenixChampion', 'VoidShieldCapacitor/FenixChampion', 'Rally'], #LotV Campaign/Protoss Story/Units/Fenix/General
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'AlarakKnockback/AlarakChampion', 'AlarakDeadlyCharge/AlarakChampion', 'Rally'], #LotV Campaign/Protoss Story/Units/Alarak
                   ['MindBolt/KerriganVoidBurrowed', 'PsionicLift/KerriganVoidBurrowed', 'WildMutation/KerriganVoidBurrowed', 'K5Leviathan/KerriganVoidBurrowed', 'BurrowUp'], #LotV Campaign/Zerg Story/Units/Kerrigan/Kerrigan - Void - Burrowed
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'MindBlast/Tosh', 'VoodooShield/Tosh', 'Consumption/Tosh', 'HeroNukeCalldown/Tosh'], #LotV Campaign/Terran Story/Units/Gabriel Tosh
                   ['hydraliskspeed/HydraliskDen', 'LurkerDen/HydraliskDen', 'Cancel'], #LotV Campaign/Zerg/Structures/Hydralisk Den
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'BurrowChargeCampaign/HotSTorrasque', 'BurrowDown'], #LotV Campaign/Zerg Story/Units/Ultralisk (Torrasque)
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'ImpalerBurrowDown'], #LotV Campaign/Zerg Story/Units/Impaler/General
                   ['Stop', 'Attack', 'BurrowUp', 'LocustFlyingLaunch/SwarmHostSplitABurrowed', 'LocustLaunch/SwarmHostBurrowed', 'LocustLaunchCreeper/SwarmHostSplitBBurrowed', 'SwarmHostDeepBurrow/SwarmHostSplitBBurrowed', 'SwarmHostUprootUnburrow'], #LotV Campaign/Zerg Story/Units/Swarm Host/Burrowed
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'KerriganVoidKineticBlast/KerriganVoidUlnar02', 'KerriganVoidSpawnBanelings/KerriganVoidUlnar02', 'KerriganVoidApocalypse/KerriganVoidUlnar02'], #LotV Campaign/Zerg Story/Units/Kerrigan/Kerrigan - Ulnar
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'Explode/HotSSplitterlingBig', 'DisableBuildingAttack/HotSSplitterlingBig', 'BurrowDown'], #LotV Campaign/Zerg Story/Units/Baneling (Splitter Strain)/Enabled Building Attack
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'Drag/Dehaka', 'DehakaMirrorImage/Dehaka', 'DehakaHeal/Dehaka', 'BurrowDown'], #LotV Campaign/Zerg Story/Units/Dehaka
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'PlantC4Charge/Raynor', 'TossGrenade/Raynor', 'ExperimentalPlasmaGun/Raynor', 'TheMorosDevice/Raynor'], #LotV Campaign/Terran Story/Units/Jim Raynor/Castanar
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'MindBolt/KerriganVoid', 'PsionicLift/KerriganVoid', 'WildMutation/KerriganVoid', 'K5Leviathan/KerriganVoid', 'Cancel'], #LotV Campaign/Zerg Story/Units/Kerrigan/Kerrigan - Void
                   ['ResearchHighCapacityBarrels/FactoryTechReactor', 'ResearchSiegeTech/FactoryTechReactor', 'Cancel'], #LotV Campaign/Terran Story/Units/Tech Reactor/Attached to Factory
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'SwarmQueenParasiticInvasion/HugeSwarmQueen', 'SwarmQueenZergling/HugeSwarmQueen', 'SwarmQueenRoach/HugeSwarmQueen', 'SwarmQueenHydralisk/HugeSwarmQueen', 'BurrowDown'], #LotV Campaign/Zerg Story/Units/Niadra/Stage 3
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'Explode/HotSSplitterlingBig', 'EnableBuildingAttack/HotSSplitterlingBig', 'BurrowDown'], #LotV Campaign/Zerg Story/Units/Baneling (Splitter Strain)/General
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'FenixSOACharge/FenixSOA', 'FenixWhirlwind/FenixSOA', 'Rally'], #LotV Campaign/Protoss Story/Units/Fenix/SOA Calldown
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'MindBolt/KerriganGhostLab', 'PsionicLift/KerriganGhostLab'], #LotV Campaign/Zerg Story/Units/Kerrigan/Umoja Missions
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'MindBolt/K5Kerrigan', 'PsionicLift/K5Kerrigan', 'WildMutation/K5Kerrigan', 'K5Leviathan/K5Kerrigan', 'BurrowDown'], #LotV Campaign/Zerg Story/Units/Kerrigan/General
                   ['MindControl/HiveMindEmulator', 'Cancel'], #LotV Campaign/Terran Story/Units/Hive Mind Emulator
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'KerriganEpilogue03QuantumRay/KerriganEpilogue03', 'KerriganEpilogue03Heal/KerriganEpilogue03', 'KerriganEpilogue03CreepTeleport/KerriganEpilogue03', 'KerriganEpilogue03Extinction/KerriganEpilogue03', 'Cancel'], #LotV Campaign/Zerg Story/Units/Kerrigan/Kerrigan - Empowered
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'Drag/DehakaMirrorImage', 'BurrowDown'], #LotV Campaign/Zerg Story/Units/Dehaka Spawn
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'ZeratulBlink/ZeratulVoidAiur01', 'PrologueVoidArmor/ZeratulVoidAiur01', 'ShadowBlade/ZeratulVoidAiur01', 'Rally'], #LotV Campaign/Protoss Story/Units/Zeratul/Aiur 01
                   ['Larva', 'Queen', 'RespawnZergling/Lair', 'overlordspeed', 'EvolveVentralSacks', 'RallyEgg', 'Rally', 'Hive/Lair', 'Cancel'], #LotV Campaign/Zerg/Structures/Lair
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'NovaSnipe/Nova', 'Domination/Nova', 'ReleaseMinion/Nova', 'HeroNukeCalldown/Nova', 'Cancel'], #LotV Campaign/Terran Story/Units/Nova
                   ['ResearchMedivacEnergyUpgrade/StarportTechLab', 'ResearchDurableMaterials/StarportTechLab', 'ResearchSeekerMissile/StarportTechLab', 'ResearchRavenEnergyUpgrade/StarportTechLab', 'ResearchBansheeCloak/StarportTechLab', 'Cancel'], #LotV Campaign/Protoss Story/Structures/Attached to Starport
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'ParasiticInvasion/LarvalQueen', 'GrowSwarmQueen/LarvalQueen'], #LotV Campaign/Zerg Story/Units/Niadra/Larva
                   ['ArtanisChannel/ArtanisVoid', 'ArtanisChannelOff/ArtanisVoid'], #LotV Campaign/Protoss Story/Units/Artanis/Extra
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'RaynorSnipe/RaynorCommando'], #LotV Campaign/Terran Story/Units/Jim Raynor/Char
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'BuildCreepTumor/Queen', 'QueenBurstHeal/Queen', 'MorphMorphalisk/Queen', 'DeepTunnel/Queen', 'BurrowDown'], #LotV Campaign/Zerg/Units/Queen
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'BonesHeal/Stetmann'], #LotV Campaign/Terran Story/Units/Egon Stetmann
                   ['Vulture/Factory', 'Hellion/Factory', 'SiegeTank/Factory', 'Diamondback/Factory', 'Goliath/Factory', 'Thor/Factory', 'CampaignVehicles/Factory', 'SelectBuilder', 'Rally', 'TechLabFactory/Factory', 'Reactor/Factory', 'Lift', 'Cancel'], #LotV Campaign/Protoss Story/Structures/Factory/General
                   ['Phoenix/StargateWarp', 'VoidRay/StargateWarp', 'Carrier/StargateWarp', 'MorphBackToStargate/StargateWarp', 'Cancel'], #LotV Campaign/Protoss Story/Structures/Warp Stargate
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'FungalGrowth/Infestor', 'InfestedTerrans/Infestor', 'InfestorConsumption/Infestor', 'Cancel', 'BurrowDown'], #LotV Campaign/Zerg/Units/Infestor/General
                   ['BuildHercules/Starport', 'Raven/Starport', 'Cancel'], #LotV Campaign/Protoss Story/Structures/Starport/AI Mess 01
                   ['Phoenix/Stargate', 'VoidRay/Stargate', 'Carrier/Stargate', 'Rally', 'UpgradeToStargateWarp/Stargate', 'Cancel'], #LotV Campaign/Protoss/Structues/Stargate
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'Reclamation/KaraxChampion', 'PhaseCannon/KaraxChampion', 'Rally'], #LotV Campaign/Protoss Story/Units/Karax
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'ArmorpiercingMode', 'Cancel'], #LotV Campaign/Protoss Story/Structures/Thor/General
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'Explode/HotSHunter', 'DisableBuildingAttack/HotSHunter', 'BurrowDown'], #LotV Campaign/Zerg Story/Units/Baneling (Hunter Strain)/Enabled Building Attack
                   ['ProtossAirWeaponsLevel1/CyberneticsCore', 'ProtossAirArmorLevel1/CyberneticsCore', 'ResearchHallucination/CyberneticsCore', 'ResearchWarpGate/CyberneticsCore'], #LotV Campaign/Protoss/Structues/Cybernetics Core
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'SpectreHoldFire/Spectre', 'SpectreWeaponsFree/Spectre', 'UltrasonicPulse/Spectre', 'Obliterate/Spectre', 'CloakOff', 'SpectreNukeCalldown/Spectre', 'Cancel'], #LotV Campaign/Terran Story/Units/Spectre/Cloaked
                   ['Hellion/Factory', 'Goliath/Factory', 'SiegeTank/Factory', 'Diamondback/Factory', 'Thor/Factory', 'MercHellion/Factory', 'HireSpartanCompany/Factory', 'HireSiegeBreakers/Factory', 'Cancel'], #LotV Campaign/Protoss Story/Structures/Factory/AI Mess 02
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'ZeratulBlink/ZeratulVoid', 'ZeratulStun/ZeratulVoid', 'Rally'], #LotV Campaign/Protoss Story/Units/Zeratul/Void
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'MassRecall/Artanis', 'Vortex/Artanis'], #LotV Campaign/Protoss Story/Units/Artanis/Mothership
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'VorazunBlink/VorazunChampion', 'MohandarOmnislash/VorazunChampion', 'Rally'], #LotV Campaign/Protoss Story/Units/Vorazun
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'SwarmQueenParasiticInvasion/LargeSwarmQueen', 'SwarmQueenZergling/LargeSwarmQueen', 'SwarmQueenRoach/LargeSwarmQueen', 'GrowHugeQueen/LargeSwarmQueen', 'BurrowDown'], #LotV Campaign/Zerg Story/Units/Niadra/Stage 2
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'ZeratulBlink/Zeratul', 'ZeratulStun/Zeratul'], #LotV Campaign/Protoss Story/Units/Zeratul/Wings of Liberty
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'SwarmQueenParasiticInvasion/SwarmQueen', 'SwarmQueenZergling/SwarmQueen', 'GrowLargeQueen/SwarmQueen', 'BurrowDown'], #LotV Campaign/Zerg Story/Units/Niadra/Stage 1
                   ['Move', 'Stop', 'MoveHoldPosition', 'MovePatrol', 'Attack', 'TossGrenadeTychus/TychusCommando']] #LotV Campaign/Terran Story/Units/Tychus Findlay

# Read the settings
settings_parser = SafeConfigParser()
settings_parser.optionxform = str
settings_parser.read('MapDefinitions.ini')

I18N_parser = SafeConfigParser()
I18N_parser.optionxform = str
I18N_parser.read('KeyboardLayouts.ini')

race_dict = {"P": 0,
             "T": 1,
             "Z": 2,
             "R": 3}

prefix = settings_parser.get("Filenames", "Prefix")
suffix = settings_parser.get("Filenames", "Suffix")
Seed_files_folder = settings_parser.get("Filenames", "Seed_files_folder")
races = ["P", "T", "R", "Z"]
layouts = ["RM"]
layoutIndices = {"LMM": 0,
                 "RMM": 1,
                 "RM": 2}
righty_index = {0: False,
                1: True,
                2: True}

def verify_file(filepath):
    print("verify file: " + filepath)
    hotkeys_file = open(filepath, 'r')
    dict = {}
    for line in hotkeys_file:
        line = line.strip()
        if len(line) == 0 or line[0] == "[":
            continue
        pair = line.split("=")
        key = pair[0]
        if key in dict:
            dict[key] = [True, pair[1], key, dict[key][3]]
        else:
            dict[key] = [True, pair[1], key, ""]

    # Check for duplicates
    if SHOW_DUPLICATES:
        verify_parser = SafeConfigParser()
        verify_parser.optionxform = str
        dup_dict = {}
        verify_parser.read(filepath)
        gen_items = verify_parser.items('Hotkeys')
        for pair in gen_items:
            if pair[1] in dup_dict:
                dup_dict[pair[1]].append(pair[0])
            else:
                dup_dict[pair[1]] = [pair[0]]
        for key in dup_dict:
            array = dup_dict[key]
            if len(array) > 1:
                print("============================")
                print(key + "    DUPLICATES")
                for a in array:
                    print(a)

    for same_set in SAME_CHECKS:
        mismatched = False
        value = dict[same_set[0]][1]
        for item in same_set:
            if not dict[item][1] == value:
                mismatched = True
        if mismatched:
            print("============================")
            print("---- Mismatched values ----")
            for item in same_set:
                print(item + " = " + dict[item][1])

    for conflict_set in CONFLICT_CHECKS:
        hotkeys = []
        count_hotkeys = {}
        for item in conflict_set:
            if not dict.__contains__(item):
                print('WARNING: ' + item + ' does not exist in HotKey-file')
            else :
                append = dict[item][1]
                hotkeys.append(append)
        for key in hotkeys:
            if not key in count_hotkeys:
                count_hotkeys[key] = 1
            else:
                count_hotkeys[key] = count_hotkeys[key] + 1
        for count in count_hotkeys:
            if count_hotkeys[count] > 1:
                print("============================")
                print("---- Conflict of hotkeys ----")
                for item in conflict_set:
                    key = dict[item][1]
                    if count_hotkeys[key] > 1:
                        print(item + " = " + key)
                # print(conflict_set)
    print("")

def parse_pair(parser, key, values, map_name, index, altgr):
    parsed = ""
    first = True
    for value in values:
        bits = value.split("+")
        if not first:
            parsed += ","
        if bits[0] == "Alt" and altgr == 1:
            bits[0] = "Control+Alt"
        last_bit = bits[len(bits) - 1]
        try:
            if index < 0:
                bits[len(bits) - 1] = parser.get(map_name, last_bit)
            else:
                bits[len(bits) - 1] = parser.get(map_name, last_bit).split(",")[index]
        except:
            last_bit = last_bit  # Do nothing
        # if is_rl_shift and "|" in bits[len(bits)-1]:
        #    try:
        #        unused = parser.get("MappingTypes", key).split(",")
        #        bits[len(bits)-1] = bits[len(bits)-1].split("|")[0]
        #    except:
        #        bits[len(bits)-1] = bits[len(bits)-1].split("|")[1]
        #    if not bits[len(bits)-1] == "":
        #        parsed += "+".join(bits)
        if not bits[len(bits) - 1] == "":
            parsed += "+".join(bits)
            
        first = False
    return parsed

def generate_layout(filename, race, layout, layoutIndex):
    filepath = Seed_files_folder + "/" + filename
    hotkeys_file = open(filepath, 'r')
    output = ""
    for line in hotkeys_file:
        line = line.strip()
        if len(line) == 0 or line[0] == "[":
            output += line + "\n"
            continue
        pair = line.split("=")
        key = pair[0]
        values = pair[1].split(",")
        output += key + "="
        
        # No need to distinguish between map types anymore. Just use GlobalMaps
        if key in EXCLUDE_MAPPING:
            output += pair[1]
        else:
            try:
                output += parse_pair(settings_parser, key, values, 'GlobalMaps', GLOBAL, 0)
            except:
                output += pair[1]
            
        # if key in CAMERA_KEYS:
            # if "R" in layout:
                # output += parse_pair(settings_parser, key, values, 'GlobalMaps', GLOBAL, 0)
            # else:
                # output += pair[1]
        # #elif race == "Z" and "MM" in layout and key in ZERG_CONTROL_GROUP_SPECIAL:
        # #    output += parse_pair(settings_parser, key, values, race + 'SCGMaps', layoutIndex, 0)
        # elif key in CONTROL_GROUP_KEYS:
            # output += parse_pair(settings_parser, key, values, race + 'CGMaps', layoutIndex, 0)
        # elif key in GENERAL_KEYS:
            # if "R" in layout:
                # output += parse_pair(settings_parser, key, values, 'GlobalMaps', GLOBAL, 0)
            # else:
                # output += pair[1]
        # else:
            # try:
                # #maptypes = settings_parser.get("MappingTypes", key).split(",")
                # maptypes = ["A","A","A","A"] # Only use ability maps
                # output += parse_pair(settings_parser, key, values, race + maptypes[race_dict[race]] + "Maps", layoutIndex, 0)
            # except:
                # output += pair[1]
        output += "\n"
    hotkeys_file.close()
    newfilename = filename.replace("LM", layout)
    newfilepath = Seed_files_folder + "/" + newfilename
    fileio = open(newfilepath, 'w')
    fileio.write(output)
    fileio.close()
    if VERIFY_ALL:
        verify_file(newfilepath)
    return newfilename

def shift_hand_size(filename, shift_right, hand_size, is_righty):
    filepath = Seed_files_folder + "/" + filename
    hotkeys_file = open(filepath, 'r')
    output = ""
    if is_righty:
        map_prefix = "R"
    else:
        map_prefix = "L"
    for line in hotkeys_file:
        line = line.strip()
        if len(line) == 0 or line[0] == "[":
            output += line + "\n"
            continue
        pair = line.split("=")
        key = pair[0]
        values = pair[1].split(",")
        output += key + "="
        
        if key in EXCLUDE_MAPPING:
            output += pair[1]
        elif shift_right:
            output += parse_pair(settings_parser, key, values, map_prefix + 'ShiftRightMaps', GLOBAL, 0)
        else:
            output += parse_pair(settings_parser, key, values, map_prefix + 'ShiftLeftMaps', GLOBAL, 0)        
        output += "\n"
    hotkeys_file.close()
    newfilename = ""
    if "MM " in filename:
        newfilename = filename.replace("MM ", hand_size + "M ")
    else:
        newfilename = filename.replace("M ", hand_size + " ")
    newfilepath = Seed_files_folder + "/" + newfilename
    fileio = open(newfilepath, 'w')
    fileio.write(output)
    fileio.close()
    if VERIFY_ALL:
        verify_file(newfilepath)
    return newfilename

def translate_file(filename, is_righty):
    if not TRANSLATE:
        return
    seed_filepath = Seed_files_folder + "/" + filename
    layouts = I18N_parser.sections()
    for layout_name in layouts:
        hotkeys_file = open(seed_filepath, 'r')
        output = ""
        if is_righty:
            altgr = int(I18N_parser.get(layout_name, "AltGr"))
        else:
            altgr = 0
    
        for line in hotkeys_file:
            line = line.strip()
            if len(line) == 0 or line[0] == "[":
                output += line + "\n"
                continue
            pair = line.split("=")
            key = pair[0]
            values = pair[1].split(",")
            output += key + "="
            
            output += parse_pair(I18N_parser, key, values, layout_name, GLOBAL, altgr)        
            output += "\n"

        hotkeys_file.close()
        filepath = layout_name + "/" + filename
        if not os.path.isdir(layout_name):
            os.makedirs(layout_name)
        fileio = open(filepath, 'w')
        fileio.write(output)
        fileio.close()
        if VERIFY_ALL:
            verify_file(filepath)
    
# Main part of the script. For each race, generate each layout, and translate that layout for large and small hands.

# NEW - Generate the file from TheCoreSeed.ini
def generate_seed_files():
    theseed_parser = SafeConfigParser()
    theseed_parser.optionxform = str
    theseed_parser.read('TheCoreSeed.ini')
    
    theseed = open("TheCoreSeed.ini", 'r')
    outputs = ["", "", "", ""]
    for line in theseed:
        line = line.strip()
        if len(line) == 0 or line[0] == "[":
            for i in range(4):
                outputs[i] += line + "\n"
            continue    

        pair = line.split("=")
        key = pair[0]
        values = pair[1].split("|")
        numvals = len(values)
        if numvals == 1:
            # it is a copy of another value
            if theseed_parser.has_option("Hotkeys", values[0]):
                values = theseed_parser.get("Hotkeys", values[0]).split("|")
            elif theseed_parser.has_option("Commands", values[0]):
                values = theseed_parser.get("Commands", values[0]).split("|")
            else:
                values = [values[0], values[0], values[0], values[0]]
            numvals = len(values)
        if numvals == 2:
            values = [values[0], values[0], values[0], values[0]]  # all layouts are the same
        for i in range(4):
            outputs[i] += key + "=" + values[i] + "\n"
    i = 0
    for r in races:
        filename = prefix + " " + r + "LM " + suffix
        filepath = Seed_files_folder + "/" + filename
        fileio = open(filepath, 'w')
        fileio.write(outputs[i])
        fileio.close()
        i += 1

def veryfy_seed_with_generate():
    print("-------------------------")
    print(" Start Comparing Seeds Files with Generated Files")
    
    for race in races:    
        
        filepath_seed = prefix + " " + race + "LM " + suffix
        filepath_gen = Seed_files_folder + "/" + filepath_seed
        
        parser_seed = SafeConfigParser()
        parser_seed.optionxform = str
        parser_seed.read(filepath_seed)
        
        parser_gen = SafeConfigParser()
        parser_gen.optionxform = str
        parser_gen.read(filepath_gen)
        
        theseed_parser = SafeConfigParser()
        theseed_parser.optionxform = str
        theseed_parser.read('TheCoreSeed.ini')

        new_defaults_parser = SafeConfigParser()
        new_defaults_parser.optionxform = str
        new_defaults_parser.read('NewDefaults.ini')

        print("Race: " + race)
        print()
        
        print("In Seed not in Gen")
        for section in theseed_parser.sections():
            for gen_item in parser_seed.items(section):
                key = gen_item[0]
                if not parser_gen.has_option(section, key):
                    print(key)
        print()
        print("In Seed diffrent in Gen")
        for section in theseed_parser.sections():
            for gen_item in parser_seed.items(section):
                key = gen_item[0]
                value_seed = gen_item[1]
                if parser_gen.has_option(section, key):
                    value_gen = parser_gen.get(section, key)
                    value_seed = gen_item[1]
                    if value_seed != value_gen:
                        value_seedini = theseed_parser.get(section, key)
                        values = value_seedini.split("|")
                        length = len(values)
                        iscopy = False
                        origninal = ""
                        if length == 1:  # this is a copy
                            iscopy = True
                            origninal = values[0]
                        if iscopy:
                            print(key + " seed: " + value_seed + " gen: " + value_gen + " hint: copy of " + origninal)
                        else:
                            print(key + " seed: " + value_seed + " gen: " + value_gen)
        print()
        print("In Gen not in Seed (defaults filtered)")
        for section in theseed_parser.sections():
            for gen_item in parser_gen.items(section):
                key = gen_item[0]
                if not parser_seed.has_option(section, key):
                    value_gen = gen_item[1]
                    value_seedini = theseed_parser.get(section, key)
                    values = value_seedini.split("|")
                    length = len(values)
                    isdefault = False
                    iscopy = False
                    origninal = default = ""
                    if length == 1:  # this is a copy
                        iscopy = True
                        origninal = values[0]
                    elif length == 2:
                        default = values[1]
                        isdefault = value_gen == default
                    elif length == 5:
                        default = values[4]
                        isdefault = value_gen == default
                    else:
                        print("Problem with " + key + " in TheCoreSeed.ini")
                        raise Exception("Problem with " + key + " in TheCoreSeed.ini")
                    
                    if not isdefault:
                        if iscopy:
                            if not new_defaults_parser.has_option(section, key):
                                print(key + " gen: " + value_gen + " copied from " + origninal 
                                      + " - No Default found - Add a default value to the NewDefaults.ini and the check will be more acurate")
                            else:
                                default = new_defaults_parser.get(section, key)
                                isdefault = value_gen == default
                                if not isdefault:
                                    if default:
                                        print(key + " gen: " + value_gen + " seed default: " + default + " hint: copy of " + origninal)
                                    else:
                                        print(key + " gen: " + value_gen + " copied from " + origninal 
                                              + " - No Value entered for this in the NewDefaults.ini - change that and the check will be more acurate")
                        else:
                            print(key + " gen: " + value_gen + " seed default: " + default)
        print()
    print("-------------------------")
        
def generate_other_files():
    for race in races:    
        filename = prefix + " " + race + "LM " + suffix
        filepath = Seed_files_folder + "/" + filename
        verify_file(filepath)
        translate_file(filename, False)
        translate_file(shift_hand_size(filename, True, "L", False), False)
        translate_file(shift_hand_size(filename, False, "S", False), False)
        for layout in layouts:
            index = layoutIndices[layout]
            layout_filename = generate_layout(filename, race, layout, index)
            translate_file(layout_filename, righty_index[index])
            if righty_index[index]:
                translate_file(shift_hand_size(layout_filename, True, "S", True), True)
                translate_file(shift_hand_size(layout_filename, False, "L", True), True)
            else:
                translate_file(shift_hand_size(layout_filename, True, "L", False), False)
                translate_file(shift_hand_size(layout_filename, False, "S", False), False)

generate_seed_files()
veryfy_seed_with_generate()
if not ONLY_SEED:
    generate_other_files()

# Quick test to see if 4 seed files are error free
#     Todo:    expand this to every single file in every directory
#             expand both SAME_CHECKS and CONFLICT_CHECKS
# for race in races:
#    filename = prefix + " " + race + "LM " + suffix
#    verify_file(filename)

