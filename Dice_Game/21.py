import time
import random


def display_rules():
    print("""
    _____________________________________________________________________________
    Twenty One is a game of chance where players take turns rolling two dice every 
    round until they decide to stop rolling and lock in their score or end up 
    going bust with a total over 21. The objective is to be the closest to 21 
    when everyone is done rolling.

    Rules are as per follows:
      - Players begin with a score of 0.
      - Each player has one turn to either roll or stop rolling each round.
      - Players can only do a regular roll of two dice until they 
        reach a score of at least 14.
      - Players with a score >= 14 have the option to only roll one dice.
      - If a player scores more than 21 they go bust and are out of the game.
      - The winning player is the one with the score closest to 21 when everyone 
        has finished rolling.
      - If all players go bust, no one wins.
      - If more than one player has the winning score, no one wins.
    _____________________________________________________________________________
    """)
    input("Press enter to go back")
    return


def display_main_menu():
    print("""
░██████╗░░█████╗░███╗░░░███╗███████╗  ░█████╗░███████╗  ██████╗░░░███╗░░
██╔════╝░██╔══██╗████╗░████║██╔════╝  ██╔══██╗██╔════╝  ╚════██╗░████║░░
██║░░██╗░███████║██╔████╔██║█████╗░░  ██║░░██║█████╗░░  ░░███╔═╝██╔██║░░
██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░  ██║░░██║██╔══╝░░  ██╔══╝░░╚═╝██║░░
╚██████╔╝██║░░██║██║░╚═╝░██║███████╗  ╚█████╔╝██║░░░░░  ███████╗███████╗
░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝  ░╚════╝░╚═╝░░░░░  ╚══════╝╚══════╝""")
    print("------------Main Menu------------")
    print("Welcome to Twenty One!")
    print("1. Solo")
    print("2. Local Multiplayer")
    print("3. Rules")
    print("4. Exit")
    print("---------------------------------")


def int_input(prompt="", restricted_to=None):
    while True:
        player_input = input(prompt)
        try:
            int_player_input = int(player_input)
        except ValueError:
            continue
        if restricted_to is None:
            break
        elif int_player_input in restricted_to:
            break
    return int_player_input


def cpu_player_choice(score):

    time.sleep(2)
    if score < 14:
        return 1
    elif score < 17:
        return 3
    else:
        return 2


"""
START OF TASK 1
"""


def display_game_options(player):

    # assign name and score variables as the name and score of the player
    name = player["name"]
    score = player["score"]

    # display which turn it is of the player
    print("------------{}'s turn------------".format(name))

    # display the current player's score
    print("{name}'s score: {score}".format(name=name, score=score))

    # display current choices: 1 and 2
    print("1. Roll")
    print("2. Stay")

    # if score >= 14 then the player will have another choice 3
    if score >= 14:
        print("3. Roll one")




def display_round_stats(round_play, players):

    # display the current round
    print("-----------Round {}-----------".format(round_play))
    
    # loop through each player in the players list
    for player in players:
        
        # assign name and score of the player to the variables
        name = player['name']
        score = player['score']

        # print current player's name and score
        print("{name} is at {score}".format(name=name, score=score))


"""
END OF TASK 1
"""


"""
START OF TASK 2
"""


def roll_dice(num_of_dice=1):
    dice_art = {
        1: ["┌─────────┐",
            "│         │",
            "│    ●    │",
            "│         │",
            "└─────────┘"],
        2: ["┌─────────┐",
            "│  ●      │",
            "│         │",
            "│      ●  │",
            "└─────────┘"],
        3: ["┌─────────┐",
            "│  ●      │",
            "│    ●    │",
            "│      ●  │",
            "└─────────┘"],
        4: ["┌─────────┐",
            "│  ●   ●  │",
            "│         │",
            "│  ●   ●  │",
            "└─────────┘"],
        5: ["┌─────────┐",
            "│  ●   ●  │",
            "│    ●    │",
            "│  ●   ●  │",
            "└─────────┘"],
        6: ["┌─────────┐",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "└─────────┘"]
    }

    rolls_result = []
    #num_of_dice refers to the amount of times dices are rolled
    for i in range(num_of_dice):

        # randomly create numbers and then append into rolls_result list
        rolls_result.append(random.randint(1, 6))
        
    # initialize an empty string, this will be the text art of dices
    dice_faces_diagram = '' 

    # loop 5 times as a die has 5 rows
    for i in range(5):

        # loop through the list of rolls number
        for roll in rolls_result:
            # access each line of each dice
            dice_faces_diagram += dice_art[roll][i]
        # add a newline 
        dice_faces_diagram += '\n'
    
    # initialize the return tuple
    my_tuple = tuple([rolls_result, dice_faces_diagram])
    return my_tuple


"""
END OF TASK 2
"""

"""
START OF TASK 3
"""


def execute_turn(player, player_input):

    # Assign player's name and score to the variable name and score
    name = player['name']
    score = player['score']

    # Initialize variable rolling dice
    rolling_dice = 0

    # Initialize variable display 
    display = ''

    # if player's choice is to keep rolling (not stay)
    if player_input != 2:
        # input 1 or 3
        if player_input == 1:  # rolling 2 dices
            rolling_dice = roll_dice(2) 
            display = "Rolling both..."
        elif player_input == 3:  # rolling 1 dice
            rolling_dice = roll_dice(1)
            display = "Rolling one..."

