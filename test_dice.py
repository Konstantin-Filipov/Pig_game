import unittest
import dice

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

    def test_diceFace(self):
        
        """Test the graphical representation of the dice"""

        die = dice.Dice()
        self.assertEqual(die.dice_graph(1)," _______\n|       |\n|   O   |\n|_______|\n")
        self.assertEqual(die.dice_graph(2)," _______\n| O     |\n|       |\n|_____O_|\n")
        self.assertEqual(die.dice_graph(3)," _______\n| O     |\n|   O   |\n|_____O_|\n")
        self.assertEqual(die.dice_graph(4)," _______\n| O   O |\n|       |\n|_O___O_|\n")
        self.assertEqual(die.dice_graph(5)," _______\n| O   O |\n|   O   |\n|_O___O_|\n")
        self.assertEqual(die.dice_graph(6)," _______\n| O   O |\n| O   O |\n|_O___O_|\n")


if __name__ == '__main__':
    unittest.main()
