import arcade

class mygame(arcade.Window):
    def __init__(self, Width, Height, title):
        super().__init__(Width, Height, title)
        self.black_pieces = None
        self.white_pieces = None

    def setup(self):
        self.black_pieces = arcade.SpriteList()
        self.white_pieces = arcade.SpriteList()

        imgblack = "b.png"
        imgwhite = "w.png"
        self.black1 = arcade.Sprite(imgblack)
        self.black1.center_x = 150
        self.black1.center_y = 750
        self.black2 = arcade.Sprite(imgblack)
        self.black2.center_x = 450
        self.black2.center_y = 750
        self.black3 = arcade.Sprite(imgblack)
        self.black3.center_x = 750
        self.black3.center_y = 750
        self.white1 = arcade.Sprite(imgwhite)
        self.white1.center_x = 150
        self.white1.center_y = 150
        self.white2 = arcade.Sprite(imgwhite)
        self.white2.center_x = 450
        self.white2.center_y = 150
        self.white3 = arcade.Sprite(imgwhite)
        self.white3.center_x = 750
        self.white3.center_y = 150
        self.black_pieces.append(self.black1)
        self.black_pieces.append(self.black2)
        self.black_pieces.append(self.black3)
        self.white_pieces.append(self.white1)
        self.white_pieces.append(self.white2)
        self.white_pieces.append(self.white3)

        
    def on_draw(self):
        self.clear()
        arcade.draw_rectangle_filled(150, 150, 300, 300, arcade.color.WHITE)
        arcade.draw_rectangle_filled(150, 750, 300, 300, arcade.color.WHITE)
        arcade.draw_rectangle_filled(450, 450, 300, 300, arcade.color.WHITE)
        arcade.draw_rectangle_filled(750, 150, 300, 300, arcade.color.WHITE)
        arcade.draw_rectangle_filled(750, 750, 300, 300, arcade.color.WHITE)
        arcade.draw_rectangle_filled(150, 450, 300, 300, arcade.color.GRAY_BLUE)
        arcade.draw_rectangle_filled(450, 150, 300, 300, arcade.color.GRAY_BLUE)
        arcade.draw_rectangle_filled(450, 750, 300, 300, arcade.color.GRAY_BLUE)
        arcade.draw_rectangle_filled(750, 450, 300, 300, arcade.color.GRAY_BLUE)
        self.black_pieces.draw()
        self.white_pieces.draw()

a = 0
window = mygame(900, 900, a)
window.setup()
arcade.run()
