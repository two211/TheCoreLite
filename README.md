The Core Lite v2.1
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

TheCore Lite Command spirit
--------------------------------

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

### Unit keys

All Units:
* D = Attack
* V = Stop
* G = Hold
* T = Patrol
* H = Move
* Space = useful ability
* E/C = any ability requiring precision

All workers:
* Space = Basic building
* F = Basic building
* CapsLock = Advanced building
* E = Return cargo
* Y = Gather

Transport/Bunker/CC
* E/CapsLock = unload all
* C = Load

Terran:
* Space/R = "transformers'" keys
* F/CapsLock = cloak/decloak
* 4 = halt key
* 4 = lift key
* 4 = ignite after burner (coop)
* 5 = select worker key
* R = Salvage
* R = Load CC/Planetary Fortress
* E = Reactor
* C = Techlab

Protoss:
* Space = blink guardian shield feedback
* F/CapsLock = orale pulsar beam
* Space/R = warp prism (phase mode)
* E = morph building to warp
* M = morph building to non-warp (intentionally out of compact keys)

Zerg:
* Space/R =  Burrow/Unburrow
* C = creep tumor
* F = morph/evolve
* E = speed key (for research affecting speed)

### Building/Unit production key/Research keys

Basic buildings:
* C = Command center / Nexus / Hatchery
* R = Refinery / Assimilator / Extractor
* D = Supply Depot / Pylon
* E = Engineering Bay / Forge / Evolution Chamber
* Space = Turret / Photo Cannon / Spore Crawler (rapid fire air defense)
* F = Bunker / Spine Crawler (rapid fire defense)

Advanced buildings:
* R = Starport / Stargate / Spire
* G = Fusion core / Fleet Beacon / Ultralisk cavern
* E = Armory (same as Engineering Bay / Forge / Evolution Chamber)

### Units

Some mnemonics:
* D for basic units in the command card
 * zergling
 * marine, hellion, viking
 * zealot, immortal, phoenix
* R for support unit
 * roach
 * marauder, hellbat, liberator
 * stalker, void ray
* F for sneak
 * infestor
 * reaper, widow mine, medivac
 * dark templar, warp prism, oracle
* V and G for advanced and ultimate units
* Space for high profile casters (high templar, ghost, raven)

Bridging method is used to try to facilitate learning.
Research will tend to have the same key as unit production key,
so as the building enabling the production of this unit.

----------------------------------------------------------------------------------------------------------------------

TheCore Lite User Interface keys
--------------------------------

Compared to legacy TheCore Lite, many changes occured in User Interface keys.

### Function keys
* F1 IdleWorker
* F2 Toggle minimap colors (no more Select all army on this key - see Tab key)
* Shift+F1 select all Idle Workers
* Shift+F2 Team Ressources
* Alt+F1 PushToTalk (to free Alt+Shift)
* Alt+F2 Show FPS
* F3 F4 F5 F6 Commander top bar ability
* Shift+F7 Toggle sound (moved to prevent mistyping)
* Shift+F8 Toggle music (could be mapped on Shift+F5 to free space)

### Select All Army on Tab key
* Ctl+Tab : alternate for "select all army"
* Ctl+Shift+Tab : alternate for "select all army"

This makes sense considering synergie with mouse clicking and group creation

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
* New alternates
 * Shift+V becomes an alternate for Telegraph inject use case
 * Shift+Alt+C

### AI keys now supported
* direct attack on Shift+Alt+R
* direct scout on Shift+Alt+T
* direct detect on Shift+Alt+F
* direct expand on Shift+Alt+G
* build style on Shift+Alt+4
* clearall on Shift+Alt+5
* open AI communication on Shift+Alt+C
* delete on Shift+Alt+V

### Moved out of the dense keycard and Function keys
* Period: Warp (to encourage production group)
* Numpad0: Quick save
* Shift+Delete: CameraFollow (confusing feature)
* Apostrophe: Minimap ping (preferred usage of QuickPing Alt+RClick)
* BackSlash: All life bars (better use show "damaged" units)
* Bracket Open: Allies life bars (better use show "damaged" units)
* Bracket Close: Player life bars (better use show "damaged" units)
* Ctl+Alt+NumPad#: append non-steal (dropped due to lack of modifier)

----------------------------------------------------------------------------------------------------------------------

TheCore Lite location cameras
-----------------------------

