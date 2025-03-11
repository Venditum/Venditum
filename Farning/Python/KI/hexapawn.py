class Hexapawn:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.gameboard = [[1, 1, 1], [0, 0, 0], [-1, -1, -1]]

    def all_valid_moves_for(self, currentplayer):
        valid_moves = []
        if currentplayer == self.player1:
            for line in range(2):
                for field in range(3):
                    if self.gameboard[line][field] == 1:
                        if self.gameboard[line + 1][field] == 0:
                            valid_moves.append([1, (line, field), "forward"])
                        if field == 0 or field == 2:
                            if self.gameboard[line + 1][1] == -1:
                                valid_moves.append([1 ,(line, field), "takes_B"]) 
                        if field == 1:
                            if self.gameboard[line + 1][0] == -1:          
                                valid_moves.append([1, (line, field), "takes_A"]) 
                            if self.gameboard[line + 1][2] == -1:          
                                valid_moves.append([1, (line, field), "takes_C"]) 
        else:                        
            for line in range(1, 3):
                for field in range(3):
                    if self.gameboard[line][field] == -1:
                        if self.gameboard[line - 1][field] == 0:
                            valid_moves.append([-1, (line, field), "forward"])
                        if field == 0 or field == 2:
                            if self.gameboard[line - 1][1] == -1:
                                valid_moves.append([-1, (line, field), "takes_B"]) 
                        if field == 1:
                            if self.gameboard[line - 1][0] == -1:          
                                valid_moves.append([-1, (line, field), "takes_A"]) 
                            if self.gameboard[line - 1][2] == -1:          
                                valid_moves.append([(line, field), "takes_C"]) 
        return valid_moves                        

    def check_if_game_is_won(self, lastplayer):
        if lastplayer == self.player1:
            return 1 in self.gameboard[2] or len(self.all_valid_moves_for(self.player2)) == 0
        else:
            return -1 in self.gameboard[0] or len(self.all_valid_moves_for(self.player1)) == 0

    def forward(self, pieceposition):
        if self.gameboard[pieceposition[0]][pieceposition[1]] == 1:
            if [1 , pieceposition, "forward"] in self.all_valid_moves_for(self.player1):
                self.gameboard[pieceposition[0]][pieceposition[1]] = 0
                self.gameboard[pieceposition[0] + 1][pieceposition[1]] = 1
                return True
            return False    
        else:        
            if [-1 , pieceposition, "forward"] in self.all_valid_moves_for(self.player1):
                self.gameboard[pieceposition[0]][pieceposition[1]] = 0
                self.gameboard[pieceposition[0] - 1][pieceposition[1]] = -1
                return True
            return False    

    def takes_A:

    def takes_B:

    def takes_C:                    

Hexa = Hexapawn(1, 2)
Hexa.forward((0, 0))
print(Hexa.gameboard)