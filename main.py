"""
Lets play "pig".

Type "roll" in order to throw the dice to collect points,

If you throw 1, your points get reset, thankfully you have the option
to stop your turn and keep the collected points by typing the command
"stop".

Whoever reaches first 100 points, wins.
"""

import multiplayer


if __name__ == "__main__":
    print(__doc__)
    multiplayer.Multiplayer().cmdloop()
