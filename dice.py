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
            dice_face = " _______\n|       |\n|   O   |\n|_______|\n"
            return dice_face

        elif r == 2:
            dice_face = " _______\n| O     |\n|       |\n|_____O_|\n"
            return dice_face

        elif r == 3:
            dice_face = " _______\n| O     |\n|   O   |\n|_____O_|\n"
            return dice_face

        elif r == 4:
            dice_face = " _______\n| O   O |\n|       |\n|_O___O_|\n"
            return dice_face

        elif r == 5:
            dice_face = " _______\n| O   O |\n|   O   |\n|_O___O_|\n"
            return dice_face

        elif r == 6:
            dice_face = " _______\n| O   O |\n| O   O |\n|_O___O_|\n"
            return dice_face
