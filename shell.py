"""Using the cmd module to create a shell for the main program"""

import cmd
import dice
import player

class Shell(cmd.Cmd):

    intro = "Welcome to the game. Type help or ? to list commands.\n"
    prompt = "(game) "

    def __init__(self):
        """Init the object."""
        super().__init__()
        self.player1 = player.Player()
        self.player2 = player.Player()
        self.dice = dice.Dice()

    def do_set_name(self, playername, index):
        printf("set new nickname for player")

        if not isinstance(index, int):
            raise TypeError("please specify the player (type '1' / '2')")

        if not index == 1 or index == 2:
            raise ValueError("No such player.")

        if index == 1:
            self.player1.setName(playerName)
            printf(f"nickname for player {index} is set to {playername}")
        elif index == 2:
            self.player2.setName(playerName)
            printf(f"nickname for player {index} is set to {playername}")


    def do_roll(self, _):
        """roll the dice"""
        rolled = dice.roll()
        printf(f"You rolled {rolled}")
        if (rolled == 1):
            printf("points are lost!")


    def do_stop(self, _):
        """stop your turn"""

    def do_exit(self, _):
        # pylint: disable=no-self-use
        """Leave the game."""
        print("Bye bye - see ya soon again")
        return True

    def do_EOF(self, arg):
        # pylint: disable=invalid-name
        """Leave the game."""
        return self.do_exit(arg)
