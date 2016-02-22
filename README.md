The Core Lite Variations
========================

TheCore Lite.SC2Hotkeys
-----------------------

Legacy "TheCore Lite" updated to fix most of TheCore standards:
* keys to be the same, or inherited
* no keys conflicts (conflicts are only partially described)

On top of that, it fits with all new introduced "seed" checks.

**Changes:**
* Functions keys have been populated, but are classical
* Far more Fire Keys (all apart "C")

TheCore LiteRehab.SC2Hotkeys
----------------------------

Same commands as TheCore Lite.SC2Hotkeys, with hotkeys changes:
* Functions keys:
 * F1 IdleWorker
 * F2 CameraFollow (no more select all army on this key)
 * F3 AlertRecall  (no more Warp on this key)
 * F4 Minimap colors
 * F5 toggle sound
 * F6 toggle music
 * F7 select all army (made less accessible to prevent over-use)
 * F8 warp (made less accessible to encourage "production facilities" group)
* Mouse middle button
 * now used for center camera view
 * Dragmouse removed (bad habit)
* Group approach
 * all groups behave with steal (for easy split), except "Q" and "W"
 * "Q" and "W" to be used for army groups to facilitate retreat/follow front-line
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
 * whatever other useful group you could think about

**NOTE:** "X" "Z" "`" groups have been chosen due to poor accessibility in TheCore Lite. Regular groups to be used for armies are:
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

**WARNING:** all those "Shift alternates" may disturb your queued command habits.
A workaround would be to remap those commands on either "Space" or "C".

Changelog for the code
======================

Compared to upstream project:
* TheCoreRemapper.py supporting other seeds than pure TheCore
* New "seed" checks:
 * check for unbound hotkeys, known from conflicts
 * check for unbound hotkeys, not part from conflicts
 * check to prevent conflicts between Commands and Hotkeys, known from conflicts
 * check to prevent conflicts between Commands and Hotkeys, unknown from conflicts
* New "quality" checks:
 * check for commands out of known conflicts (warning only in case of inherit/same)
* Debug mode
 * optional generation
 * optional seed selection (you could run the script for your seed)
 * optional quality checks (to just run "seed" checks)
 * optional hint through a "verbose" and "verydetail" options (including the remapHint function)
 * optional IgnoredContext (such as "WoL Campaign" or "Coop") to filter conflicts and keys only
* Some .ini file fixed to prevent wrong positive
