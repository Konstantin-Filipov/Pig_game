"""
Module dedicated for testing bot module.
"""
import bot
import unittest
from unittest import mock
from unittest.mock import patch

class TestBot(unittest.TestCase):

    @patch('builtins.input', return_value = 'n')
    def test_set_bot_level_normal(self, mock_input):
        """test set bot level method"""
        b_obj = bot.Bot()
        b_obj.set_bot_level()
        self.assertEqual(b_obj.level, "normal")

    @patch('builtins.input', return_value = 'h')
    def test_set_bot_level_hard(self, mock_input):
        """test set bot level method"""
        b_obj = bot.Bot()
        b_obj.set_bot_level()
        self.assertEqual(b_obj.level, "hard")

    def test_set_iterations_n(self):
        """test set iterations method"""
        b_obj = bot.Bot()
        b_obj.level = "normal"
        b_obj.set_iterations()
        self.assertTrue(2 <= b_obj.iterations <= 4)

    def test_set_iterations_h(self):
        """test set iterations method"""
        b_obj = bot.Bot()
        b_obj.level = "hard"
        b_obj.set_iterations()
        self.assertTrue(5 <= b_obj.iterations <= 8)

    @patch("bot.Bot.print_score")
    def test_bot_turn(self, mock_print):
        """test bot turn method"""
        b_obj = bot.Bot()
        b_obj.level = "normal"
        b_obj.bot_turn()
        self.assertTrue(mock_print.called)
