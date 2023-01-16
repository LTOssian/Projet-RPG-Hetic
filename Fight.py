from Monster.Attack_Monster import *
from Monster.Boss import *
from Monster.Chest_buster import *
from Monster.Monster import * 
from Monster.effect import *
from player import *
from weapons import weapon_data

class Combat:
    def __init__(self, player, monster):
        self.player = player
        self.monster = monster
    
    def draw(self):
        print ("\n-----------------\n")

    def fight(self):
        while self.player.alive or self.monster.alive:

                #———————— check if player and monster are alive  ————————
                self.player.update_alive()
                self.monster.update_alive()
                if self.player.status :
                    self.player.hp -= Effect(self.player.status).damage_tick
                    print("\n", self.player.name, "perd:", Effect(self.player.status).damage_tick, "à cause de", self.player.status, "il vous reste ", self.player.hp, "hp")

                if self.monster.status :
                    self.monster.hp -= Effect(self.monster.status).damage_tick
                    print("\n", self.monster.name, "perd:", Effect(self.monster.status).damage_tick, "à cause de", self.monster.status, "il reste ", self.monster.hp, "hp")

                self.player.update_alive()
                self.monster.update_alive()
                state = 0
                count_item_use = 0


                #———————— print hp player, monster ————————
                self.draw()
                print(self.player.name, "à", self.player.hp, "hp")
                print(self.monster.name, 'à', self.monster.hp, "hp")

                #———————— if player alive, ask what to do ————————
                self.draw()
                if self.player.alive and state == 0:
                    count_item_use = 0
                    print("1. Attaque | 2. Utiliser un item | 3. Changer d'arme\n")
                    choose = input("Que voulez vous faire ?\n")
                    print("\n")

                    #———————— repeat until good input to do ————————

                    while choose != "1" and choose != "2" and choose != "3":

                        choose = input("Que voulez vous faire ?\n")
                    #———————— player attack ————————
                    if choose == "1" :
                        self.player.use_weapon(self.monster)
                        state = 1
                    
                    #———————— player use item ————————

                    elif choose == "2" :
                        if self.player.item_turn == 0:
                            self.player.choose_item(self.player)
                            self.player.item_turn = 1
                            state = 0
                        else:
                            print("Vous avez déjà utilisé l'inventaire ce tour-ci. Patience.")

                    #———————— player change weapon ————————    

                    elif choose == "3" :
                        print(self.player.current_weapon[0],"\n")
                        self.player.change_weapon()
                        print("Vous changez d'armes pour:", self.player.current_weapon[0])

                        state == 0

                #———————— player dead ———————— 

                elif self.player.alive == False:
                    print(self.player.name, "est mort")
                    return False

                #———————— check if player and monster are alive  ————————

                self.player.update_alive()
                self.monster.update_alive()

                #———————— if monster alive, attack  ————————

                if self.monster.alive and state == 1:
                    self.monster.use_attack(self.player)
                    state = 1
                    self.player.item_turn = 0

                #———————— monster dead ———————— 

                elif self.monster.alive == False:
                    print(self.monster.name, "est mort\n")
                    self.monster.drop_item(self.player)
                    print("Vous gagnez:", self.monster.gxp,'xp')
                    self.player.get_xp(self.monster.gxp)
                    print("Vous avez actuellement:", self.player.current_xp, "xp /", self.player.xp_to_next_lvl)
                    self.player.item_turn = 0
                    return True