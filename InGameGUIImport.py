##################################################
#
# Filename: InGameGUIImport.py
# Author: Jonny Weiss
# Description: Script to incorporate changes to the 4 *LM layouts into TheCoreSee.ini
# Change Log:
#   4/06/13 - Created
#
################################################## 
from configparser import SafeConfigParser
import os

ADD_MISSING = True

seed_parser = SafeConfigParser()
seed_parser.optionxform = str
seed_parser.read('TheCoreSeed.ini')

settings_parser = SafeConfigParser()
settings_parser.optionxform = str
settings_parser.read('MapDefinitions.ini')

prefix = settings_parser.get("Filenames", "Prefix")
suffix = settings_parser.get("Filenames", "Suffix")
races = ["P", "T", "Z", "R"]

class Hotkey:
    def __init__(self, name, P="", T="", Z="", R="", default="", copyOf=None):
        self.name = name
        self.P = P
        self.T = T
        self.Z = Z
        self.R = R
        self.default = default
        self.copyOf = copyOf
        
    def __str__(self):
        if not self.copyOf is None:
            return self.name + "=" + self.copyOf
        if (self.P == self.T and self.P == self.Z and self.P == self.R):
            return self.name + "=" + self.P + "|" + self.default     
        return self.name + "=" + self.P + "|" + self.T + "|" + self.R + "|" + self.Z + "|" + self.default
 
def SaveSeedFile(hotkeys, commands):
    seed_file = open('TheCoreSeed.ini', 'w')
    seed_file.write("[Settings]\n")
    seed_file.write("AllowSetConflicts=1\n\n")
    seed_file.write("[Hotkeys]\n")
    for hotkey in hotkeys:
        seed_file.write(str(hotkey) + "\n")
    seed_file.write("\n[Commands]\n")
    for command in commands:
        seed_file.write(str(command) + "\n")
    seed_file.close()
    
def get_hotkey(pair):
    values = pair[1].split("|")
    length = len(values)
    P = T = Z = R = default = ""
    if length == 1:  # this is a copy
        hotkey = Hotkey(name=pair[0], copyOf=values[0])
        return hotkey
    if length == 2:
        P = values[0]
        T = values[0]
        R = values[0]
        Z = values[0]
        default = values[1]
    elif length == 5:
        P = values[0]
        T = values[1]
        R = values[2]
        Z = values[3]
        default = values[4]
    else:
        raise Exception("Problem with " + pair[0] + " in TheCoreSeed.ini")
    hotkey = Hotkey(name=pair[0], P=P, T=T, Z=Z, R=R, default=default)
    return hotkey

def fill_hotkey(parsers, hotkey, section):
    for r in races:
        value = hotkey.default
        if parsers[r].has_option(section, hotkey.name):
            value = parsers[r].get(section, hotkey.name)
        setattr(hotkey, r, value)
    return hotkey

def get_hotkeys(parsers, section):
    new_defaults_parser = parsers['defaults'] 
    array = [] 
    for item_pair in seed_parser.items(section):
        hotkey = get_hotkey(item_pair)
        hotkey = fill_hotkey(parsers, hotkey, section)
        array.append(hotkey)

    files_hotkeys = [] 
    for r in races:
        for item_pair in parsers[r].items(section):
            has_hotkey = False
            for hotkey in array:
                if hotkey.name == item_pair[0]:
                    has_hotkey = True
            for hotkey in files_hotkeys:
                if hotkey.name == item_pair[0]:
                    has_hotkey = True
            if not has_hotkey:
                hotkey = Hotkey(name=item_pair[0])
                if new_defaults_parser.has_option(section, hotkey.name):
                    hotkey.default = new_defaults_parser.get(section, hotkey.name)
                hotkey = fill_hotkey(parsers, hotkey, section)
                files_hotkeys.append(hotkey)
                if ADD_MISSING:
                    if hotkey.default != "":
                        array.append(hotkey)
                
    
    if not ADD_MISSING:
        print('--- missing ' + section + ' (in hotkey file/s but not in TheCoreSeed.ini) ---');
    else:
        print('--- add missing ' + section + ' (in hotkey file/s but not in TheCoreSeed.ini) ---')    
    print('--- no defauls found ---')
    for hotkey in files_hotkeys:
        if hotkey.default == "":
            print(hotkey.name+'=') 
            #print(str(hotkey))  
    print()  
    print('--- missing defauls found ---')
    for hotkey in files_hotkeys:
        if hotkey.default != "":
            #print(hotkey.name+'=') 
            print(str(hotkey))  
    print()        
    return array

def ImportChanges():
    parsers = {}
    for r in races:
        hotkeyfile_parser = SafeConfigParser()
        hotkeyfile_parser.optionxform = str
        hotkeyfile_parser.read(prefix + " " + r + "LM " + suffix)
        parsers[r] = hotkeyfile_parser
    new_defaults_parser = SafeConfigParser()
    new_defaults_parser.optionxform = str
    new_defaults_parser.read('NewDefaults.ini')
    parsers['defaults'] = new_defaults_parser
    
    hotkeys = get_hotkeys(parsers, "Hotkeys")    
    commands = get_hotkeys(parsers, "Commands")
    SaveSeedFile(hotkeys, commands)
        
ImportChanges()
