from __future__ import annotations
from cards import Card, Rank, Suit


class Player:

    def __init__(self, name: str) -> None:
        """
        This method initialize a Player object with instances variables: 
            - name: user input / AI name
            - hand: empty list at the beginning 
            - round_score: score of each round
            - total_score: total score of every played rounds
        """
        self.name = name
        self.hand = []
        self.round_score = 0
        self.total_score = 0
        
    def __repr__(self):
        return self.__str__()

    def __str__(self) -> str:
        return str(self.name)

    def check_valid_play(self, card: Card, trick: list[Card], broken_hearts: bool) -> tuple[bool, str]:  # return a tuple (boolean, "Player still has cards from the suit of the current trick")
        """
        The method check if the card that player choose to play is valid or not

        Argument:
            - card: the card player choose to play
            - trick: a list of cards that have been played in the current trick
            - broken_hearts: boolean, condition if the hearts have been broken or not
        
        Return:
            - a tuple:
                + tuple[0]: boolean logic -> valid play or not
                + tuple[1]: a string
        """
        
        # return this tuple if the card is invalid
        invalid = (False, """
████████████████████████████████████
█▄─▄▄─█▄─▄▄▀█▄─▄▄▀█─▄▄─█▄─▄▄▀█░█░█░█
██─▄█▀██─▄─▄██─▄─▄█─██─██─▄─▄█▄█▄█▄█
▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▄▀▄▄▀▄▄▀▄▀▄▀▄▀
        """)

        valid = (True, "") # return this tuple if the card is valid

        two_of_clubs = Card(Rank.Two, Suit.Clubs) # the smallest card in the deck, also the player holding this card have to lead the first trick

        queen_of_spades = Card(Rank.Queen, Suit.Spades)
        
        if len(trick) == 0:  # the player is leading the trick
            if two_of_clubs in self.hand and card != two_of_clubs:  # if the player is leading, has a two of clubs in his hand but not play it => invalid move
                return invalid
            if card.suit == Suit.Hearts and broken_hearts is False:  # if the card that player play is a heart
                for each_card in self.hand:                                 # loop through the hand of the player, if there is still an option
                    if each_card.suit != Suit.Hearts:                # which means a card that is not a heart
                        return invalid                                      # this is an invalid move
                        
        else:  # the player is not leading the trick
            if card.suit != trick[0].suit:  # if the played card has different suit from the leading card
                for each_card in self.hand:  # check if there is still a possible card that can be played, if there is => an invalid play
                    if each_card.suit == trick[0].suit:
                        return invalid
                if trick[0] == two_of_clubs:  # if this is the first trick of the round
                    if card.suit == Suit.Hearts or card == queen_of_spades:  # the player cannot play hearts or queen of spades
                        return invalid  # this is an invalid move
        return valid  # any other cases are all valid
