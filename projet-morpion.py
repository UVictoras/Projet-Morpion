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

class Morpion(Player, IA):

    def __init__(self):
        self.grid = []

    def PrepareGrid(self):
        for i in range(3):
            row = []
            for i in range(3):
                row.append('-')
            self.grid.append(row)

    def PrintGrid(self):
        for i in range(3):
            print(self.grid[i])
    
    def VerifyEmptyCase(self, x, y):
        if self.grid[x-1][y-1] == 'X' or self.grid[x-1][y-1] == 'O':
            return False
        else:
            return True

    def UpdateGrid(self, x, y):
        if self.VerifyEmptyCase(self, x, y):
            if Player.sign == 'X':
                self.grid[x-1][y-1] = 'X'
            else:
                self.grid[x-1][y-1] = 'O'
        else:
            print("Choose another case please, this one is already full.")


''' FIN '''