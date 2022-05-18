from find_possible_words import possible_words
from make_guesses import make_guess, print_guess
from optimal_guess import make_optimal_guess


def play_game(answer, first_word="tares", make_optimal_choice=True):
    """
    Simulates the program's attempt to guess the word in the smallest number of turns.

    :param make_optimal_choice: boolean representing whether or not to make the mathematically optimal choice given by
                                algorithm in optimal_guess.py. If False, chooses a random guess among the valid options.
    :param answer: Word to be guessed
    :param first_word: the first guess in the game. The optimal guess was found to be "tares" by this program, which is
                       the default first guess.
    :return: list of guesses by turn
    """
    guess = first_word
    guesses = [guess]
    blacks = set()
    yellows = dict()
    greens = dict()
    no_words = False

    while guess != answer:
        new_blacks, new_yellows, new_greens = make_guess(answer, guess)

        # updates blacks and greens dictionary
        blacks.update(new_blacks)
        greens.update(new_greens)

        # updates yellows dictionary

        # removes black and green elements from yellows
        bad_yellows = set()
        for yellow in yellows:
            if yellow in blacks or yellow in greens:
                bad_yellows.add(yellow)
        for by in bad_yellows:
            del yellows[by]

        # updates yellows with new_yellows
        for letter, location in new_yellows.items():
            if letter not in yellows:
                yellows[letter] = {location}
            else:
                yellows[letter].add(location)

        potential_words = possible_words(blacks, yellows, greens)

        # handles missing words
        if len(potential_words) == 0:
            print("No compatible words found.\n")
            no_words = True
            break

        if make_optimal_choice:
            guess = make_optimal_guess(potential_words)
            if guess in potential_words:
                potential_words.remove(guess)
        else:
            guess = potential_words.pop()
        guesses.append(guess)

    if not no_words:
        print_guess(answer, dict(), {0: guess[0], 1: guess[1], 2: guess[2], 3: guess[3], 4: guess[4]})

    print("Final list of guesses: " + str(guesses))

    return guesses
