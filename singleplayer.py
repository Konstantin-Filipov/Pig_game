"""Using the cmd module to create a shell for the main program"""
"""Welcome to the game. Type help or ? to list commands.\nGame mode set to singleplayer.\n"""

import cmd
import dice
import player
import bot

class Singleplayer(cmd.Cmd):
    isprompt = True

    if isprompt == True:
        prompt = "(game): "

    def __init__(self):
        """Init the object."""
        super().__init__()
        self.player1 = player.Player(1) # score = 0, index = 1
        self.dice = dice.Dice() # dice object to call the roll() later
        self.bot = bot.Bot() # create bot obj
        self.bot.set_bot_level() # call set_level() to set level atribute
        print("Please set player's name\n")
        name = input()
        self.do_set_name(name)

    def do_set_name(self, playerName):
        """Change real player's name"""
        self.player1.setName(playerName)
        print(f"player nickname is set to {playerName}")

    def do_hold(self, _):
        """Switches the turn """
        self.player1.score_turn = 0 # reset the score turn for player 1
        print(f"Now is BOT's turn")
        self.bot.bot_turn()#bot rolls the dice multiple times here
        print (f"Now is {self.player1.name}'s turn")

    def do_roll(self, _):
        """roll the dice"""
        rolled = self.dice.roll()
        self.dice.dice_graph(rolled)

        if rolled != 1:
            self.player1.score_turn = rolled
            self.player1.update_score() # update overall score
            print(f"Player {self.player1.name} rolled {rolled}, overall score: {self.player1.score}")
        else:
            print(f"{self.player1.name} rolled 1 and lost the points from this turn")
            self.do_hold(self)


    def do_exit(self, _):
        # pylint: disable=no-self-use
        """Leave the game."""
        print("Bye bye - see ya soon again")
        return True

    def do_EOF(self, arg):
        # pylint: disable=invalid-name
        """Leave the game."""
        return self.do_exit(arg)
