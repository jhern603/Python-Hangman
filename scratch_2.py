import random
import time
import collections
import sys
class hangman_logic:
    #Cannot check for multiple letters, does not check for incorrect variable type

    def __init__(self):

        self.words = ['abaft', 'spiffy', 'flag', 'deep', 'fill', 'outstanding', 'maid', 'tacit', 'suspect', 'spiders',
                 'toys', 'ill-fated', 'summer', 'punch', 'godly', 'snow', 'appear', 'amount', 'cup', 'private',
                 'parcel', 'different', 'sign', 'apparatus', 'fair', 'afternoon', 'bea', 'snakes', 'fancy', 'smile',
                 'kiss']
        self.picker = random.randint(0, len(self.words)) - 2
        self.word_selector()
        print("Your word is: "+str(len(self.word))+" characters long.")
        time.sleep(1.5)
        self.ask_mistakes()
        while self.is_int is False:
            self.ask_mistakes()
        time.sleep(.300)
        self.ask_hints()
        while self.is_inth is False:
            self.ask_hints()
        time.sleep(.300)
        self.guessed_correctly=[]
        self.incorrectly_guessed=[]
        self.mistakes=0
        self.hint_count=0
        print("\n\nHangman is starting soon...\n")
        time.sleep(1)

    def ask_mistakes(self):
        self.is_int=False
        self.allowable_mistakes = input("What do you want to be the maximum number of mistakes? ")
        if self.allowable_mistakes != '' and int(self.allowable_mistakes) > 0 :
            print("The maximum number of mistakes you can make this round is: " + self.allowable_mistakes + '\n')
            self.is_int=True
        elif self.allowable_mistakes == '':
            print('Insert an integer! \n')
            self.is_int = False

    def ask_hints(self):
        self.is_inth=False
        self.allowable_hints = input("What do you want the maximum number of hints to be? ")
        if self.allowable_hints != '' and int(self.allowable_hints) > 0 :
            print("The maximum number of hints you can request this round is: " + self.allowable_hints + '\n')
            self.is_inth=True
        elif self.allowable_hints == '':
            print('Insert an integer! \n')
            self.is_inth = False

    def word_selector(self):
        self.word = self.words[self.picker].lower()
        self.counter= collections.Counter(self.word)

    def isStringRepeated(self):
        self.repeattracker = False
        for k in self.counter:
            if self.counter[k] > 1:
                self.repeattracker = True
        return self.repeattracker

    def evaluate(self, choice):

        if choice in self.word and choice not in self.guessed_correctly and choice != ''and choice != float():
            self.correct()
        elif 'hint count' in self.user_choice:
            print("You have requested"+ str(self.hint_count) +" hints.")
        elif 'hint' in choice:
            self.hint()
        elif 'mistakes' in self.user_choice:
            print("You have made "+str(self.mistakes)+" mistakes.")
        else:
            self.incorrect()

    def hint(self):
        if "hint" in self.user_choice and self.hint_count < int(self.allowable_hints):
            self.hint_count+=1
            self.num_picker = random.randint(0, len(self.word) - 1)
            self.letter_hint=self.word[self.num_picker]
            print("Your hint is '" +self.letter_hint.upper()+ ".'")
        else:
            print("You have used too many hints!")

    def correct(self):
        if self.user_choice in self.word and len(self.guessed_correctly) <= len(self.word):
            self.guessed_correctly.append(self.user_choice)
            print("\n'"+self.user_choice.upper() + "' was correct.\n")
        return len(self.guessed_correctly)

    def incorrect(self):
        if self.user_choice in self.guessed_correctly:
            self.mistakes += 1
            print("\nYou already guessed '" + self.user_choice.upper() + ",' try again. \n")
        elif self.mistakes < len(self.word):
            self.mistakes += 1
            self.incorrectly_guessed.append(self.user_choice)
            print("\n'"+self.user_choice.upper() + "' was incorrect.")
        if self.mistakes >= len(self.word) or self.mistakes >= int(self.allowable_mistakes):
                print("\nYou have made too many incorrect guesses. The correct word was '"+self.word+"'\n")

    def play(self):
        while True:
            if len(self.word) == len(self.guessed_correctly):
                print("You win! The word was '" + self.word + "!'\n")
                sys.exit(1)
            self.user_choice = input("\nPick a letter:").lower()
            self.evaluate(self.user_choice)
            print(self.guessed_correctly)

#After logic, add in features for settings or to replay in a separate class.
hangman = hangman_logic()
hangman.play()