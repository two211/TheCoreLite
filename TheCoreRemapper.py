##################################################
#
# Filename: TheCoreRemapper.py
# Author: Jonny Weiss, Mark Rösler
# Description: Script to take the LM layouts of TheCore and generate the other 44 layouts.
# Change Log:
#   9/25/12 - Created
#   9/26/12 - Finished initial functionality
#
##################################################
import collections
import configparser
import os

from conflict_checks import *  # @UnresolvedImport
from same_checks import *  # @UnresolvedImport

SHOW_DUPLICATES = False
VERIFY_ALL = False

class ConfigParser(configparser.ConfigParser):
    """Case-sensitive ConfigParser."""
 
    def optionxform(self, opt):
        return opt
    
    def write(self, file):
        return super().write(file, space_around_delimiters=False)

PROTOSS = "P"
TERRAN = "T"
RANDOM = "R"
ZERG = "Z"
races = [PROTOSS, TERRAN, RANDOM, ZERG]

RIGHT = "R"
LEFT = "L"
sides = [LEFT, RIGHT]

SMALL = "S"
MEDIUM = "M"
LARGE = "L"
sizes = [SMALL, MEDIUM, LARGE]

# Read the settings
settings_parser = ConfigParser()
settings_parser.read('MapDefinitions.ini')

layout_parser = ConfigParser()
layout_parser.read('KeyboardLayouts.ini')

default_filepath = 'NewDefaults.ini'
default_parser = ConfigParser()
default_parser.read(default_filepath)

ddefault_filepath = 'different_default.ini'
ddefault_parser = ConfigParser()
ddefault_parser.read(ddefault_filepath)

inherit_filepath = 'TheCoreSeed.ini'
inherit_parser = ConfigParser()
inherit_parser.read(inherit_filepath)
    
prefix = settings_parser.get("Filenames", "Prefix")
suffix = settings_parser.get("Filenames", "Suffix")
seed_layout = settings_parser.get("Filenames", "Seed_files_folder")

hotkeyfile_parsers = {}

class Hotkey:
    
    def __init__(self, name, section, P=None, T=None, Z=None, R=None, default=None, copyOf=None):
        self.name = name
        self.section = section
        self.P = P
        self.T = T
        self.Z = Z
        self.R = R
        self.default = default
        self.copyOf = copyOf

    def set_value(self, race, value):
        if race == PROTOSS:
            self.P = value
        elif race == RANDOM:
            self.R = value
        elif race == TERRAN:
            self.T = value
        elif race == ZERG:
            self.Z = value
    
    def default_instead_of_none_value(self, value):
        if value is None:
            value = self.default
        return value
    
    def get_raw_value(self, race):
        if race == PROTOSS:
            return self.P
        elif race == RANDOM:
            return self.R
        elif race == TERRAN:
            return self.T
        elif race == ZERG:
            return self.Z
    
    def get_value(self, race):
        return self.default_instead_of_none_value(self.get_raw_value(race))
    
    def get_values_id(self):
        values = ""
        for race in races:
            value = self.get_value(race)
            first = True
            alternates = value.split(",")
            alternates.sort()
            for alternate in alternates:
                if first:
                    value = alternate
                    first = False
                else:
                    value = value + "," + alternate 
            values = values + race + ":" + value + "\n"
        return values
        
def init_seed_hotkeyfile_parser():
    for race in races:
        hotkeyfile_parser = ConfigParser()
        hotkeyfilepath = create_filepath(race, LEFT, MEDIUM)
        hotkeyfile_parser.read(hotkeyfilepath)
        hotkeyfile_parsers[race] = hotkeyfile_parser

def create_filepath(race, side, size, path=""):
    filename = prefix + " " + race + side + size + " " + suffix
    filepath = filename
    if path:
        filepath = path + "/" + filename
    return filepath

def new_keys_from_seed_hotkeys():
    for race in races:
        for section in hotkeyfile_parsers[race].sections():
            for item in hotkeyfile_parsers[race].items(section):
                key = item[0]
                if not default_parser.has_option(section, key):
                    default_parser.set(section, key, "")

    file = open(default_filepath, 'w')
    default_parser.write(file)
    file.close()
    order(default_filepath)
    default_parser.read(default_filepath)

def order(filepath):
    read_parser = ConfigParser()
    read_parser.read(filepath)

    dicti = {}
    for section in read_parser.sections():
        items = read_parser.items(section)
        items.sort()
        dicti[section] = items

    open(filepath, 'w').close()  # clear file

    write_parser = ConfigParser()  # on other parser just for the safty
    write_parser.read(filepath)

    write_parser.add_section("Settings")
    write_parser.add_section("Hotkeys")
    write_parser.add_section("Commands")

    for section in dicti.keys():
        if not write_parser.has_section(section):
            write_parser.add_section(section)
        items = dicti.get(section)
        for item in items:
            write_parser.set(section, item[0], item[1])

    file = open(filepath, 'w')
    write_parser.write(file)
    file.close()

