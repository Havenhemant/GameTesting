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
        print(f"rolls : {Rolls}")
        print(f"expected score : {ExpectedScore}")
        print(f"actual score : {ActualScore}")
        print("correct implementation :", "✓" if ActualScore == ExpectedScore else "✗")
        
        # Assert equal method used that the actual score matches the expected score
        self.assertEqual(ActualScore, ExpectedScore)
    def test_all_ones(self):
        """
        next   test or second test a   game where all rolls knock down exactly one pin.
        
        This   could   provide   result in a total score of 20 and 1 pin per roll x 20 rolls.
        without any spares or strikes.
        """
        print("\n Test case where All Ones")
        # create a list of 20 rolls and all with 1 pin
        Rolls = [1] * 20
        ExpectedScore = 20
        
        # try to simulate all rolls in the game
        for Pins in Rolls:
            self.Game.Roll(Pins)
        
        # try to calculate the actual score
        ActualScore = self.Game.Score()
        
        # print   test   data
        print(f"rolls : {Rolls}")
        print(f"expected score : {ExpectedScore}")
        print(f"actual score : {ActualScore}")
        print("correct implementation : ", "✓" if ActualScore == ExpectedScore else "✗")
        
        # testing actual score match the expected score or not
        self.assertEqual(ActualScore, ExpectedScore)
    def test_one_spare(self):
        """
        trying to test a game with one spare followed by a normal roll.
        and trying to calculate a spare is when all 10 pins are knocked down in two rolls in a frame of game.
        The spare bonus adds the next rolls pins to the spare frame.
        
        """
        print("\nTest: One Spare")
        # First frame contains spare (5 + 5), second frame contains first roll 3 pins, then zeros for remaining rolls
        Rolls = [5, 5, 3] + [0] * 17
        ExpectedScore = 16  # 10 spare + 3 bonus + 3 next roll = 16
        
        # trying to simulate all rolls in the game
        for Pins in Rolls:
            self.Game.Roll(Pins)
        
        # try to calculate the actual score
        ActualScore = self.Game.Score()
        
        # print all data
        print(f" rolls: {Rolls}")
        print(f" expected score: {ExpectedScore}")
        print(f" actual score: {ActualScore}")
        print(" correct implementation:", "✓" if ActualScore == ExpectedScore else "✗")
        
        # using assert function testing actual score match the expected score or not
        self.assertEqual(ActualScore, ExpectedScore)
    def test_one_strike(self):
        """
        trying to test a game with one strike followed by normal rolls in the pins game.
        and  strike   is when all 10 pins are knocked down in the first roll of a frame in the game.
        and strike bonus adds the next two rolls pins to the strike frame.
    
        """
        print("\nTest: One Strike")
        # First frame contains strike 10 and same as second frame contains rolls 3 and 4, and then zeros for remaining rolls
        Rolls = [10, 3, 4] + [0] * 16
        ExpectedScore = 24  # 10 + 3+4 bonus + 3 + 4 = 24
        
    
        for Pins in Rolls:
            self.Game.Roll(Pins)

        ActualScore = self.Game.Score()
        
       
        # print all data
        print(f" rolls: {Rolls}")
        print(f" expected score: {ExpectedScore}")
        print(f" actual score: {ActualScore}")
        print(" correct implementation:", "✓" if ActualScore == ExpectedScore else "✗")
        
        # using assert function testing actual score match the expected score or not
        self.assertEqual(ActualScore, ExpectedScore)
    def test_consecutive_strikes(self):
        """
        fifth test a game with consecutive strikes.
    
        First strike: 10 + next two rolls that is 10 + 4 = 24
        Second strike: 10 + next two rolls that is 4 + 2 = 16
        Third frame: 4 + 2 = 6
        Total: 24 + 16 + 6 = 46
        """
        print("\n next test : consecutive Strikes")
       
        Rolls = [10, 10, 4, 2] + [0] * 14
        ExpectedScore = 46  # 10+(10+4)=24, 10+(4+2)=16, 4+2=6 → 24+16+6=46
        
     
        for Pins in Rolls:
            self.Game.Roll(Pins)
      
        ActualScore = self.Game.Score()

        # print all data
        print(f" rolls: {Rolls}")
        print(f" expected score: {ExpectedScore}")
        print(f" actual score: {ActualScore}")
        print(" correct implementation:", "✓" if ActualScore == ExpectedScore else "✗")
        
        # using assert function testing actual score match the expected score or not
        self.assertEqual(ActualScore, ExpectedScore)
    def test_spare_in_last_frame(self):
        """
        next sixth test a game with a spare in the last 10th frame.
        
        The 10th frame has special rules suppose if you get a spare and you get an extra roll in the pins game.
        and next caluclate that the bonus for the spare is the pins from the extra roll.
        expected score is : 5 + 5 spare + 3 bonus = 13
        """
        print("\nTest: Spare in Last Frame")
   
        Rolls = [0] * 18 + [5, 5, 3]
        ExpectedScore = 13 
        
        for Pins in Rolls:
            self.Game.Roll(Pins)
        
        ActualScore = self.Game.Score()

        # print all data
        print(f" rolls: {Rolls}")
        print(f" expected score: {ExpectedScore}")
        print(f" actual score: {ActualScore}")
        print(" correct implementation:", "✓" if ActualScore == ExpectedScore else "✗")
        
        # using assert function testing actual score match the expected score or not
        self.assertEqual(ActualScore, ExpectedScore)
    def test_strike_in_last_frame(self):
        print("\nTest: Strike in Last Frame")
        # First 9 frames and all zeros, 10th frame with strike and two extra rolls 3 and 4
        Rolls = [0] * 18 + [10, 3, 4]
        ExpectedScore = 17  # 10+3+4 = 17
        

        for Pins in Rolls:
            self.Game.Roll(Pins)

        ActualScore = self.Game.Score()
        
        # print all data
        print(f" rolls: {Rolls}")
        print(f" expected score: {ExpectedScore}")
        print(f" actual score: {ActualScore}")
        print(" correct implementation:", "✓" if ActualScore == ExpectedScore else "✗")
        
        # using assert function testing actual score match the expected score or not
        self.assertEqual(ActualScore, ExpectedScore)
    def test_perfect_game(self):
        """
        at last test a perfect game with all strikes.
        
        Total: 10 frames x 30 points = 300
        """
        print("\n last test : Perfect Game")
        # 12 strikes: 10 regular frames + 2 bonus rolls in the 10th frame
        Rolls = [10] * 12
        ExpectedScore = 300  # Perfect game score
        
      
        for Pins in Rolls:
            self.Game.Roll(Pins)
        
  
        ActualScore = self.Game.Score()
        
        
        print(f" rolls: {Rolls}")
        print(f" expected score: {ExpectedScore}")
        print(f" actual score: {ActualScore}")
        print(" correct implementation:", "✓" if ActualScore == ExpectedScore else "✗")
        
        # using assert function testing actual score match the expected score or not
        self.assertEqual(ActualScore, ExpectedScore)
if __name__ == '__main__':
    """
    main entry point for running the tests.
    it runs all the test cases defined in this class using unittest's test runner.
    """
    unittest.main()