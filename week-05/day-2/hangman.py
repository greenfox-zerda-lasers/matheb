import random
import string

class Hangman_game():

    def __init__(self):
        self.words = ["krokodil", "ananasz", "nomenklatura", "sokadalom", "barack"]
        self.guess_left = 6
        self.state = "playing"
        self.secretWord = self.words[random.randint(0,4)]
        self.guessed = []
        self.wrong = []

    def test_input(self):
        if self.guess in list(string.ascii_lowercase):
            return True
        else:
            print("Please add only one letter!")

    def display_start(self):
        self.start = []
        for i in range(len(self.secretWord)):
            self.start.append('_')
        return self.start

    def display_progress(self):
        self.progress = self.start
        for i in range(len(self.secretWord)):
            for j in self.guessed:
                if j == self.secretWord[i]:
                    self.progress[i] = j
        return self.progress

    def hangman_graphic(self):
        if self.guess_left == 6:
            print ("________      ")
            print ("|      |      ")
            print ("|             ")
            print ("|             ")
            print ("|             ")
            print ("|             ")
        elif self.guess_left == 5:
            print ("________      ")
            print ("|      |      ")
            print ("|      0      ")
            print ("|             ")
            print ("|             ")
            print ("|             ")
        elif self.guess_left == 4:
            print ("________      ")
            print ("|      |      ")
            print ("|      0      ")
            print ("|      |      ")
            print ("|             ")
            print ("|             ")
        elif self.guess_left == 3:
            print ("________      ")
            print ("|      |      ")
            print ("|      0      ")
            print ("|     /|      ")
            print ("|             ")
            print ("|             ")
        elif self.guess_left == 2:
            print ("________      ")
            print ("|      |      ")
            print ("|      0      ")
            print ("|     /|\     ")
            print ("|             ")
            print ("|             ")
        elif self.guess_left == 1:
            print ("________      ")
            print ("|      |      ")
            print ("|      0      ")
            print ("|     /|\     ")
            print ("|     /       ")
            print ("|             ")
        else:
            print ("________      ")
            print ("|      |      ")
            print ("|      0      ")
            print ("|     /|\     ")
            print ("|     / \     ")
            print ("|             ")


    def the_game(self):
        print("Here is the mistery :", self.display_start())

        while self.state == "playing":

            print("You have already guessed: ", self.wrong)
            self.guess = str(input("Guess a letter!")).lower()
            self.guessed.append(self.guess)
            if self.guess not in self.secretWord:
                self.wrong.append(self.guess)
            self.test_input()

            if self.test_input() == True:
                print(self.display_progress())
                print ("You have ", self.guess_left, " guesses left")
                if self.guess in self.secretWord:
                    if self.guess_left > 0 and self.progress != list(self.secretWord):
                        self.guess_left = self.guess_left
                        self.hangman_graphic()
                    elif self.progress == list(self.secretWord):
                        self.hangman_graphic()
                        print("You won")
                        self.state = "finished"
                    else:
                        self.hangman_graphic()
                        print("You lost")
                        self.state = "finished"
                else:
                    print ("This letter is not in the word.")
                    self.guess_left -= 1
                    self.hangman_graphic()


game = Hangman_game()
print(game.the_game())
