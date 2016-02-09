##################################################
#
# Filename: TheCoreRemapper.py
# Author: Jonny Weiss, Mark Rösler
# Description: Script to take the LM layouts of TheCore and generate the other 44 layouts.
# Change Log:
#   9/25/12 - Created
#   9/26/12 - Finished initial functionality
#
##################################################
import configparser
import os, sys

from conflict_checks import *

TRANSLATE = not "US" in sys.argv
ONLY_SEED = "LM" in sys.argv

GLOBAL = -1

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
               ['YamatoGun', 'SJHyperionYamato/SJHyperion', 'HyperionVoidCoopYamatoCannon/HyperionVoidCoop'],
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
               ['VoidSentryShieldRepair/Sentry', 'VoidSentryShieldRepairDouble/SentryAiur'],
               ['UpgradeToWarpGate/Gateway', 'UpgradeToRoboticsFacilityWarp/RoboticsFacility', 'UpgradeToStargateWarp/Stargate'],
               ['MorphBackToGateway/WarpGate', 'MorphBackToRoboticsFacility/RoboticsFacilityWarp', ],
               ['Vortex/Mothership', 'Vortex/Artanis', 'VoidSentryBlackHole/SOAMothershipv4', 'TemporalField/Mothership', 'TemporalField/MothershipCore'],
               ['250mmStrikeCannons/Thor', '250mmStrikeCannons/ThorWreckageSwann'],
               ['SelfRepair/Thor', 'SelfRepair/ThorWreckageSwann'],
               ['Salvage/Bunker', 'Salvage/MissileTurret', 'Salvage/KelMorianGrenadeTurret', 'Salvage/PerditionTurret', 'Salvage/KelMorianMissileTurret'],
               ['Hyperjump/Battlecruiser', 'HyperionVoidCoopHyperjump/HyperionVoidCoop', 'HyperjumpHercules/Hercules'],
               ['Charge/Zealot', 'Charge/ZealotAiur', 'Charge/ZealotPurifier', 'VoidZealotShadowCharge/ZealotShakuras', 'Charge/ShadowOfTheVoidZealot'],
               ['ResearchIncineratorGauntlets/BarracksTechLab', 'ResearchIncineratorGauntlets/BarracksTechReactor'],
               ['ResearchJuggernautPlating/BarracksTechLab', 'ResearchJuggernautPlating/BarracksTechReactor'], ['ResearchStabilizerMedpacks/BarracksTechLab', 'ResearchStabilizerMedpacks/BarracksTechReactor'],
               ['ResearchHellbatHellArmor/FactoryTechLab', 'ResearchHellbatHellArmor/FactoryTechReactor'],
               ['ResearchAresClassTargetingSystem/FactoryTechLab', 'ResearchAresClassTargetingSystem/FactoryTechReactor'],
               ['ResearchMultiLockWeaponsSystem/FactoryTechLab', 'ResearchMultiLockWeaponsSystem/FactoryTechReactor'],
               ['ResearchMaelstromRounds/FactoryTechLab', 'ResearchMaelstromRounds/FactoryTechReactor'],
               ['ResearchLockOnRangeUpgrade/FactoryTechLab', 'ResearchLockOnRangeUpgrade/FactoryTechReactor'],
               ['ResearchCycloneLockOnDamageUpgrade/FactoryTechLab', 'ResearchCycloneLockOnDamageUpgrade/FactoryTechReactor'],
               ['Research330mmBarrageCannon/FactoryTechLab', 'Research330mmBarrageCannon/FactoryTechReactor'],
               ['ResearchShockwaveMissileBattery/StarportTechLab', 'ResearchShockwaveMissileBattery/StarportTechReactor'],
               ['ResearchPhobosClassWeaponsSystem/StarportTechLab', 'ResearchPhobosClassWeaponsSystem/StarportTechReactor'],
               ['ResearchRipwaveMissiles/StarportTechLab', 'ResearchRipwaveMissiles/StarportTechReactor'],
               ['SummonNydusWorm/NydusNetwork', 'ZagaraVoidCoopNydusWorm/NydusNetwork'],
               ['Queen', 'QueenCoop'],
               ['BuildCreepTumor/Queen', 'BuildCreepTumor/QueenCoop'],
               ['MorphMorphalisk/Queen', 'MorphMorphalisk/QueenCoop'],
               ['Transfusion/Queen', 'Transfusion/QueenCoop'],
               ['Immortal/RoboticsFacility', 'Immortal/RoboticsFacilityWarp'],
               ['Colossus/RoboticsFacility', 'Colossus/RoboticsFacilityWarp'],
               ['Observer/RoboticsFacility', 'Observer/RoboticsFacilityWarp']]


