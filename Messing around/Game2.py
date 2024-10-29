mage1 = {
    'name' : 'Gandalf',
    'hp' : 1000,
    'mp' : 100,
    'mana' : 50,
    'util-spells' : {'mana gather': {'mp' : 1, 'focus' : 1}},
    'atk-spells' : {
        'mana-spike' : {'atk' : 10, 'mp' : 5},
        'blaze' : {'atk' : 450, 'mp' : 20},
        'inferno' : {'atk' : 300, 'mp' : 90}
    }
}
def stats(obj):
    print(f"~{obj['name']} | stats~")
    print()
    print(f"Health | {obj['hp']}")
    print(f"Magic Capacity | {obj['mp']}")
    print(f"Condensed Mana {obj['mana']}")
    print()
    print("Utillity spells:")
    for key, value in obj['util-spells'].items():
        if key == 'mana gather':
            print(f"{key.title()} | MP : +{value.get('mp')}/s, Focus : -{value.get('focus')}/s")
        else:
            print(f"{key.title()} | MP : {value.get('mp')}, Focus : {value.get('focus')}")
    print()
    print("Attack spells:")
    for key, value in obj['atk-spells'].items():
        print(f"{key.title()} | Atk : {value.get('atk')}, MP : {value.get('mp')}") 
    print()
    print()

def addAtkSpell(obj,name,atk,mp):
    obj['atk-spells'][name] = {'atk' : atk, 'mp' : mp}
def addUtilSpell(obj,name,mp,focus):
    obj['util-spells'][name] = {'mp' : mp, 'focus' : focus}
def newMage(name,mp,talent, mana=False):
    if mana == False:
        mana = mp
    obj = {
        'name' : name,
        'hp' : 1000,
        'mp' : mp,
        'mana' : mana,
        'util-spells' : {'mana gather': {'mp' : talent, 'focus' : 1}},
        'atk-spells' : {'mana-spike' : {'atk' : 10, 'mp' : 5}}
    }
    return obj

def newObject(name,rarity,grade, mp=False):
    if mp == False:
         mp = 0
    obj = {
        'name' : name,
        'mp' : mp,
        'rarity' : [grade, rarity],
        'effects' : {
            'mana boost': {'mp' : 1, 'focus' : 1},
        }
    }
    return obj

def healthDuct(dam, obj):
    hp = obj['hp']
    if hp - dam <= 0:
        print(f"{obj['name'].title()} has died!")
        return False
    else:
        obj['hp'] -= dam
        print(f"{obj['name']} takes {dam} damage!\n{obj['name']}'s health is now at {obj['hp']}")
        return True

def spellCasting(spellType,spell,obj):
    mana = obj['mana']
    mp = obj['mp']
    if spellType == 'atk':
        consump = obj['atk-spells'][spell]['mp']
    elif spellType == 'util':
        consump = obj['util-spells'][spell]['mp']
    if (mana-consump) < 0:
        print(f"{spell.title()} failed to cast!\nNot enough mana!")
        return False
    else:
        obj['mana'] = mana - consump
        print(f"{spell.title()} was successfuly cast!\nMana is now at {obj['mana']}/{obj['mp']}")
        return True

def fight(objOne, objTwo):
    spellsOne = [key for key in objOne['atk-spells']]
    spellsTwo = [key for key in objTwo['atk-spells']]
    print(f"A wild {objTwo['name']} has appeared! Fight!\n")
    while (objOne['hp'] > 0 and objTwo['hp'] > 0):
        input2 = input('would you like to use mana gather? (y/n): ')
        if str(input2) == 'n':
            input1 = int(input("Which spell do you select:\n 0 = first spell, 1 = second spell etc\n "))
            print()
            spell = spellsOne[input1]
            if spellCasting('atk',spell,objOne) == True:
                print(f"{objOne['name']} Uses {spell.title()}!")
                print()
                temp = objOne['atk-spells'][spell]['atk']
                if (healthDuct(temp, objTwo)) == False:
                    break
        else:
            if objOne['mana'] >= objOne['mp']:
                print('failed!\nMana Full!')
            else:
                objOne['mana'] += 30
                print(f"Mana is now at {objOne['mana']}/{objOne['mp']}")
        print()
        spell = spellsTwo[1]
        if spellCasting('atk',spell,objTwo) == True:
            print(f"{objTwo['name']} Uses {spell.title()}!")
            print()
            temp = objTwo['atk-spells'][spell]['atk']
            if (healthDuct(temp, objOne)) == False:
                break
        print()

    
    
addUtilSpell(mage1, 'spark', 2, 1)
stats(mage1)

mage2 = newMage('Rak', 50, 1)
stats(mage2)

mage3 = newMage('Promos', 200, 3)
stats(mage3)

addAtkSpell(mage2, 'tsunami', 400, 50)

obj1 = newObject('magic stick', 'common', '-')
fight(mage1, mage2)
game = True
while game:
    games = str(input(': '))
    if games.lower() == 'quit':
        break
    else:
        continue

    
