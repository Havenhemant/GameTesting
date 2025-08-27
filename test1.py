import unittest
from bowling_game import BowlingGame
class TestBowlingGame(unittest.TestCase):
    def setUp(self):
        self.game = BowlingGame()
    def test_gutter_game(self):
        for i in range(20):
            self.game.roll(0)
        self.assertEqual(self.game.score(), 0)
    def test_all_ones(self):
        for i in range(20):
            self.game.roll(1)
        self.assertEqual(self.game.score(), 20)
    def test_one_spare(self):
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        for i in range(17):
            self.game.roll(0) 
        self.assertEqual(self.game.score(), 16)
    def test_one_strike(self):
        self.game.roll(10)  
        self.game.roll(3)
        self.game.roll(4)
        for i in range(16):
            self.game.roll(0)
        self.assertEqual(self.game.score(), 24)
    def test_consecutive_strikes(self):
        self.game.roll(10)  
        self.game.roll(10)  
        self.game.roll(4)
        self.game.roll(2)
        for i in range(14):
            self.game.roll(0)
        self.assertEqual(self.game.score(), 46)
    def test_spare_in_last_frame(self):
        for i in range(18):
            self.game.roll(0)
        self.game.roll(5)
        self.game.roll(5)  
        self.game.roll(3)  
        self.assertEqual(self.game.score(), 13)
    def test_strike_in_last_frame(self):
        for i in range(18):
            self.game.roll(0)
        self.game.roll(10)  
        self.game.roll(3)   
        self.game.roll(4)  
        self.assertEqual(self.game.score(), 17)
    def test_perfect_game(self):
        for i in range(12):
            self.game.roll(10)
        self.assertEqual(self.game.score(), 300)
    def test_all_spares(self):
        for i in range(21):
            self.game.roll(5)
        self.assertEqual(self.game.score(), 150)
if __name__ == '__main__':
    unittest.main()