class ConfigParser(configparser.ConfigParser):
    """Case-sensitive ConfigParser."""
 
    def optionxform(self, opt):
        return opt
 

# Read the settings

races = ["P", "T", "R", "Z"]
sides = ["L", "R"]
sizes = ["S", "M", "L"]

settings_parser = ConfigParser()
settings_parser.read('MapDefinitions.ini')

layout_parser = ConfigParser()
layout_parser.read('KeyboardLayouts.ini')

prefix = settings_parser.get("Filenames", "Prefix")
suffix = settings_parser.get("Filenames", "Suffix")
seed_layout = settings_parser.get("Filenames", "Seed_files_folder")

class Hotkey:
    def __init__(self, name, section, P=None, T=None, Z=None, R=None, default=None, copyOf=None):
        self.name = name
        self.section = section
        self.P = P
        self.T = T
        self.Z = Z
        self.R = R
        self.default = default
        self.copyOf = copyOf

    def set_value(self, race, value):
        if race == "P":
            self.P = value
        elif race == "R":
            self.R = value
        elif race == "T":
            self.T = value
        elif race == "Z":
            self.Z = value

    def get_value(self, race):
        if race == "P":
            return self.P
        elif race == "R":
            return self.R
        elif race == "T":
            return self.T
        elif race == "Z":
            return self.Z

def verify_file(filepath):
    print("verify file: " + filepath)
    hotkeys_file = open(filepath, 'r')
    dicti = {}
    for line in hotkeys_file:
        line = line.strip()
        if len(line) == 0 or line[0] == "[":
            continue
        pair = line.split("=")
        key = pair[0]
        if key in dicti:
            dicti[key] = [True, pair[1], key, dicti[key][3]]
        else:
            dicti[key] = [True, pair[1], key, ""]

    # Check for duplicates
    if SHOW_DUPLICATES:
        verify_parser = ConfigParser()
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
        value = dicti[same_set[0]][1]
        for item in same_set:
            if not dicti[item][1] == value:
                mismatched = True
        if mismatched:
            print("============================")
            print("---- Mismatched values ----")
            for item in same_set:
                print(item + " = " + dicti[item][1])

    for commandcard, conflict_set in CONFLICT_CHECKS.items():
        hotkeys = []
        count_hotkeys = {}
        for item in conflict_set:
            if not dicti.__contains__(item):
                print('WARNING: ' + item + ' does not exist in HotKey-file')
            else :
                append = dicti[item][1]
                hotkeys.append(append)
        for key in hotkeys:
            if not key in count_hotkeys:
                count_hotkeys[key] = 1
            else:
                count_hotkeys[key] = count_hotkeys[key] + 1
        for count in count_hotkeys:
            if count_hotkeys[count] > 1:
                print("============================")
                print("---- Conflict of hotkeys in " + commandcard + " ----")
                for item in conflict_set:
                    key = dicti[item][1]
                    if count_hotkeys[key] > 1:
                        print(item + " = " + key)
                # print(conflict_set)
    print("")
    
def create_filepath(race, side, size, path=""):
    filename = prefix + " " + race + side + size + " " + suffix
    filepath = filename
    if path:
        filepath = path + "/" + filename
    return filepath

