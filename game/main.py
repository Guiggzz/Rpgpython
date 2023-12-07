from gears.armor import armor
from gears.weapon import Weapon
from characters.character import Character

little_armor = armor('armure partielle', 50)
mid_armor = armor('armure moyenne', 75)
complete_armor = armor('armure partielle', 100)

sword_weapon = Weapon('Epée', 30)
pickaxe_weapon = Weapon('Pioche', 25)
fist_weapon = Weapon('Coup de poing', 20)

armor_choose = input("Quelle armure souhaitez-vous équiper 1, 2, 3 ? (1 : armure partielle, 2 : armure moyenne, 3 : armure complète) : ")
user_armor = ''
equipment_condition = False

if armor_choose == "1":
    user_armor = little_armor
    equipment_condition = True
elif armor_choose == "2":
    user_armor = mid_armor
    equipment_condition = True
elif armor_choose == "3":
    user_armor = complete_armor
    equipment_condition = True
else: 
    print("Vous n'aver pas choisi d'armure")


weapon_choose = input("Quelle arme souhaitez-vous équiper 1, 2, 3 ? (1 : Epée, 2 : Pioche, 3 : Coup de poing) : ")
user_weapon = ''

if armor_choose == "1":
    user_weapon = sword_weapon
    equipment_condition = True
elif armor_choose == "2":
    user_weapon = pickaxe_weapon
    equipment_condition = True
elif armor_choose == "3":
    user_weapon = fist_weapon
    equipment_condition = True
else: 
    print("Vous n'aver pas choisi d'armure")


if equipment_condition == True:
    print(f"Vous avez une {user_weapon.name} et elle met {user_weapon.damage} de points de dégat")
    print(f"Vous avez une {user_armor.name} et elle a {user_armor.defense} de points de défense")


jane = Character("Jane", armor_choose, weapon_choose, 120)
john = Character("John", armor_choose, weapon_choose, 100)

john.attack(jane)
print("Results: ")
print(john.name, john.hp, "HP")
print(jane.name, jane.hp, "HP")
input("------------------")

