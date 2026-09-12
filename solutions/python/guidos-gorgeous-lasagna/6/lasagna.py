"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2 # 2 minutes per layer

def bake_time_remaining(bake_time_elapsed):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - bake_time_elapsed


def preparation_time_in_minutes(number_of_layers):
    """Calculate the time to prepare the lasagne for the number of layers it contains.

    Parameters:
        number_of_layers (int): The number of layers the lasagne contains.

    Returns:
        int: The time (in minutes) derived from 'PREPARATION_TIME'.

    Function that takes the number of layers the lasagna contains as
    an argument and returns how many minutes it will take to prepare it 
    based on the `PREPARATION_TIME`.
    """

    return number_of_layers * PREPARATION_TIME


#TODO (student): define the 'elapsed_time_in_minutes()' function below.

def elapsed_time_in_minutes(number_of_layers,bake_time_elapsed):
    """Calculate the time spent in the kitchen preparing and baking the lasagne (so far).

    Parameters:
        number_of_layers (int): The number of layers the lasagne contains.
        elapsed_bake_time (int): The time (in minutes) already spent in the oven.

    Returns:
        int: The time (in minutes) derived from preparation time (per layer) and time already spent baking.

    Function that multiplies the preparation time per layer for the number of layers
    and sums this with the time already spent in the oven 
    to returns how many minutes have already been spent in the kitchen. 
    """

    return preparation_time_in_minutes(number_of_layers) + bake_time_elapsed