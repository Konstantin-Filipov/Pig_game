import random
class Dice:
    faces = 6
    def __init__(self):
        random.seed()

    def roll(self):
        """Roll a dice once and return the value."""
        roll = random.randint(1, self.faces)
        if roll == 1:
            print(" _______")
            print("|       |")
            print("|   O   |")
            print("|_______|\n")
            return roll
        elif roll == 2:
            print(" _______")
            print("| O     |")
            print("|       |")
            print("|_____O_|\n")
            return roll
        elif roll == 3:
            print(" _______")
            print("| O     |")
            print("|   O   |")
            print("|_____O_|\n")
            return roll
        elif roll == 4:
            print(" _______")
            print("| O   O |")
            print("|       |")
            print("|_O___O_|\n")
            return roll
        elif roll == 5:
            print(" _______")
            print("| O   O |")
            print("|   O   |")
            print("|_O___O_|\n")
            return roll
        elif roll == 6:
            print(" _______")
            print("| O   O |")
            print("| O   O |")
            print("|_O___O_|\n")
            return roll
