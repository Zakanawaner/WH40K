# !python GetData.py <Name of the army>

import re
import os
import sys

# We define the paths
if len(sys.argv) > 1:
    Army = sys.argv[1]
    InWeaponsPath = './Source/Datainput/{}/weapons.txt'.format(Army)
    InWeaponListPath = './Source/Datainput/{}/weaponlist.txt'.format(Army)
    InPointsPath = './Source/Datainput/{}/points.txt'.format(Army)
    InUnitsPath = './Source/Datainput/{}/units.txt'.format(Army)

    if not os.path.exists('./Source/Dataoutput/{}'.format(Army)):
        os.makedirs(Army)

    OutWeaponsPath = './Source/Dataoutput/{}/weapons.txt'.format(Army)
    OutWeaponListPath = './Source/Dataoutput/{}/weaponlist.txt'.format(Army)
    OutUnitsPath = './Source/Dataoutput/{}/units.txt'.format(Army)
    OutSquadsPath = './Source/Dataoutput/{}/squads.txt'.format(Army)
else:
    Army = 'AdeptaSororitas'
    InWeaponsPath = './Datainput/{}/weapons.txt'.format(Army)
    InWeaponListPath = './Datainput/{}/weaponlist.txt'.format(Army)
    InPointsPath = './Datainput/{}/points.txt'.format(Army)
    InUnitsPath = './Datainput/{}/units.txt'.format(Army)

    if not os.path.exists('./Dataoutput/{}'.format(Army)):
        os.makedirs(Army)

    OutWeaponsPath = './Dataoutput/{}/weapons.txt'.format(Army)
    OutWeaponListPath = './Dataoutput/{}/weaponlist.txt'.format(Army)
    OutUnitsPath = './Dataoutput/{}/units.txt'.format(Army)
    OutSquadsPath = './Dataoutput/{}/squads.txt'.format(Army)

with open(InWeaponsPath, 'r') as f:
    weaponsfile = f.read().split('\n')
f.close()
with open(InWeaponListPath, 'r') as f:
    weaponlistfile = f.read().split('\n')
f.close()
with open(InPointsPath, 'r') as f:
    pointsfile = f.read().split('\n')
f.close()
with open(InUnitsPath.format(Army), 'r') as f:
    unitsfile = f.read().split('\n')
f.close()

# Weapons
guns = []
for weapon in weaponsfile:
    i = weapon.find('Melee')
    if i != -1:
        gun = {'name': weapon[:i].replace(' ', ''), 'points': 0}
        for point in pointsfile:
            if re.search(r"\d", point) is not None:
                d = re.search(r"\d", point).start()
                if point[:d].replace(' ', '') == gun['name']:
                    gun['points'] = point[point.rfind(' '):].replace(' ', '')
        weapon = weapon[i:]
        j = weapon.find(' ')
        gun['range'] = weapon[:j]
        weapon = weapon[j + 1:]
        j = weapon.find(' ')
        gun['type'] = weapon[:j]
        weapon = weapon[j + 1:]
        j = weapon.find(' ')
        gun['s'] = weapon[:j]
        weapon = weapon[j + 1:]
        j = weapon.find(' ')
        gun['ap'] = weapon[:j]
        weapon = weapon[j + 1:]
        j = weapon.find(' ')
        gun['d'] = weapon[:j]
        weapon = weapon[j + 1:]
        gun['abilities'] = weapon
        guns.append(gun)
    else:
        m = re.search(r"\d", weapon)
        if m is not None:
            i = m.start()
            gun = {'name': weapon[:i].replace(' ', ''), 'points': 0}
            for point in pointsfile:
                if re.search(r"\d", point) is not None:
                    d = re.search(r"\d", point).start()
                    if point[:d].replace(' ', '') == gun['name']:
                        gun['points'] = point[point.rfind(' '):].replace(' ', '')
            weapon = weapon[i:]
            j = weapon.find(' ')
            gun['range'] = weapon[:j].replace('"', '')
            weapon = weapon[j + 1:]
            j = weapon.find(' ')
            gun['type'] = weapon[:j]
            weapon = weapon[j + 1:]
            j = weapon.find(' ')
            gun['a'] = weapon[:j]
            weapon = weapon[j + 1:]
            j = weapon.find(' ')
            gun['s'] = weapon[:j]
            weapon = weapon[j + 1:]
            j = weapon.find(' ')
            gun['ap'] = weapon[:j]
            weapon = weapon[j + 1:]
            j = weapon.find(' ')
            gun['d'] = weapon[:j]
            weapon = weapon[j + 1:]
            gun['abilities'] = weapon
            guns.append(gun)

