from classes.game import bcolors, person
from classes.magic import Spell

# Create black magic
fire = Spell("fire", 10, 100, "black")
thunder = Spell("thunder", 12, 110, "black")
blizzard = Spell("blizzard", 13, 120, "black")

# Create white magic
cure = Spell("cure", 12, 120, "white")
cura = Spell("cura", 18, 200, "white")

# Instantiate people
player = person(460, 65, 60, 35, [fire, thunder, blizzard, cure, cura])
enemy = person(1200, 65, 25, 20, [])

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print("===========")
    player.choose_action()
    choice = input("Choose action:")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg)
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose Magic:")) - 1

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(bcolors.FAIL + "\nNot enough MP!\n" + bcolors.ENDC)
            continue

        player.reduce_mp(spell.cost)

        if spell.type == "white":
            player.heal(magic_dmg)
            print(bcolors.OKGREEN + "\n" + spell.name + "heals for", str(magic_dmg), "HP." + bcolors.ENDC)
        elif spell.type == "black":
            enemy.take_damage(magic_dmg)
            print(bcolors.OKGREEN + "\n" + spell.name + "deals with", str(magic_dmg), "points of damage." + bcolors.ENDC)
        enemy.take_damage(magic_dmg)
        print(bcolors.OKBLUE + "\n" + spell.name + "\tdeals", str(magic_dmg), "points of damage" + bcolors.ENDC)

    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg)

    print("------------------------")
    print("Enemy HP:" + bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_maxhp()) + bcolors.ENDC + "\n")

    print("Your HP:" + bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_maxhp()) + bcolors.ENDC + "\n")
    print("Your MP:" + bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_maxmp()) + bcolors.ENDC + "\n")

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + bcolors.UNDERLINE + "YOU WIN!" + bcolors.ENDC)
        running = False

    elif player.get_hp() == 0:
        print(bcolors.FAIL + bcolors.UNDERLINE + "YOU GOT DEFEATED" + bcolors.ENDC)
        running = False










