from wordle_wordlist_filter import words as five_words


def possible_words(blacks, yellows, greens):
    """
    Finds a set of possible five-letter words given current knowledge.

    :param yellows: dictionary mapping letters in word to set of incorrect locations
    :param greens: dictionary mapping location to correct letters
    :param blacks: list of letters not included in the word
    :return: set of possible five-letter words.
    """
    potential_words = five_words
    bad_words = set()

    for word in potential_words:
        remove_flag = False

        # filters for green letters
        for location, letter in greens.items():
            if word[location] != letter:
                remove_flag = True

        # filters for black letters
        for black in blacks:
            # ensures the letters designated as black aren't actually yellow or green
            if black in word and black not in yellows.keys() and black not in greens.values():
                remove_flag = True

        # filters for yellow letters
        for letter, locations in yellows.items():
            if letter not in word:
                remove_flag = True
            for location in locations:
                if word[location] == letter:
                    remove_flag = True

        # adds word to list of words to be removed if it doesn't fit
        if remove_flag:
            bad_words.add(word)

    # removes impossible words from the list
    potential_words.difference_update(bad_words)

    return potential_words
