# DEV: JOSE HERNANDEZ
# BUGS:
# NOTES: Added ability to check for repeated characters
import random, sys, collections, os


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
        self.repeated_char_dict = collections.defaultdict(int)
        #Booleans
        self.category_selected = False
        #User Inputs
        self.guessed_correctly = {}
        self.guessed_wrong = {}
        self.allowable_mistakes = int(0)
        self.allowable_hints = int(0)
        #Counters
        self.mistake_count = int(0)
        self.hint_count = int(0)
        self.win_count = int(0)
        self.loss_count = int(0)
        self.total_guessed = int(0)

    def __str__(self):
        return "\nERROR: Please start the game by using the '.play()' method!"

    def word_selector(self, category):
        randWord = random.randint(0, len(hangman_logic.options[category]) - 1)
        self.selected_word = hangman_logic.options[category][randWord].replace(
            ' ', '').lower()
        self.selected_word = sorted(self.selected_word)
        os.system('cls' if os.name == 'nt' else 'clear')
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
        if userGuess not in self.guessed_correctly and userGuess not in self.guessed_wrong and self.total_guessed <= len(self.selected_word):
            print(userGuess, " was correct!")
            self.total_guessed += 1
            #TODO: Figure out the Python equivalent of Java's .getOrDefault()
            self.guessed_correctly[userGuess] = 1 
            print('You have made, ', self.total_guessed, ' guesses!')
        elif 'hint' in userGuess:
            self.hint()
        elif 'quit':
            print('Thank you for playing!')
            sys.exit(1)
        else:
            print(userGuess, " was wrong!")
            self.total_guessed += 1
            self.guessed_wrong += 1
            print('You have made, ', self.total_guessed, ' guesses!')

    def hint(self):
        randChar = random.randint(0, len(self.selected_word) - 1)
        print('Your hint is: ', self.selected_word[randChar])

    def win(self):
        if self.guessed_correctly == len(self.selected_word):
            print("You win! Your word was, ", self.selected_word)

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