def order(filepath):
    read_parser = ConfigParser()
    read_parser.read(filepath)

    dicti = {}
    for section in read_parser.sections():
        items = read_parser.items(section)
        items.sort()
        dicti[section] = items

    open(filepath, 'w').close()  # clear file

    write_parser = ConfigParser()  # on other parser just for the safty
    write_parser.read(filepath)

    write_parser.add_section("Settings")
    write_parser.add_section("Hotkeys")
    write_parser.add_section("Commands")

    for section in dicti.keys():
        if not write_parser.has_section(section):
            write_parser.add_section(section)
        items = dicti.get(section)
        for item in items:
            write_parser.set(section, item[0], item[1])

    file = open(filepath, 'w')
    write_parser.write(file, space_around_delimiters=False)
    file.close()


def generate(seed_model):
    models = {}
    for race in races:
        models[race] = {}
        for side in sides:
            models[race][side] = {}
            for size in sizes:
                models[race][side][size] = {}
    
    for race in races:
        models[race]["L"]["M"][seed_layout] = extract_race(seed_model, race)
        models[race]["R"]["M"][seed_layout] = convert_side(models[race]["L"]["M"][seed_layout])
        models[race]["L"]["S"][seed_layout] = shift_left(models[race]["L"]["M"][seed_layout], "L")
        models[race]["R"]["S"][seed_layout] = shift_right(models[race]["R"]["M"][seed_layout], "R")
        models[race]["L"]["L"][seed_layout] = shift_right(models[race]["L"]["M"][seed_layout], "L")
        models[race]["R"]["L"][seed_layout] = shift_left(models[race]["R"]["M"][seed_layout], "R")
    
    layouts = layout_parser.sections()
    for race in races:
        for side in sides:
            for size in sizes:
                for layout in layouts:
                    if layout != seed_layout:
                        models[race][side][size][layout] = translate(models[race][side][size][seed_layout], layout, side)
    for race in races:
        for side in sides:
            for size in sizes:
                for layout in layouts:
                    create_file(models[race][side][size][layout], race, side, size, layout)
    # verify_file(filepath)
    

def extract_race(seed_model, race):
    model_dict = {}
    for section in seed_model:
        model_dict[section] = {}
        for key, hotkey in seed_model[section].items():
            value = resolve_copyof(seed_model, section, hotkey, race)
            model_dict[section][key] = value
    return model_dict

def modify_model(seed_model, parser, parser_section, check_altgr=False):
    model_dict = {}
    for section in seed_model:
        model_dict[section] = {}
        for key, value in seed_model[section].items():
            if section == "Settings":
                newvalue = value
            else:
                newvalue = modify_value(value, parser, parser_section, check_altgr)
            model_dict[section][key] = newvalue
    return model_dict

def convert_side(seed_model):
    return modify_model(seed_model, settings_parser, 'GlobalMaps')

def shift_right(seed_model, side):
    shift_section = side + 'ShiftRightMaps'
    return shift(seed_model, shift_section)

def shift_left(seed_model, side):
    shift_section = side + 'ShiftLeftMaps'
    return shift(seed_model, shift_section)
            
def shift(seed_model, shift_section):
    return modify_model(seed_model, settings_parser, shift_section)

def translate(seed_model, layout, side):
    check_altgr = False
    if side == "R":
        check_altgr = True
    return modify_model(seed_model, layout_parser, layout, check_altgr)

