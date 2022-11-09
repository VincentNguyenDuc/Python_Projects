from __future__ import annotations  # for type hints of a class in itself
from enum import Enum


class Rank(Enum):
    """
    This class represents the range of ranks within a suit
    Two is the smallest rank of a card, and Ace is the highest rank of a card
    """
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13
    Ace = 14

    def __lt__(self, other):
        """
        This magic method allows you to compare ranks like regular integer types with inequality operators "<" or ">"
        """
        return self.value < other.value



class Suit(Enum):
    """
    This class represents the suit of the deck
    CLubs is the smallest suit of the class, and Hearts is the biggest sut of the class
    Clubs < Diamonds < Spades < Hearts
    """
    Clubs = 1
    Diamonds = 2
    Spades = 3
    Hearts = 4

    def __lt__(self, other: Suit) -> bool:
        """
        This magic method allows you to compare suits like regular integer types with inequality operators "<" or ">"
        """
        return self.value < other.value


class Card:
    def __init__(self, rank, suit):
        """
        This magic method initializes a Card object with instances variables rank and suit
        
        Argument: 
            - rank: rank of the card
            - suit: suit of the card
        """

        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str("{Rank} of {Suit}".format(Rank=self.rank.name, Suit=self.suit.name))

    def __eq__(self, other: Card) -> bool:
        """
        This magic method allows you to compare 2 equal card objects with equality operators "=="

        Argument:
            - other: a Card object
        
        Return: boolean
            - True: if 2 objects is the same
            - False: if not
        """

        if self.rank == other.rank and self.suit == other.suit:
            return True
        return False

    def __lt__(self, other: Card) -> bool:
        """
        This magic method allows you to compare 2 card objects with inequality operators ">" and "<"

        Argument:
            - other: a Card object

        Return:
            - True: if this Card is smaller than the other Card
            - False: if not
        """

        # Comparing the suit of 2 cards.
        if self.suit < other.suit:
            return True
        
        # If the suit is equal, then comparing the rank of 2 cards
        if self.suit == other.suit:
            if self.rank < other.rank:
                return True
        return False
