import unittest
from bowling_game import BowlingGame

class TestBowlingGame(unittest.TestCase):
    """
    A bunch of unit test created for the BowlingGame class.
    
    The above said class contains nine unit tests that verify the correctness of the bowling game
    scoring system implementation. There are various scenarios created and tested that includes normal rolls,
    spares, strikes, and edge cases example perfect games and gutter games.
    """
    
    def setUp(self):
        """
        Set up method or function used to runs before each test case.

        """
        self.Game = BowlingGame()

    def test_gutter_game(self):
        """
        first test is created to test a gutter game where all rolls knock down zero pins in the game.
        
        A gutter game method must return result in a total score of 0.
        This test provide information whether it's correctly handles this scenario.
        """
        print("\n        First Test is => Gutter Game")
        # first of all create a list of 20 rolls, all with 0 pins
        Rolls = [0] * 20
        ExpectedScore = 0
        
        # trying to simulate all rolls in the game
        for Pins in Rolls:
            self.Game.Roll(Pins)
        
        # next calculate the actual score
        ActualScore = self.Game.Score()
        
        # print the all details
        print(f"Rolls: {Rolls}")
        print(f"Expected score: {ExpectedScore}")
        print(f"Actual score: {ActualScore}")
        print("Correct implementation:", "✓" if ActualScore == ExpectedScore else "✗")
        
        # Assert equal method used that the actual score matches the expected score
        self.assertEqual(ActualScore, ExpectedScore)

if __name__ == '__main__':
    """
    main entry point for running the tests.
    it runs all the test cases defined in this class using unittest's test runner.
    """
    unittest.main()