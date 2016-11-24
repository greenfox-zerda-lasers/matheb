import rpgModel
import rpgView
import sys
import random

class Controller():

    def __init__(self):

        self.model = rpgModel.Model()
        self.character = rpgModel.Character()
        self.hero = rpgModel.Hero()
        self.monster = rpgModel.Monster()
        self.keyholder = rpgModel.Monster()
        self.boss = rpgModel.Boss()
        self.view = rpgView.DisplayBoard()
        self.view.root.bind('<Left>', self.leftKeyDetected)
        self.view.root.bind('<Right>', self.rightKeyDetected)
        self.view.root.bind('<Up>', self.upKeyDetected)
        self.view.root.bind('<Down>', self.downKeyDetected)
        self.view.root.bind('<space>', self.battleHappens)

    def startBoard(self):
        self.view.drawMap(self.model.map())

    def startHero(self):
        self.view.drawCharacter(self.hero.sendPosition(), 'hero_down')

    def startMonster(self):
        self.view.drawCharacter(self.monster.sendPosition(), 'monster')

    def startKeyholder(self):
        self.view.drawCharacter(self.keyholder.sendPosition(), 'monster')

    def startBoss(self):
        self.view.drawCharacter(self.boss.sendPosition(), 'boss')

    def writeDatasHero(self):
        self.view.drawTextHero(self.character.HP, self.character.DP, self.character.SP, self.character.level)

    def writeDatasEnemy(self, enemy):
        self.view.drawTextEnemy(enemy.HP, enemy.DP, enemy.SP)

    def drawMonsters(self):
        self.view.drawCharacter((self.monster.position_i, self.monster.position_j), 'monster')

    def drawKeyholder(self):
        self.view.drawCharacter((self.keyholder.position_i, self.keyholder.position_j), 'monster')

    def monsterMoves(self):
        self.view.clearCharacter((self.monster.position_i, self.monster.position_j))
        self.monster.moveMonster()
        self.view.drawCharacter((self.monster.position_i, self.monster.position_j), 'monster')

    def keyholderMoves(self):
        self.view.clearCharacter((self.keyholder.position_i, self.keyholder.position_j))
        self.keyholder.moveMonster()
        self.view.drawCharacter((self.keyholder.position_i, self.keyholder.position_j), 'monster')

    def bossMoves(self):
        self.view.clearCharacter((self.boss.position_i, self.boss.position_j))
        self.boss.moveMonster()
        self.view.drawCharacter((self.boss.position_i, self.boss.position_j), 'boss')

    def checkFiguresStatesAndMoveAndDraw(self):
        if self.monster.state == 'alive':
            self.monsterMoves()
            self.drawMonsters()
        elif self.keyholder.state == 'alive':
            self.keyholderMoves()
            self.drawKeyholder()
        elif self.boss.state == 'alive':
            self.bossMoves()
            self.view.drawCharacter((self.boss.position_i, self.boss.position_j), 'boss')

    def downKeyDetected(self, event):
        self.view.clearCharacter((self.character.position_i, self.character.position_j))
        self.character.moveDown()
        self.checkFiguresStatesAndMoveAndDraw()
        self.view.drawCharacter((self.character.position_i, self.character.position_j), 'hero_down')

    def upKeyDetected(self, event):
        self.view.clearCharacter((self.character.position_i, self.character.position_j))
        self.character.moveUp()
        self.checkFiguresStatesAndMoveAndDraw()
        self.view.drawCharacter((self.character.position_i, self.character.position_j), 'hero_up')

    def rightKeyDetected(self, event):
        self.view.clearCharacter((self.character.position_i, self.character.position_j))
        self.character.moveRight()
        self.checkFiguresStatesAndMoveAndDraw()
        self.view.drawCharacter((self.character.position_i, self.character.position_j), 'hero_right')

    def leftKeyDetected(self, event):
        self.view.clearCharacter((self.character.position_i, self.character.position_j))
        self.character.moveLeft()
        self.checkFiguresStatesAndMoveAndDraw()
        self.view.drawCharacter((self.character.position_i, self.character.position_j), 'hero_left')

    def battleHappens(self, event):
        self.view.clearText()
        self.writeDatasHero()
        if [self.character.position_i, self.character.position_j] == [self.monster.position_i, self.monster.position_j]:
            enemy = self.monster
        elif [self.character.position_i, self.character.position_j] == [self.boss.position_i, self.boss.position_j]:
            enemy = self.boss
        elif [self.character.position_i, self.character.position_j] == [self.keyholder.position_i, self.keyholder.position_j]:
            enemy = self.keyholder
        if [self.character.position_i, self.character.position_j] == [enemy.position_i, enemy.position_j]:
            if self.character.state == 'alive' and enemy.state == 'alive':
                self.strike('event', enemy)
                self.writeDatasEnemy(enemy)
                if self.boss.state == 'dead' and self.keyholder.state == 'dead':
                    self.character.level += 1
                    self.view.clearCharacter((self.character.position_i, self.character.position_j))
                    self.startGame()

    def isHeroSuccessful(self, enemy):
        if self.character.SV >= enemy.DP and enemy.HP > 0:
            return True
        elif enemy.HP <= 0:
            enemy.state = 'dead'
            self.view.clearCharacter((self.character.position_i, self.character.position_j))
            self.view.drawCharacter((self.character.position_i, self.character.position_j) , 'hero')
            self.character.HP += random.randint(1,6)
            self.character.DP += random.randint(1,6)
            self.character.SP += random.randint(1,6)
            print('Enemy is dead')

    def isEnemySuccessful(self, enemy):
        if self.character.DP < enemy.SV and self.character.HP > 0:
            return True
        elif self.character.HP <= 0:
            self.character.state = 'dead'
            self.view.clearCharacter((self.character.position_i, self.character.position_j))
            self.view.drawTextGameOver()
            print('Game Over')

    def strikeEnemy(self, event, enemy):
        """SV = 2*random.randint(1,6) + enemy.SP
        self.character.SV = 2*random.randint(1,6) + self.character.SP"""
        if self.isHeroSuccessful(enemy) == True:
            enemy.HP -= (self.character.SV - enemy.DP)


    def strikeHero(self, event, enemy):
        """SV = 2*random.randint(1,6) + enemy.SP
        self.character.SV = 2*random.randint(1,6) + self.character.SP"""
        if self.isEnemySuccessful(enemy) == True:
            self.character.HP -= (enemy.SV - self.character.DP)


    def strike(self, event, enemy):
        self.strikeEnemy(event, enemy)
        self.strikeHero(event, enemy)

    def startGame(self):
        self.view.clearScreen()
        self.startBoard()
        self.monster.initDataMonster()
        self.keyholder.initDataMonster()
        self.boss.initDataBoss()
        self.character.setPosition(0, 0)
        self.startHero()
        self.startMonster()
        self.startKeyholder()
        self.startBoss()
        self.writeDatasHero()
        #self.battleHappens('event')


first = Controller()
first.startGame()
first.view.root.mainloop()
