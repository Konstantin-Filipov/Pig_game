"""The dice class where is generated a random number to be thrown for yeah roll method
which after that passes argument to dice_graph() method """
import random

class Dice:
    def __init__(self):
        random.seed()

    def roll(self):
        """Roll a dice once and return the value."""
        roll = random.randint(1, 6)
        return roll

    def dice_graph(self, r):
        """Produce graphical representation of current dice's face"""
        if r == 1:
            print(" _______\n|       |\n|   O   |\n|_______|\n")

        elif r == 2:
            print(" _______\n| O     |\n|       |\n|_____O_|\n")

        elif r == 3:
            print(" _______\n| O     |\n|   O   |\n|_____O_|\n")

        elif r == 4:
            print(" _______\n| O   O |\n|       |\n|_O___O_|\n")

        elif r == 5:
            print(" _______\n| O   O |\n|   O   |\n|_O___O_|\n")

        elif r == 6:
            print(" _______\n| O   O |\n| O   O |\n|_O___O_|\n")
            
