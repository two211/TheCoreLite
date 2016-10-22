The Core Lite v2.0
==================

Some graphic ressources is available in Image directory,
please download the following .pdf file:

https://github.com/bobo38/TheCoreLite/raw/master/Images/TheCore_Lite.pdf

Goals of this version
---------------------

The goals are:
* keep as much consistency with legacy "TheCore Lite" for unit commands
* get rid of bad habits
* develop sane mechanics
* allow easy 2-keys-based macro mechanics
* encourage camera keys usage for:
 * rally points
 * warp pylons
 * creep spread

Coverage and checks:
* no keys conflicts accross supported modes (please report anyone you found)
 * WoL HoTS LoTV multiplayer
 * Campaigns ( WoL HoTS LoTV Nova)
 * Coop
* pass TheCore standards
 * keys supposed to be the same, or inherited
 * delivered in a set of supported keyboard layouts
 * it passes all the new introduced "seed" checks (there are still some command out of any identified conflict)

----------------------------------------------------------------------------------------------------------------------

TheCore Lite User Interface keys
--------------------------------

Compared to legacy TheCore Lite, many changes occured in User Interface keys.

### Function keys
* F1 IdleWorker
* Shift+F1 select all Idle Workers
* Alt+F1 PushToTalk (to free Alt+Shift)
* F2 Toggle minimap colors (no more Select all army on this key - see Tab key)
* Shift+F2 Team Ressources
* F3 F4 F5 F6 Commander top bar ability
* Shift+F7 Toggle sound (moved to prevent mistyping)
* Shift+F8 Toggle music (could be mapped on Shift+F5 to free space)

### Select All Army on Tab key
* Ctl+Tab : alternate for "select all army"
* Ctl+Shift+Tab : alternate for "select all army"

Some examples:
* After Ctl+Shift+Tab, Ctl+Shift+click will remove entire unit type from selection
* After Ctl+Tab, Ctl+click will select only unit of the clicked type
* Others actions:
 * Ctl+Shift+Alt+#group key will create non-steal the group

**Note:** Alt+Tab is an alias for "add to nexus/CC/hatch group"

### Rapid Fire and Precision keys.
There are now far more Rapid Fire Hotkeys: Space, R, T, D, F, G, V, H, CapsLock.
Now all Warp-Inable units are bound on Rapid Fire keys.
If you don't know what rapid fire keys are, please check out JaKaTaK's video on Youtube.

"E" and "C" keep on being non Rapid Fire, because they are precision key.
They are used for precision spells/ability.
You can keep those key pressed and just click on the target.
After the click the ability will be called again and you just have to click on the next target.

**Note:** like legacy TheCore Lite, some spells have 2 alternates: one on "rapid fire" key, the other on "precision" key

### Browsing subgroups
* Tab and Shift+Tab are used
* Back/Forward Mouse Button added to browse between subgroups

### Ping allies !
* Alert jump
 * accessible with Shift+Grave
 * accessible with Alt+Grave
* Minimap ping
 * MinimapPing on Shift+1
 * MinimapPing on Alt+1
* QuickPing now mapped on Alt+RightClick

If you have some spare time, it may worth to try push Shift|Alt+\` to jump to last alerts.
Alt+\` could be easily chain with Alt+1 or Alt+RightClick to ping the event to teammates.
Shit+\` to be chained with Shift+1.

### Fight against invisible
* Alt+T : Rotate camera Left
* Alt+G : Rotate camera Right

Immobile invisible units can't be seen with static camera.
Camera rotation allows to spot invisible static units.
Alternate Alt+T and Alt+G to rotate the camera and send detection at the right place.
Alt+RightClick pings the invisible unit location to allies.

**Note:** T and G have been chosen because:
* there is no Alt shortcut on them
* the fingers are more on the command space (than ` and 1)
* D could not be chosen due to alias to append to macro group
* Rotate camera (help to spot invisible)

### More Town cameras
* B remains toggle base camera
* Shift+V becomes an alternate for telegraph inject use case

### AI keys now supported
* direct attack on Ctl+Alt+D
* direct scout on Ctl+Alt+T
* direct detect on Ctl+Alt+F
* direct expand on Ctl+Alt+G
* open AI communication on Ctl+Alt+V
* build on Ctl+Alt+C
* clearall on Ctl+Alt+E
* delete on Ctl+Alt+R

