import arcade
import arcade.gui
import time
from KI import TTT_God
from KI import Level_2

WIDTH = 900
HEIGHT = 900
pointso = 0
pointsx = 0

def kzuf(x, y, seitenlänge):
    return x // (seitenlänge // 3) + 7 - 3 * (y // (seitenlänge // 3))

def fzuk(feld, seitenlänge):
    return [((seitenlänge / 6) + (((feld - 1) % 3)) * (seitenlänge / 3)), (seitenlänge - seitenlänge / 6) - ((feld - 1) // 3) * (seitenlänge / 3)]

class AIButton(arcade.gui.UIFlatButton, arcade.View):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        print("hallo ai")
        spiel = SpielAI()
        window.show_view(spiel)

class HumanButton(arcade.gui.UIFlatButton, arcade.View):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        print("hallo")
        spiel = Spiel()
        window.show_view(spiel)        

class First(arcade.View):
    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        arcade.set_background_color(arcade.color.WHITE)

        self.v_box = arcade.gui.UIBoxLayout()

        start_button = arcade.gui.UIFlatButton(text="Start Game", width=200)
        self.v_box.add(start_button.with_space_around(bottom=20))

        settings_button = arcade.gui.UIFlatButton(text="Settings", width=200)
        self.v_box.add(settings_button.with_space_around(bottom=20))

        @settings_button.event("on_click")
        def on_click_settings(event):
            print("hallo ai")
            spiel = Spiel()
            window.show_view(spiel)
            self.v_box.remove()

        AI_button = AIButton(text="Play with AI", width=200)
        self.v_box.add(AI_button)    

        Human_button = HumanButton(text="Play with Human", width=200)
        self.v_box.add(Human_button)    

        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def on_click_start(self, event):
        print("Start:", event)

    def on_draw(self):
        self.clear()
        self.manager.draw()

class SpielAI(arcade.View):
    
    def __init__(self):
        super().__init__()
        self.breite = 900
        self.höhe = 900
        self.pointso = 0
        self.pointsx = 0
        self.human = "x"
        self.AI = "o"
        self.setup()

    def setup(self):
        self.spielfeld = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.spritelist = arcade.SpriteList()
        self.human_list = arcade.SpriteList()
        self.ai_list = arcade.SpriteList()

        arcade.set_background_color(arcade.color.WHITE)

        self.gegenstand_list = arcade.SpriteList()
        self.spieler = self.human
        self.spielfelds = arcade.Sprite("feld1.png", 6)
        self.spielfelds.center_x = self.breite / 2
        self.spielfelds.center_y = self.höhe / 2
        self.spritelist.append(self.spielfelds)
    
    def __gewinnprüfung(self):
        return self.spielfeld[0] == self.spielfeld[1] == self.spielfeld[2] or \
                self.spielfeld[3] == self.spielfeld[4] == self.spielfeld[5] or \
                self.spielfeld[6] == self.spielfeld[7] == self.spielfeld[8] or \
                self.spielfeld[0] == self.spielfeld[3] == self.spielfeld[6] or \
                self.spielfeld[1] == self.spielfeld[4] == self.spielfeld[7] or \
                self.spielfeld[2] == self.spielfeld[5] == self.spielfeld[8] or \
                self.spielfeld[0] == self.spielfeld[4] == self.spielfeld[8] or \
                self.spielfeld[2] == self.spielfeld[4] == self.spielfeld[6]

    def test(self):
        for i in range(9):
            if self.spielfeld[i - 1] == str(i):
                return False
        return True

    def on_mouse_press(self, x, y, taste, modifiers):
        
        self.feld = kzuf(x, y, 900)

        if self.spielfeld[self.feld - 1] == self.human or self.spielfeld[self.feld - 1] == self.AI:
            return None

        self.spielfeld[self.feld - 1] = self.human
        
        x = arcade.Sprite("x.png", 0.3)
        x.center_x = 150 + ((self.feld - 1) % 3) * 300
        x.center_y = 750 - ((self.feld - 1) // 3) * 300
        self.human_list.append(x)

        if self.test():
            return None

        self.feld = Ai2.zug(self.spielfeld)
        self.spielfeld[self.feld - 1] = self.AI
        
        o = arcade.Sprite("o.png", 0.3)
        o.center_x = 150 + ((self.feld - 1) % 3) * 300
        o.center_y = 750 - ((self.feld - 1) // 3) * 300
        self.ai_list.append(o)            

    def on_draw(self):
        self.clear()  
        self.spritelist.draw()
        self.human_list.draw()
        self.ai_list.draw()
        arcade.draw_text("o: " + str(self.pointso) + ", x: " + str(self.pointsx), 20, 880, arcade.color.BLACK, font_size=10)
        if self.__gewinnprüfung() or self.test():  
            if self.test():
                None
            else:
                if self.spieler == self.human:
                    self.pointso += 1
                else:
                    self.pointsx += 1            
            self.setup()             

class Spiel(arcade.View):
    
    def __init__(self):
        super().__init__()
        self.breite = 900
        self.höhe = 900
        self.pointso = 0
        self.pointsx = 0
        self.spieler1 = "x"
        self.spieler2 = "o"
        self.setup()

    def setup(self):
        self.spielfeld = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.spritelist = arcade.SpriteList()

        arcade.set_background_color(arcade.color.WHITE)

        self.gegenstand_list = arcade.SpriteList()
        self.spieler = self.spieler1
        self.spielfelds = arcade.Sprite("feld1.png", 6)
        self.spielfelds.center_x = self.breite / 2
        self.spielfelds.center_y = self.höhe / 2
        self.spritelist.append(self.spielfelds)
    
    def __gewinnprüfung(self):
        return self.spielfeld[0] == self.spielfeld[1] == self.spielfeld[2] or \
                self.spielfeld[3] == self.spielfeld[4] == self.spielfeld[5] or \
                self.spielfeld[6] == self.spielfeld[7] == self.spielfeld[8] or \
                self.spielfeld[0] == self.spielfeld[3] == self.spielfeld[6] or \
                self.spielfeld[1] == self.spielfeld[4] == self.spielfeld[7] or \
                self.spielfeld[2] == self.spielfeld[5] == self.spielfeld[8] or \
                self.spielfeld[0] == self.spielfeld[4] == self.spielfeld[8] or \
                self.spielfeld[2] == self.spielfeld[4] == self.spielfeld[6]

    def test(self):
        for i in range(9):
            if self.spielfeld[i - 1] == str(i):
                return False
        return True

    def on_mouse_press(self, x, y, taste, modifiers):

        self.feld = kzuf(x, y, 900)

        if self.spielfeld[self.feld - 1] == self.spieler1 or self.spielfeld[self.feld - 1] == self.spieler2:
            return None

        self.spielfeld[self.feld - 1] = self.spieler
        
        if self.spieler == self.spieler1:
            x = arcade.Sprite("x.png", 0.3)
            x.center_x = 150 + ((self.feld - 1) % 3) * 300
            x.center_y = 750 - ((self.feld - 1) // 3) * 300
            self.spritelist.append(x)

        if self.spieler == self.spieler2:
            o = arcade.Sprite("o.png", 0.3)
            o.center_x = 150 + ((self.feld - 1) % 3) * 300
            o.center_y = 750 - ((self.feld - 1) // 3) * 300
            self.spritelist.append(o)    

        self.spieler = self.spieler2 if self.spieler == self.spieler1 else self.spieler1   

    def on_draw(self):
        self.clear()  
        self.spritelist.draw()
        arcade.draw_text("o: " + str(self.pointso) + ", x: " + str(self.pointsx), 20, 880, arcade.color.BLACK, font_size=10)
        if self.__gewinnprüfung() or self.test():  
            if self.test():
                None
            else:
                if self.spieler == self.spieler1:
                    self.pointso += 1
                else:
                    self.pointsx += 1    
            self.setup()                      

Ai = TTT_God("", "o", "x")
Ai2 = Level_2("")
window = arcade.Window(WIDTH, HEIGHT, "Different Views Example")
menu_view = First()
window.show_view(menu_view)
arcade.run()