The Core Lite Variations
========================

toto

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

**Note:** F3 to F8 cannot be used in direct access due to SelectHero

#### Macro groups
TheCore Lite comes with suggestions of control groups.
Q is intended for production facilities or inject queens.
W is intended for CC Nexus Hatcheries.

source: https://docs.google.com/spreadsheets/d/1v1gTY9suNstl6KoYQ0zIA8_dIBAJ9COmdtbQ1AEuxV4/edit?pref=2&pli=1#gid=56

#### Use case: expansions cameras
* Select new base under construction
* Alt+Shift: center view on base
* Alt(+Shift)+[camera\_key]: make view on associated key
* Alt(+Shift)+D: append expansion to Nexus/CC/Hatch group

#### Use case: send worker back to ressources gathering after queued commands
* press shift to queue all necessary commands
* Shift+[camera\_key]: jump to base
* Shift + right click on mineral or gaz; last action of the queue is to go back to work

TheCore LiteRehab.SC2Hotkeys
----------------------------

The goals are:
* get rid of bad habits
* develop sane mechanics
* allow easy 2-keys-based macro mechanics
* encourage camera keys for:
 * rally points
 * warp pylons
 * creep spread
* no modification of TheCore Lite key basic layout

Same commands as TheCore Lite.SC2Hotkeys, with hotkeys changes:
* Function key reorganization
 * F2 ToggleColors (no more Select all army on this key - see Tab key)
 * Shift+F2 Team Ressources
* Tab no longer used for subgroup browsing (to encourage mouse usage)
 * Tab : Alert Jump
 * Shift+Tab : alternate for "choose target" (see "telegraph inject" below)
 * Ctl+Tab : alternate for "select all army"
 * Ctl+Shift+Tab : alternate for "select all army"
* Group approach
 * all groups behave with steal (for easy split)
 * Extra Alt modifier enables non-steal behavior
 * **Note** TheCore approach is to make all groups behave the same, you can adapt on your own
* Alt now show Ennemy life bar (useful for quick check of stacked ground/air armies)
* Moved out of the dense keycard and Function keys
 * Period: Warp (to encourage production group)
 * Numpad0: Quick save
 * Delete: CameraFollow
* QuickPing now mapped on Alt+LeftClick
* Rotate camera (help to spot invisible)
 * Alt+Grave : Rotate camera Left 
 * Alt+1 : Rotate camera Right
* Support for autocentered cameras
 * Alt+Shift Camera center (for some reason Alt has to be pressed before Shift)
 * Alt+Shift+23QWASZX are alternate to declare the camera
 * Alt+Space PushToTalk (to free Alt+Shift)
* "Control" Cameras
 * Suitable for creep spread as an example
* Support for telegraph inject (a variant of backspace inject)
 * Shift+` base camera
 * Shift+Tab target choose
 * read use case below
* AI keys now supported
 * direct attack on Ctl+Alt+D
 * direct scout on Ctl+Alt+T
 * direct detect on Ctl+Alt+F
 * direct expand on Ctl+Alt+G
 * open AI communication on Ctl+Alt+V
 * build on Ctl+Alt+C
 * clearall on Ctl+Alt+E
 * delete on Ctl+Alt+R

#### Select all army Tab alternates
* After Ctl+Shift+Tab
 * Ctl+Shift+click will remove entire unit type from selection
* After Ctl+Tab
 * Ctl+click will select only unit of the clicked type
* Others actions
 * Ctl+Shift+Alt+#group key will create non-steal the group

#### Jump to last alert
If you have some time, it may worth to try push Tab to jump to last alerts.
It's in line with TheCore Lite suggested macro groups (Q and W)

#### Fight against invisible
* immobile invisible units can't be seen with static camera
* camera rotation allows to spot invisible static units
* Alternate Alt+` and Alt+1 to rotate the camera and send detection at the right place

#### Additional cameras alternates
2 "Control" camera alternates:
* Ctl+E = Shift+2
* Ctl+D = Shift+3 <= 1st camera key
* Ctl+C = Shift+Z

Camera creation:
* Ctl+R = Alt+2
* Ctl+F = Alt+3 <= 1st camera key
* Ctl+V = Alt+Z
* Ctl+Space centers camera view (if you want to center a warp pylon, or a creep tumor)

