def make_guess(answer, guess):
    """
    Makes a guess (plays a single turn in the game). Only the first index of a yellow letter is included in the
    returned yellows dictionary, and yellows maps letters to that specific index as an integer (yellows: str -> int)

    :param answer: Word to be guessed
    :param guess: the guess being made
    :return: The resulting blacks, yellows, and greens from this single guess
    """
    blacks = set()
    yellows = dict()
    greens = dict()

    # iterates by character over the word
    for idx in range(5):
        letter = guess[idx]

        # add to blacks
        if letter not in answer:
            blacks.add(letter)
            continue

        # add to greens
        if answer[idx] == letter:
            greens[idx] = letter
            continue

        # add to yellows (this implementation ensures only the first yellow is included)
        if letter not in yellows:
            yellows[letter] = idx

    print_guess(guess, yellows, greens)

    return blacks, yellows, greens


def print_guess(guess, yellows, greens):
    """
    Prints a guess mapping letters to 'B' if black, 'Y' if yellow, and 'G' if green.

    :param guess: the guess being printed
    :param yellows: dictionary mapping letters to list of incorrect locations
    :param greens: dictionary mapping indices to correct letters
    """
    letters = [char for char in guess]
    line_one = letters[0]
    for idx in range(1, 5):
        line_one += " - " + letters[idx]

    line_two = "|   |   |   |   |"

    # sets up coloring label system
    idx_to_clr = dict()
    for i in range(5):
        letter = guess[i]
        if i in greens and greens[i] == letter:
            idx_to_clr[i] = 'G'
        elif letter in yellows and yellows[letter] == i:
            idx_to_clr[i] = 'Y'
        # this should work as the default case- necessary because of first yellow rule
        else:
            idx_to_clr[i] = 'B'

    # defines line_three string based on coloring dictionary
    line_three = idx_to_clr[0]
    for i in range(1, 5):
        line_three += " - " + idx_to_clr[i]

    print(line_one)
    print(line_two)
    print(line_three)
    print()
