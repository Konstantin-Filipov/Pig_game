"""
Module dedicated for testing chooseGameMode module.
"""
import unittest
from unittest import mock
from unittest.mock import patch
import cmd
import chooseGameMode

class Test_chooseGameMode(unittest.TestCase):

    def test_ChooseGameMode(self):
        """test instantiation of an object"""
        res = chooseGameMode.ChooseGameMode(cmd.Cmd)
        exp = chooseGameMode.ChooseGameMode
        self.assertIsInstance(res, exp)

    @mock.patch("singleplayer.Singleplayer.cmdloop") # make a mock of the function
    #that you want to check if it was called
    def test_do_s(self, mock):
        """Testing do_s() executes with cmdloop() the singleplayer module"""
        chooseGame_obj = chooseGameMode.ChooseGameMode(cmd.Cmd) #instance of the chooseGameMode class
        chooseGame_obj.do_s(self)
        self.assertTrue(mock.called)

    @mock.patch("multiplayer.Multiplayer.cmdloop") # make a mock of the function
    #that you want to check if it was called
    def test_do_s(self, mock):
        """Testing do_m() executes with cmdloop() the multiplayer module"""
        chooseGame_obj = chooseGameMode.ChooseGameMode(cmd.Cmd) #instance of the chooseGameMode class
        chooseGame_obj.do_m(self)
        self.assertTrue(mock.called)
