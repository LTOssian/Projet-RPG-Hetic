import arcade
import arcade. gui
from player import player
#SETTINGS
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 720
SCREEN_TITLE = "RPG_INVENTAIRE"

class InventoryView(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self._inventory_box = arcade.gui.UIBoxLayout()
        arcade.set_background_color(arcade.color.WHITE)

        title = "INVENTAIRE (i pour ouvrir/fermer)"
        label = arcade.gui.UITextArea(text = title,
            width = SCREEN_WIDTH,
            height = 36,
            font_size = 24,
            font_name = "comic")        
        self._inventory_box.add(label.with_space_around(bottom=0))

        for item_type, item_list  in player.inventory.items():
            title = item_type
            label = arcade.gui.UITextArea(
                text = title,
                width = 400,
                height= 50,
                font_size = 24,
                font_name = "comic"
            )
            self._inventory_box.add(label)
            text = ""
            for item in item_list:
                text += f"{item[0]} : "
                if item_type == "weapons":
                    text += f"Dégats = {item[1]['damage']} "
                    if item[1]['effect']:
                        text += f"Effet = {item[1]['effect'].get_name()}"
                    else:
                        text += "Effet = None"
                
                if item_type == "consommables":
                    if item[1].heal:
                        text += f"Soin = {item[1].heal} "
                    if item[1].effect_to_debuff:
                        text += f"Débuff = {item[1].effect_to_debuff.name} "
                    if item[1].stat_boost:
                        text += f"Boost de stat = {item[1].stat_boost} "

                text += '\n'

                #if item_type == "weapons": #pcq j'ai pas les consommables ni leur sprite
                 #   texture = arcade.load_texture(f"./weapons_sprite/{item}.png")
                  #  scale = .6
                   # arcade.draw_scaled_texture_rectangle(50, 50, texture, scale, 0)
                    #arcade.draw_scaled_texture_rectangle(50, 50, texture, scale, 45)
            label_content = arcade.gui.UITextArea(
                    text = text,
                    width = SCREEN_WIDTH,
                    height = 250,
                    font_size = 12,
                    font_name = "comic"
                )
            self._inventory_box.add(label_content)

        self.manager.add(
                arcade.gui.UIAnchorWidget(
                    anchor_x="center_x",
                    anchor_y="center_y",
                    child=self._inventory_box)
            )
    def on_draw(self):
        self.clear()
        self.manager.draw()


window = InventoryView()
arcade.run()

