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
        for i in range(3):
            row = []
            for i in range(3):
                row.append('-')
            self.grid.append(row)

''' FIN '''