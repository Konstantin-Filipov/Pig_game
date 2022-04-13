"""Multiplayer class unittest."""
import multiplayer
from multiplayer import player
from multiplayer import dice
import unittest
from unittest import mock
from unittest.mock import patch, mock_open
import cmd

class Test_multiplayer(unittest.TestCase):
    """testing multiplayer class."""

    def test_init_obj(self):
        """test constructor"""
        res = multiplayer.Multiplayer()
        exp = multiplayer.Multiplayer
        self.assertIsInstance(res, exp)

    @patch("player.Player.setName")
    def test_do_set_name(self, mock):
        """test setName method call"""
        mult_obj = multiplayer.Multiplayer()
        mult_obj.do_set_name(self)
        self.assertTrue(mock.called)
        mult_obj.turn_index = 2 #check if it works for player 2
        mult_obj.do_set_name(self)
        self.assertTrue(mock.called)

    def test_do_hold(self):
        """test hold hand method"""
        mult_obj = multiplayer.Multiplayer()
        mult_obj.do_hold(self)
        self.assertEqual(mult_obj.turn_index, 2)
        #now check if the index changes to point to value 1
        mult_obj.turn_index = 2
        mult_obj.do_hold(self)
        self.assertEqual(mult_obj.turn_index, 1)

    @patch('builtins.input', return_value = "l")
    @patch("player.Player.cheat")
    def test_do_cheat(self, mock, mock_input):
        """test cheat method call and then do_exit"""
        mult_obj = multiplayer.Multiplayer()
        mult_obj.do_cheat(self)
        self.assertTrue(mock.called)
        mult_obj.turn_index = 2 #check if it works for player 2
        mult_obj.do_cheat(self)
        self.assertTrue(mock.called)
        #mock the input when do_exit method gets called
        mult_obj.do_exit(self)
        exp = 'l'
        self.assertTrue(exp)

    @patch('builtins.input', return_value = "l")
    @patch("player.Player.isWinner")
    @patch("dice.Dice.roll")
    def test_do_roll(self, mock_roll, mock_win, mock_input):
        """test roll method"""
        mult_obj = multiplayer.Multiplayer()
        mult_obj.do_roll(self)
        inst = mock_win.return_value
        inst.score = 100 # set score so isWinner() to return True
        self.assertTrue(mock_roll.called)

    @patch('builtins.input', return_value = "l")#patch for automatic input
    @patch("player.Player.isWinner")
    def test_updateScore_checkWinner(self, mock_win, mock_input):
        """test update_score method for player 1"""
        inst = mock_win.return_value
        inst.score = 100 # set score True so isWinner() to return True
        mult_obj = multiplayer.Multiplayer()
        to_test = mult_obj.updateScore_checkWinner(6)
        self.assertTrue(mock_win.called)

    @patch('builtins.input', return_value = "l")#patch for automatic input
    @patch("player.Player.isWinner")
    def test_updateScore_checkWinner2(self, mock_isWinner, mock_input):
        """test update_score method for player 2"""
        inst = mock_isWinner.return_value
        inst.score = 100# set score True so isWinner() to return True
        mult_obj = multiplayer.Multiplayer()
        mult_obj.turn_index = 2
        to_test = mult_obj.updateScore_checkWinner(6)
        self.assertTrue(mock_isWinner.called)

    @patch("player.Player.remove_points")
    def test_removePoints_switchTurn1(self, mock_remove):
        """test remove points for 1st player"""
        mult_obj = multiplayer.Multiplayer()
        mult_obj.removePoints_switchTurn()
        self.assertTrue(mock_remove.called)

    @patch("player.Player.remove_points")
    def test_removePoints_switchTurn2(self, mock_remove):
        """test remove points for 2nd player"""
        mult_obj = multiplayer.Multiplayer()
        mult_obj.turn_index = 2
        mult_obj.removePoints_switchTurn()
        self.assertTrue(mock_remove.called)

    def test_dumpHighScore(self):
        """test writing player scores to file"""
        with patch("builtins.open", mock_open(read_data="data")) as mock_file:
            assert open("multipl_highscores.txt").read() == "data"
        mock_file.assert_called_with("multipl_highscores.txt")

    def test_do_show_scores(self):
        """test show scores method"""
        with patch("builtins.open", mock_open(read_data="data")) as mock_file:
            assert open("multipl_highscores.txt").read() == "data"
        mock_file.assert_called_with("multipl_highscores.txt")

    @mock.patch("builtins.print")
    def test_do_start(self, mock):
        """test start of new game"""
        mult_obj = multiplayer.Multiplayer()
        mult_obj.do_start(self)
        str = "You have started a new game.\n"
        mock.assert_called_with(str)

    @patch("builtins.print")
    def test_do_restart(self, mock):
        """test restart method"""
        mult_obj = multiplayer.Multiplayer()
        mult_obj.do_restart(self)
        str = "Game has been restarted.\n"
        mock.assert_called_with(str)

    @patch('builtins.input', return_value = "s")#patch for automatic input
    def test_do_exit(self, mock_input):
        """test exit game method"""
        mult_obj = multiplayer.Multiplayer()
        mult_obj.do_exit(self)
        exp = 'l'
        self.assertTrue(exp)
