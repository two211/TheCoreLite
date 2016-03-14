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
 * Shift+F2 CameraFollow
 * Shift+F3 Select all army (moved to prevent over-use)
 * Shift+F4 Team Ressources
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
 * all groups behave with steal (for easy split), except "Q" and "W"
 * "Q" and "W" to be used for shared army groups to facilitate retreat/follow front-line
 * **Note** TheCore approach is to make all groups behave the same, you can adapt on your own
* AI keys now supported
 * direct attack on Alt+D
 * direct scout on Alt+T
 * direct detect on Alt+F
 * direct expand on Alt+G
 * open AI communication on Alt+C
 * build on Alt+B
 * clearall on Alt+V

TheCore LiteMonitor.SC2Hotkeys
--------------------------------

Same as TheCore LiteRehab.SC2Hotkeys with an experimental "monitor" overlay.
The principle is to use "shift" as a "monitor mode" modifier.
The goal is encourage camera keys, having also the useful stuff pressing "shift".

### Additional groups (create/add work the same Ctrl+Shift/Ctrl):
* Shift+F is an alternate for "X" to be used for CC/Nexus/Hatch and tech
* Shift+D is an alternate for "Z" to be used for "production facilities" or "inject queens"
* Shift+V is an alternate for "`" to be used for
 * "creep queen"
 * mothership (core)
 * wall supply depot
 * base defense squad
 * whatever other useful group you could think about

**Note:** "X" "Z" "`" groups have been chosen due to poor accessibility in TheCore Lite.
Regular groups to be used for armies are:
```
123 <= steal
 QW <= no steal
 AS <= steal
```

### Additionnal free cameras (save camera view with "Alt" or "Shift+Alt")
* Shift+E is an alternate for Shift+2
* Shift+R is an alternate for Shift+3

**Note:** to be used for "creep cameras" or "rally points",
could bother you with queued commands (please report)

### More accessible view related features
* ~~Shift+T is an alternate for "follow selection"~~
* ~~Shift+G is an alternate for "alert recall"~~
* Shift+B has the same effect as "base" key (still true :D)

**Dropped:** Shift+T is definitely useful,
follow selection and alert recall have been mapped somewhere else anyway (look at TheCore LiteRehab)

### Use case: zerg macro routine
* Shift+F = hatch group + tech (check larva count + researchs on going)
* Shift+D = select inject queens
* Shift+Space = queue inject (prevent queens from walking around)
* center mouse
* Shift+Z|X|A|S + click = base camera + inject
* Shift+V = select creep queen
* Shift+C = queue creep tumor
* click = drop creep tumors
* Shift+E = jump to creep camera 1
* move mouse on creep Tumor
* Shift+Forward|Back Mouse Button = select creep tumor
* double-click to select creep tumors
* Shift+C = queue creep tumor
* click = drop creep tumor
* middle-click = drag camera
* Shift+Alt+E = update creep camera

Optional second creep camera:
* Shift+R = jump to creep camera 2
* move mouse on creep Tumor
* Shift+Forward|Back Mouse Button = select creep tumor
* Shift+double-click to select creep tumors
* Shift+C = queue creep tumor
* click = drop creep tumor
* middle-click = drag camera
* Shift+Alt+R = update creep camera

**NOTE:** Shift+Alt+E|R doesn't center the camera if Alt is pressed after Shift

### Monitor mode summary
Accessible keys in "Monitor" mode (pressing Shift)
```
QWER
ASDF
ZXCV
Space
```
* Camera keys = QWER, AS, ZX
* Utility groups = DF, V
* Queuable commands = C, Space

**WARNING:** all those "Shift alternates" may disturb your queued command habits.
A workaround would be to remap those commands on either "Space" or "C".

**Possible changes:** please report any painful problems, regarding convenient queued commands.
TheCore LiteMonitor tricks could be dropped or commands may be changed to solve them.

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
