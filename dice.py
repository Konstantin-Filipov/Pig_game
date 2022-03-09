import random
class Dice:
    faces = 6
    def __init__(self):
        random.seed()

    def roll(self):
        """Roll a dice once and return the value."""
        roll = random.randint(1, self.faces)
        return roll