Compared to legacy TheCore Lite:
* one camera key changed: Q has been replaced by 1
* camera creation still based on Alt modifier
* camera recall still based on Shift modifier
* "control" cameras were introduced

### Other features
* Alt now shows Ennemy life bar (useful for quick check for mana bars of stacked ground/air armies)
* ` is used for jump to last alert (with Shift)

### Additional cameras alternates on control

2 "Control" camera alternates:
* Ctl+D = Shift+1
* Ctl+F = Shift+2
* Ctl+G = Shift+3

Camera creation:
* Ctl+E = Alt+1
* Ctl+R = Alt+2
* Ctl+T = Alt+3
* Ctl+Space centers camera view (if you want to center a warp pylon, or a creep tumor)

Those aliases allow easy save/recall locations.
Same modifier is applied for save and recall.
Using them you have a finger on Ctl:
Ctl+LeftClick on a units selects all visible units of this type.
It is particularly useful for spreading creep.

----------------------------------------------------------------------------------------------------------------------

TheCore Lite Macro groups
-------------------------

### History

Legacy TheCore Lite comes with suggestions of control groups.
Q is intended for production facilities or inject queens.
W is intended for CC Nexus Hatcheries + Tech.

### Nexus/CC/Hatch group = **W**

Group content:
* All Nexus/CC/Hatch
* Terran and Protoss should add research facilities to this group

Tip for additional expansion:
* Center base at camera creation with:
 * Alt+Shift
 * Alt+CapsLock
 * Alt+Tab
 * Alt+`
 * Alt+Q
* Add to Nexus/CC/Hatch with alternates Alt+D

### Production group (or inject queens) = **Q**

Group content:
* Terran & Protoss: All army production facilities
* Zerg: inject queens
* Zerg should add research facilities to this group

Tips for rally point | warp-in pylon:
* Shift+Q has the same effect than pressing Q
* Shift+Q+W mechanics
 * Shift+Q selects this group
 * Shift+W recalls camera (rally point)

Race specific:
* Related to warp-in
 * Keep shift pressed, while holding unit key (queued rapid-fire warp-in)
 * Shift+3 could be used for secondary warp-in zone
* Related to egg inject
 * W camera would be main hive
 * Shift+Q+W helps getting Shift already pressed for queued commands
 * please read dedicated usecase "Telegraph inject" and "TheCore inject"

### Group display

The 2 "macro" groups are positioned in the center to split the remaining groups by 4 keys.
This facilitates the visual representation of existing groups.
The 10 groups are displayed in this order (| figures the separation):
```
`123|QW|ASZX
```

**Note:** the icon representing the group seems to be the best selectable unit at group creation.
If you wanted to update the icon, select the group and recreate it.

----------------------------------------------------------------------------------------------------------------------

TheCore Lite Group modifiers
----------------------------

Compared to legacy TheCore Lite:
* all group keys are similar
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
* Append non-steal has been dropped

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

### Additional group for easy caster selection

You may want to have units in both a main army group and a caster group.
It is the case of the Stalker group in [JaKaTaK's video on Protoss control groups](https://www.youtube.com/watch?v=Hu7sLfLpkaM&index=10&list=PLiejbQlQAdGlM1wWWxMGZsBAFCrIRjGJn).

* Select the group where the casters are
* Ctl+LeftClick a caster in the board (select all units)
* Use Shift+Alt+group# to create/overwrite the caster group without stealing from the main army

----------------------------------------------------------------------------------------------------------------------

Use case scenarii
-----------------

### Use case: expansions cameras
* Select new base under construction
* Alt+CapsLock|`|Tab|Q: center view on base
* Alt+[camera\_key]: make view on associated key
* Alt+D: Append expansion to Nexus/CC/Hatch group

### Use case: send worker back to ressources gathering after queued commands
* press shift to queue all necessary commands
* Shift+[camera\_key]: jump to base
* Shift+RightClick on mineral or gaz; last action of the queue is to go back to work

### Use case: army production + rally point (optional warp-in pylon)
* Hold Shift
* Shift+Q: select production facilities
* Shift+W: jump to rally point (declared with Alt+W)
* inspect rallied army
* optional redeclaration of the rally point (RightClick, in case of new integrated facility)
* browse subgroup and launch production
* select rallied army and add to control groups

### Use case: warp-in pylon

