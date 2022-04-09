import unittest
from unittest import mock
from unittest.mock import patch
import player

class TestPlayerClass(unittest.TestCase):

    @patch('builtins.input', return_value = "Koko")
    def test_setName(self, mock_input):
        """"Tests set name"""
        player_obj = player.Player(1)
        player_obj.setName()
        exp = player_obj.name == "Koko"
        self.assertTrue(exp)

    def test_update_score(self):
        """Test update_score() method."""
        player_obj = player.Player(1)
        add = 6
        res = player_obj.score + add
        player_obj.update_score(add)
        exp = player_obj.score
        self.assertEqual(res, exp)

    def test_isWinner(self):
        """test is winner method."""
        player_obj = player.Player(1)
        player_obj.score = 100
        res = player_obj.isWinner()
        exp = True
        self.assertEqual(res, exp)

    def test_remove_points(self):
        """test remove points from turn"""
        player_obj = player.Player(1)
        player_obj.score = 10
        player_obj.score_turn = 4
        res = player_obj.score - player_obj.score_turn
        exp = player_obj.remove_points()
        self.assertEqual(res, exp)

    def test_cheat(self):
        """test cheat method"""
        player_obj = player.Player(1)
        player_obj.cheat()
        self.assertEqual(player_obj.isCheater, True)
