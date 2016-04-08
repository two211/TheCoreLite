The Core Lite Variations
========================

TheCore Lite.SC2Hotkeys
-----------------------

This set fits with the legacy "TheCore Lite" updated to fix most of TheCore standards:
* keys to be the same, or inherited
* no keys conflicts (conflicts are only partially described)
On top of that, it passes most of the new introduced "seed" checks.
There are remaining errors in UnknownHotkeyCommandCheck.log

**Changes:**
* Minor command changes for compliance accross:
 * Multiplayer
 * Campaigns
 * Coop
* Far more Fire Hotkeys (all but "E" and "C")
* Functions keys have been populated, but are classical
 * F1 IdleWorker
 * F2 Select all army (changed in other variants)
 * Shift+F2 Minimap colors (to make it more accessible)
 * Shift+F3 Warp (swapped in other variants)
 * Shift+F5 Toggle sound (moved to prevent mistyping)
 * Shift+F6 Toggle music (could be mapped on Shift+F5 to free space)
* Back/Forward Mouse Button added to browse between subgroups

**Notes:** F3 to F8 cannot be used in direct access due to SelectHero

TheCore LiteRehab.SC2Hotkeys
----------------------------

Same commands as TheCore Lite.SC2Hotkeys, with hotkeys changes:
* Function key reorganization
 * F2 ToggleColors (no more Select all army on this key)
 * Shift+F2 Team Ressources
 * Shift+F3 Select all army (moved to prevent over-use)
 * Shift+F4 CameraFollow
 * Shift+F7 Warp (to encourage production group)
* Tab no longer used for subgroup browsing (to encourage mouse usage)
 * Tab : Alert Jump
 * Shift+Tab : Rotate Right (help to spot invisible)
 * Shift+Grave : Rotate Left (help to spot invisible)
* Support for autocentered cameras
 * Alt+Shift Camera center (for some reason Alt has to be pressed before Shift)
 * Alt+Shift+23QWASZX are alternate to declare the camera
 * Alt+Space PushToTalk (to free Alt+Shift)
* Group approach
 * all groups behave with steal (for easy split)
 * **Note** TheCore approach is to make all groups behave the same, you can adapt on your own
 * **Note** TheCore LiteMonitor allows some non-stealing alternates
* AI keys now supported
 * direct attack on Ctl+D
 * direct scout on Ctl+T
 * direct detect on Ctl+F
 * direct expand on Ctl+G
 * open AI communication on Ctl+C
 * build on Ctl+B
 * clearall on Ctl+V

TheCore LiteMonitor.SC2Hotkeys
--------------------------------

Same as TheCore LiteRehab.SC2Hotkeys with an experimental "monitor" overlay.
The principle is to use "Alt" as a "monitor mode" modifier.

The goals are:
* put all useful keys on 3 lines
* get a convenient macro mode key (Alt) : building groups + other utilities groups
* encourage camera keys for rally points, creep spread and warp pylons
* allow non-stealing group create|append that could be useful in some contexts
* do not disturb TheCore Lite key spirit

### Additional groups alternates (create/add work the same Ctrl+Shift/Ctrl):

4 "Monitor" group alternates:
* Alt+D is an alternate for "`" to be used for "production facilities" or "inject queens&tech"
* Alt+F is an alternate for "1" to be used for CC/Nexus+tech or hatches
* Alt+C is an alternate for "2" to be used for utility group or army composed of different groups (not behave with steal)
* Alt+V is an alternate for "3" to be used for utility group or army composed of different groups (not behave with steal)
* **NOTE:** Shift+V is an alternate for selecting the "inject queens" group (See "zerg macro routine" below)

Examples of utility groups:
* mothership (core)
* wall supply depot
* base defense squad
* SCV construction team
* whatever other useful group you could think about
* **exception** Z or X group may be better for *creep queens* (read zerg routine below)

Army composed of different groups usage ("C" taken as an example):
```
Control+<group_#>+C => appendSteal selection to group #, then append to group on key "2"
<group_#>,  Control+C => select group # then, append to group on key "2"
Control+Shift+C => create group "2" based on selection, without stealing units
Alt+C , D => select group "2" then attack
```

**Note:** "`" "1" "2" "3" groups have been chosen due to poor accessibility in TheCore Lite.
Regular groups to be used for armies are:
```
steal => 23
steal => QW
steal => AS
steal => ZX|CV <= non-steal alternate for "23" (selection with Alt)
```
**NOTE:** W and X could be used for "precision" group, to hold down precision keys (E and C) for precise clicking.
Examples:
Ghost/Raven/Liberator/Cyclone/BattleCruiser,
Infestor/Viper/Ravager,
High Templar/Sentry/Phoenix/Disruptor.
It's important for caster groups to be able to select/cast in a raw.
Same logic could be applied for harass units, which may benefit of it as well.
Groups keys convenient for fast selection&cast are:
```
QW
AS
ZX
```

