"""Using the cmd module to create a shell for the main program"""

import cmd
import dice

class Shell(cmd.Cmd):

    def __init__(self):
        """Init the object."""
        super().__init__()
        self.dice = dice.Dice()

    def do_roll(self, _):
        rolled = dice.roll()
        printf(f"You rolled {rolled}")

    def do_exit(self, _):
        # pylint: disable=no-self-use
        """Leave the game."""
        print("Bye bye - see ya soon again")
        return True

    def do_EOF(self, arg):
        # pylint: disable=invalid-name
        """Leave the game."""
        return self.do_exit(arg)
