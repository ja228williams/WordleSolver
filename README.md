# WordleSolver
Python project with the goal of finding optimal solutions to Wordle puzzles using a guess optimization algorithm based on the frequency of letters by position in words in the list of valid solutions. 

The project involves two different methods of applying the algorithms used to find solutions; first, play_game.py provides the option for running a simulation of solution-hunting when given the solution to the puzzle, and second, main.py allows for words and their letter-color designations from Wordle to be given one at at a time, at which point the set of possible solutions as well as the next optimal guess are printed out, until there is one or zero possible solutions left. 

The code in this project has largely not been optimized for efficiency, since the total data set of five-letter English words contains about 12,000 words, and the code operates over only five indices (the length of each word), so the code runs fairly quickly regardless; still, the more obvious optimizations have been implemented. 

# Finding possible solutions
find_possible_words.py finds all possible solutions given the "black", "yellow" and "green" letters (stored as a set, a dictionary mapping letters to incorrect indices, and a dictionary mapping indices to correct letters, respectively) and corresponding indices by ruling out words that contradict these patterns. The function in this file is continuously called from other functions, with the black, yellow, and green data sets being adjusted accordingly. 

# Guess Optimization
// description of algorithm (+ implementation?)

# main.py
// description + instructions of how to use


# play_game Simulation
make_guess.py plays a single turn in the game given the correct answer and the guess to be made by calculating which letters are designated as black, yellow and green, and prints out the results from the guess; i.e., the word and its corresponding black-yellow-green letter designation. 
// add instructions of how to use


# Word list
The word list was retrieved from https://www.nytimes.com/games/wordle/index.html to match the words used by Wordle. wordle_wordlist_filter.py contains commented out code that was used to filter through the string retrieved from the client-side source code from the website, as well as an uncommented-out variable containing a list of these words calculated by the rest of the commented-out code for reference from other functions. 