with open(OutWeaponsPath, 'w') as f:
    for gun in guns:
        if gun['range'] == 'Melee':
            if 'D' in gun['d']:
                f.write('class {}(Melee, DiceDamageGun):\n'.format(gun['name']))
            else:
                f.write('class {}(Melee):\n'.format(gun['name']))
            f.write('\tdef __init__(self, A=1, S=4):\n')
            f.write('\t\tsuper().__init__(A=A, S=S)\n')
            f.write('\t\tself.POINTS = {}\n'.format(gun['points'])) if int(gun['points']) > 0 else None
            f.write('\t\tself.S = {}\n'.format(gun['s']) if '+' not in gun['s'] and 'x' not in gun['s'] and
                                                            '-' not in gun['s'] and gun[
                                                                's'] != '4' else '\t\tself.S {}= {}\n'.format(
                gun['s'][0], gun['s'][1:]))
            f.write('\t\tself.AP = {}\n'.format(gun['ap'])) if gun['ap'] != '0' else None
            f.write('\t\tself.D = {}\n'.format(gun['d'])) if gun['d'] != '1' else None
            f.write('\t\tself.ABILITY = "{}"\n'.format(gun['abilities'])) if gun['abilities'] != '-' else None
            f.write('\t\tself.TYPE = "{}"\n'.format(gun['type']))
            f.write('\n')
            f.write('\n')
        else:
            if 'D' in gun['d']:
                if 'D' in gun['a']:
                    f.write('class {}(Weapon, DiceAttackGun, DiceDamageGun):\n'.format(gun['name']))
                else:
                    f.write('class {}(Weapon, DiceDamageGun):\n'.format(gun['name']))
            else:
                if 'D' in gun['a']:
                    f.write('class {}(Weapon, DiceAttackGun):\n'.format(gun['name']))
                else:
                    f.write('class {}(Weapon):\n'.format(gun['name']))
            f.write('\tdef __init__(self):\n')
            f.write('\t\tsuper().__init__()\n')
            f.write('\t\tself.POINTS = {}\n'.format(gun['points'])) if int(gun['points']) > 0 else None
            f.write('\t\tself.RANGE = {}\n'.format(gun['range'])) if gun['range'] != '12' else None
            f.write('\t\tself.A = {}\n'.format(gun['a'])) if gun['a'] != '1' else None
            f.write('\t\tself.S = {}\n'.format(gun['s'])) if gun['s'] != '4' else None
            f.write('\t\tself.AP = {}\n'.format(gun['ap'])) if gun['ap'] != '0' else None
            f.write('\t\tself.D = {}\n'.format(gun['d'])) if gun['d'] != '1' else None
            f.write('\t\tself.ABILITY = "{}"\n'.format(gun['abilities'])) if gun['abilities'] != '-' else None
            f.write('\t\tself.TYPE = "{}"\n'.format(gun['type']))
            f.write('\n')
            f.write('\n')
f.close()

# WeaponList
weaponlists = []
j = 0
for i, unit in enumerate(weaponlistfile):
    if unit == '':
        weaponlists.append(weaponlistfile[j + 1 if i > 0 else 0:i])
        j = i
weaponlists = weaponlists[1:]
with open(OutWeaponListPath, 'w') as f:
    f.write('class WeaponList:\n')
    for weaponlist in weaponlists:
        f.write('\t{} = {}\n'.format(weaponlist[0].replace(' ', '').replace('-', ''),
                                     [re.findall('([A-Z][a-z]*)',
                                                 gunname.replace(' ', '').replace('-',
                                                                                  ''))[0] if '•' in gunname else gunname
                                      for gunname in weaponlist[1:]]))
f.close()

# Units
units = []
j = 0
for i, unit in enumerate(unitsfile):
    if unit == '':
        units.append(unitsfile[j + 1 if i > 0 else 0:i])
        j = i
