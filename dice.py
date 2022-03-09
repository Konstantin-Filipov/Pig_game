import random

class Dice:
    def __init__(self):
        random.seed()

    def roll(self):
        """Roll a dice once and return the value."""
        roll = random.randint(1, 6)
        return roll
    
    def dice_graph(self, r):
        if r == 1:
            print(" _______")
            print("|       |")
            print("|   O   |")
            print("|_______|\n")
            
        elif r == 2:
            print(" _______")
            print("| O     |")
            print("|       |")
            print("|_____O_|\n")
            
        elif r == 3:
            print(" _______")
            print("| O     |")
            print("|   O   |")
            print("|_____O_|\n")
        
        elif r == 4:
            print(" _______")
            print("| O   O |")
            print("|       |")
            print("|_O___O_|\n")
            
        elif r == 5:
            print(" _______")
            print("| O   O |")
            print("|   O   |")
            print("|_O___O_|\n")
            
        elif r == 6:
            print(" _______")
            print("| O   O |")
            print("| O   O |")
            print("|_O___O_|\n")
            
