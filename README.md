The Core Lite v2.0
==================

This is the Github repository for TheCore Lite Starcraft2 bindkeys.

The goals are:
* keep as much consistency with legacy "TheCore Lite" for unit commands
* get rid of bad habits and develop sane mechanics
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
 * keys supposed to be the same, or inherited (multi-racial support)
 * delivered in a set of supported keyboard layouts
 * it passes all the new introduced "seed" checks

### Ressources

Some graphic ressources is available in Image directory,
please download the following .pdf file:

[TheCore_Lite.pdf](https://github.com/bobo38/TheCoreLite/raw/master/Images/TheCore_Lite.pdf)

Legacy ressources:
* [historical Master Spreadsheet](https://docs.google.com/spreadsheets/d/1v1gTY9suNstl6KoYQ0zIA8_dIBAJ9COmdtbQ1AEuxV4/edit?pref=2&pli=1#gid=56)
* [TheCore Lite thread on teamliquid.net](http://www.teamliquid.net/forum/sc2-strategy/333891-thecore-lite-advanced-keyboard-layout)

### Aknowledgments

Loads of thanks to:
* TheCore project, whose this repo is a fork, and all the accumulated work over the years
* JaKaTaK, the originator of the first TheCore Lite version
* BeedeBdoo, who explained me the arcanes of TheCore, and datamined command card conflicts

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

This makes sense considering synergie with mouse clicking and group creation

### Rapid Fire and Precision keys

There are now far more Rapid Fire Hotkeys: Space, R, T, Y, D, F, G, H, V, CapsLock.
Now all Warp-Inable units are bound to Rapid Fire keys.
If you don't know what rapid fire keys are, please check out JaKaTaK's videos on Youtube.

source: [JaKaTaK's Rapid Fire Hotkeys thread](http://www.teamliquid.net/forum/sc2-strategy/446530-rapid-fire-hotkey-trick) on TeamLiquid.net

"E" and "C" keep on being non Rapid Fire, because they are precision keys.
They are used for precision spells/ability.
You can keep those key pressed and just click on the target.
After the click the ability will be called again and you just have to click on the next target.

**Note:** like legacy TheCore Lite, some spells have 2 alternates; one on "rapid fire" key, the other on "precision" key

### Browsing subgroups
* Tab and Shift+Tab are used
* Back/Forward Mouse Button added to browse between subgroups

### Ping allies !
* Alert jump accessible with Shift+Grave
* QuickPing now mapped on Alt+RightClick

### Fight against invisible
* Alt+T : Rotate camera Left
* Alt+G : Rotate camera Right

Immobile invisible units can't be seen with static camera.
Camera rotation allows to spot invisible static units.
Alternate Alt+T and Alt+G to rotate the camera and send detection at the right place.
Alt+RightClick pings the invisible unit location to allies.

### More Town cameras
* B remains toggles base camera
* Shift+V becomes an alternate for Telegraph inject use case

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
* Delete: CameraFollow (confusing feature)
* Apostrophe: Minimap ping (preferred usage of QuickPing Alt+RClick)
* BackSlash: All life bars (better use show "damaged" units)
* Bracket Open: Allies life bars (better use show "damaged" units)
* Bracket Close: Player life bars (better use show "damaged" units)

----------------------------------------------------------------------------------------------------------------------

TheCore Lite location cameras 
-----------------------------

Compared to legacy TheCore Lite:
* one camera key changed: X has been replaced by 1
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
* Alt+X centers the camera on the selection
* ` is used for jump to last alert (with Shift)
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

TheCore Lite Macro groups
-------------------------

### History

Legacy TheCore Lite comes with suggestions of control groups.
Q is intended for production facilities or inject queens.
W is intended for CC Nexus Hatcheries.

Macros keys have been changing for this version to benefit from Shift+Z+X mechanics.

### Nexus/CC/Hatch group = **Z**

Group content:
* All Nexus/CC/Hatch
* Terran and Protoss should add research facilities to this group

Tip for additional expansion:
* Center base at camera creation with Alt+X
* Add to Nexus/CC/Hatch with alternates:
 * Alt+D (legacy alternate)
 * Alt+Grave
 * Alt+Tab
 * Alt+CapsLock

### Production group (or inject queens) = **X**

Group content:
* Terran & Protoss: All army production facilities
* Zerg: inject queens
* Zerg should add research facilities to this group

Tips for rally point | warp-in pylon:
* Shift+X has the same effect than pressing X
* Shift+Z+X mechanics
 * Shift+Z recall camera (rally point)
 * Shift+X select this group

Race specific:
* Related to warp-in
 * Keep shift pressed, while holding unit key (queued rapid-fire warp-in)
 * Shift+S could be used for secondary warp-in zone
* Related to egg inject
 * Z camera would be main hive
 * Shift+Z+X helps getting Shift already pressed for queued commands
 * please read dedicated usecase "Telegraph inject" and "TheCore inject"

### Group display

The 2 "macro" groups are positioned in the center to split the remaining groups by 4 keys.
This facilitates the visual representation of existing groups.
The 10 groups are displayed in this order (| figures the separation):
```
`123|ZX|QWAS
```

**Note:** the icon representing the group seems to be the best selectable unit at group creation.
If you wanted to update the icon, select the group and recreate it.

----------------------------------------------------------------------------------------------------------------------

TheCore Lite Group modifiers
----------------------------

Compared to legacy TheCore Lite:
* all group keys are similar
* the suggested macro group keys changed from QW to ZX
* modifier have been changed

LoTV introduced steal behavior, for Archon mode.
"Steal" enables to remove the selection from any other groups,
including Archon partner or your own groups.
TheCore team concluded that this property worths using it by default.
JaKaTaK explains pros and cons in this video: [To steal or not to steal](https://www.youtube.com/watch?v=ayngEqIaWmM)

For TheCore Lite, here are the modifiers:
* AppendSteal = Ctrl
* CreateSteal = Ctrl+Shift
* Create non-steal = Shift+Alt (and Ctrl+Shift+Alt)
* Append non-steal = Ctrl+Alt

### Mouse synergies with Ctrl and Ctrl+Shift

Those behaviors are similar if Alt is pressed simultaneously:
* Ctrl+
 * one click on the map, selects all visible units similar to target
 * one click on the board, keeps selected only units similar to target
* Ctrl+Shift+
 * one click on the map, adds all visible units similar to target in selection
 * one click on the board, removes all units similar to target in selection

In case you want to split a group,
just box some units then appendsteal them to another group with Ctl+click+#groupnumber.

In case you want to remove a unit type from a group
* Ctl+click a unit+#groupnumber, you probably want all units to be a target group anyway
* Ctl+Shift+click a unit+#groupnumber, deselected units won't have any group :(

Shift+Alt would be recommanded if you want to remove some units from control groups.
Just recreate group with Shift+Alt after shift clicking the units supposed to stay at their place
(or execute the last command - read next section).

Some examples with "Select All Army":
* After Ctl+Tab
 * Ctl+click will select only all units of the clicked type
 * Ctl+#group key will append/steal the selection
* After Ctl+Shift+Tab
 * Ctl+Shift+click will remove any unit of the clicked type
 * Ctrl+Shift+#group key will create/steal a group with this selection
  * alternatively Shift+Alt+#group key will create group/non-steal the selection

### Easier cloning through Shift+Alt

Shift+Alt+LeftClick acts as Shift+LeftClick when deselecting a unit from the selection.
Shift+Alt+RightClick is an alias for Smart Command, it **inhibits the queuing**.
As a consequence Shift+Alt could be hold during a typical cloning routine.
More info at the following URLs.

Shift+Alt+#groupkey is used for create/non-steal group.
It could help in creating groups after unit deselection.
Please refer to JaKaTaK video for more details.

sources:
* [TeamLiquid's page about "Cloning"](http://wiki.teamliquid.net/starcraft2/Cloning)
* [JaKaTaK's "How to clone - manual cloning" video](https://www.youtube.com/watch?v=S4Q9ghZbqpA&list=PLiejbQlQAdGnuLyxXEC7fnLIy-hdD7J-8&index=7)
* [JaKaTaK's "How to clone - control group cloning" video](https://www.youtube.com/watch?v=1cozEzPaxnw&list=PLiejbQlQAdGnuLyxXEC7fnLIy-hdD7J-8&index=11)

### Twin group for easy caster selection

You may want to have units in both a main army group and a caster group.
It is the case of the Stalker group in [JaKaTaK's video on Protoss control groups](https://www.youtube.com/watch?v=Hu7sLfLpkaM&index=10&list=PLiejbQlQAdGlM1wWWxMGZsBAFCrIRjGJn).
Ctl+Alt modifier is an alternate for Append non-steal on this purpose.

* select main group
* Ctrl+(Alt)+ click unit to select only units of this type
* Ctrl+Alt+#groupnumber to append to target group
 * alternatively Shift+Alt if the group needs to be overwritten

----------------------------------------------------------------------------------------------------------------------

Use case scenarii
-----------------

### Use case: expansions cameras
* Select new base under construction
* Alt+X: center view on base
* Alt+[camera\_key]: make view on associated key
* Append expansion to Nexus/CC/Hatch group
 * Alt+Grave
 * Alt+Tab (**warning** could bring back to desktop)
 * Alt+CapsLock

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

Optional:
* Ctl+click: on a unit, select all units for this type
* Ctl+[army\_group]: add selection to an army group
* right click for rally
* [army\_group]: attack

### Use case: Telegraph inject

The "Telegraph" inject is an implementation of the [Backspace inject](http://wiki.teamliquid.net/starcraft2/Spawn_Larva_(Legacy_of_the_Void)#Backspace_Method).
It relies on:
* no mouse click
* 2 neighbour keys, comfortably pressable
* holding left Shift during the whole inject phase
* to queue command

TheCore Lite inject initiate:
* Shift+Z = jump to main hatch (first hatch)
* Shift+X = select inject queens + tech
* Shift+Space = inject
* center mouse
* keep Shift hold (to queue target)

Cycle through bases with fingers only:
* press Shift+V to cycle base
 * depending on habbits/comfort preference Shift+B works as well
* if queen is there, with enough energy, press one of those depending on your comfort preference:
 * Shift+Space
 * Shift+F
 * Shift+D, all of them are alternate for TargetChoose (aka Rapid Fire key)

**Note:** In case of wandering queen, release shift and press V

### Use case: TheCore inject

The [TheCore inject](http://wiki.teamliquid.net/starcraft2/Spawn_Larva_(Legacy_of_the_Void)#The_Core_Method)
benefits as well of TheCore Lite inject initiate.

* TheCore Lite inject initiate
 * Shift+Z = jump to main hatch (first hatch)
 * Shift+X = select inject queens + tech
 * Shift+Space = inject
 * center mouse
* Shift+Q|W|A|S+click = base camera + inject if needed

Suggested camera locations:
* Z main
* A 2nd
* W 3rd
* Q 4th
* 3 5th

### Use case: zerg macro routine
* Hatch check
 * Z: hatch group
 * check supply depot at this step, to produce overlords
 * morph other larvaes depending on needs
 * add eggs to control groups and give them rally points
* Inject routine of your choice
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
  * altenatively, CapsLock for rapid fire creep tumor
 * click = select a new creep tumor
 * Ctl+Space = center view on selection
 * Ctl+R|F|V = update creep camera

sources:
[JaKaTaK's "Egg Hotkey Drill" video](https://www.youtube.com/watch?v=GWgwuce9q6o&list=PLiejbQlQAdGl0uqlZUauzrxwcM5fquSPh&index=6)
[JaKaTaK's "Rapid Fire Creep Spread" video](https://www.youtube.com/watch?v=av2kaBI-gKg&index=11&list=PLiejbQlQAdGl0uqlZUauzrxwcM5fquSPh)

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
