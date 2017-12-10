"""Let 0b1000 = diamonds
Let 0b0100 = clubs
Let 0b0010 = hearts
Let 0b0001 = spades"""

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
