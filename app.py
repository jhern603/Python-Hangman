# DEV: JOSE HERNANDEZ
# BUGS:
# NOTES: Added ability to check for repeated characters
import random
import sys
import collections
import os


class hangman_logic:
    options = {'movies': ['full metal jacket', 'Major Payne', 'American Sniper',
                          'Lone Survivor', 'twelve strong'], 'games': ["hangman", "tic tac toe", "Monopoly"]}
    categories = []
    for key, value in options.items():
        categories.append(key)

    def __init__(self):
        print('Welcome to hangman!\n\nThe available categories to pick from are:',
              ', '.join(hangman_logic.categories))

        self.selected_word = ""
        self.word_cache = ""
        self.repeated_char_dict = collections.defaultdict(int)
        # Booleans
        self.category_selected = False
        # User Inputs
        self.guessed_correctly = {}
        self.guessed_wrong = {}
        self.allowable_mistakes = int(0)
        self.allowable_hints = int(0)
        # Counters
        self.mistake_count = int(0)
        self.hint_count = int(0)
        self.win_count = int(0)
        self.loss_count = int(0)
        self.total_guessed = int(0)

    def __str__(self):
        return "\nERROR: Please start the game by using the '.play()' method!"

    def word_selector(self, category):
        randWord = random.randint(0, len(hangman_logic.options[category]) - 1)
        self.selected_word = hangman_logic.options[category][randWord].lower()
        self.word_cache = self.selected_word
        self.selected_word = sorted(self.selected_word.replace(' ', ''))
        os.system('cls' if os.name == 'nt' else 'clear')
        self.repeatedCharCounter()
        print('Your word is ', len(self.selected_word), 'characters long\n')
        self.category_selected = True
        print('\n\n', self.selected_word)

    def ask_mistakes(self):
        try:
            self.allowable_mistakes = int(
                input('How many mistakes would you like to have?\n'))
            if self.allowable_mistakes >= len(self.selected_word):
                print(
                    'The number of mistakes should be less than the length of the word\n')
                self.ask_mistakes()
        except ValueError:
            print(
                'The value for mistakes should be an integer between 0 and less than the length of the word\n')
            self.ask_mistakes()

    def ask_hints(self):
        try:
            self.allowable_hints = int(
                input('How many hints would you like to have?\n'))
            if self.allowable_hints >= len(self.selected_word):
                print(
                    'The number of hints should be less than the length of the word\n')
                self.ask_hints()
        except ValueError:
            print(
                'The value for hints should be an integer between 0 and less than the length of the word\n')
            self.ask_hints()

    def repeatedCharCounter(self):
        for character in self.selected_word:
            self.repeated_char_dict[character] += 1

    def evaluate(self, userGuess):
        guessNotInWrongList = userGuess not in self.guessed_wrong
        if userGuess in self.repeated_char_dict.keys() and guessNotInWrongList and self.total_guessed <= len(self.selected_word) and userGuess in self.selected_word:
            print(userGuess, " was correct!")
            self.total_guessed += 1
            self.guessed_correctly[userGuess] = self.guessed_correctly.get(
                userGuess, 1) + 1
            self.repeated_char_dict[userGuess] -= 1
            if self.repeated_char_dict[userGuess] == 0:
                del self.repeated_char_dict[userGuess]
            print('You have made,', self.total_guessed, 'guess(es)!')
        elif self.guessed_correctly == len(self.selected_word) or sorted(userGuess) in self.selected_word:
            self.win_count += 1
            print("You win! Your word was,", self.selected_word)
            self.win()
        elif 'hint' in userGuess:
            self.hint()
        elif 'quit' in userGuess:
            print('Thank you for playing!')
            sys.exit(1)
        elif self.total_guessed >= len(self.selected_word):
            print("You have made the maximum amount of guesses! Your word was,",
                  self.word_cache, "\n\n")
            playAgain = input("Would you like to play again?").lower()
            if 'y' in playAgain:
                self.loss_count += 1
                self.play()
            else:
                sys.exit(1)
        else:
            print(userGuess, " was wrong!")
            self.total_guessed += 1
            self.guessed_wrong[userGuess] = self.guessed_wrong.get(
                userGuess, 1) + 1
            print('You have made,', self.total_guessed, 'guess(es)!')
            print(sorted(userGuess), " ", self.selected_word)


    def hint(self):
        randChar = random.randint(0, len(self.selected_word) - 1)
        print('Your hint is: ', self.selected_word[randChar])

    def win(self):
        print("You win! Your word was, ", self.word_cache)
        playAgain = input("Would you like to play again?").lower()
        if 'y' in playAgain:
            self.loss_count += 1
            self.play()
        else:
            sys.exit(1)

    def play(self):
        try:
            self.selected_category = input('')
            if self.selected_category.isalpha() and self.category_selected is False:
                self.word_selector(self.selected_category)
        except KeyError:
            print('That is not a valid category. IN EXCEPT BLOCK')
            self.play()
        self.ask_hints()
        self.ask_mistakes()
        while True:
            self.evaluate(input('Pick a letter: '))


hangman = hangman_logic()
hangman.play()
