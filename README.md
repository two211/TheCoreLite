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
 * Shift-F2 Minimap colors (to make it more accessible)
 * Shift-F4 Warp (swapped in other variants)
 * Shift-F5 Toggle sound (moved to prevent mistyping)
 * Shift-F6 Toggle music (could be mapped on Shift+F5 to free space)

TheCore LiteRehab.SC2Hotkeys
----------------------------

Same commands as TheCore Lite.SC2Hotkeys, with hotkeys changes:
* Functions keys swap:
 * F2 AlertRecall (no more Select all army on this key)
 * Shift-F3 Select all army (made less accessible to prevent over-use)
* More accessible views keys
 * Shift+Grave CameraCenter
 * Shift+1 CameraFollow
 * Dragmouse finally kept
* Group approach
 * all groups behave with steal (for easy split), except "Q" and "W"
 * "Q" and "W" to be used for shared army groups to facilitate retreat/follow front-line
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

**WARNING** section outdated, 
data is kept unchanged for reader to get the initial ideas,
feel free to send feedback

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
 * whatever other useful group you could think about

**Note:** "X" "Z" "`" groups have been chosen due to poor accessibility in TheCore Lite.
Regular groups to be used for armies are:
```
123 <= steal
 QW <= no steal
 AS <= steal
```

### Additionnal views (save camera view with "Alt")
* Shift+E is an alternate for Shift+2
* Shift+R is an alternate for Shift+3

**Note:** to be used for "creep cameras" or "rally points"

### More accessible view related features
* Shift+T is an alternate for "follow selection"
* Shift+G is an alternate for "alert recall"
* Shift+B has the same effect as "base" key

### Use case: zerg macro routine
* Shift+F = hatch group + tech (check larva count + researchs on going)
* Shift+D = select inject queens
* Shift+Space = queue inject (prevent queens from walking around)
* center mouse
* Shift+Z|X|A|S + click = base camera + inject
* Shift+V = select creep queen
* Shift+C = queue creep tumor
* click = drop creep tumors
* Shift+E = jump to creep camera 1 (for creep push, Alt+E to update camera)
* Shift+R = jump to creep camera 2 (for creep push, Alt+R to update camera)

### Monitor mode summary
Accessible keys in "Monitor" mode (pressing Shift)
```
QWERT
ASDFG
ZXCVB
Space
```
* Camera keys = QWER, AS, ZX
* Utility groups = DF, V
* Queuable commands = C, Space
* Convenient view tuning:
 * T = follow selection
 * G = Alert Recall
 * B = base key

**WARNING:** all those "Shift alternates" may disturb your queued command habits.
A workaround would be to remap those commands on either "Space" or "C".

**Possible changes:** please report any painful problems, regarding convenient queued commands.
Commands may be changed to solve them.

### Dropped ideas due to queuability of commands
Cameras views (save camera view with "Alt"), to be used for "creep cameras" or "rally points":
* Shift+E is an alternate for Shift+2
* Shift+R is an alternate for Shift+3

View related feature
* Shift+T is an alternate for "follow selection" (easily accessible through F2)

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
