#DEV: JOSE 'POOPITYSCOOP' HERNANDEZ
#SSN: 123-45-7890
#BUGS: non-valid category thrown out inf times
#NOTES: Added ability to check for repeated characters
#TODO: Add in inf mistakes and hints capability, add in a mulligan for words with non-alpha characters
#NOTES FOR FUTURE DEV: Categories by dictionary
import random
import time
import collections
import sys
class hangman_logic:
    #Initializes base variables
    def __init__(self):
        self.words = {'movies':['full metal jacket', 'Major Payne', 'American Sniper', 'Lone Survivor', 'twelve strong']}
        self.guessed_correctly=[]
        self.incorrectly_guessed=[]
        self.mistakes=0
        self.hint_count=0
        self.win_counter=0
        self.loss_counter=0
        print("\n\nHangman is starting soon...\n")
        time.sleep(1)
    #Asks the user for max number of mistakes for that round
    def ask_mistakes(self):
        self.is_int = False
        self.allowable_mistakes = input("What do you want to be the maximum number of mistakes? ")
        try:
            int(self.allowable_mistakes)
            self.is_int = True
            if self.allowable_mistakes.isdigit() and int(self.allowable_mistakes) <= len(self.word):
                print("The maximum number of mistakes you can make this round is: " + self.allowable_mistakes + '\n')
            elif int(self.allowable_mistakes) > len(self.word):
                print("\nThe maximum amount of mistakes allowed is up to the length of the word.\n")
                self.ask_mistakes()
        except ValueError:
            self.is_int = False
            print("Strings are not accepted: insert an integer!")
    # Asks the user for max number of hints for that round
    def ask_hints(self):
        self.is_inth=False
        self.allowable_hints = input("What do you want the maximum number of hints to be? ")
        try:
            int(self.allowable_mistakes)
            if self.allowable_hints != '' and int(self.allowable_hints) <= len(self.word):
                print("The maximum number of hints you can request this round is: " + self.allowable_hints + '\n')
                self.is_inth = True
            elif int(self.allowable_hints) > len(self.word):
                print("\nThe maximum amount of hints allowed are up to the length of the word.\n")
        except ValueError:
            print("Strings are not accepted: insert an integer!")
            self.is_inth = False
    # Check for character repetition in selected string
    def isRepeated(self):
        self.isRepeated = False
        self.charRepeated = []
        for k in self.counter:
            if self.counter[k] > 1:
                self.charRepeated.append(k)
                self.isRepeated = True
    # Selects a string for the round
    def word_selector(self,category):
        self.properCategory = False
        if category in self.words:
            self.properCategory = True
            print("\nYou selected: '" +self.category+ "' as the category for this round.\n")
            self.picker = random.randint(0, len(self.words[self.category])) - 2
            self.selected_category = self.words[category]
            self.word = self.selected_category[self.picker].lower()
            self.counter = collections.Counter(self.word)
            self.isAlpha = True
        else:
            self.properCategory=False
            print("\nThat is not a valid category, try again...\n")
        ####WTF####
        '''
        for char in self.word:
            if not char.isalpha():
                print(char)
                self.isRepeated = False
                self.play()
                '''
    # Evaluates the user input for a character that is within the selected string
    def evaluate(self, choice):

        if choice in self.word and choice not in self.guessed_correctly and choice.isalpha():
            self.correct()
        elif 'hint count' in self.user_choice:
            if self.hint_count<=1 and self.hint_count != 0:
                print("You have requested "+ str(self.hint_count) +" hints.")
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
            self.hint_count+=1
            self.num_picker = random.randint(0, len(self.word) - 1)
            self.letter_hint=self.word[self.num_picker]
            print("Your hint is '" +self.letter_hint.upper()+ ".'")
        else:
            print("You have used too many hints!")
    # Tracks the amount of correctly guessed characters
    def correct(self):
        if self.user_choice in self.word and len(self.guessed_correctly) <= len(self.word):
            self.guessed_correctly.append(self.user_choice)
            if self.user_choice in self.charRepeated:
                self.guessed_correctly.append(self.user_choice)
            print("\n'"+self.user_choice.upper() + "' was correct.\n")
    # Tracks the amount of incorrectly guessed characters
    def incorrect(self):
        if self.user_choice in self.guessed_correctly:
            self.mistakes += 1
            print("\nYou already guessed '" + self.user_choice.upper() + ",' try again. \n")
        elif not self.user_choice.isalpha():
            print("\nPlease insert a character. \n")
        elif self.mistakes < len(self.word):
            self.mistakes += 1
            self.incorrectly_guessed.append(self.user_choice)
            print("\n'"+self.user_choice.upper() + "' was incorrect.")
        if self.mistakes >= len(self.word) or self.mistakes >= int(self.allowable_mistakes):
            print("\nYou have made too many incorrect guesses. The correct word was '"+self.word+"'\n")
            self.loss_counter+=1
            self.guessed_correctly = []
            self.incorrectly_guessed = []
            self.fail_again=input("Do you want to play again? ").lower()
            if 'y' in self.fail_again:
                self.play()
            else:
                sys.exit(1)
    # Initiates the play sequence
    def play(self):
        self.category=input("What category of words do you want?").lower()
        self.word_selector(self.category)
        while self.properCategory is False:
            self.word_selector(self.category)
        time.sleep(.300)
        self.isRepeated()
        if self.isRepeated is True:
            print("Your word is: " + str(len(self.word)) + " characters long and has "+ str(len(self.charRepeated)) +" repeated character(s).")
        else:
            print("Your word is: " + str(len(self.word)) + " characters long.")
        time.sleep(1.5)
        self.ask_mistakes()
        while self.is_int is False:
            self.ask_mistakes()
        time.sleep(.300)
        self.ask_hints()
        while self.is_inth is False:
            self.ask_hints()
        time.sleep(.300)
        while True:
            if len(self.word) == len(self.guessed_correctly):
                print("You win! The word was '" + self.word + "!'\n")
                self.win_again = input("Do you want to play again? ").lower()
                self.win_counter+=1
                print(self.win_counter)
                self.guessed_correctly = []
                self.incorrectly_guessed = []
                if 'y' in self.win_again:
                    self.play()
                else:
                    sys.exit(1)
            self.user_choice = input("\nPick a letter:").lower()
            self.evaluate(self.user_choice)
hangman = hangman_logic()
hangman.play()