import rpgModel
import rpgView
import sys

class Controller():

    def __init__(self):

        self.model = rpgModel.Model()
        self.character = rpgModel.Character()
        self.hero = rpgModel.Hero()
        self.monster = rpgModel.Monster()
        self.monster2 = rpgModel.Monster()
        self.monster3 = rpgModel.Monster()
        self.boss = rpgModel.Boss()
        self.view = rpgView.DisplayBoard()
        # irányító gombok
        self.view.root.bind('<Left>', self.leftKeyDetected)
        self.view.root.bind('<Right>', self.rightKeyDetected)
        self.view.root.bind('<Up>', self.upKeyDetected)
        self.view.root.bind('<Down>', self.downKeyDetected)
        #self.view.root.bind('<Return>', self.return_key_detected)

    def startBoard(self):
        self.view.drawMap(self.model.map())

    def startHero(self):
        self.view.drawCharacter(self.hero.sendPosition(), 'hero_down')

    def startMonster(self):
        self.view.drawCharacter(self.monster.sendPosition(), 'monster')
        self.view.drawCharacter(self.monster2.sendPosition(), 'monster')
        self.view.drawCharacter(self.monster3.sendPosition(), 'monster')

    def startBoss(self):
        self.view.drawCharacter(self.boss.sendPosition(), 'boss')

    def startGame(self):
        self.startBoard()
        self.startHero()
        self.startMonster()
        self.startBoss()
        #if self.hero.state == 'alive':
        #self.down_key_detected('event')

    def drawMonsters(self):
        self.view.drawCharacter((self.monster.position_i, self.monster.position_j), 'monster')
        self.view.drawCharacter((self.monster2.position_i, self.monster2.position_j), 'monster')
        self.view.drawCharacter((self.monster3.position_i, self.monster3.position_j), 'monster')

    def monsterMoves(self):
        self.view.clearCharacter((self.monster.position_i, self.monster.position_j))
        self.monster.moveMonster()
        self.view.drawCharacter((self.monster.position_i, self.monster.position_j), 'monster')
        self.view.clearCharacter((self.monster2.position_i, self.monster2.position_j))
        self.monster2.moveMonster()
        self.view.drawCharacter((self.monster2.position_i, self.monster2.position_j), 'monster')
        self.view.clearCharacter((self.monster3.position_i, self.monster3.position_j))
        self.monster3.moveMonster()
        self.view.drawCharacter((self.monster3.position_i, self.monster3.position_j), 'monster')

    def bossMoves(self):
        self.view.clearCharacter((self.boss.position_i, self.boss.position_j))
        self.boss.moveMonster()
        self.view.drawCharacter((self.boss.position_i, self.boss.position_j), 'boss')


    def downKeyDetected(self, event):
        self.view.clearCharacter((self.character.position_i, self.character.position_j))
        self.character.moveDown()
        self.drawMonsters()
        self.view.drawCharacter((self.boss.position_i, self.boss.position_j), 'boss')
        self.monsterMoves()
        self.bossMoves()
        self.view.drawCharacter((self.character.position_i, self.character.position_j), 'hero_down')

    def upKeyDetected(self, event):
        self.view.clearCharacter((self.character.position_i, self.character.position_j))
        self.character.moveUp()
        self.drawMonsters()
        self.view.drawCharacter((self.boss.position_i, self.boss.position_j), 'boss')
        self.monsterMoves()
        self.bossMoves()
        self.view.drawCharacter((self.character.position_i, self.character.position_j), 'hero_up')

    def rightKeyDetected(self, event):
        self.view.clearCharacter((self.character.position_i, self.character.position_j))
        self.character.moveRight()
        self.drawMonsters()
        self.view.drawCharacter((self.boss.position_i, self.boss.position_j), 'boss')
        self.monsterMoves()
        self.bossMoves()
        self.view.drawCharacter((self.character.position_i, self.character.position_j), 'hero_right')

    def leftKeyDetected(self, event):
        self.view.clearCharacter((self.character.position_i, self.character.position_j))
        self.character.moveLeft()
        self.drawMonsters()
        self.view.drawCharacter((self.boss.position_i, self.boss.position_j), 'boss')
        self.monsterMoves()
        self.bossMoves()
        self.view.drawCharacter((self.character.position_i, self.character.position_j), 'hero_left')





first = Controller()
"""first.startBoard()
first.startHero()
first.startMonster()
first.startBoss()"""
first.startGame()
first.view.root.mainloop()
