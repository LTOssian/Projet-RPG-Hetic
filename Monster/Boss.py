from Monster.Monster import *
from Monster.Attack_Monster import *

class Boss(Monster):
    def __init__(self, name, ad, level, defense, hp, gxp, inventory = [], attack_list = []):
        super().__init__(name,level)
        self.name = name 
        self.ad = ad
        self.defense = defense 
        self.hp = hp 
        self.inventory = inventory
        self.attack_list = attack_list
        self.gxp = gxp
        self.status = None
        self.alive = True
        self.can_attack = True




