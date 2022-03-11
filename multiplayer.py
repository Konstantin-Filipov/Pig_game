"""Using the cmd module to create a shell for the main program"""

import cmd
import dice
import player

class Multiplayer(cmd.Cmd):


    intro = "Welcome to the game. Type help or ? to list commands.\n"

    def __init__(self):
        """Init the object."""
        super().__init__()
        self.dice = dice.Dice() # dice object to call the roll() later
        self.player1 = player.Player(1) # score = 0, index = 1
        self.player2 = player.Player(2) # score = 0, index = 2
        self.playerTurn = player.Player(1) # score = 0, index = 1

        print("set 1st player name:")
        name = input()
        self.do_change_name(name)

        print("set 2nd player name:")
        self.playerTurn.index = 2#change index to point to 2nd player
        name = input()
        self.do_change_name(name)
        self.playerTurn.index = 1 #change back the index to point to 1st player



    def do_change_name(self, playerName):
        """Type "change_name <your new name>" to set a new nickname"""
        if self.playerTurn.index == 1:
            self.player1.setName(playerName)
            print(f"nickname for player{self.playerTurn.index} is set to {playerName}\n")
        elif self.playerTurn.index == 2:
            self.player2.setName(playerName)
            print(f"nickname for player{self.playerTurn.index} is set to {playerName}\n")

    def do_hold(self, _):
        """Type in "hold" to end your current turn"""
        if self.playerTurn.index == 1:
            self.player1.score_turn = 0 # reset the score turn for player 1
            self.playerTurn.index = 2 #change the index to point to 2nd obj player
            print(f"Now is {self.player2.name}'s turn")
        elif self.playerTurn.index == 2:
            self.player2.score_turn = 0# reset the score turn for player 2
            self.playerTurn.index = 1 #change the index to point to 1st obj player
            print(f"Now is {self.player1.name}'s turn")

    def do_cheat(self, _):
        """Type in "cheat" to win the game instantly"""
        if self.playerTurn.index == 1:
            self.player1.cheat()
        elif self.playerTurn.index == 2:
            self.player2.cheat()
        self.do_EOF(self)

    def do_roll(self, _):
        """Type "roll" to throw the dice"""
        rolled = self.dice.roll()
        self.dice.dice_graph(rolled) # pass rolled as argument to generate graphical dice face
        if rolled != 1:
            if self.playerTurn.index == 1:
                self.player1.score_turn += rolled
                self.player1.update_score(rolled) # update ocerall score
                print(f"Player {self.player1.name} rolled {rolled}, overall score: {self.player1.score}")
                #self.player1.check_score(self.player1.score, self.player1.name) # check if the score exceed 100
            elif self.playerTurn.index == 2:
                self.player2.score_turn += rolled
                self.player2.update_score(rolled) # update ocerall score
                print(f"Player {self.player2.name} rolled {rolled}, overall score: {self.player2.score}")
                #self.player2.check_score(self.player2.score, self.player2.name) # check if the score exceed 100
        else:
            if self.playerTurn.index == 1:
                self.player1.score -= self.player1.score_turn
                print(f"{self.player1.name} rolled 1 and lost points from this turn, overall score is {self.player1.score}")
                self.do_hold(self)
            elif self.playerTurn.index == 2:
                self.player2.score -= self.player2.score_turn
                print(f"{self.player2.name} rolled 1 and lost the points from this turn, overall score is {self.player2.score}")
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
