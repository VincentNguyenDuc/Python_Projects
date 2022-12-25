from __future__ import annotations
from random import shuffle
from better_ai import BetterAIPlayer
from cards import Card, Rank, Suit
from basic_ai import BasicAIPlayer
from human import HumanPlayer
from round import Round


class Hearts:
    # Class variables
    suit_list = [Suit.Clubs, Suit.Spades, Suit.Diamonds, Suit.Hearts]
    rank_list = [Rank.Two, Rank.Three, Rank.Four, Rank.Five, Rank.Six, Rank.Seven, Rank.Eight, Rank.Nine, Rank.Ten, Rank.Jack, Rank.Queen, Rank.King, Rank.Ace]

    def __init__(self) -> None:
        print("""
░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ████████╗░█████╗░  ██╗░░██╗███████╗░█████╗░██████╗░████████╗░██████╗
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ╚══██╔══╝██╔══██╗  ██║░░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ░░░██║░░░██║░░██║  ███████║█████╗░░███████║██████╔╝░░░██║░░░╚█████╗░
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ░░░██║░░░██║░░██║  ██╔══██║██╔══╝░░██╔══██║██╔══██╗░░░██║░░░░╚═══██╗
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ░░░██║░░░╚█████╔╝  ██║░░██║███████╗██║░░██║██║░░██║░░░██║░░░██████╔╝
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ░░░╚═╝░░░░╚════╝░  ╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═════╝░
""")
        self.target_score = self.int_input("Please enter a target score to end the game: ")  # get the target score from the user input
        self.number_of_players = self.int_input("Please enter the number of players (3-5): ", [3, 4, 5])  # get the number of players from the user input
        self.game_play()

    def int_input(self, prompt="", restricted_to=None):
        """
        Helper function that modifies the regular input method,
        and keeps asking for input until a valid one (which is a positive integer) is entered. Input
        can also be restricted to a set of integers.

        Arguments:
          - prompt: String representing the message to display for input
          - restricted: List of integers for when the input must be restricted
                        to a certain set of numbers

        Returns the input in integer type.
        """
        invalid_display = """
████████████████████████████████████
█▄─▄▄─█▄─▄▄▀█▄─▄▄▀█─▄▄─█▄─▄▄▀█░█░█░█
██─▄█▀██─▄─▄██─▄─▄█─██─██─▄─▄█▄█▄█▄█
▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▄▀▄▄▀▄▄▀▄▀▄▀▄▀
"""
        while True:
            player_input = input(prompt)  # get the input from the user
            try:
                int_player_input = int(player_input)  # check if it can be changed to int
                if int_player_input <= 0:  # restricted so that the input always > 0
                    print(invalid_display)  # if player input a number that <= 0, then print the error message and ask the user to input again
                    continue
            except ValueError:  # the input cannot be changed to int
                print(invalid_display)
                continue
            if restricted_to is None:
                break
            else:
                if int_player_input in restricted_to:
                    break
                else:
                    print(invalid_display)
                    continue
        return int_player_input


    def deck_generator(self):
        """
        This method returns a list of cards containing all 52 possible cards of a deck

        Arguments: None

        Returns: a list of cards
        """
    
        deck = []  # the list contains every card, initialize as empty list at the beginning
        for suit in self.suit_list:  # sort through every suits 
            for rank in self.rank_list:  # sort through every ranks
                deck.append(Card(rank, suit))  # get the combination of every suits and ranks and append it to deck => we get 52 cards

        # remove two of diamonds if the number of players is 3
        if self.number_of_players == 3:
            deck.remove(Card(Rank.Two, Suit.Diamonds))

        # remove two of diamonds and two of spades if the number of players is 5
        elif self.number_of_players == 5:
            deck.remove(Card(Rank.Two, Suit.Diamonds))
            deck.remove(Card(Rank.Two, Suit.Spades))

        # randomly shuffle the deck
        shuffle(deck)

        return deck
    
    def player_generator(self):
        """
        This method returns a list of Player objects.

        Arguments: None

        Returns: a list of BasicAIPlayer objects
        """
        players = []  # the list of players playing the game

        user = HumanPlayer()  # the first player is the user
        players.append(user)

        better_ai_player = BetterAIPlayer("Player 1")  # the second player is the better AI Player, call it "Player 1"
        players.append(better_ai_player)

        # the rest are basic AI players
        for i in range(2, self.number_of_players):
            players.append(BasicAIPlayer(f"Player {i}"))

        return players   

    def dealing_cards(self, deck, players):
        """
        This method deal card to player hand. 

        Arguments: None

        Returns: None
        """
        number_1 = 0
        number_2 = len(deck) / len(players)
        count = len(deck) / len(players)
        for player in players:
            player.hand.append(deck[number_1:number_2])
            number_1 = number_2
            number_2 += count
    
        for card_index in range(len(deck)):  # loop through the deck 
            player_index = card_index % self.number_of_players  # get the index of the player that we will pass the current card to
            players[player_index].hand.append(deck[card_index])  # deal the card to that player

        return players
    
    def passing_card(self, players, round_tracker):
        """
        This method pass card to player hand

        Arguments: 
            - players: list of players
            - round_tracker: the round number
        
        Return: a list of players (hand updated)
        """
        pass_index = round_tracker % self.number_of_players  # get the step that we need to pass 
        pass_list = []  # this list contain every cards that will be pass, store in a list of list
        
        # loop through every players and get a list of 3 cards that they are going to pass
        for player in players:
            card_pass = player.pass_cards()
            pass_list.append(card_pass)  # then append that list to pass_list => create a list of list ()

        # loop through every players and let that player take the list of cards that they will be passed
        index_tracker = 0  
        for player in players:
            player.hand = player.hand + pass_list[index_tracker - pass_index]  
            index_tracker += 1

        return players
    
    def checking_winner(self, players):
        """
        This method check if there has been a player reach the target score 
        
        Argument: list of players
        Return: Boolean
        """
        # loop through every players and check if there is someone has reached the target score
        for player in players:
            if player.total_score >= self.target_score:
                return False
        return True
    
    def find_the_winner(self, players):
        """
        This method find the winner (after there has been a player reach the target score), and check if there is two or more player share the same lowest points
        Argument: list of players
        Return:
            - False if there are >= 2 players share the same lowest points
            - winner: player object if we have the winner (only 1 player has the lowest points )
        """
        # find the lowest point and find the player who has that point
        lowest_point = 1000000000000
        for player in players:
            if player.total_score < lowest_point:
                lowest_point = player.total_score
                winner = player
        
        # count how many people share the same lowest point
        winner_count = 0
        for player in players:
            if player.total_score == lowest_point:
                winner_count += 1
        
        # if there are more than 1 people sharing the same lowest point then the game have to keep playing
        if winner_count > 1:
            return False
        
        # else we return the winner
        return winner
    
    def round_points_display(self, players):
        """
		This method display the round score of every player after a round

		Arguement: None
		
		Return: Print the round scores of all players
		"""
        for player in players:
            player.total_score += player.round_score
            print(f"{player}'s total score: {player.total_score}")
            player.round_score = 0
    
    def shoot_the_moon(self, players):
        """
        This method check if there is a player shooting the moon, and updated the points to the total points of every players
        Argument: a list of players

        """
        # check if there has been somebody who has 26 points in a round
        condition = False
        for player in players:
            if player.round_score == 26:
                print(f"{player} has shot the mooon! Everyone else receives 26 points")
                shooter = player
                condition = True
        
        # if there is a player shooting the moon, then update the round score of every players, which will be add to the total score
        if condition == True:
            for player in players:
                if player == shooter:
                    player.round_score = 0
                else: 
                    player.round_score = 26

    def game_play(self):
        """
        This method execute the whole game
        """
        condition = True  # condition to check if the game is over
        round_tracker = 1  # keep track with the round
        players = self.player_generator()  # generate players to play the game

        while condition is True:
            print(f"\n========= Starting round {round_tracker} =========\n")

            deck = self.deck_generator()  # generate a new deck every round

            players = self.dealing_cards(deck, players)  # deal it to everybody

            players = self.passing_card(players, round_tracker)  # players pass 3 cards at the beginning of a round

            Round(players)  # execute the round

            print(f"\n========= End of round {round_tracker} =========\n")

            self.shoot_the_moon(players)  # after every round, check if there is a player shooting the moon

            self.round_points_display(players)  # display players' total points after a round

            # check if there has been a player reach the target score
            if self.checking_winner(players) is False:
                condition = False   
            
            # increment the round tracker
            round_tracker += 1

            # if there has been a player reach the target score, but there are more than 1 player have the same lowest points, then the game keep playing
            if self.find_the_winner(players) is False:
                condition = True
        
        # if the game has ended
        if condition is False:
            winner = self.find_the_winner(players)
            print("""
████████████████████████▀███████████████████████████████████████████████████████████████████
█─▄▄▄─█─▄▄─█▄─▀█▄─▄█─▄▄▄▄█▄─▄▄▀██▀▄─██─▄─▄─█▄─██─▄█▄─▄████▀▄─██─▄─▄─█▄─▄█─▄▄─█▄─▀█▄─▄█─▄▄▄▄█
█─███▀█─██─██─█▄▀─██─██▄─██─▄─▄██─▀─████─████─██─███─██▀██─▀─████─████─██─██─██─█▄▀─██▄▄▄▄─█
▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▀▄▄▄▀▀▀▄▄▄▄▀▀▄▄▄▄▄▀▄▄▀▄▄▀▀▄▄▄▀▀▄▄▄▀▄▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀
""")
            print(f"{winner} is the winner!")
    



if __name__ == "__main__":
    Hearts()