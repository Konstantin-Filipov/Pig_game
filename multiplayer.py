"""Using the cmd module to create a shell for the main program"""

import cmd
import dice
import player

class Multiplayer(cmd.Cmd):

    turn_index = 0
    intro = """Type help or ? to list commands.\n"""
    isprompt = True

    if isprompt == True:
        prompt = "(game): "

    def __init__(self):
        """Init the object."""
        super().__init__()
        self.dice = dice.Dice() # dice object to call the roll() later
        self.turn_index = 1
        self.player1 = player.Player(1) # score = 0, index = 1
        self.player2 = player.Player(2) # score = 0, index = 2

    def do_set_name(self, _):
        """Type "set_name" to set a new nickname"""
        if self.turn_index == 1:
            self.player1.setName()
        elif self.turn_index == 2:
            self.player2.setName()

    def do_hold(self, _):
        """Type in "hold" to end your current turn"""
        if self.turn_index == 1:
            self.player1.score_turn = 0 # reset the score turn for player 1
            self.turn_index = 2 #change the index to point to 2nd obj player
            print(f"Now is {self.player2.name}'s turn")
        elif self.turn_index == 2:
            self.player2.score_turn = 0# reset the score turn for player 2
            self.turn_index = 1 #change the index to point to 1st obj player
            print(f"Now is {self.player1.name}'s turn")

    def do_cheat(self, _):
        """Type in "cheat" to win the game instantly"""
        if self.turn_index == 1:
            self.player1.cheat()
        elif self.turn_index == 2:
            self.player2.cheat()
        self.do_exit(self)

    def do_roll(self, _):
        """Type "roll" to throw the dice"""
        rolled = self.dice.roll()
        self.dice.dice_graph(rolled) # pass rolled as argument to generate graphical dice face

        if rolled != 1:
            self.updateScore_checkWinner(rolled)
        else:
            self.removePoints_switchTurn()

    def updateScore_checkWinner(self, arg):
        """update player's score and check if there is winner"""
        if self.turn_index == 1:
            self.player1.update_score(arg) # update ocerall score
            if self.player1.isWinner():
                self.do_exit(self)
        elif self.turn_index == 2:
            self.player2.update_score(arg) # update ocerall score
            if self.player2.isWinner():
                self.do_exit(self)

    def removePoints_switchTurn(self):
        """reset points from current turn & switch turn"""
        if self.turn_index == 1:
            self.player1.remove_points()
            self.do_hold(self)
        elif self.turn_index == 2:
            self.player2.remove_points()
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
        print("press any key to leave game, press 's' to start a new one")
        comand = input()
        if comand == 's':
            self.do_start(self)
        return True

    def do_EOF(self, arg):
        # pylint: disable=invalid-name
        """Leave the game."""
        return self.do_exit(arg)