### Moved out of the dense keycard and Function keys
* Period: Warp (to encourage production group)
* Numpad0: Quick save
* Delete: CameraFollow
* BackSlash: All life bars
* Bracket Open: Allies life bars
* Bracket Close: Player life bars

----------------------------------------------------------------------------------------------------------------------

TheCore Lite groups
-------------------

Compared to legacy TheCore Lite:
* all group keys are similar
* the suggested macro group keys changed from QW to ZX
* Ctl is now used for AppendSteal
* Ctl+Shift is now used of CreateSteal

Non-steal aliases:
* Ctl+Alt could be used for Append non-steal
* Ctl+Shift+Alt could be used for Create non-steal

### Macro groups

#### History

Legacy TheCore Lite comes with suggestions of control groups.
Q is intended for production facilities or inject queens.
W is intended for CC Nexus Hatcheries.

source: https://docs.google.com/spreadsheets/d/1v1gTY9suNstl6KoYQ0zIA8_dIBAJ9COmdtbQ1AEuxV4/edit?pref=2&pli=1#gid=56

Macros keys have been changing for this version to benefit from Shift+Z+X mechanics.

#### Nexus/CC/Hatch group = **Z**

Group content:
* All Nexus/CC/Hatch
* Terran and Protoss should add research facilities to this group

Tip for additional expansion:
* Alt+D helps to append base to this group after camera creation
* Alt+Tab helps to append base to this group after camera creation
* Alt+Shift helps to center base at camera creation

#### Production group (or inject queens) = **X**

Group content
* Terran & Protoss: All army production facilities
* Zerg: inject queens
* Zerg should add research facilities to this group

Tip for rally point | warp-in pylon:
* Shift+X has the same effect than pressing X
* Shift+Z+X mechanics
 * Shift+Z recall camera (rally point)
 * Shift+X select this group

Race specifics:
* warp-in: keep shift pressed, while holding unit key (queued rapid-fire warp-in)
* egg inject:
 * Z camera would be main hive
 * Shift+Z+X helps getting Shift already pressed for queued commands
 * please read dedicated usecase "telegraph inject" and "zerg macro routine"

### Group display

