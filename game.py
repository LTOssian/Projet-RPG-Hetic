import arcade
from player import *
from Fight import *
from Monster import *

#Canva
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 960
SCREEN_TITLE = "Alien : Escape spaceship n°58008"

#Regarde les mouvement du joueur
RIGHT_FACING = 0
LEFT_FACING = 1
UP_FACING = 2
DOWN_FACING = 3

#Nom du joueur
LAYER_NAME_PLAYER = "ELLEN RIPLEY"

#Joueur | Taille
CHARACTER_SCALING = 0.65
TILE_SCALING = 1

#Joueur | Vitesse
PLAYER_MOVEMENT_SPEED =  5

class Terminal():
    def __init__(self, nb_sautligne):
        self.nb_sdl = nb_sautligne

    def sdl(self):
        for i in range (0,self.nb_sdl,1):
            print("\n")
            print("----------------------")
            print("\n")

#Les maps
class Rooms:
    #Initialiser les rooms
    def __init__(self, r_link, r_name, r_next):
        self.room_link = r_link
        self.room_name = r_name
        self.room_next = r_next
    #Ajouter les rooms adjacent à self.room_next
    def add_next_room(self, list_room):
        for i in range(0,len(list_room),1):
            self.room_next.append(list_room[i])

#La direction où regarde le sprite du joueur
class PlayerCharacter(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.character_face_direction = DOWN_FACING
        self.cur_texture = 0
        self.scale = CHARACTER_SCALING
        main_path = "sprites/player/"
       
        #Animation Up
        self.idle_u_texture_pair = []
        for i in range(4):
            texture = arcade.load_texture(f"{main_path}up/ellen_ripley_u_{i}.png")
            self.idle_u_texture_pair.append(texture)

        #Animation Right
        self.idle_r_texture_pair = []
        for i in range(4):
            texture = arcade.load_texture(f"{main_path}right/ellen_ripley_r_{i}.png")
            self.idle_r_texture_pair.append(texture)
        
        #Animation Down
        self.idle_d_texture_pair = []
        for i in range(4):
            texture = arcade.load_texture(f"{main_path}down/ellen_ripley_d_{i}.png")
            self.idle_d_texture_pair.append(texture)
        
        #Animation Left
        self.idle_l_texture_pair = []
        for i in range(4):
            texture = arcade.load_texture(f"{main_path}left/ellen_ripley_l_{i}.png")
            self.idle_l_texture_pair.append(texture)

        self.texture = self.idle_d_texture_pair[0]
        self.hit_box = self.texture.hit_box_points


    def update_animation(self, delta_time: float = 1 / 60):
        # Figure out if we need to flip face left or right
        if self.change_x < 0 and self.character_face_direction != LEFT_FACING:
            self.character_face_direction = LEFT_FACING
        elif self.change_x > 0 and self.character_face_direction != RIGHT_FACING:
            self.character_face_direction = RIGHT_FACING
        if self.change_y < 0 and self.character_face_direction != DOWN_FACING:
            self.character_face_direction = DOWN_FACING
        elif self.change_y > 0 and self.character_face_direction != UP_FACING:
            self.character_face_direction = UP_FACING
        
        #Ne pas animer si aucun mouvement
        if self.change_x == 0 and self.change_y == 0:
            if self.character_face_direction == 2:
                self.texture = self.idle_u_texture_pair[0]
            elif self.character_face_direction == 0:
                self.texture = self.idle_r_texture_pair[0]
            elif self.character_face_direction == 3:
                self.texture = self.idle_d_texture_pair[0]
            elif self.character_face_direction == 1:
                self.texture = self.idle_l_texture_pair[0]
            self.cur_texture = 0
            return
        
        if self.change_x < 0:
            self.cur_texture += 1
            if self.cur_texture > 3:
                self.cur_texture = 0
            self.texture = self.idle_l_texture_pair[self.cur_texture]
            self.hit_box = self.texture.hit_box_points
        elif self.change_x > 0:
            self.cur_texture += 1
            if self.cur_texture > 3:
                self.cur_texture = 0
            self.texture = self.idle_r_texture_pair[self.cur_texture]
            self.hit_box = self.texture.hit_box_points
        
        if self.change_y < 0:
            self.cur_texture += 1
            if self.cur_texture > 3:
                self.cur_texture = 0
            self.texture = self.idle_d_texture_pair[self.cur_texture]
            self.hit_box = self.texture.hit_box_points
        elif self.change_y > 0:
            self.cur_texture += 1
            if self.cur_texture > 3:
                self.cur_texture = 0
            self.texture = self.idle_u_texture_pair[self.cur_texture]
            self.hit_box = self.texture.hit_box_points

#——————————————— FIN SCREEN ——————————————— 

class Fin(arcade.View):
    def on_show(self):
            self.texture = arcade.load_texture('interface/ingame/fin.png')
            arcade.set_viewport(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT - 1)

    def setup(self):
        pass
    
    def on_draw(self):
        arcade.start_render()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT)

    # ——————— go back to title screen ———————   

    def on_key_press(self, key, modifiers): 
        if key == arcade.key.ENTER:
            Terminal(1).sdl()
            print("Merci d'avoir joué")
            Terminal(1).sdl()
            arcade.exit()

