import rpgModel
import rpgView
import sys
import random

class Controller():

    def __init__(self):

        self.model = rpgModel.Model()
        self.character = rpgModel.Character()
        self.hero = rpgModel.Hero()
        for i in range(random.randint(3,5)):
            self.monster = rpgModel.Monster()
        #self.monster2 = rpgModel.Monster()
        #self.monster3 = rpgModel.Monster()
        self.boss = rpgModel.Boss()
        self.view = rpgView.DisplayBoard()
        self.enemy = 'none'
        # irányító gombok
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
        """self.view.drawCharacter(self.monster2.sendPosition(), 'monster')
        self.view.drawCharacter(self.monster3.sendPosition(), 'monster')"""

    def startBoss(self):
        self.view.drawCharacter(self.boss.sendPosition(), 'boss')

    def writeDatasHero(self):
        self.view.drawTextHero(self.hero.HP, self.hero.DP, self.hero.SP, self.hero.SV)

    def writeDatasMonster(self):
        self.view.drawTextMonster(self.monster.HP, self.monster.DP, self.monster.SP, self.monster.SV)

    def startGame(self):
        self.startBoard()
        self.startHero()
        self.startMonster()
        self.startBoss()
        self.writeDatasHero()
        self.writeDatasMonster()
        #if self.hero.state == 'alive':
        #self.down_key_detected('event')

    def drawMonsters(self):
        self.view.drawCharacter((self.monster.position_i, self.monster.position_j), 'monster')
        """self.view.drawCharacter((self.monster2.position_i, self.monster2.position_j), 'monster')
        self.view.drawCharacter((self.monster3.position_i, self.monster3.position_j), 'monster')"""

    def monsterMoves(self):
        self.view.clearCharacter((self.monster.position_i, self.monster.position_j))
        self.monster.moveMonster()
        self.view.drawCharacter((self.monster.position_i, self.monster.position_j), 'monster')
        """self.view.clearCharacter((self.monster2.position_i, self.monster2.position_j))
        self.monster2.moveMonster()
        self.view.drawCharacter((self.monster2.position_i, self.monster2.position_j), 'monster')
        self.view.clearCharacter((self.monster3.position_i, self.monster3.position_j))
        self.monster3.moveMonster()
        self.view.drawCharacter((self.monster3.position_i, self.monster3.position_j), 'monster')"""

    def bossMoves(self):
        self.view.clearCharacter((self.boss.position_i, self.boss.position_j))
        self.boss.moveMonster()
        self.view.drawCharacter((self.boss.position_i, self.boss.position_j), 'boss')


    def downKeyDetected(self, event):
        self.view.clearCharacter((self.character.position_i, self.character.position_j))
        self.character.moveDown()
        if self.monster.state == 'alive':
            self.drawMonsters()
            self.monsterMoves()
        self.view.drawCharacter((self.boss.position_i, self.boss.position_j), 'boss')
        self.bossMoves()
        self.view.drawCharacter((self.character.position_i, self.character.position_j), 'hero_down')
        print([self.monster.position_i, self.monster.position_j])
        print([self.character.position_i, self.character.position_j])

    def upKeyDetected(self, event):
        self.view.clearCharacter((self.character.position_i, self.character.position_j))
        self.character.moveUp()
        if self.monster.state == 'alive':
            self.drawMonsters()
            self.monsterMoves()
        self.view.drawCharacter((self.boss.position_i, self.boss.position_j), 'boss')
        self.bossMoves()
        self.view.drawCharacter((self.character.position_i, self.character.position_j), 'hero_up')
        print([self.monster.position_i, self.monster.position_j])
        print([self.character.position_i, self.character.position_j])

    def rightKeyDetected(self, event):
        self.view.clearCharacter((self.character.position_i, self.character.position_j))
        self.character.moveRight()
        if self.monster.state == 'alive':
            self.drawMonsters()
            self.monsterMoves()
        self.view.drawCharacter((self.boss.position_i, self.boss.position_j), 'boss')
        self.bossMoves()
        self.view.drawCharacter((self.character.position_i, self.character.position_j), 'hero_right')
        print([self.monster.position_i, self.monster.position_j])
        print([self.character.position_i, self.character.position_j])

    def leftKeyDetected(self, event):
        self.view.clearCharacter((self.character.position_i, self.character.position_j))
        self.character.moveLeft()
        if self.monster.state == 'alive':
            self.drawMonsters()
            self.monsterMoves()
        self.view.drawCharacter((self.boss.position_i, self.boss.position_j), 'boss')
        self.bossMoves()
        self.view.drawCharacter((self.character.position_i, self.character.position_j), 'hero_left')
        print([self.monster.position_i, self.monster.position_j])
        print([self.character.position_i, self.character.position_j])

    def battleHappens(self, event):
        if [self.character.position_i, self.character.position_j] == [self.monster.position_i, self.monster.position_j]:
            #enemy = self.monster
            """ elif [self.hero.position_i, self.hero.position_j] == [self.monster2.position_i, self.monster2.position_j]:
                enemy = self.monster2
            elif [self.hero.position_i, self.hero.position_j] == [self.monster3.position_i, self.monster3.position_j]:
                enemy = self.monster3
            elif [self.hero.position_i, self.hero.position_j] == [self.monster3.position_i, self.monster3.position_j]:
                enemy = self.monster3
            elif [self.hero.position_i, self.hero.position_j] == [self.boss.position_i, self.boss.position_j]:
                enemy = self.boss"""

            while self.character.state == 'alive' and self.monster.state == 'alive':
            #print("FIGHT",self.monster)
                self.strike('event', self.monster)
                self.view.clearText()
                self.writeDatasHero()
                self.writeDatasMonster()
                self.view.root.canvas_update()

    def isHeroSuccessful(self, enemy):
        if self.character.SV >= self.monster.DP and self.monster.HP > 0:
            return True
        elif self.monster.HP <= 0:
            self.monster.state = 'dead'
            self.view.clearCharacter((self.character.position_i, self.character.position_j))
            self.view.drawCharacter((self.character.position_i, self.character.position_j), 'hero')
            print('Enemy is dead')

    def isEnemySuccessful(self, enemy):
        if self.hero.SV < self.monster.DP and self.hero.HP > 0:
            return True
        elif self.character.HP <= 0:
            self.character.state = 'dead'
            self.view.clearCharacter((self.character.position_i, self.character.position_j))
            print('Game Over')

    def strikeEnemy(self, event, enemy):
        #while self.hero.state == 'alive' and enemy.state == 'alive':
        if self.isHeroSuccessful(enemy) == True:
            self.monster.HP -= (self.character.SV - self.monster.DP)

    def strikeHero(self, event, enemy):
        if self.isEnemySuccessful(enemy) == True:
            self.character.HP -= (self.monster.SV - self.character.DP)

    def strike(self, event, enemy):
        self.strikeEnemy(event, enemy)
        self.strikeHero(event, enemy)




first = Controller()
"""first.startBoard()
first.startHero()
first.startMonster()
first.startBoss()"""
first.startGame()
first.view.root.mainloop()
