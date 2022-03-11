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
        self.do_change_name(name)

    def do_change_name(self, playerName):
        """Change real player's name"""
        self.player1.setName(playerName)
        print(f"player nickname is set to {playerName}")

    def do_hold(self, _):
        """Switches the turn """
        self.player1.score_turn = 0 # reset the score turn for player 1
        print(f"Now is BOT's turn")
        self.bot.bot_turn()#bot rolls the dice multiple times here
        print (f"Now is {self.player1.name}'s turn")

    def do_cheat(self, _):
        """roll dice until exceeds 100"""
        while self.player1.score < 100:
            rolled = self.dice.roll()
            if rolled == 1:
                rolled += 1
            self.dice.dice_graph(rolled)
            self.player1.update_score(rolled)
            print(f"Player {self.player1.name} rolled {rolled}, overall score: {self.player1.score}")

        print("Congrats!!! You won by cheating :0!")
        self.player1.isCheater = True

    def do_roll(self, _):
        """roll the dice"""
        rolled = self.dice.roll()
        self.dice.dice_graph(rolled)

        if rolled != 1:
            self.player1.score_turn = rolled
            self.player1.update_score(rolled) # update overall score
            print(f"Player {self.player1.name} rolled {rolled}, overall score: {self.player1.score}")
        else:
            print(f"{self.player1.name} rolled 1 and lost the points from this turn")
            self.do_hold(self)

    def do_start(self, _):
        """start a new game"""
        print("You have started a new game.\n")
        self.__init__()

    def do_restart(self, _):
        """Type "restart" to reset the current game and start a new one."""
        print("Game has been restarted.\n")
        self.__init__()

    def do_exit(self, _):
        # pylint: disable=no-self-use
        """Leave the game."""
        print("You left the current game, type 'start' to start a new one.\n")
        return True

    def do_EOF(self, arg):
        # pylint: disable=invalid-name
        """Leave the game."""
        return self.do_exit(arg)
