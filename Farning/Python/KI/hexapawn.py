import random
import copy

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
        self.gameboard = [[1, 1, 1], [0, 0, 0], [-1, -1, -1]]
        currentplayer = Humanplayer()
        while not self.check_if_game_is_won(currentplayer.symbol):
            currentplayer = self.player2 if currentplayer == self.player1 else self.player1
            self.show()
            move = currentplayer.move(self)
            self.move(currentplayer, move[1], move[2])
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

class AI:
    def __init__(self):
        self.symbol = 0
        self.matchbox = []
        self.movespergame = []
        
    def train(self, trainingplayer, repetition):
        for i in range(repetition):
            self.movespergame = []
            game = Hexapawn(trainingplayer, self)
            winner = game.play()
            if winner == trainingplayer:
                self.removebadmove(1)

    def removebadmove(self, index):
        for i in range(len(self.matchbox)):
            if self.matchbox[i][0] == self.movespergame[-index][0]:
                self.matchbox[i][1].remove(self.movespergame[-index][1])
                if self.matchbox[i][1] == []:
                    del self.matchbox[i]
                    self.removebadmove(index + 1)
                return True    

    def move(self, game):
        for i in range(len(self.matchbox)):
            if game.gameboard == self.matchbox[i][0]:
                choice = random.choice(self.matchbox[i][1])
                self.movespergame.append((copy.deepcopy(game.gameboard), choice))
                return choice
        self.matchbox.append((copy.deepcopy(game.gameboard), game.all_valid_moves_for(self.symbol)))
        return self.move(game)     

player1 = Humanplayer()
player2 = Humanplayer()
AI1 = AI()
AI2 = AI()
AI1.train(player1, 100)
Hexa = Hexapawn(player1, AI1)
for i in range(5):
    Hexa.play()