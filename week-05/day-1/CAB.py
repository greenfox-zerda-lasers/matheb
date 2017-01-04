#Create a class what is capable of playing exactly one game of Cows and
#Bulls (CAB). The player have to guess a 4 digit number. For every digit
#that the player guessed correctly in the correct place, they have a “cow”.
#For every digit the player guessed correctly in the wrong place is a “bull.”
import random

class CAB_game():

    def __init__(self):
        self.secretNumber = str(random.randint(1000,9999))
        self.count = 0
        self.state = "playing"
        #print(self.secretNumber)

    def state_of_game(self):
        if self.result == ['cow', 'cow', 'cow', 'cow']:
            self.state = "finished"

    def guess_result(self):
        self.guessedNumber = str(input("Guess an integer from 1000-9999: "))
        self.result = []
        for i in range(4):
            if self.guessedNumber[i] == self.secretNumber[i]:
                self.result.append('cow')
            elif self.guessedNumber[i] not in self.secretNumber:
                self.result.append('none')
            else:
                self.result.append('bull')

    def count_guess(self):
        if self.result != ['cow', 'cow', 'cow', 'cow']:
            self.count += 1

    def play(self):
        self.guess_result()
        self.count_guess()
        self.state_of_game()
        return self.result

game = CAB_game()
while game.state == "playing":
    print(game.play())