def check_defaults():
    warn = False
    parsers = {}
    for race in races:
        filepath = prefix + " " + race + "LM " + suffix
        seed_hotkeyfile_parser = ConfigParser()
        seed_hotkeyfile_parser.read(filepath)
        parsers[race] = seed_hotkeyfile_parser

    for section in default_parser.sections():
        for item in default_parser.items(section):
            key = item[0]
            default = item[1]
            multidefault = ddefault_parser.has_option(section, key)
            if not default or multidefault:
                seedhas = True
                for race in races:
                    if not parsers[race].has_option(section, key):
                        seedhas = False
                inherit = inherit_parser.has_option(section, key)
                
                if multidefault:
                    if not seedhas and not inherit:
                        print("[ERROR] key has multiple diffrent defaults: set in all seed layouts value for this key (or unbound) " + key)
                
                if not default:
                    if seedhas or inherit:
                        if warn:
                            print("[WARN] no default " + key)
                    else:
                        print("[ERROR] no default " + key)

def create_model():
    model = {}
    for section in default_parser.sections():
        section_dict = {}
        for item in default_parser.items(section):
            key = item[0]
            hotkey = Hotkey(key, section)

            default = item[1]
            hotkey.default = default

            for race in races:
                if hotkeyfile_parsers[race].has_option(section, key):
                    value = hotkeyfile_parsers[race].get(section, key)  #
                    hotkey.set_value(race, value)

            if inherit_parser.has_option(section, key):
                copyof = inherit_parser.get(section, key)
                hotkey.copyOf = copyof
            section_dict[key] = hotkey
        model[section] = section_dict
    return model

def generate(seed_model):
    seed_models = init_models()
    for race in races:
        seed_models[race][LEFT][MEDIUM] = extract_race(seed_model, race)
        seed_models[race][RIGHT][MEDIUM] = convert_side(seed_models[race][LEFT][MEDIUM], RIGHT)
        seed_models[race][LEFT][SMALL] = shift_left(seed_models[race][LEFT][MEDIUM], LEFT)
        seed_models[race][RIGHT][SMALL] = shift_right(seed_models[race][RIGHT][MEDIUM], RIGHT)
        seed_models[race][LEFT][LARGE] = shift_right(seed_models[race][LEFT][MEDIUM], LEFT)
        seed_models[race][RIGHT][LARGE] = shift_left(seed_models[race][RIGHT][MEDIUM], RIGHT)
    translate_and_create_files(seed_models)

def init_models():
    models = {}
    for race in races:
        models[race] = {}
        for side in sides:
            models[race][side] = {}
    return models

def extract_race(seed_model, race):
    model_dict = {}
    for section in seed_model:
        model_dict[section] = {}
        for key, hotkey in seed_model[section].items():
            value = resolve_inherit(seed_model, section, hotkey, race)
            model_dict[section][key] = value
    return model_dict

def resolve_inherit(model, section, hotkey, race):
    hotkey = resolve_copyof(model, section, hotkey)
    value = hotkey.get_value(race)
    return value

def resolve_copyof(model, section, hotkey):
    while True:
        if hotkey.copyOf:
            hotkey = model[section][hotkey.copyOf]
        else:
            return hotkey

def convert_side(seed_model, side):
    return modify_model(seed_model, settings_parser, 'GlobalMaps', side)

def modify_model(seed_model, parser, parser_section, side):
    model_dict = {}
    for section in seed_model:
        model_dict[section] = {}
        for key, value in seed_model[section].items():
            if section == "Settings":
                newvalue = value
            else:
                newvalue = modify_value(value, parser, parser_section, side)
            model_dict[section][key] = newvalue
    return model_dict

def modify_value(org_value, parser, section, side):
    altgr = "0"
    if parser == layout_parser and side == RIGHT:
        altgr = layout_parser.get(section, "AltGr")

    newalternates = []
    for alternate in org_value.split(","):
        keys = alternate.split("+")
        newkeys = []
        # filter "Shift" only to make sure it is the same output as the old script
        if altgr == "1" and keys.count("Alt") == 1 and keys.count("Control") == 0 and keys.count("Shift") == 0:
            newkeys.append("Control")
        for key in keys:
            if parser.has_option(section, key):
                newkey = parser.get(section, key)
            else:
                newkey = key
            newkeys.append(newkey)
        newalternate = ""
        first = True
        for newkey in newkeys:
            if not first:
                newalternate = newalternate + "+"
            else:
                first = False
            if not newkey:
                newalternate = ""
            else:
                newalternate = newalternate + newkey
        newalternates.append(newalternate)
    first = True
    newvalues = ""
    for newalternate in newalternates:
        if not newalternate:
            continue
        if not first:
            newvalues = newvalues + ","
        else:
            first = False
        newvalues = newvalues + newalternate
    return newvalues