def modify_value(org_value, parser, section, check_altgr):
    if check_altgr:
        altgr = layout_parser.get(section, "AltGr")

    newalternates = []
    for alternate in org_value.split(","):
        keys = alternate.split("+")
        newkeys = []
        # filter "Shift" only to make sure it is the same output as the old script
        if check_altgr and altgr == "1" and keys.count("Alt") == 1 and keys.count("Control") == 0 and keys.count("Shift") == 0:
            newkeys.append("Control")
        for key in keys:
            if parser.has_option(section, key):
                newkey = parser.get(section, key)
            else:
                newkey = key
            newkeys.append(newkey)
        newalternate = ""
        first = True
        for newkey in newkeys:
            if not first:
                newalternate = newalternate + "+"
            else:
                first = False
            if not newkey:
                newalternate = ""
            else:
                newalternate = newalternate + newkey
        newalternates.append(newalternate)
    first = True
    newvalues = ""
    for newalternate in newalternates:
        if not newalternate:
            continue
        if not first:
            newvalues = newvalues + ","
        else:
            first = False
        newvalues = newvalues + newalternate
    return newvalues

def create_file(model, race, side, size, layout):
    hotkeyfile_parser = ConfigParser()
    for section in model:
        if not hotkeyfile_parser.has_section(section):
                hotkeyfile_parser.add_section(section)
        for key, value in model[section].items():
            hotkeyfile_parser.set(section, key, value)
    if not os.path.isdir(layout):
        os.makedirs(layout)
    filepath = create_filepath(race, side, size, layout)
    hotkeyfile = open(filepath, 'w')
    hotkeyfile_parser.write(hotkeyfile, space_around_delimiters=False)
    hotkeyfile.close()
    order(filepath)

def resolve_copyof(model, section, hotkey, race):
    value = None
    while True:
        if hotkey.copyOf:
            hotkey = model[section][hotkey.copyOf]
        else:
            value = hotkey.get_value(race)
            if value is None:
                value = hotkey.default
            break
    return value
    
def verify_seed_with_generate():
    print("-------------------------")
    print(" Start Comparing Seeds Files with Generated Files")

    for race in races:
        filepath_seed = prefix + " " + race + "LM " + suffix
        filepath_gen = seed_layout + "/" + filepath_seed

        parser_seed = ConfigParser()
        parser_seed.read(filepath_seed)

        parser_gen = ConfigParser()
        parser_gen.read(filepath_gen)

        theseed_parser = ConfigParser()
        theseed_parser.read('TheCoreSeed.ini')

        new_defaults_parser = ConfigParser()
        new_defaults_parser.read('NewDefaults.ini')

        print("Race: " + race)
        print()

        print("In Seed not in Gen")
        for section in parser_seed.sections():
            for seed_item in parser_seed.items(section):
                key = seed_item[0]
                if not parser_gen.has_option(section, key):
                    print(key)
        print()
        print("In Seed diffrent in Gen")
        for section in new_defaults_parser.sections():
            for item in new_defaults_parser.items(section):
                key = item[0]
                if parser_gen.has_option(section, key) and parser_seed.has_option(section, key):
                    value_gen = parser_gen.get(section, key)
                    value_seed = parser_seed.get(section, key)
                    seed_value_set = set(str(value_seed).split(","))
                    gen_value_set = set(str(value_gen).split(","))
                    if seed_value_set != gen_value_set:
                        if theseed_parser.has_option(section, key):
                            original = theseed_parser.get(section, key)
                            print(key + " seed: " + value_seed + " gen: " + value_gen + " hint: copy of " + original)
                        else:
                            print(key + " seed: " + value_seed + " gen: " + value_gen)

        print()
        print("In Gen not in Seed (defaults filtered)")
        for section in parser_gen.sections():
            for gen_item in parser_gen.items(section):
                key = gen_item[0]
                value_gen = gen_item[1]
                if not parser_seed.has_option(section, key):
                    default = new_defaults_parser.get(section, key)
                    default_value_set = set(str(default).split(","))
                    gen_value_set = set(str(value_gen).split(","))
                    if gen_value_set != default_value_set:
                        if theseed_parser.has_option(section, key):
                            original = theseed_parser.get(section, key)
                            print(key + " gen: " + value_gen + " seed default: " + default + " hint: copy of " + original)
                        else:
                            print(key + " gen: " + value_gen + " seed default: " + default)
        print()
    print("-------------------------")