units = units[1:]
auxUnits = []
for unit in units:
    index = 0
    auxUnit = {}
    d = 0
    if re.search(r"\d", unit[index]) is not None:
        d = re.search(r"\d", unit[index]).start()
    auxUnit['name'] = unit[index][:d - 1]
    i = unit[index][d:].find(' ')
    auxUnit['m'] = unit[index][d:i + d].replace('"', '')
    d = i + d + 1
    i = unit[index][d:].find(' ')
    auxUnit['ws'] = unit[index][d:i + d].replace('+', '')
    d = i + d + 1
    i = unit[index][d:].find(' ')
    auxUnit['bs'] = unit[index][d:i + d].replace('+', '')
    d = i + d + 1
    i = unit[index][d:].find(' ')
    auxUnit['s'] = unit[index][d:i + d]
    d = i + d + 1
    i = unit[index][d:].find(' ')
    auxUnit['t'] = unit[index][d:i + d]
    d = i + d + 1
    i = unit[index][d:].find(' ')
    auxUnit['w'] = unit[index][d:i + d]
    d = i + d + 1
    i = unit[index][d:].find(' ')
    auxUnit['a'] = unit[index][d:i + d]
    d = i + d + 1
    i = unit[index][d:].find(' ')
    auxUnit['ld'] = unit[index][d:i + d]
    d = i + d + 1
    auxUnit['sv'] = unit[index][d:].replace('+', '')
    if '"' not in unit[1]:
        index += 1
        auxUnit['MoreUnits'] = False
    else:
        auxUnit['MoreUnits'] = True
        index += 2
    d = unit[index].find('armed with ')
    i = unit[index][d:].find(';') if unit[index][d:].find(';') != -1 else 100000
    auxUnit['gun1'] = unit[index][d:i + d]
    guncount = 1
    if i < 100000:
        d = i + d + 2
        i = unit[index][d:].find(';') if unit[index][d:].find(';') != -1 else 100000
        auxUnit['gun2'] = unit[index][d:i + d]
        guncount += 1
    if i < 100000:
        d = i + d + 2
        i = unit[index][d:].find(';') if unit[index][d:].find(';') != -1 else 100000
        auxUnit['gun3'] = unit[index][d:i + d]
        guncount += 1
    if i < 100000:
        d = i + d + 2
        i = unit[index][d:].find(';') if unit[index][d:].find(';') != -1 else 100000
        auxUnit['gun4'] = unit[index][d:i + d]
        guncount += 1
    if i < 100000:
        d = i + d + 2
        i = unit[index][d:].find(';') if unit[index][d:].find(';') != -1 else 100000
        auxUnit['gun5'] = unit[index][d:i + d]
        guncount += 1
    auxUnit['gun{}'.format(guncount)] = auxUnit['gun{}'.format(guncount)][:auxUnit['gun{}'.format(guncount)].find('.')]
    auxUnit['keywords'] = unit[len(unit) - 1]
    auxUnit['points'] = 0
    for point in pointsfile:
        d = 0
        if re.search(r"\d", point) is not None:
            d = re.search(r"\d", point).start()
            if point[:d].replace(' ', '') == auxUnit['name']:
                auxUnit['points'] = point[point.rfind(' '):].replace(' ', '')
    auxUnits.append(auxUnit)

with open(OutUnitsPath, 'w') as f:
    for auxUnit in auxUnits:
        f.write('class {}({}, Human):\n'.format(auxUnit['name'].replace(' ', ''),
                                                'Infantry' if 'INFANTRY' in auxUnit['keywords'] else 'Vehicle'))
        f.write('\t# MORE THAN ONE UNIT IN THE SQUAD\n') if auxUnit['MoreUnits'] else None
        f.write('\tdef __init__(self):\n')
        f.write('\t\tsuper().__init__()\n')
        f.write('\t\tHuman.__init__(self, Mesh.{})\n'.format(auxUnit['name'].replace(' ', '')))
        f.write('\t\tself.POINTS = {}\n'.format(auxUnit['points']))
        f.write('\t\tself.M = {}\n'.format(auxUnit['m'])) if auxUnit['m'] != '6' else None
        f.write('\t\tself.WS = {}\n'.format(auxUnit['ws'])) if auxUnit['ws'] != '3' else None
        f.write('\t\tself.BS = {}\n'.format(auxUnit['bs'])) if auxUnit['bs'] != '3' else None
        f.write('\t\tself.S = {}\n'.format(auxUnit['s'])) if auxUnit['s'] != '4' else None
        f.write('\t\tself.T = {}\n'.format(auxUnit['t'])) if auxUnit['t'] != '4' else None
        f.write('\t\tself.W = {}\n'.format(auxUnit['w'])) if auxUnit['w'] != '1' else None
        f.write('\t\tself.A = {}\n'.format(auxUnit['a'])) if auxUnit['a'] != '1' else None
        f.write('\t\tself.Ld = {}\n'.format(auxUnit['ld'])) if auxUnit['ld'] != '7' else None
        f.write('\t\tself.Sv = {}\n'.format(auxUnit['sv'])) if auxUnit['sv'] != '3' else None
        f.write('\t\tself.Gun = []\n')
        f.write('\t\tself.Gun.append(Weapons.{}())\n'.format(
            auxUnit['gun1'].replace(' ', ''))) if 'gun1' in auxUnit.keys() else None
        f.write('\t\tself.POINTS += self.Gun[0].POINTS\n'.format(
            auxUnit['gun1'].replace(' ', ''))) if 'gun1' in auxUnit.keys() else None
        f.write('\t\tself.Gun.append(Weapons.{}())\n'.format(
            auxUnit['gun2'].replace(' ', ''))) if 'gun2' in auxUnit.keys() else None
        f.write('\t\tself.POINTS += self.Gun[1].POINTS\n'.format(
            auxUnit['gun2'].replace(' ', ''))) if 'gun2' in auxUnit.keys() else None
        f.write('\t\tself.Gun.append(Weapons.{}())\n'.format(
            auxUnit['gun3'].replace(' ', ''))) if 'gun3' in auxUnit.keys() else None
        f.write('\t\tself.POINTS += self.Gun[2].POINTS\n'.format(
            auxUnit['gun3'].replace(' ', ''))) if 'gun3' in auxUnit.keys() else None
        f.write('\t\tself.Gun.append(Weapons.{}())\n'.format(
            auxUnit['gun4'].replace(' ', ''))) if 'gun4' in auxUnit.keys() else None
        f.write('\t\tself.POINTS += self.Gun[3].POINTS\n'.format(
            auxUnit['gun4'].replace(' ', ''))) if 'gun4' in auxUnit.keys() else None
        f.write('\t\tself.Gun.append(Weapons.{}())\n'.format(
            auxUnit['gun5'].replace(' ', ''))) if 'gun5' in auxUnit.keys() else None
        f.write('\t\tself.POINTS += self.Gun[4].POINTS\n'.format(
            auxUnit['gun5'].replace(' ', ''))) if 'gun5' in auxUnit.keys() else None
        f.write('\n')
        f.write('\n')

