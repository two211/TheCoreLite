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
 * Shift+F4 Quick save
 * Shift+F7 Warp (to encourage production group)
 * Shift+F8 CameraFollow
* Tab no longer used for subgroup browsing (to encourage mouse usage)
 * Tab : Alert Jump
 * Shift+Tab : Rotate Right (help to spot invisible)
 * Shift+Grave : Rotate Left (help to spot invisible)
 * Ctl+Tab : alternate for "select all army"
 * Ctl+Shift+Tab : alternate for "select all army"
* Support for autocentered cameras
 * Alt+Shift Camera center (for some reason Alt has to be pressed before Shift)
 * Alt+Shift+23QWASZX are alternate to declare the camera
 * Alt+Space PushToTalk (to free Alt+Shift)
* Group approach
 * all groups behave with steal (for easy split)
 * Extra Alt modifier enables non-steal behavior
 * **Note** TheCore approach is to make all groups behave the same, you can adapt on your own
* AI keys now supported
 * open AI communication on Ctl+Alt+Tab
 * direct attack on Ctl+Alt+D
 * direct scout on Ctl+Alt+T
 * direct detect on Ctl+Alt+F
 * direct expand on Ctl+Alt+G
 * build on Ctl+Alt+C
 * clearall on Ctl+Alt+E
 * delete on Ctl+Alt+R

### Select all army Tab alternates

* Ctl+Shift+Tab
 * Ctl+Shift+click will remove entire unit type from selection
 * Ctl+Shift+Alt+#group key will create non-steal the group
* Ctl+Tab
 * Ctl+click will select only unit of the clicked type

TheCore LiteMonitor.SC2Hotkeys
--------------------------------

Same as TheCore LiteRehab.SC2Hotkeys with an experimental "monitor" overlay.
The principle is to use "Alt" as a "monitor mode" modifier.

The goals are:
* put all useful group&camera bindkeys over commands
* get a convenient macro mode key (Alt) : building groups + other utilities groups
* encourage camera keys for rally points, creep spread and warp pylons
* do not disturb TheCore Lite key spirit

### Additional groups alternates (create/add work the same Ctl+Shift/Ctl):

2 "Monitor" group alternates:
* Alt+D is an alternate for "`" to be used for CC/Nexus+tech or hatches
* Alt+V is an alternate for "1" to be used for "production facilities" or "inject queens&tech"
* Ctl+V is an alternate for "1" to be used for "production facilities" or "inject queens&tech"
* Shift+V is an alternate for "1" to be used for "production facilities" or "inject queens&tech"

**Note:** "`" "1" groups have been chosen due to poor accessibility in TheCore Lite.
Regular groups to be used for armies are:
```
steal => 23
steal => QW
steal => AS
steal => ZX
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
QW <= in line with E
AS
ZX <= in line with C
```

### Group display

The 2 "macro" groups (` and 1) are positioned in the center to split the remaining groups by 4 keys.
This facilitates the visual representation of existing groups.
Unstealable groups (2 and 3) are the 2 first groups displayed.

The 10 groups are displayed in this order (| figures the separation):
```
23QW|`1|ASZX <= standard group keys
    |DV|     <=  monitor group keys (Alt+D|V, Ctl+V)
```

**NOTE:** the icon representing the group seems to be the best selectable unit at group creation
If you wanted to update the icon, select the group and recreate it.

### Additionnal cameras alternates
2 "Monitor" camera alternates:
* Ctl+E is an alternate for Shift+2
* Ctl+D is an alternate for Shift+3

Camera creation:
* Ctl+R is an alternate for Alt+2
* Ctl+F is an alternate for Alt+3
* Ctl+Space center camera view (if you want to center a warp pylon, or a creep tumor)

### Nexus/CC/Hatch group
* Corresponds to group `
* Alt+D helps select this group
* Ctl+` append selection to this group (same behavior as standard group)
* Ctl+Shift+` create group from selection (same behavior as standard group)

Tip for additional expansion
* *Alt+Tab* helps to append base to this group after camera creation
* *Alt+Shift* helps to center base at camera creation

### Production group
* Corresponds to group 1
* Alt+V helps select this group (for macro monitoring)
* Ctl+V helps select this group (for warp-in at camera)
* Shift+V helps select this group (for inject queen to initiate TheCore inject)
* Ctl+1 appends selection to this group (same behavior as standard group)
* Ctl+Shift+1 creates group from selection (same behavior as standard group)

### Use case: expansions
* Select new base
* Alt+Shift: center view on base
* Alt(+Shift)+Q|W|A|S|Z|X: make view on associated key
* Alt+Tab: append expansion to Nexus/CC/Hatch group

### Use case: warp-in pylon (with Ctl layer)
* Ctl+V: select production facilities (WarpGate have higher selection priority)
* Ctl+DE: center on warp pylon
* hold key for warping-in units (rapid fire warp-in)
* Ctl+click: on a unit, select all units for this type
* Ctl+2|3|Q|W|A|S|Z|X: add selection to an army group

### Use case: warp-in pylon (with usual keys)
* Shift+1: select production facilities (WarpGate have higher selection priority)
* Shift+2|3: center on warp pylon
* hold key for warping-in units (rapid fire warp-in)
* Ctl+click: on a unit, select all units for this type
* Ctl+2|3|Q|W|A|S|Z|X: add selection to an army group

### Use case: zerg macro routine
* Hatch check
 * Alt+D = hatch group
 * try to check supply depot at this step
* Inject cycle (hold Shift)
 * Shift+V = select inject queens + tech
 * Shift+Space = queue inject (prevent queens from walking around)
 * center mouse
 * Shift+Q|W|A|S|Z|X+click = base camera + inject
* Tech check
 * You had time to check upgrades as they were selected with inject queeens
 * browse subgroup + add new research
* Creep queen
 * Z = select creep queen (same raw as C for fast spawn creep tumor)
 * Shift+C + clicks = drop creep tumors (queued)
* Creep cameras (E or D)
 * Ctl+E|D = jump to creep camera
 * Ctl+click to select creep tumors
 * Shift+C then clicks = queued creep tumor spread
 * click = select a new creep tumor
 * Ctl+Space = center view on selection
 * Ctl+R|F = update creep camera

**NOTE:** creep tumor spawn/expand could be perform without queue
, if you're not careful you would have to cancel the action before selection with click or double-click

### Monitor mode summary
Accessible keys in "Monitor" mode:
```
23
QWER
ASDF
ZXCV
Space
```
* Camera keys = Q|W, A|S, Z|X (Shift to go, Alt to create)
* Monitor Camera keys jump = Ctl+E|D
* Monitor Camera keys creation = Ctl+R|F
* Monitor Camera center = Ctl+Space
* Nexus/CC/Hatch group selection = Alt+D
* Production group selection = Alt+V Ctl+V Shift+V

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
