from random import choice

class Possibility:
    """

    """
    def dice_roll(self):
        return choice("1", "2", "3", "4", "5", "6")

    def head_tail(self):
        return choice("Head", "Tail")

    def rock_paper_scissors(self):
        return choice("rock", "paper", "scissors")