"""Using the cmd module to create a shell for the main program"""

import cmd
import dice
import player

class Multiplayer(cmd.Cmd):


    intro = "Welcome to the game. Type help or ? to list commands.\n"

    def __init__(self):
        """Init the object."""
        super().__init__()
        self.player1 = player.Player(1) # score = 0, index = 1
        self.player2 = player.Player(2) # score = 0, index = 2
        self.playerTurn = player.Player(1) # score = 0, index = 1

        self.dice = dice.Dice() # dice object to call the roll() later

    def do_change_name(self, playerName):
        """Sets a new player nickname"""
        if self.playerTurn.index == 1:
            self.player1.setName(playerName)
            print(f"nickname for player{self.playerTurn.index} is set to {playerName}")
        elif self.playerTurn.index == 2:
            self.player2.setName(playerName)
            print(f"nickname for player{self.playerTurn.index} is set to {playerName}")

    def do_hold(self, _):
        """Its next player turn"""
        if self.playerTurn.index == 1:
            self.player1.score_turn = 0 # reset the score turn for player 1
            self.playerTurn.index = 2 #change the index to point to 2nd obj player
            print(f"Now is {self.player2.name}'s turn")
        elif self.playerTurn.index == 2:
            self.player2.score_turn = 0# reset the score turn for player 2
            self.playerTurn.index = 1 #change the index to point to 1st obj player
            print(f"Now is {self.player1.name}'s turn")

    def do_roll(self, _):
        """roll the dice"""
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


    def do_exit(self, _):
        # pylint: disable=no-self-use
        """Leave the game."""
        print("Bye bye - see ya soon again")
        return True

    def do_EOF(self, arg):
        # pylint: disable=invalid-name
        """Leave the game."""
        return self.do_exit(arg)