#——————————————— FIN ALT SCREEN ——————————————— 

class Fin_alt(arcade.View):
    def on_show(self):
            self.texture = arcade.load_texture('interface/ingame/fin_alt.png')
            arcade.set_viewport(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT - 1)

    def setup(self):
        pass
    
    def on_draw(self):
        arcade.start_render()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT)

    # ——————— go back to title screen ———————   

    def on_key_press(self, key, modifiers): 
        if key == arcade.key.ENTER:
            Terminal(1).sdl()
            print("Merci d'avoir joué")
            Terminal(1).sdl()
            arcade.exit()

#——————————————— GAME OVER ——————————————— 

class GameOver(arcade.View):
    def on_show(self):
            self.texture = arcade.load_texture('interface/ingame/gameover.png')
            arcade.set_viewport(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT - 1)

    def setup(self):
        pass
    
    def on_draw(self):
        arcade.start_render()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT)

    # ——————— go back to title screen ———————   

    def on_key_press(self, key, modifiers): 
        if key == arcade.key.ENTER:
            Terminal(1).sdl()
            print("Relancer le jeu pour une seconde chance")
            Terminal(1).sdl()
            arcade.exit()
            
#Le jeu
# class arcade.Sound(file_name: Union[str, pathlib.Path], streaming: bool = False)
class MyGame(arcade.View):
    def __init__(self):
        #Initialiser la fenêtre
        super().__init__()
        #Initialiser les variables
        self.background = None
        self.tile_map = None
        self.scene = None
        self.player = None
        self.physics_engine = None
        self.contgen = 0
        self.load_audio_background = None
        self.audio_background = None
        self.background_music_playing = 0
        self.load_sound_effect = arcade.load_sound("music/succes-sound-effect.wav")
        self.sound_effect = None
        self.player_fight = player
        self.combat_1 = 0
        self.combat_2 = 0
        self.combat_3 = 0
        self.combat_4 = 0
        self.combat_5 = 0
        self.combat_6 = 0
        self.combat_7 = 0
        self.combat_8 = 0
        self.combat_9 = 0

        #Les items à recup 
        self.coffre_1 = weapon_data["SAS-10-1"]
        self.coffre_2 = weapon_data["SAS-03"]
        self.coffre_3 = weapon_data["SAS-14"]
        self.coffre_4 = weapon_data["SAS-05"]
        self.coffre_5 = weapon_data["SAS-23"]

        self.coffre_list = [
            self.coffre_1,
            self.coffre_2,
            self.coffre_3,
            self.coffre_4,
            self.coffre_5
        ]

        #Background de la map
        arcade.set_background_color(arcade.csscolor.BLACK)

        #Initialiser les touches
        self.up_pressed = False
        self.left_pressed = False
        self.down_pressed = False
        self.right_pressed = False
        self.lshift_pressed = False
        
    def setup(self, room, posx, posy):
        #Charger l'image de fond
        self.background = arcade.load_texture("maps/star_background.jpeg")
        #Charger la première map
        self.room = room
        self.map_name = self.room.room_link

        #Charger les musique suivant les maps
        #Si aucune musique de charger (au start)
        if self.load_audio_background == None:
            self.load_audio_background = arcade.load_sound("music/background-music.wav")
            self.audio_background = arcade.play_sound(self.load_audio_background,1.0,-1,True)
            self.background_music_playing = 1
        #Musique de combat finale
        elif self.room.room_name == "SAS-16-1":
            arcade.stop_sound(self.audio_background)
            self.load_audio_background = arcade.load_sound("music/fight-music.wav")
            self.audio_background = arcade.play_sound(self.load_audio_background,1.0,-1,True)
            self.background_music_playing = 0
        #Musique de fin
        elif self.room.room_name == "SAS-17" or self.room.room_name == "SAS-10-2":
            arcade.stop_sound(self.audio_background)
            self.load_audio_background = arcade.load_sound("music/end-music.wav")
            self.audio_background = arcade.play_sound(self.load_audio_background,1.0,-1,True)
            self.background_music_playing = 0
        #Si la musique de fond déjà chargé
        elif self.background_music_playing == 1:
            pass
        #Musique de fond après une autre musique
        else:
            arcade.stop_sound(self.audio_background)
            self.load_audio_background = arcade.load_sound("music/background-music.wav")
            self.audio_background = arcade.play_sound(self.load_audio_background,1.0,-1,True)
            self.background_music_playing = 1

        #Définir le calque "Collisions" des map Tiled
        layer_options = {"Collisions": {"use_spatial_hash": True,},}

        #Lire la map Tiled
        self.tile_map = arcade.load_tilemap(self.map_name, TILE_SCALING, layer_options)
        
        #Lire et initialiser la Tiled map et les calques la composant
        self.scene = arcade.Scene.from_tilemap(self.tile_map)

        #Initialisation du personnages Joueur
        self.player = PlayerCharacter()
        #Position du player X/Y
        self.player.center_x = posx
        self.player.center_y = posy
        #Ajout du player à la scène
        self.scene.add_sprite(LAYER_NAME_PLAYER, self.player) 

        #Ajouter les collisions
        self.physics_engine = arcade.PhysicsEngineSimple(self.player, walls=self.scene["Collisions"])

    def player_movement(self):
        #Initialiser les valeurs de player_movement
        self.player.change_x = 0
        self.player.change_y = 0
        speed_value = 2

        #Recevoir et renvoyer les mouvements du Joueur
        if self.lshift_pressed == False:
            if self.left_pressed and not self.right_pressed:
                self.player.change_x = -PLAYER_MOVEMENT_SPEED
            elif self.right_pressed and not self.left_pressed:
                self.player.change_x = PLAYER_MOVEMENT_SPEED
            if self.up_pressed and not self.down_pressed:
                self.player.change_y = PLAYER_MOVEMENT_SPEED
            elif self.down_pressed and not self.up_pressed:
                self.player.change_y = -PLAYER_MOVEMENT_SPEED
        else:
            if self.left_pressed and not self.right_pressed:
                self.player.change_x =  -PLAYER_MOVEMENT_SPEED - speed_value
            elif self.right_pressed and not self.left_pressed:
                self.player.change_x =  PLAYER_MOVEMENT_SPEED + speed_value
            if self.up_pressed and not self.down_pressed:
                self.player.change_y =  PLAYER_MOVEMENT_SPEED + speed_value
            elif self.down_pressed and not self.up_pressed:
                self.player.change_y =  -PLAYER_MOVEMENT_SPEED - speed_value

    def on_draw(self):
        #Clear la scène
        self.clear()
        #Dessiner l'image de background
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        #Dessiner la scène
        self.scene.draw()

    def check_pos(self, pos_x_max, pos_x_min, pos_y_min):
        player_x = self.player.center_x 
        player_y = self.player.center_y 
        if player_x > pos_x_min and player_x < pos_x_max and player_y > pos_y_min - 30:
            return True
        else:
            return False

    def get_coffre(self, n_coffre, room, pos_x, pos_y, intervalle):
        if room == self.room.room_name and self.coffre_list[n_coffre] and self.check_pos(pos_x + intervalle, pos_x, pos_y):
            Terminal(1).sdl()
            for name, data in self.coffre_list[n_coffre].items():
                self.player_fight.add_weapon([name, data])
                print(f"Vous venez de trouver {name}")
            Terminal(1).sdl()
            self.coffre_list[n_coffre] = False
            return True
        else:
            return False
    
    def get_kits(self, gen_room):
        print(f"Vous avez trouvé des objets près du générateur...")
        print(f"Votre inventaire est mis à jour. Faites (i)")
        Terminal(1).sdl()
        for name, data in weapon_data[gen_room].items():
            self.player_fight.add_weapon([name, data])
        for name, data in consommables_data[gen_room].items():
            self.player_fight.add_item([name, data])
            

    def on_key_press(self, key, modifiers):
        #Définir touches analysées si pressées
        if key == arcade.key.UP or key == arcade.key.Z:
            self.up_pressed = True
            self.player_movement()
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.down_pressed = True
            self.player_movement()
        elif key == arcade.key.LEFT or key == arcade.key.Q:
            self.left_pressed = True
            self.player_movement()
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = True
            self.player_movement()
        
        #Sprint
        if key == arcade.key.LSHIFT:
            self.lshift_pressed = True
            self.player_movement()
     
        #TEMP DONNER LA POSITION
        if key == arcade.key.P:
            print(f'X : {self.player.center_x} | Y : {self.player.center_y}')

        #Intéractions inventaire
        if key == arcade.key.I:
            self.player_fight.show_weapon()
            self.player_fight.show_conso()

        #Intéractions items et générateurs
        if key == arcade.key.E:

            #tous les items à trouver
            if self.get_coffre(0, 'SAS-10-1', 645, 562, 30):
                return
            if self.get_coffre(1, "SAS-03", 480, 402, 30):
                return
            if self.get_coffre(2, "SAS-14", 320, 435, 30):
                return
            if self.get_coffre(3, "SAS-05", 445, 402, 30):
                return
            if self.get_coffre(4, "SAS-23", 420, 238, 100):
                return


            #EASTER EGG | Lance flamme
            if self.room.room_name == "SAS-04" and self.player.center_y < 401 and self.player.center_x > 450 and self.player.center_x < 470:
                room_03.room_next[0] = room_13_v2
                room_14.room_next[3] = room_13_v2
                Terminal(1).sdl()
                print("Vous entendez un bruit anormal...")
                Terminal(1).sdl()
                self.load_sound_effect = arcade.load_sound("music/easter-egg-sound.wav")
                self.sound_effect = arcade.play_sound(self.load_sound_effect,0.5,-1,False)
                self.load_sound_effect = arcade.load_sound("music/succes-sound-effect.wav")

            #EASTER EGG | Fuite
            elif self.room.room_name == "SAS-10-1" and self.player.center_y > 463 and self.player.center_y < 496 and self.player.center_x > 75 and self.player.center_x < 90:
                self.setup(room_10_v2, 268, 483)
                Terminal(1).sdl()
                print("Vous avez trouvé la fin alternative. Bravo!")
                Terminal(1).sdl()
                start_view = Fin_alt()
                self.window.show_view(start_view)
                start_view.setup()

            #Générateur n°1
            elif self.room.room_name == "SAS-22-1" and self.player.center_y > 170:
                self.contgen = self.contgen + 1
                self.sound_effect = arcade.play_sound(self.load_sound_effect,0.5,-1,False)
                Terminal(1).sdl()
                print(f"Vous avez allumé {self.contgen}/3 générateur")
                self.get_kits("SAS-22-1")
                self.setup(room_22_v2, self.player.center_x, self.player.center_y)
                room_11.room_next[1] = room_12_v2

            #Générateur n°2
            elif self.room.room_name == "SAS-24-1" and self.player.center_y > 170:
                self.contgen = self.contgen + 1
                self.sound_effect = arcade.play_sound(self.load_sound_effect,0.5,-1,False)
                Terminal(1).sdl()
                print(f"Vous avez allumé {self.contgen}/3 générateur")
                self.get_kits('SAS-24-1')
                self.setup(room_24_v2, self.player.center_x, self.player.center_y)
                room_14.room_next[0] = room_24_v2

            #Générateur n°3
            elif self.room.room_name == "SAS-06-1" and self.player.center_y > 590 and self.player.center_x >= 460 and self.player.center_x <= 500:
                self.contgen = self.contgen + 1
                self.sound_effect = arcade.play_sound(self.load_sound_effect,0.5,-1,False)
                Terminal(1).sdl()
                print(f"Vous avez allumé {self.contgen}/3 générateur")
                self.get_kits('SAS-06-1')

                self.setup(room_06_v2, self.player.center_x, self.player.center_y)
                room_05.room_next[1] = room_06_v2

            #Aucune interaction
            else:
                print("Il n'y a rien ici")

            if self.contgen == 3:
                room_14.room_next[1] = room_15_v2
                room_05.room_next[0] = room_15_v2

    def on_key_release(self, key, modifiers):
        #Définir touches analysées si relâchées
        if key == arcade.key.UP or key == arcade.key.Z:
            self.up_pressed = False
            self.player_movement()
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.down_pressed = False
            self.player_movement()
        elif key == arcade.key.LEFT or key == arcade.key.Q:
            self.left_pressed = False
            self.player_movement()
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = False
            self.player_movement()
        
        #Sprint
        if key == arcade.key.LSHIFT:
            self.lshift_pressed = False
            self.player_movement()

    def on_update(self, delta_time):
        #Déplacer le joueur en temps réel
        self.physics_engine.update()

        self.scene.update_animation(
            delta_time, [LAYER_NAME_PLAYER]
        )

        #Changement de map
        if self.player.center_y > SCREEN_HEIGHT:
            self.setup(self.room.room_next[0], 480, 10)
        elif self.player.center_x > SCREEN_WIDTH:
            if self.room.room_next[1].room_name == "SAS-16-1":
                self.setup(self.room.room_next[1], 250, 480)
            elif self.room.room_next[1].room_name == "SAS-16-2":
                self.setup(self.room.room_next[1], 250, 480)
            elif self.room.room_next[1].room_name == "SAS-17":
                Terminal(1).sdl()
                print("Vous avez survécu, BRAVO!")
                Terminal(1).sdl()
                start_view = Fin()
                self.window.show_view(start_view)
                start_view.setup()
                self.setup(self.room.room_next[1], 480, 480)
            else:
                self.setup(self.room.room_next[1], 10, 480)
        elif self.player.center_y < 0:
            self.setup(self.room.room_next[2], 480, SCREEN_HEIGHT - 10)
        elif self.player.center_x < 0:
            self.setup(self.room.room_next[3], SCREEN_WIDTH - 10, 480)
        
        #Les combats
        if self.room.room_name == "SAS-11" and self.player.center_x > 315 and self.combat_1 == 0:
            Terminal(1).sdl()
            print("Un facehugger essaye de vous sauter dessus")
            self.combat_1 = 1
            combat = Combat(self.player_fight, face_hugger_SAS_11)
            if not combat.fight():
                Terminal(1).sdl()
                print("Ce qui est mort ne saurait mourir...")
                Terminal(1).sdl()
                start_view = GameOver()
                self.window.show_view(start_view)
                start_view.setup()
        
        if self.room.room_name == "SAS-22-1" and self.player.center_y > 100 and self.combat_2 == 0:
            Terminal(1).sdl()
            print("Un facehugger vous tombe dessus")
            self.combat_2 = 1
            combat = Combat(self.player_fight, face_hugger_SAS_22)
            if not combat.fight():
                Terminal(1).sdl()
                print("Ce qui est mort ne saurait mourir...")
                Terminal(1).sdl()
                start_view = GameOver()
                self.window.show_view(start_view)
                start_view.setup()
        
        if (self.room.room_name == "SAS-13-1" or self.room.room_name == "SAS-13-2") and self.player.center_x > 360 and self.player.center_x < 660 and self.player.center_y > 300 and self.combat_3 == 0:
            Terminal(1).sdl()
            print("Un chestbuster vous fonce dessus")
            self.combat_3 = 1
            combat = Combat(self.player_fight, chest_buster_SAS_13)
            if not combat.fight():
                Terminal(1).sdl()
                print("Ce qui est mort ne saurait mourir...")
                Terminal(1).sdl()
                start_view = GameOver()
                self.window.show_view(start_view)
                start_view.setup()
        
        if self.room.room_name == "SAS-04" and self.player.center_x > 300  and self.player.center_y < 670 and self.combat_4 == 0:
            Terminal(1).sdl()
            print("Un face hugger tombe du plafond")
            self.combat_4 = 1
            combat = Combat(self.player_fight, face_hugger_SAS_04)
            if not combat.fight():
                Terminal(1).sdl()
                print("Ce qui est mort ne saurait mourir...")
                Terminal(1).sdl()
                start_view = GameOver()
                self.window.show_view(start_view)
                start_view.setup()
        
        if self.room.room_name == "SAS-14" and self.player.center_x > 390 and self.player.center_x < 570  and self.player.center_y > 400 and self.player.center_y < 575 and self.combat_5 == 0:
            Terminal(1).sdl()
            print("Un face hugger sort de sous la table")
            self.combat_5 = 1
            combat = Combat(self.player_fight, face_hugger_SAS_14)
            if not combat.fight():
                Terminal(1).sdl()
                print("Ce qui est mort ne saurait mourir...")
                Terminal(1).sdl()
                start_view = GameOver()
                self.window.show_view(start_view)
                start_view.setup()
        
        if self.room.room_name == "SAS-06-1" and self.player.center_x > 195 and self.combat_6 == 0:
            Terminal(1).sdl()
            print("Un face hugger vous saute dessus")
            self.combat_6 = 1
            combat = Combat(self.player_fight, chest_buster_SAS_06)
            if not combat.fight():
                Terminal(1).sdl()
                print("Ce qui est mort ne saurait mourir...")
                Terminal(1).sdl()
                start_view = GameOver()
                self.window.show_view(start_view)
                start_view.setup()

        if self.room.room_name == "SAS-15-2" and self.player.center_x > 325 and self.player.center_y > 325 and self.combat_7 == 0:
            Terminal(1).sdl()
            print("Un face hugger vous saute dessus")
            self.combat_7 = 1
            combat = Combat(self.player_fight, face_hugger_SAS_15)
            if not combat.fight():
                Terminal(1).sdl()
                print("Ce qui est mort ne saurait mourir...")
                Terminal(1).sdl()
                start_view = GameOver()
                self.window.show_view(start_view)
                start_view.setup()

        if self.room.room_name == "SAS-23" and self.player.center_y > 100 and self.combat_8 == 0:
            Terminal(1).sdl()
            print("Un Runner était coincé dans cette salle")
            self.combat_8 = 1
            combat = Combat(self.player_fight, Runner_SAS_23)
            if not combat.fight():
                Terminal(1).sdl()
                print("Ce qui est mort ne saurait mourir...")
                Terminal(1).sdl()
                start_view = GameOver()
                self.window.show_view(start_view)
                start_view.setup()
        
        if self.room.room_name == "SAS-16-1" and self.combat_9 == 0 and (self.player.center_x != 250 or self.player.center_y != 480):
            Terminal(1).sdl()
            print("Le Xénomorph est ici, le combat commence")
            self.combat_9 = 1
            combat = Combat(self.player_fight, Xenomorph_SAS_16)
            if not combat.fight():
                Terminal(1).sdl()
                print("Ce qui est mort ne saurait mourir...")
                Terminal(1).sdl()
                start_view = GameOver()
                self.window.show_view(start_view)
                start_view.setup()
            self.setup(room_16_v2, self.player.center_x, self.player.center_y)

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = MyGame()
    window.show_view(start_view)
    start_view.setup(room_10_v1, 480, 0)
    arcade.run()
    #ERROR POSSIBLE VENANT DE LA LIB ARCADE :
    #Exception has occurred: AttributeError 
    # ObjCInstance b'__NSSingleObjectArrayI' has no attribute b'type'
    # File "/Users/benjaminschinkel/Desktop/Projet RPG/RPG/game.py", line 235, in main
    # arcade.run()
    # File "/Users/benjaminschinkel/Desktop/Projet RPG/RPG/game.py", line 299, in <module>
    # main()
    # AttributeError: ObjCInstance b'__NSSingleObjectArrayI' has no attribute b'type'

