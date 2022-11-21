''' DEBUT '''

' --- Importation du ou des modules --- '

import random as r
import itertools

' --- Définition de la classe Player --- '

class Player():

    def __init__(self, name, sign):
        
        self.name = name
        self.sign = sign

    def PlayersPlay(self, x, y):
        
        return (x-1, y-1)

' --- Définition de la classe Morpion --- '

class Morpion(Player):

    def __init__(self):
        
        self.grid = []

    def PrepareGrid(self):
        
        row1 = ['-', '-', '-']
        row2 = ['-', '-', '-']
        row3 = ['-', '-', '-']
        self.grid.append(row1)
        self.grid.append(row2)
        self.grid.append(row3)


    def PrintGrid(self):
        
        for i in range(3):
            
            print(self.grid[i])
    
    def VerifyEmptyCase(self, x, y):
        
        if self.grid[x-1][y-1] == 'X' or self.grid[x-1][y-1] == 'O':
            
            return False
        
        else:
            
            return True

    def UpdateGrid(self, x, y, Player):
        
        if self.VerifyEmptyCase(x, y):
            
            if Player.sign == 'X':
                
                self.grid[x-1][y-1] = 'X'
            
            else:
                
                self.grid[x-1][y-1] = 'O'
        
        else:
            
            print("Choose another case please, this one is already full.")

    def VerifyLine(self):
        
        win = False
        
        for i in range(3):
            
            if self.grid[i][0] == 'X' and self.grid[i][1] == 'X' and self.grid[i][2] == 'X':
                
                win = True
            
            elif self.grid[i][0] == 'O' and self.grid[i][1] == 'O' and self.grid[i][2] == 'O':
                
                win = True
        
        return win

    def VerifyColumn(self):
        
        win = False
        
        for i in range(3):
            
            if self.grid[0][i] == 'X' and self.grid[1][i] == 'X' and self.grid[2][i] == 'X':
                
                win = True
            
            elif self.grid[0][i] == 'O' and self.grid[1][i] == 'O' and self.grid[2][i] == 'O':
                
                win = True
        
        return win

    def VerifyDiagonal(self):
        
        win = False
        
        if (self.grid[0][0] == 'X' and self.grid[1][1] == 'X' and self.grid[2][2] == 'X') or (self.grid[0][2] == 'X' and self.grid[1][1] == 'X' and self.grid[2][0] == 'X'):
            
            win = True
        
        elif (self.grid[0][0] == 'O' and self.grid[1][1] == 'O' and self.grid[2][2] == 'O') or (self.grid[0][2] == 'O' and self.grid[1][1] == 'O' and self.grid[2][0] == 'O'):
            
            win = True
        
        return win
        
    def VerifyWin(self):
        
        if self.VerifyLine() == True or self.VerifyColumn() == True or self.VerifyDiagonal() == True:
            
            return True
        
        else:
            
            return False

' --- Définition de la classe IA --- '

