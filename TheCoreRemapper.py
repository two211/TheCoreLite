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
        value = self.get_raw_value(race)
        if value is None:
            value = self.default
        return value

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
    same_check(model)
    conflict_check(model)
    wrong_inherit(model)
    suggest_inherit(model)


def same_check(model):
    for race in races:
        for same_set in SAME_CHECKS:  # @UndefinedVariable
            same_set.sort()
            first_key = same_set[0]
            for section in collections.OrderedDict(sorted(model.items())):
                if not first_key in model[section]:
                    continue
                mismatched = False
                value = model[section][first_key].get_value(race)
                for key in same_set:
                    if not model[section][key].get_value(race) == value:
                        mismatched = True
                if mismatched:
                    print("============================")
                    print("---- Mismatched values in " + race + " ----")
                    for key in same_set:
                        print(key + " = " + model[section][key].get_value(race))

def conflict_check(model):
    for race in races:
        for commandcard_key, conflict_set in collections.OrderedDict(sorted(CONFLICT_CHECKS.items())).items():  # @UndefinedVariable
            conflict_set.sort()
            count_hotkeys = {}
            for section in model:
                for key, hotkey in model[section].items():
                    if key in conflict_set:
                        values = hotkey.get_value(race).split(",")
                        for value in values:
                            if not value:
                                continue
                            if not value in count_hotkeys:
                                count_hotkeys[value] = 1
                            else:
                                count_hotkeys[value] = count_hotkeys[value] + 1
            
            
            for value, count in collections.OrderedDict(sorted(count_hotkeys.items())).items():
                if count > 1:
                    print("============================")
                    print("---- Conflict of hotkeys in " + race + " " + commandcard_key + " ----")
                    for key in conflict_set:
                        for section in collections.OrderedDict(sorted(model.items())):
                            if not key in model[section]:
                                continue
                            raw_values = model[section][key].get_value(race)
                            values = raw_values.split(",")
                            values.sort()
                            issue = False
                            for issue_value in values:
                                if issue_value == value:
                                    issue = True
                            if issue:        
                                print(key + " = " + raw_values)

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

    for section in collections.OrderedDict(sorted(outputdict.items())):
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
    for section in collections.OrderedDict(sorted(model.items())):
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


init_seed_hotkeyfile_parser()
# check sections
new_keys_from_seed_hotkeys()
check_defaults()
model = create_model()
generate(model)
analyse(model)