### Group display

The 2 "macro" groups (` and 1) are positioned in the center to split the remaining groups by 4 keys.
This facilitates the visual representation of existing groups.
Unstealable groups (2 and 3) are the 2 first groups displayed.

The 10 groups are displayed in this order (| figures the separation):
```
23QW|`1|ASZX <= standard group keys
CV  |DF|     <=  monitor group keys
```

**NOTE:** the icon representing the group seems to be the best selectable unit at group creation.
If you wanted to update the icon, select the group and recreate it.
You'd better avoid such funny business if you use monitor unstealable groups (CV).

### Additionnal cameras alternates (save camera view with "Ctl" or "Alt+Shift")
2 "Monitor" camera alternates:
* Alt+E is an alternate for Shift+2
* Alt+R is an alternate for Shift+3

Camera creation:
* Ctl+E|R = free camera
* Alt+Shift+E|R = camera creation with preliminary center view with Alt+Shift

Examples of use cases:
* Rally points = free camera
* Warp Pylon = centered camera
* Creep Tumor zone = centered or free camera (see "zerg macro routine")

**NOTE:** Shift+Alt+E|R doesn't center the camera if Alt is pressed after Shift

### Use case: zerg macro routine
* Hatch check
 * Alt+F = hatch group + tech 
 * try to check supply depot at this step
* Inject cycle (hold Shift)
 * Shift+V = select inject queens + tech
 * Shift+Space = queue inject (prevent queens from walking around)
 * center mouse
 * Shift+Z|X|A|S + click = base camera + inject
* Tech check
 * You had time to check upgrades as they were selected with inject queeens
 * browse subgroup + add new research 
* Creep queen
 * Z = select creep queen (same raw as C for fast spawn creep tumor)
 * Shift+C + clicks = drop creep tumors (queued)
* Creep cameras (E or R)
 * Alt+E|R = jump to creep camera 1
 * double-click to select creep tumors
 * Shift+C + click = queue creep tumor
 * click = select a new creep tumor
 * Alt+Shift+E|R = update creep camera (with center view)

**NOTE:** creep tumor spawn/expand could be perform without queue
, if you're not careful you would have to cancel the action before selection with click or double-click

### Monitor mode summary
Accessible keys in "Monitor" mode (pressing Shift)
```
QWER
ASDF
ZXCV
```
* Camera keys = QW, AS, ZX (Shift to go, Alt to create)
* Monitor Camera keys = ER (Alt to go, Ctl or Shift+Alt to create)
* Utility groups = DF (Alt to select), Shift+V for safe inject routine
* Extra utility group = CV (Alt to select), behave with non-steal

**Note about history:**

An "Alt" overlay has been preferred as the Alt modifier is under a stronger finger: the thumb.
Only Shift+V serves for compliance with [TheCore inject](http://wiki.teamliquid.net/starcraft2/Spawn_Larva_%28Legacy_of_the_Void%29#The_Core_Method)
, as nobody would queue Stop.

A former version was based on a "Shift" overlay:
* it was tiring for the little finger especially for zerg macro routine.
* it messed up the queued command

**Drawbacks of the "Alt" overlay:**

Space is not being pressable with Alt, making a couple of action difficult to do.
~~Following changes could be used:~~
* ~~produce workers (4)~~
* ~~select larva (4)~~
* ~~unload command (5)~~

Other related changes propagated to other variants
* AI hotkey modifier has to change from Alt to Control
* Remap of building using "V" for construction, to allow queued build (sensor tower & baneling nest)

Changelog for the code
======================

Compared to upstream project:
* TheCoreRemapper.py supporting other seeds than pure TheCore
* New "seed" checks:
 * check for unbound comands, known from conflicts
 * check to prevent conflicts between Hotkeys and Commands, known from conflicts
 * check to prevent conflicts between Hotkeys and Commands, unknown from conflicts
* New "quality" checks:
 * check for commands out of known conflicts (warning only in case of inherit/same)
* Debug mode
 * optional generation
 * optional seed selection (you could run the script for the seeds you want)
 * optional quality checks (otherwise just run "seed" checks)
 * optional hint through a "verbose" and "verydetail" options (including the remapHint function)
 * optional IgnoredContext (such as "WoL Campaign" or "Coop") to filter conflicts and keys
* Some .ini file fixed to prevent wrong positive
