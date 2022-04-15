"""
Module dedicated for testing singleplayer module.
"""

import unittest
from unittest import mock
from unittest.mock import patch, mock_open
import singleplayer
import cmd

class TestSingleplayer(unittest.TestCase):
    """Singleplayer test class"""

    @patch('builtins.input', return_value = "n")
    def test_init_(self, mock_constInput):
        """test init object"""
        s_obj = singleplayer.Singleplayer()
        e_obj = singleplayer.Singleplayer
        self.assertIsInstance(s_obj, e_obj)

    @patch('builtins.input', return_value = "n")
    @patch("player.Player.setName")
    def test_do_set_name(self, mock_set, mock_constInput):
        """test dosetname method"""
        s_obj = singleplayer.Singleplayer()
        s_obj.do_set_name(self)
        self.assertTrue(mock_set.called)

    @patch("bot.Bot.bot_turn")
    @patch('builtins.input', return_value = "n")
    def test_do_hold(self, mock_constInput, mock_turn):
        """test do_hold method"""
        s_obj = singleplayer.Singleplayer()
        s_obj.do_hold(self)
        self.assertTrue(mock_turn.called)

    @patch('builtins.input', return_value = "n")
    @patch("player.Player.cheat")
    def test_do_cheat(self, mock_consInput, mock_cheat):
        """do cheat method"""
        s_obj = singleplayer.Singleplayer()
        s_obj.do_cheat(self)
        self.assertTrue(mock_cheat)

    @patch("player.Player.isWinner")
    @patch("dice.Dice.roll")
    @patch('builtins.input', return_value = "n")
    def test_do_roll(self, mock_constInput, mock_roll, mock_winner):
        """test do roll method"""
        s_obj = singleplayer.Singleplayer()
        s_obj.do_roll(self)
        inst = mock_winner.return_value
        inst.score = 100 # set score True so isWinner() to return True
        self.assertTrue(mock_roll.called)


    @patch("singleplayer.Singleplayer.do_exit")
    @patch("player.Player.update_score")
    @patch('builtins.input', return_value = "n")
    @patch("player.Player.isWinner")
    def test_updateScore_checkWinner(self, mock_win, mock_constInput, mock_update, mock_exit):
        """test updating player score"""
        inst = mock_win.return_value
        inst.score = 100    # set score True so isWinner() to return True
        s_obj = singleplayer.Singleplayer()
        s_obj.updateScore_checkWinner(6)
        self.assertTrue(mock_update.called)
        self.assertTrue(mock_exit.called)

    @patch("player.Player.remove_points")
    @patch('builtins.input', return_value = "n")
    def test_removePoints_switchTurn(self, mock_constInput, mock_called):
        """test remove points and switch turn methods"""
        s_obj = singleplayer.Singleplayer()
        s_obj.removePoints_switchTurn()
        self.assertTrue(mock_called.called)

    def test_dumpHighScore(self):
        """test writing player scores to file"""
        with patch("builtins.open", mock_open(read_data="data")) as mock_file:
            assert open("singlepl_highscores.txt").read() == "data"
        mock_file.assert_called_with("singlepl_highscores.txt")

    def test_do_show_scores(self):
        """test show scores method"""
        with patch("builtins.open", mock_open(read_data="data")) as mock_file:
            assert open("singlepl_highscores.txt").read() == "data"
        mock_file.assert_called_with("singlepl_highscores.txt")

    @mock.patch("builtins.print")
    @patch('builtins.input', return_value = "n")
    def test_do_start(self, mock_constInput, mock):
        """test do start method"""
        s_obj = singleplayer.Singleplayer()
        s_obj.do_start(self)
        str = "Difficulty set to NORMAL.\n"
        mock.assert_called_with(str)