#Création des rooms
room_10_v1 = Rooms("maps/SAS/SAS-10-V1.tmx", "SAS-10-1", [])
room_10_v2 = Rooms("maps/SAS/SAS-10-V2.tmx", "SAS-10-2", [])
room_11 = Rooms("maps/SAS/SAS-11.tmx", "SAS-11", [])
room_12_v1 = Rooms("maps/SAS/SAS-12-V1.tmx", "SAS-12-1", [])
room_12_v2 = Rooms("maps/SAS/SAS-12-V2.tmx", "SAS-12-1", [])
room_22_v1 = Rooms("maps/SAS/generateurs-1-V1.tmx", "SAS-22-1", [])
room_22_v2 = Rooms("maps/SAS/generateurs-1-V2.tmx", "SAS-22-2", [])
room_02 =  Rooms("maps/SAS/SAS-02.tmx", "SAS-02", [])
room_03 =  Rooms("maps/SAS/SAS-03.tmx", "SAS-03", [])
room_04 =  Rooms("maps/SAS/SAS-04.tmx", "SAS-04", [])
room_13_v1 =  Rooms("maps/SAS/SAS-13-V1.tmx", "SAS-13-1", [])
room_13_v2 =  Rooms("maps/SAS/SAS-13-V2.tmx", "SAS-13-2", [])
room_14 =  Rooms("maps/SAS/SAS-14.tmx", "SAS-14", [])
room_23 = Rooms("maps/SAS/SAS-23.tmx", "SAS-23", [])
room_15_v1 =  Rooms("maps/SAS/SAS-15-V1.tmx", "SAS-15-1", [])
room_15_v2 =  Rooms("maps/SAS/SAS-15-V2.tmx", "SAS-15-2", [])
room_05 =  Rooms("maps/SAS/SAS-05.tmx", "SAS-05", [])
room_06_v1 =  Rooms("maps/SAS/generateurs-3-V1.tmx", "SAS-06-1", [])
room_06_v2 =  Rooms("maps/SAS/generateurs-3-V2.tmx", "SAS-06-2", [])
room_24_v1 =  Rooms("maps/SAS/generateurs-2-V1.tmx", "SAS-24-1", [])
room_24_v2 =  Rooms("maps/SAS/generateurs-2-V2.tmx", "SAS-24-2", [])
room_16_v1 =  Rooms("maps/SAS/SAS-16-V1.tmx", "SAS-16-1", [])
room_16_v2 =  Rooms("maps/SAS/SAS-16-V2.tmx", "SAS-16-2", [])
room_17 =  Rooms("maps/SAS/Capsule.tmx", "SAS-17", [])

