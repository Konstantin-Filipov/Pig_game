import unittest
import dice
from unittest import mock
from unittest.mock import patch

class Testdice(unittest.TestCase):
    """ Test the dice class """

    def test_init_obj(self):
        """Instantiate an object and check its properties."""
        res = dice.Dice()
        exp = dice.Dice
        self.assertIsInstance(res, exp)

    def test_roll(self):
        """Test the roll function of the dice class and check if it's in bounds"""
        die = dice.Dice()
        res = die.roll()
        exp = 1 <= res <= 6
        self.assertTrue(exp)

    @patch("builtins.print")
    def test_dice_graph(self, mock_print):
        """Test the graphical representation of the dice"""
        die = dice.Dice()
        die.dice_graph(1)
        str = " _______\n|       |\n|   O   |\n|_______|\n"
        mock_print.assert_called_with(str)
        die.dice_graph(2)
        str = " _______\n| O     |\n|       |\n|_____O_|\n"
        mock_print.assert_called_with(str)
        die.dice_graph(3)
        str = " _______\n| O     |\n|   O   |\n|_____O_|\n"
        mock_print.assert_called_with(str)
        die.dice_graph(4)
        str = " _______\n| O   O |\n|       |\n|_O___O_|\n"
        mock_print.assert_called_with(str)
        die.dice_graph(5)
        str = " _______\n| O   O |\n|   O   |\n|_O___O_|\n"
        mock_print.assert_called_with(str)
        die.dice_graph(6)
        str = " _______\n| O   O |\n| O   O |\n|_O___O_|\n"
        mock_print.assert_called_with(str)
