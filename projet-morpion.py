''' DEBUT '''

' --- Importation du ou des modules --- '

import random as r

' --- Définition de la classe Player --- '

class Player():

    def __init__(self, name, sign):
        self.name = name
        self.sign = sign

    def PlayersPlay(self, x, y):
        return (x-1, y-1)

' --- Définition de la classe IA --- '

class IA():

    pass

' --- Définition de la classe Morpion --- '

class Morpion():

    def __init__(self):
        self.grid = []

    def PrepareGrid(self):
        row1 = ["-", "-", "-"]
        row2 = ["-", "-", "-"]
        row3 = ["-", "-", "-"]
        self.grid.append(row1)
        self.grid.append(row2)
        self.grid.append(row3)


    def PrintGrid(self):
        for i in range(3):
            print(self.grid[i])
    
    def VerifyEmptyCase(self, x, y):
        if self.grid[x-1][y-1] == "X" or self.grid[x-1][y-1] == "O":
            return False
        else:
            return True

    def UpdateGrid(self, x, y):
        if self.VerifyEmptyCase(x, y):
            if Player.sign == 'X':
                self.grid[x-1][y-1] = 'X'
            else:
                self.grid[x-1][y-1] = 'O'
        else:
            print("Choose another case please, this one is already full.")

    def VerifyLine(self):
        for i in range(3):
            if self.grid[i][0] == 'X' and self.grid[i][1] == 'X' and self.grid[i][2] == 'X':
                print("The winner is Player 1 ! Congratulations {} !".format(Player1.name))


' --- Commandes pour jouer une partie ---'

turn = 0
GameTicTacToe = Morpion()
GameTicTacToe.PrepareGrid()
Player1 = Player('Victor', 'X')
Player2 = Player('Benjamin', 'O')
while turn < 9:
    GameTicTacToe.PrintGrid()
    if turn%2 == 0:
        Player1ChoiceX = input("Which line do you choose, {} : ".format(Player1.name))
        Player1ChoiceY = input("Which column do you choose, {} : ".format(Player1.name))
        GameTicTacToe.UpdateGrid(Player1ChoiceX, Player1ChoiceY)
    else:
        Player2ChoiceX = input("Which line do you choose, {} : ".format(Player2.name))
        Player2ChoiceY = input("Which column do you choose, {} : ".format(Player2.name))
        GameTicTacToe.UpdateGrid(Player2ChoiceX, Player2ChoiceY)




''' FIN '''