def create_model():
    theseed_parser = ConfigParser()
    theseed_parser.read('TheCoreSeed.ini')

    default_parser = ConfigParser()
    default_parser.read('NewDefaults.ini')

    parsers = {}
    for race in races:
        filepath = prefix + " " + race + "LM " + suffix
        seed_hotkeyfile_parser = ConfigParser()
        seed_hotkeyfile_parser.read(filepath)
        parsers[race] = seed_hotkeyfile_parser

    model = {}
    for section in default_parser.sections():
        section_dict = {}
        for item in default_parser.items(section):
            key = item[0]
            hotkey = Hotkey(key, section)

            default = item[1]
            hotkey.default = default

            for race in races:
                if parsers[race].has_option(section, key):
                    value = parsers[race].get(section, key)  #
                    hotkey.set_value(race, value)

            if theseed_parser.has_option(section, key):
                copyof = theseed_parser.get(section, key)
                hotkey.copyOf = copyof
            section_dict[key] = hotkey
        model[section] = section_dict
    return model

def new_keys_from_seed_hotkeys():
    default_filepath = 'NewDefaults.ini'
    default_parser = ConfigParser()
    default_parser.read(default_filepath)

    for race in races:
        filepath = prefix + " " + race + "LM " + suffix
        seed_hotkeyfile_parser = ConfigParser()
        seed_hotkeyfile_parser.read(filepath)

        for section in seed_hotkeyfile_parser.sections():
            for item in seed_hotkeyfile_parser.items(section):
                key = item[0]
                if not default_parser.has_option(section, key):
                    default_parser.set(section, key, "")

    file = open(default_filepath, 'w')
    default_parser.write(file, space_around_delimiters=False)
    file.close()
    order(default_filepath)

def check_defaults():
    warn = False
    default_filepath = 'NewDefaults.ini'
    default_parser = ConfigParser()
    default_parser.read(default_filepath)
    
    ddefault_filepath = 'different_default.ini'
    ddefault_parser = ConfigParser()
    ddefault_parser.read(ddefault_filepath)
    
    theseed_parser = ConfigParser()
    theseed_parser.read('TheCoreSeed.ini')
    
    parsers = {}
    for race in races:
        filepath = prefix + " " + race + "LM " + suffix
        seed_hotkeyfile_parser = ConfigParser()
        seed_hotkeyfile_parser.read(filepath)
        parsers[race] = seed_hotkeyfile_parser

    for section in default_parser.sections():
        for item in default_parser.items(section):
            key = item[0]
            default = item[1]
            multidefault = ddefault_parser.has_option(section, key)
            if not default or multidefault:
                seedhas = True
                for race in races:
                    if not parsers[race].has_option(section, key):
                        seedhas = False
                inherit = theseed_parser.has_option(section, key)
                
                if multidefault:
                    if not seedhas and not inherit:
                        print("[ERROR] key has multiple diffrent defaults: set in all seed layouts value for this key (or unbound) " + key)
                
                if not default:
                    if seedhas or inherit:
                        if warn:
                            print("[WARN] no default " + key)
                    else:
                        print("[ERROR] no default " + key)