#Room adjacent
room_10_v1.add_next_room([None, room_11, None, None])
room_10_v2.add_next_room([None, None, None, None])
room_11.add_next_room([None, room_12_v1, None, room_10_v1])
room_12_v1.add_next_room([room_22_v1, None, None, room_11])
room_12_v2.add_next_room([room_22_v2, None, room_02, room_11])
room_22_v1.add_next_room([None, None, room_12_v1, None])
room_22_v2.add_next_room([None, None, room_12_v2, None])
room_02.add_next_room([room_12_v2, room_03, None, None])
room_03.add_next_room([room_13_v1, room_04, None, room_02])
room_04.add_next_room([room_14, None, None, room_03])
room_13_v1.add_next_room([None, room_14, room_03, None])
room_13_v2.add_next_room([room_23, room_14, room_03, None])
room_14.add_next_room([room_24_v1, room_15_v1, room_04, room_13_v1])
room_23.add_next_room([None, None, room_13_v2, None])
room_15_v1.add_next_room([None, None, room_05, room_14])
room_15_v2.add_next_room([None, room_16_v1, room_05, room_14])
room_05.add_next_room([room_15_v1,room_06_v1,None,None])
room_06_v1.add_next_room([None,None,None,room_05])
room_06_v2.add_next_room([None,None,None,room_05])
room_24_v1.add_next_room([None,None,room_14,None])
room_24_v2.add_next_room([None,None,room_14,None])
room_16_v1.add_next_room([None,None,None,None])
room_16_v2.add_next_room([None,room_17,None,None])
room_17.add_next_room([None,None,None,None])

if __name__ == "__main__":
    main()