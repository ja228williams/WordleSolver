# WordleSolver
Python project with the goal of finding optimal solutions to Wordle puzzles using a guess optimization algorithm based on the frequency of letters by position in words in the list of valid solutions. 

# Finding possible solutions
find_possible_words.py finds all possible solutions given the "black", "yellow" and "green" letters (stored as a set, a dictionary mapping letters to incorrect indices, and a dictionary mapping indices to correct letters, respectively) and corresponding indices by ruling out words that contradict these patterns. 

# Guess Optimization

# main.py


# play_game Simulation
make_guess.py plays a single turn in the game given the correct answer and the guess to be made by calculating which letters are designated as black, yellow and green, and prints out the results from the guess; i.e., the word and its corresponding black-yellow-green letter designation. 


# Word list
The word list was retrieved from https://www.nytimes.com/games/wordle/index.html to match the words used by Wordle. wordle_wordlist_filter.py contains commented out code that was used to filter through the string retrieved from the client-side source code from the website. 