# Squads
squads = []
for unit in units:
    squad = {}
    index_wargear = None
    index_abilities = None
    for i, line in enumerate(unit):
        if 'WARGEAR' in line:
            index_wargear = i
        if 'ABILITIES' in line:
            index_abilities = i
    wargear_options = []
    if index_abilities is not None and index_wargear is not None:
        for i in range(index_wargear, index_abilities):
            point = unit[i].find('• ')
            if point != -1:
                wargear_option = unit[i][point + 2:]
                wargear_options.append(wargear_option)
            else:
                wargear_options[-1] += unit[i]
    faction_keywords = unit[len(unit) - 2].replace('FACTION KEYWORDS ', '').split(',')
    keywords = unit[len(unit) - 1].replace('KEYWORDS ', '').split(',')
    d = 0
    if re.search(r"\d", unit[0]) is not None:
        d = re.search(r"\d", unit[0]).start()
    squad['name'] = unit[0][:d - 1].replace(' ', '')
    squad['keywords'] = [keyword[1:] if keyword[0] == ' ' else keyword for keyword in keywords]
    squad['factionkeywords'] = [faction_keyword[1:] if faction_keyword[0] == ' ' else faction_keyword for
                                faction_keyword in faction_keywords]
    squad['wargear'] = wargear_options
    squads.append(squad)

with open(OutSquadsPath, 'w') as f:
    for squad in squads:
        f.write('class {}Squad(Squad):\n'.format(squad['name']))
        f.write('\tdef __init__(self):\n')
        f.write('\t\tsuper().__init__(Power=, MaxUnits=, AddedPower=)\n')
        keywords = ['"{}"'.format(keyword) for keyword in squad['keywords']]
        f.write('\t\tself.Keywords = [' + ', '.join(keywords) + ']\n')
        f.write('\t\tself.ABILITIES = []\n')
        f.write('\t\tself.Units.append(Units.{}())\n'.format(squad['name']))
        f.write('\t\tself.Units.append(Units.{}())\n'.format(squad['name']))
        f.write('\t\tself.Units.append(Units.{}())\n'.format(squad['name']))
        f.write('\t\tself.Units.append(Units.{}())\n'.format(squad['name']))
        f.write('\t\tself.Units.append(Units.{}())\n'.format(squad['name']))
        f.write('\t\t# TODO Equipment singularities\n')
        f.write('\t\tself.SquadType = ''  # TODO squad type\n')
        f.write('\t\tself.calculate_points()\n')
        f.write('\t\tself.WargeatOptions = []\n')
        for i, wargear in enumerate(squad['wargear']):
            f.write("\t\tself.WargeatOptions.append('''{}''')\n".format(wargear))
        f.write('\n')
        for wargear in squad['wargear']:
            f.write('\t\t# {}\n'.format(wargear))
        f.write('\n')
        f.write('\n')
f.close()
