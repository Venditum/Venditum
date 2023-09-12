import arcade
import random

class Spiel(arcade.Window):
  
    def __init__(self, breite, höhe, titel):
        self.breite = breite
        self.höhe = höhe

        super().__init__(breite, höhe, titel)

        arcade.set_background_color(arcade.color.WHITE)

        self.gegenstand_list = arcade.SpriteList()

        self.setup()

    def setup(self):

        laptop = arcade.Sprite("Sprite-0001.png")
        laptop.center_x = random.randrange(self.breite)
        laptop.center_y = random.randrange(self.höhe)
        self.gegenstand_list.append(laptop)

        phone = arcade.Sprite("Sprite-0002.png")
        phone.center_x = random.randrange(self.breite)
        phone.center_y = random.randrange(self.höhe)
        self.gegenstand_list.append(phone)

        phone1 = arcade.Sprite("Sprite-0003.png")
        phone1.center_x = random.randrange(self.breite)
        phone1.center_y = random.randrange(self.höhe)
        self.gegenstand_list.append(phone1)

        cube = arcade.Sprite("Sprite-0004.png")
        cube.center_x = random.randrange(self.breite)
        cube.center_y = random.randrange(self.höhe)
        self.gegenstand_list.append(cube)   

    def on_mouse_press(self, x, y, taste, modifiers):
        pseudosprite= arcade.Sprite()
        pseudosprite.center_x = x
        pseudosprite.center_y = y
        pseudosprite.set_hit_box([(-2, -2), (2, -2), (-2, 2), (2, 2)])

        gegenstand_hitliste = arcade.check_for_collision_with_list(pseudosprite, self.gegenstand_list)    

        for gegenstand in gegenstand_hitliste:
            gegenstand.kill()

    def on_draw(self):
        self.clear()  

        self.gegenstand_list.draw()  

spiel = Spiel(1960, 1080, "Suchspiel")
arcade.run()