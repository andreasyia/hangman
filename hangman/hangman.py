import random


class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.
    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for letter in range(len(self.word))]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

        print("The mistery word has {num_letters} charecters".format(num_letters=self.num_letters))
        print("{word_guessed}".format(word_guessed=self.word_guessed))



    def check_letter(self, letter) -> None:
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked

        '''
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
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''
        while True:
            letter = input("Guess a letter:")
            if len(letter) != 1 or not letter.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif letter in self.list_of_guesses:
                print("You already tried this letter!")
            else:
                self.check_letter(letter)
                self.list_of_guesses.append(letter)

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
