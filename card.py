'''
This is a class that creates a list of the suits of cards...
'''
class Card:
    """This assigns the card rank to a suit"""
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit
    