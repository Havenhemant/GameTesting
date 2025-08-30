class BowlingGame:
    """Above said BowlingGame class create for a game of 10 pin bowling and calculate scores accordingly.
    
    This class used to implement with standard scoring rules for ten pin bowling game,
    this class include different functions like strikes, spares, and the special rules for the 10th frame.
    """
    
    def __init__(self):
        """Initialize a new bowling game using the constructor function.
        
        Creates an empty list to store the rolls pins knocked down for the game.
        """
        self.Rolls = []
    
    def Roll(self, Pins):
        """Record the number of pins knocked down in a roll.
        
        Parameters:
        Pins in int datatype: The number of pins knocked down in this roll from 0 to 10
        """
        self.Rolls.append(Pins)
    
    def Score(self):
        """above score function calculate and return the total score for the pins knocked game.
        Returns:
        The total score for the game calculate in the integer data type, score is calculated according to bowling rules
        including bonuses for strikes and spares.
        
        the above said function iterates through each frame, checking for strikes and spares in the game,
        and calculates the relevant bonuses based on subsequent rolls.
        """
        TotalScore = 0
        FrameIndex = 0
        # For loop iterate 0 to 9 means ten times
        # Refractor the game here because provided code contain 9 iterations only in For Loop
        for Frame in range(10):
            if self.IsStrike(FrameIndex):
                # first if condition track we don't go out of bounds for the last frame in the game
                if FrameIndex + 2 < len(self.Rolls):
                    TotalScore += 10 + self.StrikeBonus(FrameIndex)
                FrameIndex += 1
            elif self.IsSpare(FrameIndex):
                # next elif condition track we don't go out of bounds for the last frame in the game
                if FrameIndex + 2 < len(self.Rolls):
                    TotalScore += 10 + self.SpareBonus(FrameIndex)
                FrameIndex += 2
            else:
                # last condition track we have at least two rolls for this frame in the game
                if FrameIndex + 1 < len(self.Rolls):
                    TotalScore += self.SumOfBallsInFrame(FrameIndex)
                FrameIndex += 2
        return TotalScore
    def IsStrike(self, FrameIndex):
        """Next function check if the roll at the given index is a strike.
        
        Parameters:
        FrameIndex in Integer Data Type: The index in the Rolls list to check
        
        Returns:
        bool: it's return true if the roll is a strike 10 pins, False otherwise
        """
        return FrameIndex < len(self.Rolls) and self.Rolls[FrameIndex] == 10
    
    def IsSpare(self, FrameIndex):
        """next above said function or method check if the two rolls starting at the given index form a spare.
        
        Parameters:
        FrameIndex integer data type: The starting index in the Rolls list to check
        
        Returns:
        bool: Next we check true if the sum of two consecutive rolls is 10 a spare, False otherwise
        """
        return (FrameIndex + 1 < len(self.Rolls) and 
                self.Rolls[FrameIndex] + self.Rolls[FrameIndex + 1] == 10)
    
    def StrikeBonus(self, FrameIndex):
        """Above StrikeBonus method calculate the bonus points for a strike.
        
        Parameters:
        FrameIndex Integer Data Type: The index of the strike roll
        
        Returns:
        It return ehe sum of the next two rolls after the strike in the pins Kno
        """
        return self.Rolls[FrameIndex + 1] + self.Rolls[FrameIndex + 2]
    
    def SpareBonus(self, FrameIndex):
        """ Last Spare bonus method used to calculate the bonus points for a spare in the game.
        
        Parameters:
        FrameIndex Integer Data type: The index of the first roll in the spare
        
        Returns:
        integer Data type: this function returns number of pins knocked down in the next roll after the spare
        """
        return self.Rolls[FrameIndex + 2]
    # New function added in the provided code or refractor existing code to calculate the sum of two rolls in a frame with no strike or spare
    def SumOfBallsInFrame(self, FrameIndex):
        """Above function used to calculate the sum of two rolls in a frame with no strike or spare
        
        Parameters:
        FrameIndex Integer Data Type: The index of the first roll in the frame
        
        Returns:
        integer Return value: The sum of two consecutive rolls
        """
        return self.Rolls[FrameIndex] + self.Rolls[FrameIndex + 1]