import random

class Game:

    def __init__(self):
        self.winningNumber = random.randint(0,100)
        self.humanGuess()

    def humanGuess(self):
        self.humanGuessNumber = int(input("Guess from 0-100"))
        self.comGuess()
        return self.humanGuessNumber
    def comGuess(self):
        self.comGuessNumber = random.randint(0,100)
        self.conclude()
        return self.comGuessNumber
    def conclude(self):
        if abs(self.winningNumber - self.humanGuessNumber)< abs(self.winningNumber - self.comGuessNumber):
            print("You win")
        else:
            print("You suck")


game = Game()
