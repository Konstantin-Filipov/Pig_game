"""
================================================================================
================================================================================
                            WELCOME TO PIG

                Type "setname" to set your username!

        Type "roll" in order to throw the dice to collect points
                        But be careful!!!
    If you roll 1 than your collected points from this round will be lost
          So if you feel like you shouldn't push your luck anymore
       Type "hold" to hold your points and pass the turn to your enemy.

                  Whoever reaches 100 is the WINNER!
================================================================================
================================================================================
"""
import chooseGameMode

if __name__ == "__main__":
    print(__doc__)
    chooseGameMode.ChooseGameMode().cmdloop()
