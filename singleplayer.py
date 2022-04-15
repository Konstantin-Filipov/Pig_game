"""
Welcome to Singleplayer mode game!
This is the module executed when the player chooses singleplayer mode
Type help or ? to list commands.
"""
import cmd
import dice
import player
import bot
import pickle


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

    def do_set_name(self, _):
        """Type "set_name" to set a new nickname"""
        self.player1.setName()

    def do_hold(self, _):
        """Type in "hold" to end your current turn, then is bot turn"""
        self.player1.score_turn = 0 # reset the score turn for player 1
        print(f"Now is BOT's turn")
        self.bot.bot_turn()#call automatic bot turn

        if self.bot.reached100(): # if True, end the game
            self.do_exit(self)
        else:
            print (f"Now is {self.player1.name}'s turn")

    def do_cheat(self, _):
        """Type in "cheat" to win the game instantly"""
        self.player1.cheat()
        self.do_exit(self)

    def do_roll(self, _):
        """Type "roll" to throw the dice"""
        rolled = self.dice.roll()
        self.dice.dice_graph(rolled)

        if rolled != 1:
            self.updateScore_checkWinner(rolled)
        else:
            self.removePoints_switchTurn()

    def updateScore_checkWinner(self, arg):
        """update player's score and check if there is winner"""
        self.player1.update_score(arg) # update ocerall score
        if self.player1.isWinner():
            self.do_exit(self)

    def removePoints_switchTurn(self):
        """reset points from current turn & switch turn"""
        self.player1.remove_points()
        self.do_hold(self)

    def do_show_scores(self, _):
        """type 'show_score' to show highscore table"""
        with open ('singlepl_highscores.txt', 'r') as f:
            data = f.read()
            print(data)

    def dumpHighScore(self):
        """move player's scores and data to file"""
        str0 = (f"mode: {self.bot.level}")
        str1 = (f"name: {self.player1.name}, score: {self.player1.score}")
        str2 = (f"name: {self.bot.name}, score: {self.bot.score}")
        str3 = ("-----------------------")

        with open('singlepl_highscores.txt', 'a+') as f:
            f.write(str0 + "\n")
            f.write(str1 + "\n")
            f.write(str2 + "\n")
            f.write(str3 + "\n")

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
        """Leave the game and save scores to a file"""
        self.dumpHighScore()
        print("press any key to leave game, press 's' to start a new one")
        comand = input()
        if comand == 's':
            self.do_start(self)
        return True

    def do_EOF(self, arg):
        # pylint: disable=invalid-name
        """Leave the game."""
        return self.do_exit(arg)