def suggest_inherit():
    print("------------------------------")
    print("suggest inherit")
    print("------------")
    default_filepath = 'NewDefaults.ini'
    default_parser = ConfigParser()
    default_parser.read(default_filepath)
    
    theseed_parser = ConfigParser()
    theseed_parser.read('TheCoreSeed.ini')
    
    parsers = {}
    for race in races:
        hotkeyfile_parser = ConfigParser()
        hotkeyfile_parser.read(prefix + " " + race + "LM " + suffix)
        parsers[race] = hotkeyfile_parser

    dicti = {}
    defaults = {}
    for section in default_parser.sections():
        for item in default_parser.items(section):
            key = item[0]
            default = item[1]
            defaults[key] = default
            values = {}
            for race in races:
                if parsers[race].has_option(section, key):
                    value = parsers[race].get(section, key)
                else:
                    value = default
                values[races.index(race)] = value
            dicti[key] = values
            
    outputdict = {}
    for key, values in dicti.items():
        for key2, values2 in dicti.items():
            if key == key2:
                continue
            
            equal = True
            for race in races:
                index = races.index(race)
                value = values.get(index)
                value2 = values2.get(index)
                value_set = set(str(value).split(","))
                value2_set = set(str(value2).split(","))
                if value_set != value2_set:
                    equal = False
                    break
                    
            if equal:
                output_key = ""
                for race in races:
                    index = races.index(race)
                    value = values.get(index)
                    output_key = output_key + race + ": " + str(value) + "\n"
                
                if not output_key in outputdict:
                    outputdict[output_key] = []
                if not key in outputdict[output_key]:
                    outputdict[output_key].append(key)
                
    for values, listkeys in outputdict.items():
        print(values, end="")
        listkeys.sort()
        for key in listkeys:
            copyofstr = ""
            default = defaults[key]
            for section in theseed_parser.sections():
                if theseed_parser.has_option(section, key):
                    seedini_value = theseed_parser.get(section, key)
                    copyofstr = " default: " + default + " copy of " + seedini_value
                    default = defaults[seedini_value]
                    break
            print("\t" + key + " " + copyofstr + " default: " + default)
        print("------------")
    print()

def wrong_inherit():
    print("------------------------------")
    print("Wrong inherit")
    default_filepath = 'NewDefaults.ini'
    default_parser = ConfigParser()
    default_parser.read(default_filepath)
    
    theseed_parser = ConfigParser()
    theseed_parser.read('TheCoreSeed.ini')
    parsers = {}
    for race in races:
        hotkeyfile_parser = ConfigParser()
        hotkeyfile_parser.read(prefix + " " + race + "LM " + suffix)
        parsers[race] = hotkeyfile_parser

    dicti = {}
    for section in default_parser.sections():
        for item in default_parser.items(section):
            key = item[0]
            default = item[1]
            values = {}
            for race in races:
                index = races.index(race)
                if parsers[race].has_option(section, key):
                    value = parsers[race].get(section, key)
                    values[index] = value
                else:
                    values[index] = default
            dicti[key] = values
    
    for section in theseed_parser.sections():
        for item in theseed_parser.items(section):
            key = item[0]
            copyofkey = item[1]
            values = dicti[key]
            copyofvalues = dicti[copyofkey]
            equal = True
            for race in races:
                index = races.index(race)
                value = values[index]
                copyofvalue = copyofvalues[index]
                value_set = set(str(value).split(","))
                copyofvalue_set = set(str(copyofvalue).split(","))
                if value_set != copyofvalue_set:
                    equal = False
            if not equal:
                print(key + " != " + copyofkey)
                for race in races:
                    index = races.index(race)
                    value = values[index]
                    copyofvalue = copyofvalues[index]
                    if not value:
                        value = " "
                    print(race + ": " + str(value) + "\t" + str(copyofvalue))
                default = default_parser.get(section, key)
                if not default:
                    default = " "
                copyofdefault = default_parser.get(section, copyofkey)
                if not copyofdefault:
                    copyofdefault = " "
                print("D: " + str(default) + "\t" + str(copyofdefault) + " (default)")
                print()
        
    print()



# check sections
new_keys_from_seed_hotkeys()
check_defaults()
model = create_model()
generate(model)
wrong_inherit()
verify_seed_with_generate()
suggest_inherit()

# Quick test to see if 4 seed files are error free
#     Todo:    expand this to every single file in every directory
#             expand both SAME_CHECKS and CONFLICT_CHECKS
# for race in races:
#    filename = prefix + " " + race + "LM " + suffix
#    verify_file(filename)

