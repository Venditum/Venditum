import tkinter as tk
from PIL import ImageTk,Image

class Hexapawn:
    def __init__(self, player1, player2):
        player1.symbol = 1
        player2.symbol = -1
        self.player1 = player1
        self.player2 = player2
        self.gameboard = [[1, 1, 1], [0, 0, 0], [-1, -1, -1]]

    def all_valid_moves_for(self, currentsymbol):
        valid_moves = []
        for line in (range(2) if currentsymbol == 1 else range(1, 3)):
            for field in range(3):
                if self.gameboard[line][field] == currentsymbol:
                    if self.gameboard[line + currentsymbol][field] == 0:
                        valid_moves.append([currentsymbol, (line, field), "forward"])
                    if field == 0 or field == 2:
                        if self.gameboard[line + currentsymbol][1] == -currentsymbol:
                            valid_moves.append([currentsymbol ,(line, field), "takes_B"]) 
                    if field == 1:
                        if self.gameboard[line + currentsymbol][0] == -currentsymbol:          
                            valid_moves.append([currentsymbol, (line, field), "takes_A"]) 
                        if self.gameboard[line + currentsymbol][2] == -currentsymbol:          
                            valid_moves.append([currentsymbol, (line, field), "takes_C"]) 
        return valid_moves                        

    def check_if_game_is_won(self, lastsymbol):
        return lastsymbol in self.gameboard[2 if lastsymbol == 1 else 0] or len(self.all_valid_moves_for(-lastsymbol)) == 0

    def move(self, player, pieceposition, action):
        if [player.symbol, pieceposition, action] in self.all_valid_moves_for(player.symbol):
            self.gameboard[pieceposition[0]][pieceposition[1]] = 0
            self.gameboard[pieceposition[0] + player.symbol][pieceposition[1] if action == "forward" else 0 if action == "takes_A" else 1 if action == "takes_B" else 2] = player.symbol
        return False           

    def show(self):
        print(str(self.gameboard[2][0]) + "|" + str(self.gameboard[2][1]) + "|" + str(self.gameboard[2][2]))                       
        print(str(self.gameboard[1][0]) + "|" + str(self.gameboard[1][1]) + "|" + str(self.gameboard[1][2]))   
        print(str(self.gameboard[0][0]) + "|" + str(self.gameboard[0][1]) + "|" + str(self.gameboard[0][2]))   

    def play(self):
        currentplayer = player1
        while not self.check_if_game_is_won(-currentplayer.symbol):
            self.show()
            move = currentplayer.move(self)
            self.move(currentplayer, move[1], move[2])
            currentplayer = player2 if currentplayer == player1 else player1
        self.show()
        return currentplayer    

class Humanplayer():
    def __init__(self):
        self.symbol = 0

    def move(self, game):
        move = []
        while move not in game.all_valid_moves_for(self.symbol):
            move = [self.symbol, (int(input("Please enter the row of the piece you want to move:")), int(input("Please enter the column of the piece you want to move:"))), input("Please enter the action you want to perform:")]  
        return move

root = tk.Tk()
root.title("Hexapawn")
root.geometry("900x900")
root.minsize(900, 900)
root.maxsize(900, 900)
field = Image.open("Field.png")
field = ImageTk.PhotoImage(field)
canvas = tk.Canvas(root, width=900, height=900)
canvas.pack(pady=20)
img = canvas.create_image(x=0, y=0, width=900, height=900, image=field)
root.mainloop()

player1 = Humanplayer()
player2 = Humanplayer()        
Hexa = Hexapawn(player1, player2)
#Hexa.forward((0, 0))
#Hexa.takes_A((2, 1))
#Hexa.move(player1, (0, 0), "forward")
#Hexa.move(player2, (2, 1), "takes_A")
Hexa.play()