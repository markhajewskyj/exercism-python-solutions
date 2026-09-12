# Ex006 little_sisters_essay
# Project: complete four tasks to create functions for 
#   1. capitalising words,.
#   2. checking for periods at end of sentences.
#   3. cleaning up spaces between words.
#   4. replacing some words with synonyms.
# # Created: 2026-06-21
# Revision History:
# v1: Initial setup and basic logic.
# v2: refined logic for task 1 (handling whether an apostrophe is present in the title sentence)
# v3:


"""Functions to help edit essay homework using string manipulation."""
import string

def capitalize_title(title):
    """Convert the first letter of each word in the title to uppercase if needed.

    Parameters:
        title (str): Essay title that needs title casing.

    Returns:
        str: The title string in title case (first letters capitalized).
    """
    if title.find("'") > -1:
        return string.capwrods(title)
    return title.title()


def check_sentence_ending(sentence):
    """Check the ending of the sentence to verify that a period is present.

    Parameters:
        sentence (str): A sentence to check.

    Returns:
        bool: Is the sentence punctuated correctly?
    """

    return sentence.endswith('.')


def clean_up_spacing(sentence):
    """Trim any leading or trailing whitespace from the sentence.

    Parameters:
        sentence (str): A sentence to clean of leading and trailing space characters.

    Returns:
        str: A sentence that has been cleaned of leading and trailing space characters.
    """

    return sentence.strip()


def replace_word_choice(sentence, old_word, new_word):
    """Replace a word in the provided sentence with a new one.

    Parameters:
        sentence (str): A sentence to replace words in.
        old_word (str): The word to replace.
        new_word (str): The replacement word.

    Returns:
        str: Input sentence with new words in place of old words.
    """

    return sentence.replace(old_word,new_word)

