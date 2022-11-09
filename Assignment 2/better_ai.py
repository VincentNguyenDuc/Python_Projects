from __future__ import annotations
from cards import Card, Rank, Suit
from player import Player


class BetterAIPlayer(Player):

    def __init__(self, name: str) -> None:
        super().__init__(name)

    
    def play_card(self, trick: list[Card], broken_hearts: bool) -> Card:
        """
        This method return the cart that better AI plays
        Strategy: - if the hearts have not been broken, then play the highest card possible, 
                  - else play the smallest card possible.

        Argument: 
            - trick: a list of cards that have been played so far in the current trick
            - broken_hears: boolean, hearts have been broken or not
        Return:
            - a Card object
        """
        if broken_hearts is True: # if the hearts have been broken
            card_play = Card(Rank.Ace, Suit.Hearts)  # the biggest card possible
            # find the smallest valid card in player's hand
            for each_card in self.hand:
                if each_card < card_play and self.check_valid_play(each_card, trick, broken_hearts)[0] is True:
                    card_play = each_card  

        elif broken_hearts is False: # if the hearts have not been broken
            # sort the self.hand in descending order (bigger card comes first), then copy it to card_list
            card_list = sorted(self.hand, reverse=True)[:]

            # loop through card_list
            for each_card in card_list:
                if self.check_valid_play(each_card, trick, broken_hearts)[0] is True:  # if it is valid, then it will be the highest valid card
                    card_play = each_card
        
        # remove the selected card
        self.hand.remove(card_play)

        return card_play


    def pass_cards(self) -> Card:
        """
        This method chooses 3 cards to pass according to 3 rules:
            - Always pass the Two of clubs
            - Never pass the Ace of clubs
            - Pass the cards with the highest rank 
        
        Return:
            - a list contains top 3 highest card in the player's hand
        """
        card_pass = []
        two_of_clubs = Card(Rank.Two, Suit.Clubs)
        ace_of_clubs = Card(Rank.Ace, Suit.Clubs)
        number_of_cards_to_pass = 3
        # 1. Always pass the 2 of clubs
        if two_of_clubs in self.hand:
            card_pass.append(two_of_clubs)
            self.hand.remove(two_of_clubs)
            number_of_cards_to_pass -= 1

        # 2. Never pass the Ace of Clubs
        for i in range(number_of_cards_to_pass): 
            smallest_rank = Rank.Two
            card_to_pass = ""
            for each_card in self.hand:
                if each_card == ace_of_clubs:
                    continue
                if each_card.rank > smallest_rank:
                    # 3. Pass the card with highest rank but not the Ace of Clubs
                    smallest_rank = each_card.rank
                    card_to_pass = each_card
            card_pass.append(card_to_pass)
            self.hand.remove(card_to_pass)

        return card_pass