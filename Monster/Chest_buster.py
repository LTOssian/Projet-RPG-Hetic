from Monster.Attack_Monster import *
from Monster.Monster import *

class Chest_buster(Monster):
    def __init__(self, name, level, inventory = [], attack_list = []):
        self.name = name 
        self.level = level
        self.ad = level * 5
        self.defense = 0
        self.hp = level * 8
        self.gxp = 0
        self.inventory = inventory
        self.attack_list = attack_list
        self.statement = None





chest_buster = Monster("Chest Buster", 5, ["x"], [bite, tackle])