The 2 "macro" groups are positioned in the center to split the remaining groups by 4 keys.
This facilitates the visual representation of existing groups.
The 10 groups are displayed in this order (| figures the separation):
```
`123|ZX|QWAS
```

**Note:** the icon representing the group seems to be the best selectable unit at group creation
If you wanted to update the icon, select the group and recreate it.

----------------------------------------------------------------------------------------------------------------------

TheCore Lite location cameras 
-----------------------------

Compared to legacy TheCore Lite:
* one camera key changed: X
* camera creation still based on Alt modifier
* camera recall still based on Shift modifier
* "control" cameras were introduced

### Standard camera views
```
`123
  QW[ER]
  AS[DF]
  Z [CV] <= no more camera on X
```
* Alt now shows Ennemy life bar (useful for quick check of stacked ground/air armies)
* Alt+Shift center the camera on the selection
* ` is used for jump to last alert (with Shift or Alt)
* CV|DF|ER are "control" cameras aliases for 1|2|3

### Additional cameras alternates on control
2 "Control" camera alternates:
* Ctl+C = Shift+1
* Ctl+D = Shift+2
* Ctl+E = Shift+3

Camera creation:
* Ctl+V = Alt+1
* Ctl+F = Alt+2
* Ctl+R = Alt+3
* Ctl+Space centers camera view (if you want to center a warp pylon, or a creep tumor)

----------------------------------------------------------------------------------------------------------------------

Experimental features
---------------------

### Easier cloning through Shift+Alt group creation

Cloning consists in recreating a group after one unit deselection.
Most of the seeds for TheCore 2.0 uses Shift as the modifier for group creation.
This allows to chain:
* select a group
* issue a command
* Shift+click on a unit in the selected group
* group recreation
* new command out of the current selection

As Shift is used for camera jump in TheCore Lite,
Shift+Alt+#groupkey has been chosen as an alternate for group creation.
* select group with #groupkey
* issue a command
* Shift(+Alt)+click on a unit from the group
* Shift+Alt+#groupkey to overwrite group
* issue a new command

**Note:** be careful not to press Alt+Shift+#camkey simultaneously while centering view with Alt+Shift,
this would overview the group affected to #camkey


----------------------------------------------------------------------------------------------------------------------

Use case scenarii
-----------------

### Use case: expansions cameras
* Select new base under construction
* Alt+Shift: center view on base
* Alt+[camera\_key]: make view on associated key
* Alt+D: append expansion to Nexus/CC/Hatch group
 * Alt+Tab could be used as well (**warning** could bring back to desktop)

### Use case: send worker back to ressources gathering after queued commands
* press shift to queue all necessary commands
* Shift+[camera\_key]: jump to base
* Shift+RightClick on mineral or gaz; last action of the queue is to go back to work

### Use case: army production + rally point (optional warp-in pylon)
* Hold Shift
* Shift+Z: jump to rally point (declared with Alt+X)
* Shift+X: select production facilities
* inspect rallied army
* optional redeclaration of the rally point (RightClick, in case of new integrated facility)
* browse subgroup and launch production
* select rallied army and add to control groups

### Use case: warp-in pylon (with Ctl camera)
* Ctl+C|D|E: center on warp pylon
* X: select production facilities (WarpGate have higher selection priority)
* hold key for warping-in units (rapid fire warp-in)
* Ctl+click: on a unit, select all units for this type
* Ctl+[army\_group]: add selection to an army group
* right click for rally
* [army\_group]: attack

### Use case: warp-in pylon (with Shift camera)
* Hold shift
* Shift+S: jump to warp-in camera (S as a suggestion with X for the regular rally point)
* Shift+X: select production facilities (WarpGate have higher selection priority)
* Shift+key for warping-in units (queued rapid fire warp-in)

### Use case: telegraph inject

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
 * Shift+Z = jump to main hatch (first hatch)
 * Shift+X = select inject queens + tech
 * Shift+Space = inject

Cycle through bases with fingers only
* center mouse
* press Shift+V to cycle base
 * depending on habbits/comfort preference Shift+B works as well
* press one of those to target hatch if queen is there, depending on your comfort preference:
 * Shift+Space
 * Shift+F
 * Shift+D

**Note:** In case of wandering queen, release shift and press V

### Use case: zerg macro routine
* Hatch check
 * Z: hatch group
 * check supply depot at this step, to produce overlords
 * morph other larvaes depending on needs
* Inject cycle (hold Shift)
 * Shift+Z = jump to main hatch (first hatch)
 * Shift+X = select inject queens + tech
 * Shift+Space = queue inject (prevent queens from walking around)
 * center mouse + click
 * Shift+A|S|Q|W|2+click = base camera + inject
 * **note** alternatively consider telegraph inject
* Tech check
 * You had time to check upgrades as they were selected with inject queeens
 * browse subgroup + add new research
* Creep queen
 * S x2 = select + jump to creep queen (same raw as C for fast spawn creep tumor)
 * Shift+C + clicks = drop creep tumors (queued)
* Creep cameras (control cameras : ER, DF, CV)
 * Ctl+E|D|C = jump to creep camera
 * Ctl+click to select creep tumors
 * Shift+C then clicks = queued creep tumor spread
 * click = select a new creep tumor
 * Ctl+Space = center view on selection
 * Ctl+R|F|V = update creep camera

**Note:** creep tumor spawn/expand could be performed without queue
, if you're not careful you would have to cancel the action before selection with click or double-click


----------------------------------------------------------------------------------------------------------------------

Changelog for the code
======================

Compared to upstream project:
* TheCoreRemapper.py supporting other seeds than pure TheCore
* New "seed" checks:
 * check for unbound commands, known from conflicts
 * check to prevent conflicts between Hotkeys (i.e. directly access such as groups, base camera key) and Commands
  * known from conflicts
  * unknown from conflicts
* New "quality" checks:
 * check for commands out of known conflicts (warning only in case of inherit/same)
* Debug mode
 * optional generation
 * optional seed selection (you could run the script for the seeds you want)
 * optional quality checks (otherwise just run "seed" checks)
 * optional hint through a "verbose" and "verydetail" options (including the remapHint function)
 * optional IgnoredContext (such as "WoL Campaign" or "Coop") to filter conflicts and keys
* Some .ini file fixed to prevent wrong positives
