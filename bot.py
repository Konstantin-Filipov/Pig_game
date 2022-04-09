import random
import dice

class Bot:
    name = "BOT"
    level = None
    score = 0
    iterations = 0

    def set_bot_level(self):
        """set what level the bot should be during the game"""
        print("Select difficulty.\nPress 'n' for normal / 'h' for hard.")
        set_d = input()

        if set_d == "n":
            print("Difficulty set to NORMAL.\n")
            self.level = "normal"
        elif set_d == "h":
            print("Difficulty set to HARD.\n")
            self.level = "hard"
        else:
            print("Wrong input.\n")
            self.set_bot_level()

    def set_iterations(self): # set the iterations count
        """Sets how many turns the bot will play"""
        if self.level == "normal":
            self.iterations = random.randint(2, 4)
        elif self.level == "hard":
            self.iterations = random.randint(5, 8)

    def bot_turn(self):
        """Automaticaly called turn which rolls multiple times depending on 'level' value"""
        self.set_iterations()
        self.die = dice.Dice()
        for i in range (self.iterations):
            roll = self.die.roll()
            if roll == 1:
                roll += 1
            self.die.dice_graph(roll)
            self.score += roll
        print("BOT Held the dice.")
        self.print_score()

    def print_score(self):
        """print score in the end of BOT's turn"""
        print(f"BOT's score is {self.score}")
