# WordleSolver
This is a Python project with the goal of finding optimal solutions to Wordle puzzles using a guess optimization algorithm based on the frequency of letters by position in words in the list of valid solutions. 

The project involves two different methods of applying the algorithms used to find solutions; first, play_game.py provides the option for running a simulation of solution-hunting when given the solution to the puzzle, and second, main.py allows for words and their letter-color designations from Wordle to be given one at at a time, at which point the set of possible solutions as well as the next optimal guess are printed out, until there is one or zero possible solutions left. 

The code in this project has largely not been optimized for efficiency, since the total data set of five-letter English words contains about 12,000 words, and the code operates over only five indices (the length of each word), so the code runs fairly quickly regardless; still, the more obvious optimizations have been implemented. 

# Finding possible solutions
find_possible_words.py finds all possible solutions given the "black", "yellow" and "green" letters (stored as a set, a dictionary mapping letters to a set of incorrect indices, and a dictionary mapping indices to correct letters, respectively) and corresponding indices by ruling out words that contradict these patterns. The function in this file is continuously called from other functions, with the black, yellow, and green data sets being adjusted accordingly. 

# Guess Optimization
The guess optimization algorithm operates by examining the structure of the remaining possible words, and chooses the word most similar to all of the other remaining words so that the most words in the remaining word set can be affected by the color designation of the guess being made. In particular, words with the same letters as most of the other words in the set (and especially in the same positions, as this provides more helpful information) are most likely to be chosen as the optimal guess. 

To implement this idea, a scoring dictionary based on the input set of guesses is created, and a guess with the highest score given by this dictionary is chosen as the optimal guess. This scoring dictionary maps each index (each position in the five-letter word) to a dictionary mapping letters to the value given in the equation f(x, y) = 3x + y, where x = the number of times that letter appears at that index in other words and y = the number of times that letter appears at a different index in other words. The score for a given guess is then given by the sum of the values of the letters over the five indices. 

Due to the issue of repeated common letters within words being given higher scores and the low practicality of this result (as it's beneficial for more letters to be explored), words with repeated letters are given a 40% decrease to their score. Also, I explored other potential coefficients of x in the formula for f(x, y) as given above, and found that 3 generally resulted in the lowest number of guesses; a lower value such as 1 does not adequately account for the benefit of the information given by the position of the guessed letter, and a much higher value underestimates the benefit of guessing letters in other positions of words. 

# main.py
main.py inquires the inputted word and the corresponding "BYG sequence", which is the colored display from Wordle in order, with 'B' corresponding to black, 'Y' corresponding to yellow, and 'G' corresponding to green. For example, with input word "sewer" and solution "stern", the corresponding BYG sequence would be "GYBBB", as Wordle only sets the first incorrectly placed instance of a character in the word as yellow. After each input, main prints out the set of possible words, the size of this set, and the optimal guess given this set of remaining words. main continues this process until there is one or zero possible words remaining. 


# play_game Simulation
make_guesses.py plays a single turn in the game given the correct answer and the guess to be made by calculating which letters are designated as black, yellow and green, and prints out the results from the guess; i.e., the word and its corresponding black-yellow-green letter designation. This file also contains a function that is called to print out the inputted guess with its black-yellow-green letter designation. 

play_game.py simulates the program's attempt to guess the word in the smallest number of turns. It takes in the solution to the puzzle, as well as the first guess to be made (with default first word "tares", found by the previously described optimization algorithm to be the optimal first guess) and a boolean representing the choice to make the optimal guess or a random guess from the set of possible remaining words, with default value of picking the optimal guess. Calling play_game prints out the results from each guess until the final word is found, at which point the list of guesses made in order is printed and returned. 


# Word list
The word list was retrieved from https://www.nytimes.com/games/wordle/index.html to match the words used by Wordle. wordle_wordlist_filter.py contains commented out code that was used to filter through the string retrieved from the client-side source code from the website, as well as an uncommented-out variable containing a list of these words calculated by the rest of the commented-out code for reference from other functions. 
