# DEV: JOSE HERNANDEZ
# BUGS:
# NOTES: Added ability to check for repeated characters
# TODO: Add in inf mistakes and hints capability
import random
import sys
import collections


class hangman_logic:
    categories_dict = {'movies': ['full metal jacket', 'Major Payne', 'American Sniper',
                                  'Lone Survivor', 'twelve strong'], 'games': ["hangman", "tic tac toe", "Monopoly"]}
    keys = []
    for key, value in categories_dict.items():
        keys.append(key)
    properCategory = False
    charRepeated = []
    # Initializes instance variables

    def __init__(self):
        self.guessed_correctly = []
        self.incorrectly_guessed = []
        self.mistakes = 0
        self.hint_count = 0
        self.win_counter = 0
        self.loss_counter = 0

    def __str__(self):
        return "\nERROR: Please start the game by using the '.play()' method!"

    def ask_mistakes(self):
        self.allowable_mistakes = input(
            "What do you want to be the maximum number of mistakes? ")
        try:
            int(self.allowable_mistakes)
            if int(self.allowable_mistakes.isdigit()) <= len(self.word):
                print("The maximum number of mistakes you can make this round is: ",
                      self.allowable_mistakes, '\n')
            else:
                print(
                    "The maximum amount of mistakes allowed is up to the length of the word.\n")
                self.ask_mistakes()
        except ValueError:
            print("Strings are not accepted: insert an integer!")

    def ask_hints(self):
        self.allowable_hints = input(
            "What do you want the maximum number of hints to be? ")
        try:
            int(self.allowable_mistakes)
            if self.allowable_hints != '' and int(self.allowable_hints) <= len(self.word):
                print("The maximum number of hints you can request this round is: " +
                      self.allowable_hints + '\n')
            elif int(self.allowable_hints) > len(self.word):
                print(
                    "\nThe maximum amount of hints allowed are up to the length of the word.\n")
        except ValueError:
            print("Strings are not accepted: insert an integer!")

    def isCharRepeated(self):
        for k in self.counter:
            if self.counter[k] > 1:
                self.charRepeated.append(k)
    # Selects a string for the round

    def word_selector(self, category):
        self.picker = random.randint(
            0, len(self.categories_dict[category])) - 2
        self.selected_category = self.categories_dict[category]
        self.word = self.selected_category[self.picker].lower().replace(
            ' ', '')
        if category in self.categories_dict:
            self.properCategory = True
            print("\nYou selected: '" + category +
                  "' as the category for this round.\n")
            self.word_sorted = sorted(self.word)
            # Counter counts the occurence of each character and stores it in a dictionary
            self.counter = collections.Counter(self.word)
            self.isAlpha = True
        elif self.word.isalpha() is False:
            self.word_selector(category)
        self.isCharRepeated()
        if self.isRepeated_bool is True:
            print("\nYour word is: " + str(len(self.word)) + " characters long and has " +
                      str(len(self.charRepeated)) + " repeated character(s).\n")
        else:
            print("\nYour word is: " +
                      str(len(self.word)) + " characters long.\n")
    # Evaluates the user input for a character that is within the selected string

    def evaluate(self, choice):
        if choice in self.word and choice not in self.guessed_correctly and choice.isalpha():
            self.correct()
        elif 'hint count' in self.user_choice:
            if self.hint_count <= 1 and self.hint_count != 0:
                print("You have requested " + str(self.hint_count) + " hints.")
            else:
                print("You have requested " + str(self.hint_count) + " hints.")
        elif 'hint' in choice:
            self.hint()
        elif 'mistakes' in self.user_choice:
            if self.mistakes <= 1 and self.mistakes != 0:
                print("You have made " + str(self.mistakes) + " mistake.")
            else:
                print("You have made "+str(self.mistakes)+" mistakes.")
        else:
            self.incorrect()
    # Provides and tracks hints for the user

    def hint(self):
        if "hint" in self.user_choice and self.hint_count < int(self.allowable_hints):
            self.hint_count += 1
            self.num_picker = random.randint(0, len(self.word) - 1)
            self.letter_hint = self.word[self.num_picker]
            if ' ' in self.letter_hint:
                self.hint()
            print("Your hint is '" + self.letter_hint.upper() + ".'")
        else:
            print("You have used too many hints!")
    # Tracks the amount of correctly guessed characters

    def correct(self):
        if self.user_choice in self.word and len(self.guessed_correctly) <= len(self.word):
            self.guessed_correctly += [self.user_choice] * \
                self.counter[self.user_choice]
            print("\n'"+self.user_choice.upper() + "' was correct.\n")
            print("You have guessed the following letters so far:",
                  ' '.join(self.guessed_correctly))
    # Tracks the amount of incorrectly guessed characters

    def incorrect(self):
        if self.user_choice in self.guessed_correctly:
            self.mistakes += 1
            print("\nYou already guessed '" +
                  self.user_choice.upper() + ",' try again. \n")
        elif not self.user_choice.isalpha():
            print("\nPlease insert a character. \n")
        elif self.mistakes < len(self.word):
            self.mistakes += 1
            self.incorrectly_guessed.append(self.user_choice)
            print("\n'"+self.user_choice.upper() + "' was incorrect.")
        if self.mistakes >= len(self.word) or self.mistakes >= int(self.allowable_mistakes):
            print(
                "\nYou have made too many incorrect guesses. The correct word was '"+self.word+"'\n")
            self.loss_counter += 1
            self.guessed_correctly = []
            self.incorrectly_guessed = []
            self.fail_again = input("Do you want to play again? ").lower()
            if 'y' in self.fail_again:
                self.play()
            else:
                sys.exit(1)

    def win(self):
        while True:
            self.guessed_correctly_sorted = sorted(self.guessed_correctly)
            if self.word_sorted == self.guessed_correctly_sorted:
                print("You win! The word was '" + self.word + "!'\n")
                self.win_again = input("Do you want to play again? ").lower()
                self.win_counter += 1
                print("\nYou have won", self.win_counter, "time(s)\n")
                self.guessed_correctly = []
                self.incorrectly_guessed = []
                if 'yes' in self.win_again:
                    self.play()
                else:
                    print("Thank you for playing!")
                    sys.exit(1)
            self.user_choice = input("\nPick a letter:").lower()
            if self.user_choice == self.word:
                print("You win! The word was '" + self.word + "!'\n")
                self.win_again = input("Do you want to play again? ").lower()
                self.win_counter += 1
                print("\nYou have won", self.win_counter, "time(s)\n")
                self.guessed_correctly = []
                self.incorrectly_guessed = []
                if 'yes' in self.win_again:
                    self.play()
                else:
                    print("Thank you for playing!")
                    sys.exit(1)
            else:
                self.evaluate(self.user_choice)
    # Initiates the play sequence

    def play(self):
        print("\nThe available categories to pick from are", ', '.join(self.keys))
        self.category = input(
            "\nWhat category of words do you want?\n").lower()
        if self.category in self.keys:
            self.word_selector(self.category)
            while self.properCategory is False:
                self.word_selector(self.category)
            
            self.ask_mistakes()
            while self.is_int is False:
                self.ask_mistakes()
            self.ask_hints()
            while self.is_inth is False:
                self.ask_hints()
            self.win()
        else:
            print("\nThat is not a valid category.\n")
            self.play()


hangman = hangman_logic()
hangman.play()
