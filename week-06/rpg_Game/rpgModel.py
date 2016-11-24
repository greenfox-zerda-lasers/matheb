import random
import board

class Model():

    def __init__(self):
        self.board = board.board
        self.level = 1

    def map(self):
        return self.board


class Character():

    def __init__(self):
        self.position_i = 0
        self.position_j = 0
        self.HP = 20 + 3 * random.randint(1,6)
        self.DP = 2 * random.randint(1,6)
        self.SP = 5 + random.randint(1,6)
        self.SV = 2*random.randint(1,6) + self.SP
        self.level = 1
        self.steps = 2
        self.state = 'alive'

    def moveDown(self):
        if self.position_i+1 <= 10 and board.board[self.position_i+1][self.position_j] != 'w':
            self.position_i += 1
            self.steps += 1

    def moveUp(self):
        if self.position_i-1 >= 0 and board.board[self.position_i-1][self.position_j] != 'w':
            self.position_i -= 1
            self.steps += 1

    def moveRight(self):
        if self.position_j+1 <= 9 and board.board[self.position_i][self.position_j+1] != 'w':
            self.position_j += 1
            self.steps += 1

    def moveLeft(self):
        if self.position_j-1 >= 0 and board.board[self.position_i][self.position_j-1] != 'w':
            self.position_j -= 1
            self.steps += 1

    def setPosition(self, i, j):
        self.position_i = i
        self.position_j = j

class Hero(Character):

    def __init__(self):
        Character.__init__(self)
        self.state = 'alive'


    def sendPosition(self):
        return(self.position_i, self.position_j)

class Monster(Character):

    def __init__(self):
        Character.__init__(self)
        self.position_i = random.randint(0, 10)
        self.position_j = random.randint(0, 9)
        self.HP = 2 * self.level * random.randint(1,6)
        self.DP = self.level/2 * random.randint(1,6)
        self.SP = self.level * random.randint(1,6)
        self.moveDirection = ['r', 'l', 'u', 'd']
        self.state = 'alive'

    def initDataMonster(self):
        self.level += 1
        self.HP = 2 * self.level * random.randint(1,6)
        self.DP = self.level/2 * random.randint(1,6)
        self.SP = self.level * random.randint(1,6)
        self.position_i = random.randint(0, 10)
        self.position_j = random.randint(0, 9)
        self.state = 'alive'

    def moveDown(self):
        if self.position_i+1 <= 10 and board.board[self.position_i+1][self.position_j] != 'w':
            self.position_i += 1

    def moveUp(self):
        if self.position_i-1 >= 0 and board.board[self.position_i-1][self.position_j] != 'w':
            self.position_i -= 1

    def moveRight(self):
        if self.position_j+1 <= 9 and board.board[self.position_i][self.position_j+1] != 'w':
            self.position_j += 1

    def moveLeft(self):
        if self.position_j-1 >= 0 and board.board[self.position_i][self.position_j-1] != 'w':
            self.position_j -= 1

    def moveMonster(self):
        if self.steps % 2 == 0:
            choose = random.randint(1, len(self.moveDirection)+1)
            if choose == 1:
                self.moveRight()
            elif choose == 2:
                self.moveLeft()
            elif choose == 3:
                self.moveUp()
            elif choose == 4:
                self.moveDown()

    def sendPosition(self):
        if board.board[self.position_i][self.position_j] != 'w':
            return(self.position_i, self.position_j)
        else:
            if self.position_j >= 6:
                while board.board[self.position_i][self.position_j] == 'w':
                    self.position_j -= 1
            else:
                while board.board[self.position_i][self.position_j] == 'w':
                    self.position_j -= 1
            return(self.position_i, self.position_j)

class Boss(Monster, Character):

    def __init__(self):
        Monster.__init__(self)
        self.HP = 2 * self.level * random.randint(1,6) + random.randint(1,6)
        self.DP = self.level/2 * random.randint(1,6) + random.randint(1,6)
        self.SP = self.level * random.randint(1,6) + self.level
        self.SV = 2*random.randint(1,6) + self.SP

    def initDataBoss(self):
        self.HP = 2 * self.level * random.randint(1,6) + random.randint(1,6)
        self.DP = self.level/2 * random.randint(1,6) + random.randint(1,6)
        self.SP = self.level * random.randint(1,6) + self.level
        self.SV = 2*random.randint(1,6) + self.SP
        self.position_i = random.randint(0, 10)
        self.position_j = random.randint(0, 9)
        self.state = 'alive'

    def sendPosition(self):
        if board.board[self.position_i][self.position_j] != 'w':
            return(self.position_i, self.position_j)
        else:
            if self.position_j >= 6:
                while board.board[self.position_i][self.position_j] == 'w':
                    self.position_j -= 1
            else:
                while board.board[self.position_i][self.position_j] == 'w':
                    self.position_j -= 1
            return(self.position_i, self.position_j)
