# Ex005 black_jack
# Project: complete six tasks to create functions for implementing some rules of BlackJack card game.
# # Created: 2026-06-17
# Revision History:
# v1: Initial setup and basic logic.
# v2: Logic change for split (based on card value not card face). Fixed logic for double-down bet.
# v3: pylint improvement for readibility of code (changing elif to a separate if, etc)


"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    Parameters:
        card (str): The given card.

    Returns:
        int: The value of a given card.  See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 1
        3.  '2' - '10' = numerical value.
    """

    card = card.upper()
    if card in {'10','J','Q','K'}:
        return 10 # all such cards are a value of 10
    if card == 'A':
        return 1
    return int(card)

def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 1
        3.  '2' - '10' = numerical value.

    Returns:
        str or tuple: The resulting tuple contains both cards if they are of equal value.
    """

    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)

    if card_one_value == card_two_value:
        return (card_one,card_two)
    if card_one_value < card_two_value:
        return card_two
    return card_one

def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for an upcoming ace card.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 11 (if already in hand)
        3.  '2' - '10' = numerical value.

    Returns:
        int: Either 1 or 11, which is the value of the upcoming ace card.
    """
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    ten = 10 # value of a 10 pip card or a 'royal' card
    one = 1 # Ace low value
    eleven = 11 # Ace high value

    if card_one == 'A' or card_two == 'A':
        # If we already have an Ace, our hand is already at least 12 (Ace + lowest card 1)
        # Adding an 11 would always bust us, so the upcoming Ace MUST be 1.
        return one
       
    if value_one + value_two <= ten:
        return eleven # an Ace would be most valuable as 11
    return one


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 11 (if already in hand)
        3.  '2' - '10' = numerical value.

    Returns:
        bool: Is the hand is a blackjack (two cards worth 21).
    """
    ten = 10 # value of a 10 pip card or a 'royal' card
    eleven = 11 # Ace high value

    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)

    return value_one + value_two == eleven and ten in (value_one, value_two)


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    Parameters:
        card_one (str): First card in the hand.
        card_two (str): Second card in the hand.

   Returns:
        bool: Can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    return value_of_card(card_one) == value_of_card(card_two)

def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    Parameters:
        card_one (str): First card in the hand.
        card_two (str): Second card in the hand.

    Returns:
        bool: Can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    optimal_cards = {9,10,11}
   
    return value_of_card(card_one) + value_of_card(card_two) in optimal_cards

# provide a set of test data and print outputs to check function logic
# card_one = '6'
# card_two = '6'
# print(f'card one = {value_of_card(card_one)} and card two = {value_of_card(card_two)}')
# print(f'higher card value = {higher_card(card_one, card_two)}')
# print(f'next ace should be counted as {value_of_ace(card_one, card_two)}')
# print(f'is this Black Jack? {is_blackjack(card_one, card_two)}')
# print(f'hand eligible for a split? {can_split_pairs(card_one, card_two)}')
# print(f'double-down bet available? {can_double_down(card_one, card_two)}')