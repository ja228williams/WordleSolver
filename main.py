import sys

from find_possible_words import possible_words
from optimal_guess import make_optimal_guess


def main():
    """
    Main method. Inquires the inputted word and the corresponding "BYG sequence", which is the colored display from
    Wordle in order, with 'B' corresponding to black, 'Y' corresponding to yellow, and 'G' corresponding to green. For
    example, with input word "sewer" and solution "stern", the corresponding BYG sequence would be "GYBBB", as Wordle
    only sets the first incorrectly placed instance of a character in the word as yellow. After each input, main prints
    out the set of possible words, the size of this set, and the optimal guess given this set of remaining words. main
    continues this process until there is one or zero possible words remaining.

    :return: the solution to the Wordle given the inputs if one exists, and None otherwise.
    """
    blacks = set()
    yellows = dict()
    greens = dict()

    while True:
        print("\nword = ")
        word = sys.stdin.readline().lower()
        print("BYG sequence = ")
        byg = sys.stdin.readline().upper()

        # iterates by letter over newest guess
        for i in range(5):
            score = byg[i]
            letter = word[i]

            # updates blacks, yellows, greens datasets from info given by current character of most recent guess
            if score == 'G':
                greens[i] = letter
                if letter in yellows:
                    del yellows[letter]
            elif score == 'B' and score not in yellows:
                blacks.add(letter)
            elif score == 'Y':
                if letter in yellows:
                    yellows[letter].add(i)
                else:
                    yellows[letter] = {i}

        pw = possible_words(blacks, yellows, greens)
        if len(pw) < 2:
            break
        print("possible options: " + str(pw))
        print("total number of remaining possible words: " + str(len(pw)))
        print("optimal guess = " + make_optimal_guess(pw))

    if len(pw) == 0:
        print("\nNo possible words given these inputs.")
        return None
    else:
        sol = pw.pop()
        print("\nWord = " + sol)
        return sol


if __name__ == "__main__":
    main()


# POTENTIAL ISSUES / BUGS:
#   -

# TO-DO:
#   1) write testing algorithm for optimizing adjusting proportional value for repeating letters grouping
#   2) incorporate functionality with wordle website
