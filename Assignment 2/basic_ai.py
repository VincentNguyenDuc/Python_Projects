from __future__ import annotations
from cards import Card, Rank, Suit
from player import Player


class BasicAIPlayer(Player):
    
    def __init__(self, name: str) -> None:
        super().__init__(name)

    
    def play_card(self, trick: list[Card], broken_hearts: bool) -> Card:
        """
        This method find the smallest valid card and return the card

        Argument: 
            - trick: a list of cards that have been played so far in the current trick
            - broken_hears: boolean, hearts have been broken or not
        Return:
            - a Card object
        """
        card_play = Card(Rank.Ace, Suit.Hearts)  # the biggest card possible

        # find the smallest valid card in player's hand
        for each_card in self.hand:  # loop through every card in the user's hand
            if each_card < card_play and self.check_valid_play(each_card, trick, broken_hearts)[0] is True:  
                card_play = each_card   
        
        # remove the card that we found 
        self.hand.remove(card_play)

        return card_play


    def pass_cards(self) -> list[Card]:
        """
        This method find 3 highest cards in the player's hand and pass them

        Return:
            - a list contains top 3 highest card in the player's hand
        """
        # get the top 3 cards
        card_pass = sorted(self.hand)[-3:]

        # remove them
        for card in card_pass:
            self.hand.remove(card)
            
        return card_pass




    

