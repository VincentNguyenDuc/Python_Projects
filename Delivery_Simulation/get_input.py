invalid = """
█ █▄ █ █ █ ▄▀█ █   █ █▀▄ █   █▀█ █   █▀▀ ▄▀█ █▀ █▀▀   ▀█▀ █▀█ █▄█   ▄▀█ █▀▀ ▄▀█ █ █▄ █ █
█ █ ▀█ ▀▄▀ █▀█ █▄▄ █ █▄▀ ▄   █▀▀ █▄▄ ██▄ █▀█ ▄█ ██▄    █  █▀▄  █    █▀█ █▄█ █▀█ █ █ ▀█ ▄
"""


def int_input(prompt="", restricted_to=None, positive=False):
    """
    Helper function that modifies the regular input method,
    and keeps asking for input until a valid one (which is an integer) is entered. Input
    can also be restricted to a set of integers.

    Arguments:
        - prompt: String representing the message to display for input
        - restricted: List of integers for when the input must be restricted
                    to a certain set of numbers
        - positive: check if the input must be > 0

    Returns the input in integer type.
    """
    # Text art for invalid input
    invalid_display = invalid

    while True:
        # promt the user to input
        player_input = input(prompt)
        try:
            # check if the user input is int
            int_player_input = int(player_input)

            # if the positive condition is True, check if the user input a positive number
            if positive is True and int_player_input <= 0:
                print(invalid_display)
                continue
        
        # catch the error
        except ValueError:
            print(invalid_display)
            continue

        # check if there is any restriction
        if restricted_to is None:
            break
        elif int_player_input in restricted_to:
            break
        else:
            print(invalid_display)

    return int_player_input


def float_input(prompt="", positive=False):
    """
    Helper function that modifies the regular input method,
    and keeps asking for input until a valid one (which is an integer) is entered. Input
    can also be restricted to positive or negative

    Arguments:
        - prompt: String representing the message to display for input
        - positive: check if the input must be > 0

    Returns the input in integer type.
    """

    # Text art for invalid input
    invalid_display = invalid

    while True:
        # get input from the user
        player_input = input(prompt)
        try:
            # check if the input is float
            float_player_input = float(player_input)

            # if the positive condition is True, check if the user input a positive number
            if positive is True and float_player_input <= 0:
                print(invalid_display)
                continue
        
        # catch the error
        except ValueError:
            print(invalid_display)
            continue

        # condition to break the while loop
        if positive is False:
            break
        elif type(float_player_input) is float:
            break

    return float_player_input