def shift_left(seed_model, side):
    shift_section = side + 'ShiftLeftMaps'
    return shift(seed_model, shift_section, side)

def shift_right(seed_model, side):
    shift_section = side + 'ShiftRightMaps'
    return shift(seed_model, shift_section, side)
            
def shift(seed_model, shift_section, side):
    return modify_model(seed_model, settings_parser, shift_section, side)

def translate_and_create_files(models):
    layouts = layout_parser.sections()
    for race in races:
        for side in sides:
            for size in sizes:
                for layout in layouts:
                    if layout != seed_layout:
                        model = translate(models[race][side][size], layout, side)
                    else:
                        model = models[race][side][size]
                    create_file(model, race, side, size, layout)

def translate(seed_model, layout, side):
    return modify_model(seed_model, layout_parser, layout, side)

def create_file(model, race, side, size, layout):
    hotkeyfile_parser = ConfigParser()
    for section in model:
        if not hotkeyfile_parser.has_section(section):
                hotkeyfile_parser.add_section(section)
        for key, value in model[section].items():
            hotkeyfile_parser.set(section, key, value)
    if not os.path.isdir(layout):
        os.makedirs(layout)
    filepath = create_filepath(race, side, size, layout)
    hotkeyfile = open(filepath, 'w')
    hotkeyfile_parser.write(hotkeyfile)
    hotkeyfile.close()
    order(filepath)
    return filepath

def analyse(model):
    conflict_and_same_checkts()
    verify_seed_with_generate()
    wrong_inherit(model)
    suggest_inherit(model)

def conflict_and_same_checkts():
    for race in races:
        hotkeyfilepath = create_filepath(race, LEFT, MEDIUM, seed_layout)
        verify_file(hotkeyfilepath)

def verify_file(filepath):
    print("verify file: " + filepath)
    hotkeys_file = open(filepath, 'r')
    dicti = {}
    for line in hotkeys_file:
        line = line.strip()
        if len(line) == 0 or line[0] == "[":
            continue
        pair = line.split("=")
        key = pair[0]
        if key in dicti:
            dicti[key] = [True, pair[1], key, dicti[key][3]]
        else:
            dicti[key] = [True, pair[1], key, ""]

    # Check for duplicates
    if SHOW_DUPLICATES:
        verify_parser = ConfigParser()
        dup_dict = {}
        verify_parser.read(filepath)
        gen_items = verify_parser.items('Hotkeys')
        for pair in gen_items:
            if pair[1] in dup_dict:
                dup_dict[pair[1]].append(pair[0])
            else:
                dup_dict[pair[1]] = [pair[0]]
        for key in dup_dict:
            array = dup_dict[key]
            if len(array) > 1:
                print("============================")
                print(key + "    DUPLICATES")
                for a in array:
                    print(a)

    for same_set in SAME_CHECKS:  # @UndefinedVariable
        mismatched = False
        value = dicti[same_set[0]][1]
        for item in same_set:
            if not dicti[item][1] == value:
                mismatched = True
        if mismatched:
            print("============================")
            print("---- Mismatched values ----")
            for item in same_set:
                print(item + " = " + dicti[item][1])

    for commandcard, conflict_set in CONFLICT_CHECKS.items():  # @UndefinedVariable
        hotkeys = []
        count_hotkeys = {}
        for item in conflict_set:
            if not dicti.__contains__(item):
                print('WARNING: ' + item + ' does not exist in HotKey-file')
            else :
                append = dicti[item][1]
                hotkeys.append(append)
        for key in hotkeys:
            if not key in count_hotkeys:
                count_hotkeys[key] = 1
            else:
                count_hotkeys[key] = count_hotkeys[key] + 1
        for count in count_hotkeys:
            if count_hotkeys[count] > 1:
                print("============================")
                print("---- Conflict of hotkeys in " + commandcard + " ----")
                for item in conflict_set:
                    key = dicti[item][1]
                    if count_hotkeys[key] > 1:
                        print(item + " = " + key)
                # print(conflict_set)
    print("")

