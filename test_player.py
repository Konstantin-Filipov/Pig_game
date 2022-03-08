import unittest
import Player

class TestPlayerClass(unittest.TestCase):
    player_list = []

    def testing_default_objects(self):
        """Instantiating a player object"""
        player_id = player.Player()

        self.assertIsInstance(player_id,player.Player())
        
        namn = 'Jane'
        point = 0
        self.assertEquals(namn,point)


    def add_objects_to_list(player_list):
        """adding a player objects to a list"""
        player_id = player.Player('Jane',0)
        player_one = player.Player('John',0)
        
        player_id.add()
        player_one.add()

    def test_updating_score(self):
        """Updating the score of each player"""
        player_id = player.Player('Jane',3)
        player_one = player.Player('John',1)
        
        player_id.update_score()
        player_one.update_score()

    def test_sort_score_list(player_list):
        """getting the scores of players and sorting the list by it scores"""
        player_list.sort()
        









