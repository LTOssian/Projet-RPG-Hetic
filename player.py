
from weapons import weapon_data, Effect
from consommables import consommables_data

class Player:
    def __init__(self, name,level):
        self.name = name
        self.level = level
        self.hp = 5
        self.ad = 3
        self.defense = 2 
        self.status = None
        self.alive = True
        self.can_attack = True

        self.inventory = {
                "weapons" : [['Poing', {'damage': 2, 'effect': Effect("SAI")}]],
                "consommables" : []
            }

        self.current_weapon = self.inventory["weapons"][0]
        self.xp_to_next_lvl = 5 * self.level
        self.current_xp = 0
        self.current_item = None
        self.item_turn = 0

# ———————————————————————— Leveling ————————————————————————
    def level_up(self):
        self.level += 1
        print(f"{self.name} passe au niveau {self.level}. Vos stats sont mises à jour.")

    def update_stat(self):
        self.ad = self.level * 4
        self.hp = self.level * 5
        self.defense = self.level * 2
        self.xp_to_next_lvl += self.level * 5

    def get_xp(self, target_gxp):
        self.current_xp += target_gxp
        self.recursion()

    def recursion(self):
        if self.current_xp >= self.xp_to_next_lvl:
            self.current_xp -= self.xp_to_next_lvl
            self.level_up()
            self.update_stat()
            self.recursion()

# ———————————————————————— Weapon management ————————————————————————

    def get_current_weapon(self):
        return self.current_weapon

    def use_weapon(self, target):
        print(f"----- Arme actuelle de {self.name} : -----")
        print(self.current_weapon[0],"\n")
        weapon_damage = self.current_weapon[1]['damage'] + self.ad - target.defense
        if self.current_weapon[1]['effect']:
            announce, effect_damage = self.current_weapon[1]['effect'].use_effect(target)
            
        else:
            effect_damage = 0
        print(self.name, "inflige", weapon_damage, "à", target.name)        
        target.hp -= weapon_damage + effect_damage 

    def change_weapon(self):
        self.show_weapon()
        n_weapons = len(self.inventory["weapons"])
        print(f"\nVous avez actuellement {n_weapons} armes\n")
        weapon_choice = int(input("Quelle arme voulez vous équiper ? (utiliser l'index)\n"))
        while type(weapon_choice) != int or weapon_choice > n_weapons - 1:
            weapon_choice = int(input("Quelle arme voulez vous équiper ? (utiliser l'index)\n"))
        if weapon_choice > n_weapons - 1 or weapon_choice < 0:
            self.change_weapon(self)
        else:
            self.current_weapon = self.inventory["weapons"][weapon_choice]

# ———————————————————————— Item management ————————————————————————
    def draw(self):
        print ("\n-----------------\n")

    def add_item(self):
        self.inventory["items"].append()
    
    def remove_item(self, target):
        self.inventory["items"].remove(target)
    
    def choose_item(self, player):
        self.show_conso()
        n_items = len(self.inventory["consommables"])
        if not n_items:
            print("Vous n\'avez aucun item à utiliser")
            return
        print(f"\nVous avez actuellement {n_items} consommables\n")
        print ("----- Utilisation consommable -----\n")
        item_choice = int(input("Quel consommable voulez vous utiliser ? (utiliser l'index)\n"))
        while type(item_choice) != int or item_choice > n_items - 1:
            item_choice = int(input("Quel consommable voulez vous utiliser ? (utiliser l'index)\n"))
        if item_choice > n_items - 1 or item_choice < 0:
            self.choose_item(self)
        else:
            self.current_item = self.inventory["consommables"][item_choice][1]
            self.current_item.use_item(player)
            removed_item = self.inventory['consommables'].pop(item_choice)
            print(f"Le {removed_item[0]} se consume.")
            
    def show_inventory(self):
        print(f"Inventaire de {self.name}:")
        
        for weapon, data in self.inventory['weapons']:
            text = f"{weapon} : "
            text += f"Dégats = {data['damage']}, "
            if data['effect']:
                text += f"Effect = {data['effect'].name} "
            print(text)
        for conso, data in self.inventory['consommables']:
            text = f"{conso} : "
            if data.heal:
                text += f"Soin = {data.heal}, "
            if data.effect_to_debuff:
                text += f"Debuff = {data.effect_to_debuff.name}"
            if data.stat_boost:
                text += f"Boost de stat = {data.stat_boost}"
            print(text)
    
    def show_conso(self):
        print("\n ----- Inventaire des consommables -----\n")
        count = 0
        for conso, data in self.inventory['consommables']:
            text = f"[{count}] {conso} : "
            if data.heal:
                text += f"Soin = {data.heal}, "
            if data.effect_to_debuff:
                text += f"Debuff = {data.effect_to_debuff.name}"
            if data.stat_boost:
                text += f"Boost de stat = {data.stat_boost}"
            print(text)
            count += 1

    def show_weapon(self):
        print("\n ----- Inventaire des armes -----\n")
        count = 0
        for weapon, data in self.inventory['weapons']:
            text = f"[{count}] {weapon} : "
            text += f"Dégats = {data['damage']}, "
            if data['effect']:
                text += f"Effect = {data['effect'].name} "
            print(text)
            count += 1
                
# ———————————————————————— Alive ————————————————————————

    def update_alive(self):
        if self.hp <= 0:
            self.alive = False

    def update_inventory(self, status):
        self.inventory = {
            "weapons" : [[weapon, data] for weapon, data in weapon_data[status].items()],
            "consommables" : [[items, data] for items, data in consommables_data[status].items()]
        }

    def add_weapon(self, weapon):
        self.inventory["weapons"].append(weapon) #item sous la forme
    def add_item(self, item):
        self.inventory["consommables"].append(item)


player = Player('Ellen Ripley', 1)