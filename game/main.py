from characters.character import Character
from gears.armor import Armor
from gears.weapon import Weapon
from characters.barbarian import Barbarian
from characters.wizard import Wizard
from gears.spell import Spell
import inquirer

fireball_spell = Spell('Boule de feu', 50, 60)
lightning_spell = Spell('Tonerre', 45, 50)
windwall_spell = Spell("Mur d'air", 30, 30)

little_armor = Armor('armure partielle', 50)
mid_armor = Armor('armure moyenne', 75)
complete_armor = Armor('armure complète', 100)

sword_weapon = Weapon('Épée', 30)
pickaxe_weapon = Weapon('Pioche', 25)
fist_weapon = Weapon('Coup de poing', 20)

questions_fighter = [
    inquirer.List('choice_fighter',
                  message="Sélectionnez un personnage ",
                  choices=['Barbare (Attaque 2 fois)', 'Sorcier (utilise des sorts)', 'Quitter'],
              ),
]
questions_weapon = [
    inquirer.List('choice_weapon',
                  message="Sélectionnez une arme ",
                  choices=['Épée (30 dps)', 'Pioche (25 dps)', 'Coup de poing (20 dps)', 'Quitter'],
              ),
]
questions_armor = [
    inquirer.List('choice_armor',
                  message="Sélectionnez une armure ",
                  choices=['Armure légère (50 de défense)', 'Armure moyenne (75 de défense)', 'Armure complète (100 de défense)', 'Quitter'],
              ),
]
questions_fight = [
    inquirer.List('choice_fight',
                  message="Voulez-vous attaquer ? ",
                  choices=['Oui', 'Non', 'Quitter'],
              ),
]
questions_spell = [
    inquirer.List('choice_spell',
                  message="Sélectionnez un sort ",
                  choices=['Boule de feu (50 dps)', 'Tonerre (45 dps)', "Mur d'air (30 dps)", 'Quitter'],
              ),
]

armor_condition = False
weapon_condition = False
fight_condition = True
while fight_condition == True:
        answers = inquirer.prompt(questions_fighter)
        if answers['choice_fighter'] == 'Barbare (Attaque 2 fois)' or answers['choice_fighter'] == 'Sorcier (utilise des sorts)':
            if answers['choice_fighter'] == "Barbare (Attaque 2 fois)":
                answers = inquirer.prompt(questions_weapon)
                user_weapon = None
                weapon_condition = True

                if answers['choice_weapon'] == 'Épée (30 dps)':
                    user_weapon = sword_weapon
                elif answers['choice_weapon'] == 'Pioche (25 dps)':
                    user_weapon = pickaxe_weapon
                elif answers['choice_weapon'] == 'Coup de poing (20 dps)':
                    user_weapon = fist_weapon
                else:
                    weapon_condition = False

                answers = inquirer.prompt(questions_armor)
                user_armor = None
                armor_condition = True

                if answers['choice_armor'] == "Armure légère (50 de défense)":
                    user_armor = little_armor
                elif answers['choice_armor'] == "Armure moyenne (75 de défense)":
                    user_armor = mid_armor
                elif answers['choice_armor'] == "Armure complète (100 de défense)":
                    user_armor = complete_armor
                else:
                    armor_condition = False

                jane = Barbarian("Jane", user_armor, user_weapon, 120, user_armor.defense)

            else:
                answers = inquirer.prompt(questions_spell)
                user_spell = None
                weapon_condition = True
                if answers['choice_spell'] == 'Boule de feu (50 dps)':
                    user_spell = fireball_spell
                elif answers['choice_spell'] == 'Tonerre (45 dps)':
                    user_spell = lightning_spell
                elif answers['choice_spell'] == "Mur d'air (30 dps)":
                    user_spell = windwall_spell
                else:
                    weapon_condition = False
                answers = inquirer.prompt(questions_armor)
                user_armor = None
                armor_condition = True

                if answers['choice_armor'] == "Armure légère (50 de défense)":
                    user_armor = little_armor
                elif answers['choice_armor'] == "Armure moyenne (75 de défense)":
                    user_armor = mid_armor
                elif answers['choice_armor'] == "Armure complète (100 de défense)":
                    user_armor = complete_armor
                else:
                    armor_condition = False

                jane = Wizard("Jane", user_armor, user_spell, 75, user_armor.defense, fist_weapon, 20)

            john = Character("John", mid_armor, pickaxe_weapon, 100, mid_armor.defense)
            attack_type = True

            if isinstance(jane, Barbarian):
                if armor_condition and weapon_condition:
                        print(f'\nVous avez choisi : \n{user_weapon.name} pour attaquer et une {user_armor.name} qui a {user_armor.defense} de défense pour vous protéger')
                        print(f"\nVotre {user_weapon.name} inflige : \n{user_weapon.damage} de dégâts et l'{user_armor.name} de votre adversaire a {john.defense} de défense")
                else:
                    print("Vous n'avez pas choisi d'équipement valide")
            else:
                    if isinstance(jane, Wizard): 
                        print(f'\nVous avez : \n un bâton qui inflige 20 de dégâts, un sort {user_spell.name} qui inflige {user_spell.damage} de dégâts, une {user_armor.name} qui a {user_armor.defense} de défense pour vous protéger')
                        print(f"\nVotre adversaire a {john.hp} de vie et {john.defense} de défense")
                    else:
                        print("Vous n'avez pas choisi d'équipement valide")


            if isinstance(jane, Barbarian): 
                print("\nVous avez la classe Barbare. Vous attaquez deux fois d'affilée !")
            elif isinstance(jane, Wizard): 
                print("\nVous avez la classe Sorcier. Vous avez des sorts.")
                
            attack_type = True
            while attack_type == True:
                answers = inquirer.prompt(questions_fight)
                if answers['choice_fight'] == 'Oui':
                    jane.attack(john)
                    if john.hp > 0:
                        print("-------------------------------")
                        print("Résultats : ")
                        print(john.name, "a", john.hp, "PV et",  john.armor.defense, 'de défense')
                        print(jane.name, 'a', jane.hp, "PV et", jane.armor.defense, 'de défense')
                        print("-------------------------------")
                    else : 
                        print("Vous avez vaincu votre adversaire (il est mort)")
                        attack_type = False
                        fight_condition = False
                elif answers['choice_fight'] == 'Non':
                    print("--------------------------------")
                    print("Résultats finaux : ")
                    print(john.name, "a", john.hp, "PV et",  john.armor.defense, 'de défense')
                    print(jane.name, 'a', jane.hp, "PV et", jane.armor.defense, 'de défense')
                    print("--------------------------------")
                    attack_type = False
                    fight_condition = False
                else :
                        print("Vous n'avez pas choisi d'action valide")
                        attack_type = False
                        fight_condition = False
        else:
            print("Au revoir !")
            break