def verify_seed_with_generate():
    print("-------------------------")
    print(" Start Comparing Seeds Files with Generated Files")

    for race in races:
        filepath_gen = create_filepath(race, LEFT, MEDIUM, seed_layout)
        parser_gen = ConfigParser()
        parser_gen.read(filepath_gen)

        print("Race: " + race)
        print()

        print("In Seed not in Gen")
        for section in hotkeyfile_parsers[race].sections():
            for seed_item in hotkeyfile_parsers[race].items(section):
                key = seed_item[0]
                if not parser_gen.has_option(section, key):
                    print(key)
        print()
        print("In Seed diffrent in Gen")
        for section in default_parser.sections():
            for item in default_parser.items(section):
                key = item[0]
                if parser_gen.has_option(section, key) and hotkeyfile_parsers[race].has_option(section, key):
                    value_gen = parser_gen.get(section, key)
                    value_seed = hotkeyfile_parsers[race].get(section, key)
                    seed_value_set = set(str(value_seed).split(","))
                    gen_value_set = set(str(value_gen).split(","))
                    if seed_value_set != gen_value_set:
                        if inherit_parser.has_option(section, key):
                            original = inherit_parser.get(section, key)
                            print(key + " seed: " + value_seed + " gen: " + value_gen + " hint: copy of " + original)
                        else:
                            print(key + " seed: " + value_seed + " gen: " + value_gen)

        print()
        print("In Gen not in Seed (defaults filtered)")
        for section in parser_gen.sections():
            for gen_item in parser_gen.items(section):
                key = gen_item[0]
                value_gen = gen_item[1]
                if not hotkeyfile_parsers[race].has_option(section, key):
                    default = default_parser.get(section, key)
                    default_value_set = set(str(default).split(","))
                    gen_value_set = set(str(value_gen).split(","))
                    if gen_value_set != default_value_set:
                        if inherit_parser.has_option(section, key):
                            original = inherit_parser.get(section, key)
                            print(key + " gen: " + value_gen + " seed default: " + default + " hint: copy of " + original)
                        else:
                            print(key + " gen: " + value_gen + " seed default: " + default)
        print()
    print("-------------------------")

def suggest_inherit(model):
    print("------------------------------")
    print("suggest inherit")
    print("------------")
    outputdict = {}
    for section in model:
        outputdict[section] = {}
        for hotkey1 in model[section].values():
            values_id = hotkey1.get_values_id()
            for hotkey2 in model[section].values():
                if hotkey1.name == hotkey2.name:
                    continue
                equal = True
                for race in races:
                    value = hotkey1.get_value(race)
                    value2 = hotkey2.get_value(race)
                    value_set = set(str(value).split(","))
                    value2_set = set(str(value2).split(","))
                    if value_set != value2_set:
                        equal = False
                        break
                if equal:
                    if not values_id in outputdict[section]:
                        outputdict[section][values_id] = {}
                    if not hotkey1.name in outputdict[section][values_id]:
                        outputdict[section][values_id][hotkey1.name] = hotkey1
                    if not hotkey2.name in outputdict[section][values_id]:
                        outputdict[section][values_id][hotkey2.name] = hotkey2
    
    for section in outputdict:
        for values_id in collections.OrderedDict(sorted(outputdict[section].items())):
            hotkeys = outputdict[section][values_id] 
            first = True
            for hotkey in collections.OrderedDict(sorted(hotkeys.items())).values():
                if first:
                    for race in races:
                        value = hotkey.get_value(race)
                        print(race + ": " + str(value))
                    first = False
                
                print("\t" + hotkey.name + " default: " + hotkey.default, end="")
                if hotkey.copyOf:
                    hotkeycopyof = model[section][hotkey.copyOf]
                    print(" copyof: " + hotkeycopyof.name + " default: " + hotkeycopyof.default, end="")
                print()
            print("------------")
    print()

def wrong_inherit(model):
    print("------------------------------")
    print("Wrong inherit")
    for section in model:
        for hotkey in collections.OrderedDict(sorted(model[section].items())).values():
            if not hotkey.copyOf:
                continue
            hotkeycopyof = resolve_copyof(model, section, hotkey)
            equal = True
            for race in races:
                value = hotkey.get_value(race)
                copyofvalue = hotkeycopyof.get_value(race)
                value_set = set(str(value).split(","))
                copyofvalue_set = set(str(copyofvalue).split(","))
                if value_set != copyofvalue_set:
                    equal = False
            if not equal:
                print(hotkey.name + " != " + hotkeycopyof.name)
                for race in races:
                    value = hotkey.get_raw_value(race)
                    copyofvalue = hotkeycopyof.get_value(race)
                    if not value:
                        value = " "
                    if not copyofvalue:
                        copyofvalue = " "
                    print(race + ": " + str(value) + "\t" + str(copyofvalue))
                default = hotkey.default
                if not default:
                    default = " "
                copyofdefault = hotkeycopyof.default
                if not copyofdefault:
                    copyofdefault = " "
                print("D: " + str(default) + "\t" + str(copyofdefault) + " (default)")
                print()
    print()


# check sections
init_seed_hotkeyfile_parser()
new_keys_from_seed_hotkeys()
check_defaults()
model = create_model()
generate(model)
analyse(model)


# Quick test to see if 4 seed files are error free
#     Todo:    expand this to every single file in every directory
#             expand both SAME_CHECKS and CONFLICT_CHECKS
