"""Set the game mode of the game, this file is called in main.py"""
import singleplayer
import multiplayer
import cmd

class ChooseGameMode(cmd.Cmd):

    intro = "game modes: singleplayer(press s and enter) / multiplayer(press m and enter).\n"

    def do_s(self, _):
        """pass 's' argument and run "singleplayer.py" and loop in cmd"""
        self.gameMode = "singleplayer"
        singleplayer.Singleplayer().cmdloop()

    def do_m(self, _):
        """pass 'm' argument and run "multiplayer.py" and loop in cmd"""
        self.gameMode = "multiplayer"
        multiplayer.Multiplayer().cmdloop()
