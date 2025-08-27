import unittest
from bowling_game import BowlingGame 
class TestBowlingGame(unittest.TestCase):
    def setUp(self):
        self.game = BowlingGame()
    def roll_many(self, rolls):
        for pins in rolls:
            self.game.roll(pins)
    def test_all_gutter_game(self):
        self.roll_many([0] * 20)
        self.assertEqual(self.game.score(), 0)
    def test_all_ones(self):
        self.roll_many([1] * 20)
        self.assertEqual(self.game.score(), 20)
    def test_one_spare(self):
        self.roll_many([5, 5, 3] + [0] * 17)
        self.assertEqual(self.game.score(), 16)
    def test_one_strike(self):
        self.roll_many([10, 3, 4] + [0] * 17)
        self.assertEqual(self.game.score(), 24)
    def test_perfect_game(self):
        self.roll_many([10] * 12)
        self.assertEqual(self.game.score(), 300)
    def test_tenth_frame_spare(self):
        self.roll_many([0] * 18 + [5, 5, 5])
        self.assertEqual(self.game.score(), 15)
    def test_tenth_frame_strike(self):
        self.roll_many([0] * 18 + [10, 10, 10])
        self.assertEqual(self.game.score(), 30)
if __name__ == '__main__':
    unittest.main()
