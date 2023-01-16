from random import randint
from Monster.effect import *

class Attack_monster:
    def __init__(self, name, ad, effect, crit):
        self.name = name
        self.ad = ad
        self.effect = effect
        self.crit = crit

#—————————— apply effect ——————————

    def chance_apply_effect(self):
        apply = randint(1,10)
        if apply < 2 :
            return self.effect
        else :
            return 0
    
    def apply_effect(self):
        return self.effect

#—————————— apply dmg ——————————

    def chance_apply_dmg(self):
        apply = randint(1, 10)
        chance_crit = randint(1,10)
        if self.crit >= chance_crit and apply < 9:
            return self.ad * 2, f"inflige un coup critique de"
        elif apply < 9:
            return self.ad, f"inflige un coup de"
        else :
            return 0, ""

#—————————— apply dmg w/ high crit rate ——————————

    # def drain(self, target):
    #     self.hp += self.ad
    

#—————————— Attack FaceHuger ——————————

claw = Attack_monster("Claw", 5, Saignement, 2)
grip = Attack_monster("Grip", 7, None, 2)

#—————————— Attack ChestBuster ——————————

bite = Attack_monster("Bite", 5, None, 2)
tackle = Attack_monster("Tackle", 7, None, 2)

#—————————— Attack Mini boss : Runner ——————————
#faire le passif 
spit = Attack_monster("Spit", 0, Poison, 2)
fury_swipes = Attack_monster("Fury Swipes", 5*randint(1,5), None, 2) 

#—————————— Attack boss : Xénomorphe ——————————

spit = Attack_monster("Spit", 0, Poison, 2)
assault = Attack_monster("Assault", 10, None, 5)
#sting setup l'effet drain
fang = Attack_monster("Fang", 10, Saignement, 2)