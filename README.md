# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

# Milestone_1
For milestone_1 a repositiry was created in github, in order to trackour changes.

# Milestone_2
The milestone_2.py takes a random word from a list called word_list and print it. Then the input function was used for the user to enter a letter with the following conditions assigned by using if-else statements. The letter has to be of lenght one and must be alphabetic. The random was imported at the very beggining of the code.

'''
import random

word_list = ['banana', 'mango', 'blueberries', 'strawbwrries', 'melon']
print(word_list)

word = random.choice(word_list)
print(word)

letter = input('Enter a single letter:')

if len(letter) == 1 and letter.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
'''

# Milestone_3
The milestone_3.py is consisting of two functions the check_letter and ask_letter. The check_letter function takes the argument letter and uses the function lower() to make the string lower case and then uses the if-esle statements to check whether the geussed word is in the word. Then it prints good guess if it is in the word and otherwise sorry the guessed word it is not in the word.

The ask_letter function takes no argument. It uses the input function nested in a while loop, asking the user to guess a letter with same conditions assigned in milestone_2.py except this time if the input is valid, it breaks out of the loop but if the input is invalid, it keeps looping until the conditions are met.

'''
def check_letter(guess):
    leetter = letter.lower()
    if letter in word:
        print("Good guess! {letter} is in the word".format(letter = letter))
    else:
        print("Sorry {letter} is not in the word. Try again!".format(letter = letter))

def ask_letter():
    while True:
        letter = input("Guess a letter:")

        if len(letter) == 1 and letter.isalpha():
            break

        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    return letteer

word = 'pineapple'

letter = ask_letter()
check_letter(letter)
'''
# Milestone_4
In milestone_4.py the class Hangman was created and initialising the following attributes word, word_guessed, num_letters, num_lives, word_list and list_of_guesses.

Then the method check_letter was created taking the letter as a parameter. An if statement was created nested with a for loop to check whether the letter is in the  and an else statement if the letter is not in the word with the num_lives reduced by 1 and messages are printed to inform the player that did not guess the right letter and of the remaining lives. Also, a line added to convert the letter to lower case before checking if it is in the word. This is to ensure that the program can correctly recognize upper case and lower case versions of the same letter as the same letter.

As for the method ask_letter is responsible for asking the user to input a letter as a guess, validating the input, and calling the check_letter method of the same class to check if the guessed letter is in the target word or not. If the guessed letter is not in the target word, it decreases the number of remaining lives by 1. It also keeps track of the guessed letters in the list_of_guesses attribute. The ask_letter method runs in an infinite loop until the game is over, which happens when the number of remaining lives reaches 0 or when the word is guessed correctly. 

'''
import random

class Hangman:

    word_list = ['banana', 'mango', 'blueberries', 'strawbwrries', 'melon']


    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for guess in range(len(self.word))]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_letter(self, letter):
            letter = letter.lower()
            if letter in self.word:
                print("Good guess! {letter} is in the word".format(letter=letter))
                for i in range(len(self.word)):
                    if self.word[i] == letter:
                        self.word_guessed[i] = letter
                self.num_letters -= 1
            else:
                self.num_lives -= 1
                print("Sorry, {letter} is not in the word.".format(letter=letter))
                print("You have {lives} lives left.".format(lives=self.num_lives))



    def ask_letter(self):
        while True:
            letter = input("Guess a letter:")
            if len(letter) != 1 or not letter.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif letter in self.list_of_guesses:
                print("You already tried this letter!")
            else:
                self.check_letter(letter)
                self.list_of_guesses.append(letter) 
'''
# Milestone_5
The function play_game was added which run all the code to run the game as expected.
The play_game function takes in a list of words (word_list) as an argument, initializes the number of lives to 5, and creates a new Hangman object with the word_list and num_lives as parameters. Then, it enters an infinite loop where it checks if the number of lives is 0 or if all the letters of the word have been guessed correctly. If the number of lives is 0, it prints "You lost!" and the mistery word and breaks out of the loop. If all the letters have been guessed correctly, it prints "Congratulations. You won the game!" and breaks out of the loop. Otherwise, the game is continuing to ask the user to guess a letter.
In this implementation, the valid_input variable is set to False at the start of each loop. The program then enters a second while loop that will continue looping until valid_input is set to True. Within this loop, the program checks if the input is a single alphabetical character and if it hasn't already been guessed. If these conditions are met, the check_letter method is called, and valid_input is set to True, exiting the second while loop and continuing the game loop. If the input is invalid, the program prints a message and the second while loop continues.

'''
def play_game(word_list):
    game = Hangman(word_list, num_lives=5)
    while True:
        if game.num_lives == 0:
            print("You lost! The word was {word}".format(word=game.word))

            break
        elif game.num_letters == 0:
            print("Congratulations! You won the game!")
            break
        else:
            valid_input = False
            while not valid_input:
                letter = input("Guess a letter:")
                if len(letter) != 1 or not letter.isalpha():
                    print("Invalid input. Please enter a single alphabetical character.")
                elif letter in game.list_of_guesses:
                    print("You already tried this letter!")
                else:
                    game.check_letter(letter)
                    game.list_of_guesses.append(letter)
                    valid_input = True

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
'''

