import arcade
from game import * 


SCREEN_WIDTH = 960
SCREEN_HEIGHT = 960
SCREEN_TITLE = "Alien Escape : Spaceship n°58008"

#——————————————— TITLE SCREEN ——————————————— 

class Title(arcade.View):
    def __init__(self):
        super().__init__()
        self.load_audio_menu_background = None
        self.audio_menu_background = None

    def on_show(self):
        self.texture = arcade.load_texture('interface/menu/main_menu.png')
        arcade.set_viewport(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT - 1)


    def setup(self):
        self.load_audio_menu_background = arcade.load_sound("music/alien_music_main_menu.wav")
        self.audio_menu_background = arcade.play_sound(self.load_audio_menu_background,1.0,-1,True)

    def on_draw(self):
        self.clear()
        arcade.start_render()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT)
    
    def on_key_press(self, key, modifiers): 
        
        # ——————— jouer ———————

        if key == arcade.key.ENTER:
            arcade.stop_sound(self.audio_menu_background)
            start_view = MyGame()
            self.window.show_view(start_view)
            start_view.setup(room_10_v1, 480, 480)
        
        # ——————— commandes ———————
        
        if key == arcade.key.C:
            arcade.stop_sound(self.audio_menu_background)
            start_view = Commandes_view()
            self.window.show_view(start_view)
            start_view.setup()

        # ——————— crédit ———————
        
        if key == arcade.key.R:
            arcade.stop_sound(self.audio_menu_background)
            start_view = Credits_view()
            self.window.show_view(start_view)
            start_view.setup()

        # ——————— quitter ———————

        if key == arcade.key.ESCAPE:
            print("Merci d'avoir joué")
            arcade.exit()

#——————————————— CREDIT SCREEN ——————————————— 

class Credits_view(arcade.View):
    def __init__(self):
        super().__init__()
        self.load_audio_credits_background = None
        self.audio_credits_background = None

    def on_show(self):
            self.texture = arcade.load_texture('interface/menu/credits.png')
            arcade.set_viewport(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT - 1)

    def setup(self):
        self.load_audio_credits_background = arcade.load_sound("music/alien_music_main_menu.wav")
        self.audio_credits_background = arcade.play_sound(self.load_audio_credits_background,1.0,-1,True)
    
    def on_draw(self):
        self.clear()
        arcade.start_render()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT)   

    # ——————— go back to title screen ———————   

    def on_key_press(self, key, modifiers): 
        if key == arcade.key.ESCAPE:
            arcade.stop_sound(self.audio_credits_background)
            start_view = Title()
            self.window.show_view(start_view)
            start_view.setup()

#——————————————— COMMANDES SCREEN ——————————————— 

class Commandes_view(arcade.View):
    def __init__(self):
        super().__init__()
        self.load_audio_menu_background = None
        self.audio_menu_background = None

    def on_show(self):
            arcade.set_background_color(arcade.color.AMAZON)
            self.texture = arcade.load_texture('interface/menu/commandes.png')
            arcade.set_viewport(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT - 1)

    def setup(self):
        self.load_audio_menu_background = arcade.load_sound("music/alien_music_main_menu.wav")
        self.audio_menu_background = arcade.play_sound(self.load_audio_menu_background,1.0,-1,True)
    
    def on_draw(self):
        self.clear()
        arcade.start_render()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT)  

    # ——————— go back to title screen ———————   

    def on_key_press(self, key, modifiers): 
        if key == arcade.key.ESCAPE:
            arcade.stop_sound(self.audio_menu_background)
            start_view = Title()
            self.window.show_view(start_view)
            start_view.setup()

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = Title()
    window.show_view(start_view)
    start_view.setup()
    arcade.run()


if __name__ == "__main__":
    main()