#### with Shift camera
* Hold shift
* Shift+Q: select production facilities (WarpGate have higher selection priority)
* Shift+3: jump to warp-in camera (S as a suggestion with Z for the regular rally point)
* Shift+key for warping-in units (queued rapid fire warp-in)

#### with Ctl camera
* Ctl+Alt: select production facilities (WarpGate have higher selection priority)
* Ctl+D|F|G: center on warp pylon
* hold key for warping-in units (rapid fire warp-in)

#### Other tips
* Ctl+click: on a unit, select all units for this type
* right click for rally

### Use case: BackSpace inject variants

The "Telegraph" inject is an implementation of the [Backspace inject](http://wiki.teamliquid.net/starcraft2/Spawn_Larva_(Legacy_of_the_Void)#Backspace_Method).
It relies on:
* no mouse click
* 2 neighbour keys, comfortably pressable
* holding left Shift during the whole inject phase
* to queue command

#### TheCore Lite inject initiate

* Shift+Q = select inject queens + tech
* Shift+W = jump to main hatch (first hatch)
* Shift+Space = inject
* center mouse
* keep Shift hold (to queue target)

#### Telegraph inject

* Start with a "TheCore Lite inject initiate"
* Then keep Shift pressed and move thumb on Alt
* Shift+Alt+E used to cycle base
* if queen is there, with enough energy, left click
 * Shift+Alt+D used to TargetChoose, like LeftClick (Rapid Fire key)

**Note:** In case of wandering queen, release shift and press V

### Use case: TheCore inject

The [TheCore inject](http://wiki.teamliquid.net/starcraft2/Spawn_Larva_(Legacy_of_the_Void)#The_Core_Method)
benefits as well of TheCore Lite inject initiate.

* TheCore Lite inject initiate
 * Shift+Q = select inject queens + tech
 * Shift+W = jump to main hatch (first hatch)
 * Shift+Space = inject
 * center mouse
* Shift+A|S|Z|X+click = base camera + inject if needed

Suggested camera locations:
* W main
* A 2nd
* S 3rd
* Z 4th
* X 5th

### Use case: zerg macro routine
* Inject routine of your choice
* check supply depot at this step and produce overlords
 * morph 1 overlord/mining hatch/egg cycle
 * rally overlords individually to strategic locations
* Hatch check
 * W: hatch group
 * morph other larvaes depending on needs
 * add eggs to control groups and give them rally points
* Tech check
 * You had time to check upgrades as they were selected with hatcheries
 * browse subgroup + add new research
* Creep queen
 * Ctl+V+V = select + jump to creep queen (same raw as C for fast spawn creep tumor)
 * Ctl+C + clicks = drop creep tumors (queued)
* Creep cameras (control cameras)
 * Ctl+D|F|G = jump to creep camera
 * Ctl+click to select creep tumors
 * Ctl+C then clicks = spread creep tumor
 * click = select a new creep tumor
 * Ctl+Space = center view on selection
 * Ctl+E|R|T = update creep camera

**Note:** keep in mind that selecting another group cancels the action

sources:
[JaKaTaK's "Egg Hotkey Drill" video](https://www.youtube.com/watch?v=GWgwuce9q6o&list=PLiejbQlQAdGl0uqlZUauzrxwcM5fquSPh&index=6)
[JaKaTaK's "Rapid Fire Creep Spread" video](https://www.youtube.com/watch?v=av2kaBI-gKg&index=11&list=PLiejbQlQAdGl0uqlZUauzrxwcM5fquSPh)



----------------------------------------------------------------------------------------------------------------------

Changelog for the code
======================

Compared to upstream project:
* TheCoreRemapper.py supporting other seeds than pure TheCore
* New "seed" checks:
 * check for unbound commands, known from conflicts
 * check to prevent conflicts between Hotkeys (i.e. directly access such as groups, base camera key) and Commands
 * regression check against stable version for Multiplayer
 * check key consistency over CommandRoot
* New "quality" checks:
 * check for commands out of known conflicts (warning only in case of inherit/same)
* Debug mode
 * optional generation
 * optional seed selection (you could run the script for the seeds you want)
 * optional quality checks (otherwise just run "seed" checks)
 * optional hint through a "verbose" and "verydetail" options (including the remapHint function)
 * optional IgnoredContext (such as "WoL Campaign" or "Coop") to filter conflicts and keys
* Some .ini file fixed to prevent wrong positives
