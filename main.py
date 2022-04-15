"""
================================================================================
================================================================================
                            WELCOME TO PIG GAME
              Choose singleplayer or multiplayer mode
        Type "roll" in order to throw the dice to collect points
                        But be careful!!!
    If you roll 1 then your collected points from this round will be lost
          So if you feel like you shouldn't push your luck anymore
       Type "hold" to hold your points and pass the turn to your enemy.
                    Type "help"/"?" to list all commands.
                  Whoever reaches 100 first is the WINNER!
"""
import chooseGameMode

if __name__ == "__main__":
    print(__doc__)
    chooseGameMode.ChooseGameMode().cmdloop()
