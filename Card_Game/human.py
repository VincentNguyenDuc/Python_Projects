from __future__ import annotations
from cards import Card, Rank, Suit
from player import Player
from time import sleep

class HumanPlayer(Player):
	
    def __init__(self) -> None: 
        """
        This method initialize a Player object with instances variables: 
            - name: user input 
            - hand: empty list at the beginning 
            - round_score: score of each round
            - total_score: total score of every played rounds
        """
        self.hand = []
        self.name = input("Please enter your name: ")
        self.round_score = 0
        self.total_score = 0
    
    def int_input(self, prompt="", restricted_to=None):
        """
        Helper function that modifies the regular input method,
        and keeps asking for input until a valid one is entered. Input 
        can also be restricted to a set of integers.

        Arguments:
            - prompt: String representing the message to display for input
            - restricted: List of integers for when the input must be restricted
                        to a certain set of numbers

        Returns the input in integer type.
        """

        # print this string if the user input is invalid
        invalid_display = """
████████████████████████████████████
█▄─▄▄─█▄─▄▄▀█▄─▄▄▀█─▄▄─█▄─▄▄▀█░█░█░█
██─▄█▀██─▄─▄██─▄─▄█─██─██─▄─▄█▄█▄█▄█
▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▄▀▄▄▀▄▄▀▄▀▄▀▄▀
"""
        while True: # while loop
            player_input = input(prompt) # get the input from the user
            try:
                int_player_input = int(player_input) # check if the input is an integer
            except ValueError:
                print(invalid_display) # if the user input is not an integer and ValueError occured,
                continue               # print error message, continue to the next loop, and let the user input 
            if restricted_to is None:  # if the input is an integer and there is no restricted, break the loop and return the value
                break
            elif int_player_input in restricted_to:  # if the input is in the allowed list, break the loop and return the value
                break 
            elif int_player_input not in restricted_to:  # if the input is not in the allowed list, print error message and let the user input again
                print(invalid_display)

        return int_player_input
    
    def cards_art(self, cards):
        """
        The method creates the text art of cards in user's hand, following this format:
            "┌───────┐┌───────┐┌───────┐┌───────┐┌───────┐┌───────┐┌───────┐┌───────┐┌───────┐┌───────┐┌───────┐┌───────┐┌───────┐" + '\n'
            "│10     ││Q      ││8      ││5      ││4      ││7      ││6      ││5      ││7      ││J      ││6      ││K      ││6      │" + '\n'
            "│   ♥   ││   ♥   ││   ♥   ││   ♠   ││   ♠   ││   ♥   ││   ♦   ││   ♣   ││   ♦   ││   ♣   ││   ♥   ││   ♣   ││   ♠   │" + '\n'
            "│     10││      Q││      8││      5││      4││      7││      6││      5││      7││      J││      6││      K││      6│" + '\n'
            "└───────┘└───────┘└───────┘└───────┘└───────┘└───────┘└───────┘└───────┘└───────┘└───────┘└───────┘└───────┘└───────┘" + '\n'
            "    0        1        2        3        4        5        6        7        8        9       10       11       12    " + '\n'
        
        Arguments: a list of Card objects
        Return: a string display the card art of user's hand 

        """
        cards_art_suits = {
            Suit.Hearts:    "│   ♥   │",
            Suit.Diamonds:  "│   ♦   │",
            Suit.Clubs:     "│   ♣   │",
            Suit.Spades:    "│   ♠   │"
        }
        cards_art_up =      "┌───────┐"
        cards_art_down =    "└───────┘"
        cards_art_ranks = {
            Rank.Two:   ["│2      │", 
                         "│      2│"],

            Rank.Three: ["│3      │", 
                         "│      3│"],

            Rank.Four:  ["│4      │", 
                         "│      4│"],

            Rank.Five:  ["│5      │", 
                         "│      5│"],

            Rank.Six:   ["│6      │", 
                         "│      6│"],

            Rank.Seven: ["│7      │", 
                         "│      7│"],

            Rank.Eight: ["│8      │", 
                         "│      8│"],

            Rank.Nine:  ["│9      │", 
                         "│      9│"],

            Rank.Ten:   ["│10     │", 
                         "│     10│"],

            Rank.Jack:  ["│J      │", 
                         "│      J│"],

            Rank.Queen: ["│Q      │", 
                         "│      Q│"],

            Rank.King:  ["│K      │", 
                         "│      K│"],

            Rank.Ace:   ["│A      │", 
                         "│      A│"],
        }

        display_card = ""  # initialize a string, which is the text art of cards in user's hand
        length_of_list = len(cards)  # the number of cards in user's hand
        # create the first line of the text art
        for i in range(length_of_list):
            display_card += cards_art_up
        display_card += '\n'  # add '\n' to move to the next line

        # add the second line of the text art (which including the rank of the card)
        for card in cards:
            display_card += cards_art_ranks[card.rank][0]  # using the rank of the card as a key to access the dictionary cards_art_ranks
        display_card += '\n'

        # add the third line of the text art (which including the suit of the card)
        for card in cards:
            display_card += cards_art_suits[card.suit]  # using the suit of the card as a key to access the dictionary cards_art_suits
        display_card += '\n'

        # add the fourth line of the text art (which including the rank of the card)
        for card in cards:
            display_card += cards_art_ranks[card.rank][1]  # using the rank of the card as a key to access the dictionary cards_art_ranks
        display_card += '\n'

        # add the last line of the text art 
        for i in range(length_of_list):
            display_card += cards_art_down
        display_card += '\n'

        # add the index below the card
        for i in range(length_of_list):
            if i < 10: 
                display_card += f"    {i}    "  # format with 1 digit number
            else:
                display_card += f"   {i}    "   # format with 2 digit number, so that every index will be straight with every cards
        display_card += '\n'
        
        return display_card


    def play_card(self, trick, broken_hearts) -> Card:
        """
        The method get the input from user (which is the index of a card), and check if it is a valid card
        If the card is valid, then the user can play the card
        If not error message is printed

        Argument: 
            - trick: a list of cards that have been played so far in the current trick
            - broken_hears: boolean, hearts have been broken or not
        """
        sleep(0.5)
        print("""
█▄█ █▀█ █░█ █▀█   █▀▀ █░█ █▀█ █▀█ █▀▀ █▄░█ ▀█▀   █░█ ▄▀█ █▄░█ █▀▄ ▀
░█░ █▄█ █▄█ █▀▄   █▄▄ █▄█ █▀▄ █▀▄ ██▄ █░▀█ ░█░   █▀█ █▀█ █░▀█ █▄▀ ▄
        """)
        print(self.cards_art(self.hand))  # print the text art of the card in user's hand
        
        number_of_card = len(self.hand)   # number of card in user's hand 

        condition = False  # condition to check if whether to continue or get out of the loop
        while condition is False:  # if condition is False keep looping
            card_index = self.int_input(prompt="Select a card to play: ", restricted_to=list(range(number_of_card)))  # get the index of the card from the user, the input must be integer, and restricted to the index of the card
            card = self.hand[card_index]  # get the card from the index
            check = self.check_valid_play(card, trick, broken_hearts)  # check if that card is valid
            if check[0] is True:  # if the card is valid
                condition is True # Change condition to True
                self.hand.remove(card)  # Remove the card from the user's hand
                return card  # Return the card
            else:
                print(check[1])  # if the card is not valid, print error message and ask the user to input again

    

    def pass_cards(self) -> Card:
        """
        The method gets the input from the user, evaluate if it is an legal input. Then pass the cards that user have chosen

        Return:
            - A list containing 3 cards objects that were chosen to be passed
        """
        sleep(0.5)
        print("""
█▄█ █▀█ █░█ █▀█   █▀▀ █░█ █▀█ █▀█ █▀▀ █▄░█ ▀█▀   █░█ ▄▀█ █▄░█ █▀▄ ▀
░█░ █▄█ █▄█ █▀▄   █▄▄ █▄█ █▀▄ █▀▄ ██▄ █░▀█ ░█░   █▀█ █▀█ █░▀█ █▄▀ ▄
        """)
        print(self.cards_art(self.hand))  # print the card art of user's hand
        number_of_card = len(self.hand)
        condition = False

        allowed_input_list = list(range(number_of_card))  # valid index that user can input

        # Get the input from user
        while condition is False:
            # change the condition to True, therefore, if it passes every conditional statement below, it will remain True and we can get out of the loop
            condition = True
            card_index_input = input("Select three cards to pass off (e.g. '0, 4, 5'): ").split(',')  # get the user input as a string and split them into list

            # check if every elements in the list can be transform to int
            for i in card_index_input:
                try:
                    i = int(i)  # if this cause ValueError
                except ValueError:
                    condition = False  # change condition to False
            
            if condition is False:  # the input didn't pass the  requirements, print the error message and move to the next loop
                print("You didn't read the instructions. Please input again!")
                continue

            card_index_list = list(map(int, card_index_input))  # if every elements in the list can be transform to int, then map them to type int

            # check if user only input valid index 
            card_list_count = len(card_index_list)
            for i in card_index_list:
                if i not in allowed_input_list:
                    condition = False
            
            # check if user only input 3 values
            if card_list_count != 3:
                condition = False
            
            # check if user input duplicates
            if card_list_count != len(set(card_index_list)):
                condition = False

            if condition is False:
                print("You didn't read the instructions. Please input again!")

        # passing cards that the player choose to pass
        passing_cards = []
        for index in card_index_list:
            card_to_pass = self.hand[index]
            passing_cards.append(card_to_pass)

        # remove the cards that have been pass out of the player's hand
        for card in passing_cards:
            self.hand.remove(card)
        print("Cards are being passed")
        sleep(0.7)
        print("""
█░░ █▀█ ▄▀█ █▀▄ █ █▄░█ █▀▀ ░ ░ ░
█▄▄ █▄█ █▀█ █▄▀ █ █░▀█ █▄█ ▄ ▄ ▄
""")
        sleep(0.7)
        print("Cards have been passed")
        return passing_cards
        


        