# calculate the score after the round and update the new score

        # calculate the points of the roll
        points = sum(rolling_dice[0])

        # calculate the score after adding the points
        score += points
        # update the new score to the player's dictionary
        player['score'] = score

        # if score of the player reach 14 and the player has not gone bust
        if 21 >= score >= 14:
            player['at_14'] = True  # update the condition at_14 in player's dictionary to True

        # display dices
        display_string = rolling_dice[1]

        # print out 
        print(display)  # the "Rolling..."
        print(display_string)  # the text art of dices
        print("{player} is now on {score}".format(player=name, score=score))  # score of player

        # bust
        if score > 21:
            player['bust'] = True  # update the 'bust' condition in the dictionary of player
            print("{} goes bust!".format(name))  # display the player who has gone bust
    else:
        # player input equals to 2, which means 'stay'
        print("{player} has stayed with a score of {score}".format(player=name, score=score))  # display the player stay and player's score
        player['stayed'] = True  # update the condition

    return player  # return the updated dictionary


"""
END OF TASK 3
"""


"""
START OF TASK 4
"""
# check if the game is over or not


def end_of_game(players):     
    # count the number of players who have gone bust                
    bust_count = 0
    
    # score of the winner
    winner_score = 0

    # count the number of player who has the same winner score
    winner_count = 0

    # name of the winner
    winner = ''

    # loop through the list of players
    for player in players:
        # if player haven't stayed or gone bust then the game keep going
        if player["stayed"] is False and player["bust"] is False:
            return False
        else: 
            # if there is a player going bust, then add 1 to the bust_count
            if player["bust"] is True:
                bust_count += 1
            
            # find the player with the highest score and his/her score (have not gone bust)
            if player["score"] > winner_score and player["bust"] is False:
                #  find any player who has higher score then update the variables
                winner_score = player["score"]
                winner = player["name"]

    # count how many people share the same highest score
    for player in players:
        if player["score"] == winner_score:
            winner_count += 1

    # if bust_count equals to the total number of players, Everyone's gone bust
    if bust_count == len(players):
        print("Everyone's gone bust! No one wins :(")
        return True
    
    # if there is more than 1 winner, the game is drawn
    if winner_count > 1:
        print("The game is a draw! No one wins :(")
        return True

    # otherwise, we have a winner
    else:
        print(f"{winner} is the winner!")
        return True


"""
END OF TASK 4
"""

"""
START OF TASK 5
"""


def solo_game():
    # List of players containing a dictionary of user input and a dictionary of the robot
    # At first, we set all the data into '0' and 'False' as there has been no round
    players_list = [{'name': 'User', 'score': 0, 'stayed': False, 'at_14': False, 'bust': False},
                    {'name': 'CPU Player', 'score': 0, 'stayed': False, 'at_14': False, 'bust': False}]

    condition = True  # tracker to decide when will the while loop stop
    round_tracker = 0  # track which round players are playing
    # for loop, while the condition is still true then keep going
    while condition is True:
        # check if there has been a winner
        if end_of_game(players_list) is True:
            # if there has been a winner, then change the condition to false, it will make the while loop stop
            condition = False
        # if there has not been any winner
        else:
            # display the title line of which round is it, and points of players
            display_round_stats(round_tracker, players_list)

            # loop through the list of players
            for player in players_list:
                # let the player play if he is not 'stayed' or 'bust' 
                if player['stayed'] is False and player['bust'] is False:

                    # display choices that player has
                    display_game_options(player)

                    # if the name of player is 'User' then require an input
                    if player['name'] == 'User':
                        option = int_input("Please enter an option: ")  # change to int_input()

                    # if player is robot
                    else:
                        option = cpu_player_choice(player['score'])  # change to cpu_player_choice(score)
                    execute_turn(player, option)
        # After finished 1 round then add 1 to the round tracker
        round_tracker += 1


"""
END OF TASK 5
"""

"""
START OF TASK 6
"""


def multiplayer_game(num_of_players):

    # Create a list of players with the given number of players
    players_list = []
    for i in range(1, num_of_players + 1):
        players_list.append({'name': 'player {}'.format(i), 'score': 0, 'stayed': False, 'at_14': False, 'bust': False})


    # while loop
    condition = True  # condition to decide when to stop the while loop
    round_tracker = 0  # track the round number

    while condition is True:
        # if there has been a winner within the list of players then change the condition to False 
        # then the while loop will stop
        if end_of_game(players_list) is True:
            condition = False

        # if there has not been any winner then let the players play
        else:

            # display round title and points of every player
            display_round_stats(round_tracker, players_list)

            # loop through the players' list
            for player in players_list:
                # if the player did not stay and has not gone bust then play
                if player['stayed'] is False and player['bust'] is False:
                    # display the choices for player
                    display_game_options(player)
                    # player input their choice
                    option = int_input("Please enter an option: ")
                    # execute a round
                    execute_turn(player, option)
        # after the round add 1 to the round tracker to display the round number in the next round
        round_tracker += 1


"""
END OF TASK 6
"""
        
"""
START OF TASK 7
"""


def main():
    condition = True  # condition to tell whether the game is still going
    while condition is True:
        # print main menu
        display_main_menu()
        # get the input of the player
        choice = int_input("Please enter your choice: ")

        # if player choose 1, they will play solo_game
        if choice == 1:
            solo_game()

        # if player choose 2, they will play with other players
        elif choice == 2:
            # get the number of players
            number_of_players = int_input("Please enter the number of players: ")
            while number_of_players == 1:
                print("You are so alone!!!")
                print("Make some friends!!!")
                number_of_players = int_input("Please enter the number of players: ")
            multiplayer_game(number_of_players)
        # if player choose 3, the game will show the rules
        elif choice == 3:
            display_rules()
            continue  # press enter and the game return to main menu

        # if player choose 4, the game will be terminated
        elif choice == 4:
            condition = False


"""
END OF TASK 7
"""


"""
MAIN FUNCTION
"""
main()