TheCore LiteMonitor.SC2Hotkeys
--------------------------------

Same as TheCore LiteRehab.SC2Hotkeys with modification to original legacy TheCore Lite.

The goals are:
* better see group affection from UI
* not disturb (too much) TheCore Lite key spirit

Modifications:
* ZX are the macro hotkeys
* Z no longer used for camera (it's camera is control Camera "CV")

### Macro groups

#### Nexus/CC/Hatch group

Group key = X

Group content
* All Nexus/CC/Hatch
* Terran and Protoss should add research facilities to this group

Tip for additional expansion
* Alt+D helps to append base to this group after camera creation
* Alt+Shift helps to center base at camera creation

#### Production group (or inject queens)

Group key = Z

Group content
* Terran & Protoss: All army production facilities
* Zerg: inject queens
* Zerg should add research facilities to this group

Tip for rally point | warp-in pylon
* no more camera on Z (moved to 1)
* X camera being used for rally point | warp-in pylon
* Shift+Z+X selects production groups
 * check rally point at army production step
 * warp-in pylon: keep shift pressed, while holding unit key (queued rapid-fire warp-in)

Tip for egg inject, please read section dedicated to zerg macro routine

#### Group display

The 2 "macro" groups are positioned in the center to split the remaining groups by 4 keys.
This facilitates the visual representation of existing groups.
The 10 groups are displayed in this order (| figures the separation):
```
`123|ZX|QWAS <= standard group keys
```

**NOTE:** the icon representing the group seems to be the best selectable unit at group creation
If you wanted to update the icon, select the group and recreate it.

### Examples

#### Use case: army production + rally point (optional warp-in pylon)
* Hold Shift
* Shift+Z: select production facilities
* Shift+X: jump to rally point (declared with Alt+X)
* optional redeclaration of the rally point (in case of new integrated facility)
* inspect rallied army
* browse subgroup and launch production
* select rallied army and add to control groups

#### Use case: warp-in pylon (with Ctl camera)
* Ctl+C|D|E: center on warp pylon
* Z: select production facilities (WarpGate have higher selection priority)
* hold key for warping-in units (rapid fire warp-in)
* Ctl+click: on a unit, select all units for this type
* Ctl+[army\_group]: add selection to an army group
* right click for rally
* [army\_group]: attack

#### Use case: zerg macro routine
* Hatch check
 * X: hatch group
 * check supply depot at this step, to produce overlords
 * morph other larvaes depending on needs
* Inject cycle (hold Shift)
 * Shift+Z = select inject queens + tech
 * Shift+X = jump to main hatch (first hatch)
 * Shift+Space = queue inject (prevent queens from walking around)
 * center mouse + click
 * Shift+A|S|Q|W|2+click = base camera + inject
* Tech check
 * You had time to check upgrades as they were selected with inject queeens
 * browse subgroup + add new research
* Creep queen
 * S x2 = select + jump to creep queen (same raw as C for fast spawn creep tumor)
 * Shift+C + clicks = drop creep tumors (queued)
* Creep cameras (E or D)
 * Ctl+E|D = jump to creep camera
 * Ctl+click to select creep tumors
 * Shift+C then clicks = queued creep tumor spread
 * click = select a new creep tumor
 * Ctl+Space = center view on selection
 * Ctl+R|F = update creep camera

**NOTE:** creep tumor spawn/expand could be performed without queue
, if you're not careful you would have to cancel the action before selection with click or double-click

#### Use case: telegraph inject

The "telegraph" inject is a variant of the "backspace" inject.
It relies on:
* command queuing
* no mouse click
* 2 neighbour keys, comfortably pressable with left Shift key hold

Initiate inject cycle (hold Shift)
* Basic principle
 * select inject queens
 * launch inject command
 * center mouse, center view on a hatch
* Monitor inject initiate 
 * Shift+Z = select inject queens + tech
 * Shift+X = jump to main hatch (first hatch)
 * Shift+Space = inject
 * center mouse

Cycle through bases with fingers only
* move thumb over Shift and hold to start command queuing
* press Shift+` to cycle base
* presse Shift+Tab to target hatch if queen is here

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
