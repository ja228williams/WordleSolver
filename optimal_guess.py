def has_repeats(str):
    """
    Simple method checking whether an input string contains repeat characters.

    :param str: input string
    :return: True if str contains repeats, False otherwise
    """
    let_set = set()
    for i in range(len(str)):
        if str[i] in let_set:
            return True
        let_set.add(str[i])
    return False


def setup_scoring_dict(guesses):
    """
    Creates the scoring dictionary based on guesses. This scoring dictionary maps each index (each position in the five
    letter word) to a dictionary mapping letters to a value based on the frequency of that letter in other words in
    guesses, and especially in the same position in these other words.

    :param guesses: the set of guesses that the scoring dictionary is based on.
    :return: the previously described scoring dictionary.
    """
    points_dict = dict()
    for i in range(5):
        points_dict[i] = dict()

    for guess in guesses:
        for i in range(5):
            for j in range(5):
                # increments the corresponding value in the dictionary by a higher amount if the letter is in the same
                # position as in guess
                if i == j:
                    letter = guess[i]
                    if letter not in points_dict[i]:
                        points_dict[i][letter] = 0
                    points_dict[i][letter] += 3
                else:
                    letter = guess[j]
                    if letter not in points_dict[i]:
                        points_dict[i][letter] = 0
                    points_dict[i][letter] += 1

    return points_dict


def score_guess(guess, points_dict):
    """
    Applies scoring algorithm for a given guess. The score for a given word is based on how similar the letters and
    letter arrangements are to other words in guesses.

    :param guess: the word being scored
    :param points_dict: the scoring dictionary created by setup_scoring_dict.
    :return: the score assigned to guess by points_dict.
    """
    score = 0
    for i in range(5):
        index_points_dict = points_dict[i]
        letter = guess[i]
        if letter in index_points_dict:
            score += index_points_dict[letter]

    # discourages repeat letters in potential words for the purposes of exploring more letters in the word- useful for
    # early guesses
    if has_repeats(guess):
        score = int(score * .6)

    return score


def make_optimal_guess(guesses):
    """
    Chooses the mathematically optimal guess out of guesses to be made based on a scoring algorithm ranking words by
    their similarity to all the other words in guesses.

    :param guesses: List of potential guesses to be made
    :return: Best word in guesses
    """
    guesses = list(guesses)
    points_dict = setup_scoring_dict(guesses)
    # print(points_dict)

    max_score = 0
    max_guess = guesses[0]
    for guess in guesses:
        score = score_guess(guess, points_dict)
        # print("guess = " + str(guess) + " has score " + str(score))
        if score > max_score:
            max_score = score
            max_guess = guess

    return max_guess
