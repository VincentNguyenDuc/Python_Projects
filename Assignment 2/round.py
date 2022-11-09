from __future__ import annotations
from cards import Card, Rank, Suit
from basic_ai import BasicAIPlayer
from time import sleep


class Round:
	"""
	This class executes a round of the game

	Arguments: a list of BasicAIPlayer objects
	"""

	# Class instances
	two_of_hearts = Card(Rank.Two, Suit.Hearts)
	two_of_clubs = Card(Rank.Two, Suit.Clubs)
	queen_of_spades = Card(Rank.Queen, Suit.Spades)

	def __init__(self, players: list[BasicAIPlayer]) -> None:
		self.players = players  # argument of the class
		self.round_play()

	
	def holding_two_of_clubs(self):
		"""
		This method returns the player who has the two of clubs at the beginning of a round.

		Arguments: None

		Returns an object of class BasicAIPlayer 
		"""
		two_of_clubs = Card(Rank.Two, Suit.Clubs)  # initialize the card two of clubs
		for player in self.players:  # loop through the list of players
			if two_of_clubs in player.hand:  # if two of clubs in player hand 
				holder = player  # we get the player who is holding two of clubs
				return holder
		

	def points_calculator(self, previous_trick):
		"""
		This method returns the sum of points that the player who takes the trick earn after a trick

		Argument: List of cards that have been played in the previous trick

		Returns an int representing the points that the player get
		"""
		point = 0
		for card in previous_trick:
			if card.suit == Suit.Hearts:  # if suit of the card is Hearts, then point += 1
				point += 1
			if card == self.queen_of_spades:  # if the card is Queen of Spade, then point += 13
				point += 13
		return point
	
	
	def taking_the_trick(self, previous_trick, previous_players_list):
		"""
		This method find the highest card after a trick, and then find the player who played that card

		Argument: a list of cards that have been played in the previous trick

		Return: the player who takes the trick
		"""
		leading_card = previous_trick[0]  # leading card is the first card that was played in the previous trick

		for card in previous_trick:
			if card > leading_card and card.suit == leading_card.suit:  # find the card that is the biggest in the trick and in the same suit with the leading card => we find the card that win that trick
				leading_card = card
		
		# from the card that win the trick, we can find the player who won the trick
		card_index = previous_trick.index(leading_card)
		player = previous_players_list[card_index]
		return player
	

	def heart_broken(self, card_play, broken_hearts_condition):
		"""
		This method checks whether hearts have been broken. If hearts have been broken then print the annoucement and change the condition of broken_hearts

		Argument: the card that have been played and the hearts_broken condition
		Return: the new condition of hearts_broken
		"""
		if card_play.suit == Suit.Hearts and broken_hearts_condition is False:
				broken_hearts_condition = True
				sleep(0.7)
				print("""
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█─█─█▄─▄▄─██▀▄─██▄─▄▄▀█─▄─▄─█─▄▄▄▄███─█─██▀▄─██▄─█─▄█▄─▄▄─███▄─▄─▀█▄─▄▄─█▄─▄▄─█▄─▀█▄─▄██▄─▄─▀█▄─▄▄▀█─▄▄─█▄─█─▄█▄─▄▄─█▄─▀█▄─▄█
█─▄─██─▄█▀██─▀─███─▄─▄███─███▄▄▄▄─███─▄─██─▀─███▄▀▄███─▄█▀████─▄─▀██─▄█▀██─▄█▀██─█▄▀─████─▄─▀██─▄─▄█─██─██─▄▀███─▄█▀██─█▄▀─██
▀▄▀▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀▀▀▄▀▄▀▄▄▀▄▄▀▀▀▄▀▀▀▄▄▄▄▄▀▀▀▄▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀	
""")
		return broken_hearts_condition
	

	def execute_trick(self, start_index, broken_hearts):
		"""
		This method execute a trick
		Argument: 
			- start_index: index of the player who is leading the trick
			- broken_hearts: condition of hearts have been broken or not
		Return:
			- current_trick: the trick have just been played
			- current_player_list: the list of players by order of turn that they have played
			- broken_hearts: update condition of hearts have been broken or not
		"""
		number_of_players = len(self.players)  # number of players
		current_trick = []  # this list holds all the cards that have been played in the current trick, reset to empty after every trick
		current_player_list = []  # the list of players by order of turn that they have played


		# execute a trick
		for turn in range(number_of_players):  # turn of every players
			# execute turns of every players
			player_index = start_index + turn  # find the index of which player to play
			player = self.players[player_index]  # find the player playing this turn
			card_play = player.play_card(current_trick, broken_hearts)  # the card that the player plays and then remove it from the player.hand

			# check if this is the turn of trick leader
			if len(current_trick) == 0:
				display = f"{player} leads with"
			# not the turn of trick leader
			else:
				display = f"{player} plays"
			sleep(0.7)
			print(display)		
			print(self.cards_art(card_play))	

			# check if hearts have been broken
			broken_hearts = self.heart_broken(card_play, broken_hearts)	

			current_trick.append(card_play)
			current_player_list.append(player)
		
		return current_trick, current_player_list, broken_hearts
	
	def cards_art(self, card):
		"""
        The method creates the text art of cards in user's hand, following this format:
            "┌───────┐" + '\n' +
            "│10     │" + '\n' +
            "│   ♥   │" + '\n' +
            "│     10│" + '\n' + 
            "└───────┘" + '\n' 
        
        Arguments: a Card object
        Return: a string display the card art 
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
		display_card = cards_art_up + '\n' + cards_art_ranks[card.rank][0] + '\n' + cards_art_suits[card.suit] + '\n' + cards_art_ranks[card.rank][1] + '\n' + cards_art_down + '\n'

		return display_card
			

	def round_play(self):
		"""
		This method executes a round of the game

		Argument: None

		Returns multiple lines of string representing each play turn of players
		"""
		number_of_tricks = len(self.players[0].hand)  	# number of tricks play in a round, which is equal to the number of cards that each player has
		number_of_players = len(self.players)  # number of players
		broken_hearts = False  # check if there has been a card of hearts being played

		
		two_of_clubs_holder = self.holding_two_of_clubs()  # find the player who has the two of clubs at the beginning of a round
		start_index = self.players.index(two_of_clubs_holder) - number_of_players  # index of the player who will lead this trick (minus to the number of players so that it does not run out of index)

		for i in range(number_of_tricks):  # a round will have number_of_tricks tricks
			
			# execute a trick: 
			# update the list of cards of that trick
			# update the list of player (according to turn of players)
			# update broken_hearts condition
			current_trick, current_player_list, broken_hearts = self.execute_trick(start_index, broken_hearts)

			# find the player who takes the trick, and will lead the next trick
			trick_leader = self.taking_the_trick(current_trick, current_player_list)

			# the index of the player who lead the trick
			start_index = self.players.index(trick_leader) - number_of_players

			# calculate the points that a player received in the trick
			trick_score = self.points_calculator(current_trick)

			# update score to the round_score of the player taking the trick
			trick_leader.round_score += trick_score

			# display who takes the trick and the received points 
			print(f"{trick_leader} takes the trick. Points received: {trick_score}\n" )

		
