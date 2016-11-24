import rpgModel
import rpgView
import sys

class Controller():

    def __init__(self):

        self.model = rpgModel.Model()
        self.character = rpgModel.Character()
        self.hero = rpgModel.Hero()
        self.monster = rpgModel.Monster()
        self.boss = rpgModel.Boss()
        self.view = rpgView.DisplayBoard()
        # irányító gombok
        #self.view.root.bind('<Left>', self.left_key_detected)
        #self.view.root.bind('<Right>', self.right_key_detected)
        #self.view.root.bind('<Up>', self.up_key_detected)
        self.view.root.bind('<Down>', self.downKeyDetected)
        #self.view.root.bind('<Return>', self.return_key_detected)

    def startBoard(self):
        self.view.drawMap(self.model.map())

    def startHero(self):
        self.view.drawCharacter(self.hero.sendPosition(), 'hero')

    def startMonster(self):
        self.view.drawCharacter(self.monster.sendPosition(), 'monster')

    def startBoss(self):
        self.view.drawCharacter(self.boss.sendPosition(), 'boss')

    def startGame(self):
        self.startBoard()
        self.startHero()
        self.startMonster()
        self.startBoss()
        #if self.hero.state == 'alive':
        #self.down_key_detected('event')

    """def gamePlay(self):
        if sys.argv[1] == "rpgController.py":
            self.startGame()
        while self.hero.sate == 'alive':"""


    def downKeyDetected(self, event):
        self.view.clearCharacter((self.character.position_i, self.character.position_j), 'hero')
        self.character.moveDown()
        self.view.drawCharacter((self.character.position_i, self.character.position_j), 'hero')





first = Controller()
"""first.startBoard()
first.startHero()
first.startMonster()
first.startBoss()"""
first.startGame()
first.downKeyDetected('event')
first.view.root.mainloop()