class AI():

    def __init__(self, sign):
        
        self.name = 'AI'
        self.sign = sign

    def AIPlayCorner(self):
        
        ChosenCorner = r.randint(1,4)
        
        if ChosenCorner == 1:
           
            Morpion.UpdateGrid(1, 1, self)
        
        elif ChosenCorner == 2:
            
            Morpion.UpdateGrid(1, 3, self)
        
        elif ChosenCorner == 3:
            
            Morpion.UpdateGrid(3, 1, self)
        
        elif ChosenCorner == 4:
            
            Morpion.UpdateGrid(3, 3, self)

    def AIMove(self, turn, game):

        if turn == 1:
            
            if game.VerifyEmptyCase(2, 2):
                
                game.UpdateGrid(2, 2, self)

            else:
                
                self.AIPlayCorner()

        elif turn > 1:

            for i in range(len(AIVar)):

                ((x1, y1), (x2, y2), (x3, y3)) = (AIVar[i])

                if game.grid[x1 - 1][y1 - 1] == 'O' and game.grid[x2 - 1][y2 - 1] == 'O':

                    if game.VerifyEmptyCase(x3, y3):

                        game.UpdateGrid(x3, y3, self)

            for i in range(len(AIVar)):

                ((x1, y1), (x2, y2), (x3, y3)) = (AIVar[i])

                if game.grid[x1 - 1][y1 - 1] == 'X' and game.grid[x2 - 1][y2 - 1] == 'X':

                    if game.VerifyEmptyCase(x3, y3):

                        game.UpdateGrid(x3, y3, self)

            if turn == 2:

                if game.grid[2][3] == 'X' and (game.grid[1][2] == 'X' or game.grid[1][1] == 'X'):

                    game.UpdateGrid(1, 3, self)

                elif game.grid[2][3] == 'X' and game.grid[3][2] == 'X':

                    game.UpdateGrid(3, 3, self)

                elif game.grid[1][2] =='X' and game.grid[3][1] == 'X':

                    game.UpdateGrid(1, 1, self)

                elif game.grid[3][1] == 'X' and game.grid[2][3] == 'X':

                    game.UpdateGrid(3, 3, self)

                elif game.grid[2][2] == 'O' and game.VerifyEmptyCase(2, 1):

                    game.UpdateGrid(2, 1, self)

            for i in range(len(AIVar)):

                ((x1, y1), (x2, y2), (x3, y3)) = (AIVar[i])

                if game.grid[x1 - 1][y1 - 1] == 'X' and ((x2, y2) in [(1,1),(1,3),(3,1),(3,3)]) and game.VerifyEmptyCase(x2, y2):

                    game.UpdateGrid(x2, y2, self)

            for i in range(len(AIVar)):

                ((x1, y1), (x2, y2), (x3, y3)) = (AIVar[i])

                if game.grid[x1 - 1][y1 - 1] == 'O':

                    if game.VerifyEmptyCase(x2, y2):

                        game.UpdateGrid(x2, y2, self)

                else:

                    while True:

                        x = r.randint(1,3)
                        y = r.randint(1,3)

                        if game.UpdateGrid(x, y, self):

                            game.UpdateGrid(x, y, self)

    def CompAI(self):

        global AIVar
        WinMoves = [((1,1),(1,2),(1,3)),((2,1),(2,2),(2,3)),((3,1),(3,2),(3,3)),((1,1),(2,1),(3,1)),((1,2),(2,2),(3,2)),((1,3),(2,3),(3,3)),((1,3),(2,2),(3,1)),((1,1),(2,2),(3,3))]
        PossibleWins = []
        
        for i in range(len(WinMoves)):
            
            PossibleWins.append(list(itertools.permutations(WinMoves[i])))

        AIVar = list(itertools.chain.from_iterable(PossibleWins))

' --- Commandes pour jouer une partie ---'

def game():
    
    turn = 0
    Player1 = Player('Victor', 'X')
    Player2 = Player('Benjamin', 'O')
    GameTicTacToe = Morpion()
    GameTicTacToe.PrepareGrid()
    
    while turn < 9 and GameTicTacToe.VerifyWin() != True:
        
        GameTicTacToe.PrintGrid()
        if turn%2 == 0:
            
            Player1ChoiceX = int(input("Which line do you choose, {} : ".format(Player1.name)))
            Player1ChoiceY = int(input("Which column do you choose, {} : ".format(Player1.name)))
            GameTicTacToe.UpdateGrid(Player1ChoiceX,Player1ChoiceY, Player1)
            turn += 1
            
            if GameTicTacToe.VerifyWin():
                
                print("{} won the game ! ".format(Player1.name))
                GameTicTacToe.PrintGrid()
                return 

        else:
            
            Player2ChoiceX = int(input("Which line do you choose, {} : ".format(Player2.name)))
            Player2ChoiceY = int(input("Which column do you choose, {} : ".format(Player2.name)))
            GameTicTacToe.UpdateGrid(Player2ChoiceX, Player2ChoiceY, Player2)
            turn += 1
            
            if GameTicTacToe.VerifyWin():
                
                print("{} won the game ! ".format(Player2.name))  
                GameTicTacToe.PrintGrid() 
                return      
        
        print("")
    
    GameTicTacToe.PrintGrid()
    print("It's a draw")

#game()

def GameWithAI():
    
    turn = 0
    Player1 = Player('Victor', 'X')
    Player2 = AI('O')
    GameTicTacToe = Morpion()
    GameTicTacToe.PrepareGrid()
    Player2.CompAI()
    
    while turn < 9 and GameTicTacToe.VerifyWin() != True:
        
        GameTicTacToe.PrintGrid()
        if turn%2 == 0:
            
            Player1ChoiceX = int(input("Which line do you choose, {} : ".format(Player1.name)))
            Player1ChoiceY = int(input("Which column do you choose, {} : ".format(Player1.name)))
            GameTicTacToe.UpdateGrid(Player1ChoiceX,Player1ChoiceY, Player1)
            turn += 1
            
            if GameTicTacToe.VerifyWin():
                
                print("{} won the game ! ".format(Player1.name))
                GameTicTacToe.PrintGrid()
                return 

        else:
            
            Player2.AIMove(turn, GameTicTacToe)
            turn += 1
            
            if GameTicTacToe.VerifyWin():
                
                print("{} won the game ! ".format(Player2.name))  
                GameTicTacToe.PrintGrid() 
                return      
        
        print("")
    
    GameTicTacToe.PrintGrid()
    print("It's a draw")

GameWithAI()

''' FIN '''