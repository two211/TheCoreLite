
The Core Lite Variations
========================

TheCore Lite.SC2Hotkeys
-----------------------

Legacy "TheCore Lite" updated to fix most of TheCore standards:
* keys to be the same, or inherited
* no keys conflicts (conflicts are only partially described)

On top of that, it fits with all new introduced "seed" checks.

Changes:
* Functions keys have been populated
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
	* all steal apart of "Q" and "W"
	* "Q" and "W" to be used for army groups to facilitate retreat/follow front-line
* AI keys now supported
	* direct attack on Alt+D
	* direct scout on Alt+T
	* direct detect on Alt+F
	* direct expand on Alt+G
	* open AI communication on Alt+C
	* build on Alt+B
	* clearall on Alt+V

TheCore LiteRehabPlus.SC2Hotkeys
----------------------------

Same as TheCore LiteRehab.SC2Hotkeys with an experimental "monitor" overlay.
The principle is to use "shift" as a "monitor mode" modifier.
The goal is encourage camera keys, having also the useful stuff pressing "shift".

1. Additional groups (create/add work the same Ctrl+Shift/Ctrl):
* Shift+F is an alternate for "X" to be used for CC/Nexus/Hatch and tech
* Shift+D is an alternate for "Z" to be used for "production facilities" or "inject queens"
* Shift+V is an alternate for "`" to be used for
	* "creep queen"
	* mothership (core)
	* wall supply depot
	* whatever other useful group you could think about

NOTE: "X" "Z" "`" groups have been chosen due to poor accessibility in TheCore Lite. Regular groups to be used for armies are:
```
123 <= steal
 QW <= no steal
 AS <= steal
```

2. Additionnal views (save camera view with "Alt")
* Shift+E is an alternate for Shift+2
* Shift+R is an alternate for Shift+3

Note: to be used for "creep cameras" or "rally points"

3. More accessible view related features
* Shift+T is an alternate for "follow selection"
* Shift+G is an alternate for "alert recall"
* Shift+B has the same effect as "base" key

Use case: zerg macro routine
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

WARNING: all those "Shift alternates" may disturb your queued command habits.
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
	* check for commands out of known conflicts (warning only in case of inherit/same), error would require to be fix
* Debug mode
	* optional generation
	* optional seed selection (you could run the script for your seed)
	* optional quality checks (to just run "seed" checks)
	* optional hint through a "verbose" and "verydetail" options (including the remapHint function)
	* optional context ignore to filter conflict and key only related to a specific "context" (such as "WoL Campaign" or "Coop")
* Some .ini file fixed to prevent wrong positive

Original README
===============

Pre-Requisites: You must have Python 3.5.1+ installed to run this script.

Brief Overview of Important Files:

1. TheCoreSeed.ini - The single file used to generate all layouts of TheCore. It is structured very similarly to a .SC2Hotkeys file,
with some notable exceptions. Each line can take on 1 of 3 forms. P, T, R, and Z stand for Protoss, Terran, Random, and Zerg, and indicate 
the key used in the left-handed, medium size layout of TheCore. D stands for the Standard default key used for a command. The line formats are:
   a. CommandName=P|T|R|Z|D
   b. CommandName=SharedKey|D (if the keys are the same for each race, don't list them 4 times, just list them once)
   c. CommandName=CommandNameToCopy (useful for campaign keys, this means the keys will be copied from another command)

2. MapDefinitions.ini - This file stores the mappings that are used to convert the left-handed medium layouts to the other layouts. 

  [GlobalMaps] are of the form L = R, and are used for mapping the global hotkeys
     L is the key in the left-handed medium layouts.
     R is the key in the right-handed medium layouts.

  [ShiftLeftMaps] and [ShiftRightMaps] are of the form B = A, and are used for shifting the medium layout one key to the left or right to generate
  the large and small layouts.
     B is the key before the shift.
     A is the key after the shift (the key that is mapped to)

  All of the other maps are of the form LM = LMM,RMM,RM (As of April 2013, LMM and RMM are obsolete)
     It is a mapping from LM to the other 3 layouts.
     [P/T/Z/R CGMaps] are the control group maps.
     [P/T/Z/R AMaps] are the unit ability maps.
     (Obsolete as of April 2013) [P/T/Z/R A/I/BB/MF/TP Maps] are the maps that are referenced in [MappingTypes]

3. KeyboardLayouts.ini - This file stores mappings for alternative keyboard layouts. TheCoreSeed.ini and MapDefinitions.ini store values designed for QWERTY keyboards.
The mappings stored in this file are applied to map from the US QWERTY version of a layout to a different keyboard layout. Each keyboard type layout takes on the form:

   [KeyboardTypeName]
   QWERTYKey=KeyboardTypeKey

The generated layouts get put in a separate folder with the name of the KeyboardType (e.g. USDvorak).

4. InGameGUIImport.py - This file will import changes made to PLM,ZLM,TLM, and RLM into TheCoreSeed.ini. The workflow is:
   a. Copy and paste the *LM.SC2Hotkeys file into your Starcraft 2 Hotkey folder.
   b. Load up SC2 and edit the layouts in game.
   c. Copy and paste the edited files back into TheCoreConverter directory, overwriting the existing ones.
   d. Run python InGameGUIImport.
   e. Check the log if any hotkeys or commands are missing in the TheCoreSeed.ini and add the ones to the NewDefaults.ini with the default value from sc2 go to d.
   f. Verify that the changes made to TheCoreSeed.ini are accurate.
   
The important thing to note about editing files with the in-game editor is that any overlaps between the edited files and the SC2 Standard hotkey layout will be stripped from the file.
This is why TheCoreSeed.ini stores the default Standard layout hotkeys, so that it can fill these back in when you run the InGameGUIImport.

5. TheCoreRemapper.py - This is the script that makes the magic happen. Once you have made appropriate changes to TheCoreSeed.ini (either by using the InGameGUIImport method above or
by editing the text file directly), you can run python TheCoreRemapper.py, and it will generate all layouts of TheCore, and check them for errors.