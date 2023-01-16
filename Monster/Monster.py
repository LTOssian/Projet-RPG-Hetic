from Monster.Attack_Monster import *
from Monster.effect import *
from consommables import Consommables
import random
from player import *



class Monster:
    def __init__(self, name, level, inventory = {}, attack_list = []):
        self.name = name 
        self.level = level
        self.ad = level * 3 
        self.defense = 0
        self.hp = level * 5
        self.gxp = 0
        self.inventory = inventory
        self.attack_list = attack_list
        self.status = None
        self.alive = True
        self.can_attack = True

#—————————— gxp / level ——————————

        if self.level < 4:
            self.gxp = 30
        elif self.level <= 6 and self.level >= 4 :
            self.gxp = 50
        elif self.level == 8 or self.level == 7:
            self.gxp = 70
        elif self.level == 9:
            self.gxp = 90
        elif self.level == 10:
            self.gxp = 110

#—————————— attack player ——————————

    def use_attack(self, target):
        attack = random.choice(self.attack_list)
        dmg, text = attack.chance_apply_dmg()

        if dmg : # comme sidmg = 1 (vrai)
            dmg += self.ad
            dmg -= target.defense
            print(self.name, text,dmg, "à", target.name)
            target.hp -= dmg
        else :
            print(self.name, "rate son attaque")
        #—————————— apply effect ——————————

            effect = attack.chance_apply_effect()
            if effect :
                print("Inflige", effect.name)
                target.status = effect.name
        return target.hp, target.status


#—————————— drop item ——————————
    def drop_item(self, target):
        if self.alive == False and self.inventory:
            for name, data in self.inventory.items():
                target.add_item([name, data])
                print(f"\n{target.name} récupère {name} sur le {self.name}.")



    #—————————— get status ——————————
    def get_status(self):
        return self.status

    # ———————————————— Alive ————————————————
    def update_alive(self):
        if self.hp <= 0:
            self.alive = False


face_hugger_SAS_11 = Monster("Face Hugger", 1, {'Kit de secours': Consommables('Kit de secours (+HP)', 5)}, [claw,grip])
face_hugger_SAS_22 = Monster("Face Hugger", 2, {'Bandage': Consommables('Bandage (-SAI)', 0, Effect('SAI'))}, [claw,grip])
chest_buster_SAS_13 = Monster("Chest Buster", 3, {'Kit de secours': Consommables('Kit de secours (+HP)', 5)}, [tackle])
face_hugger_SAS_04 = Monster("Face Hugger", 4, {'Orangina' : Consommables('Orangina (+AD)', 0, None, "ad")}, [claw,grip])
face_hugger_SAS_14 = Monster("Face Hugger", 5, {'Kit de secours 2': Consommables('Kit de secours (+HP)', 10)}, [claw,grip])
chest_buster_SAS_06 = Monster("Chest Buster", 6, {'Morphine' : Consommables('Morphine (-DEF)', 0, None, "defense")}, [bite,tackle])
face_hugger_SAS_15 = Monster("Face Hugger", 7, {'Kit de secours 3': Consommables('Kit de secours (+HP)', 20)}, [claw,grip])
Runner_SAS_23 = Monster("Runner", 8, {'Pomme dorée': Consommables('Pomme dorée', 10, Effect('PSN'), "defense")}, [spit,fury_swipes])
Xenomorph_SAS_16 = Monster("Xenomorph", 11, {}, [spit, assault, fang])