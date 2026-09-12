# Ex007 little sisters vocabulary
# Project: complete four tasks to create functions for 
#   1. adding a prefix to a word (make words negative by prefixing them with 'un').
#   2. adding prefixes to word groups (apply specific prefixes to particular groups of words and output a string of results).
#   3. remove a suffix from a word (find the original root word by removing the suffix but with care for root word spelling).
#   4. extract and transform a word (changing an adjective into a verb by adding a suffix).
# # Created: 2026-06-23
# Revision History:
# v1: Initial setup and basic logic.
# v2: Refined logic for 2nd function (prefixing a group of words)
# v3: 


"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    Parameters:
        word (str): The root word.

    Returns:
        str: Root word prepended with 'un'.
    """

    pref = 'un'
    return pref + word.lstrip()


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words.

    Parameters:
        vocab_words (list[str]): Vocabulary words with prefix at first index.

    Returns:
        str: Prefix followed by vocabulary words with prefix applied.

    This function takes a `vocab_words` list of strings and returns a string
    with the prefix and the words with prefix applied, separated by ' :: '.

    Examples:
        >>> list('en', 'close', 'joy', 'lighten')
        'en :: enclose :: enjoy :: enlighten'.

    """
    separator = ' :: '
    prefix = vocab_words[0]
    base_words = vocab_words[1:]
    prefixed_words = []
    for word in base_words:
        prefixed_words.append(prefix + word)
    return prefix + separator + separator.join(prefixed_words)


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    Parameters:
        word (str): Word to remove suffix from.

    Returns:
        str: Word with suffix removed & spelling adjusted.

    Examples:
        >>> remove_suffix_ness('heaviness')
        'heavy'

        >>> remove_suffix_ness('sadness')
        'sad'

    """
    suffix = 'ness'
    new_list = word.split(suffix)
    new_word = new_list[0]
    if new_word[-1] == 'i':
        new_word = new_word[0:-1] + 'y'
    return new_word


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    Parameters:
        sentence (str): The word used in a sentence as an adjective.
        index (int): Index of the adjective to remove and transform.

    Returns:
        str: The extracted adjective in verb form.

    Examples:
        >>> adjective_to_verb('It got dark as the sun set.', 2)
        'darken'

        >>> adjective_to_verb('The ink stains her fingers black.', -1)
        'blacken'

    """
    verbed = sentence.split()[index]
    if index == -1:
        verbed = verbed[0:-1]
    return verbed + 'en'

print(f'{add_prefix_un("happy")}')
print(f'{make_word_groups(['pre', 'serve', 'dispose', 'position'])}')
print(f'{remove_suffix_ness("emptiness")}')
print(f'{adjective_to_verb('It felt thick when it was wet.', 2)}')