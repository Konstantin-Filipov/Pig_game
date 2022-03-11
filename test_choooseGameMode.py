import unittest
import sys
import chooseGameMode

class Test_chooseGameMode(unittest.TestCase):

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        res = chooseGameMode.ChooseGameMode()
        exp = chooseGameMode.ChooseGameMode
        self.assertIsInstance(res, exp)
