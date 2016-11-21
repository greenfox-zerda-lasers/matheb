# Create a robot controller class. This is the mind of the robot.
# It should take an user input by listening to user input:
# Default functionaly when the robot is switched on:
#  - Automatically names the robot
#  - Sets it's position
#
# List of commands:
#  1) memorize: add a new memory entry to the memory
#  2) recall: displays a list memories
#  3) move: increments the robot's position by one coordinate the N-S-E-W directions
#     - it also displays the new position
#  4) speak: it can introduce itself by saying its name and mood and last memory
#
# Create the class with MVC pattern in mind. It should get and store data in the model object
# and it should pass the data to the view objects

import robot_model
import robot_view
import sys

class Control():

    def __init__(self):
        self.model = robot_model.Model()
        self.view = robot_view.View()

    def flow(self):
        if sys.argv[0] == "robot_controller.py" and len(sys.argv) < 2:
            self.printUsage()
        elif sys.argv[0] == "robot_controller.py" and sys.argv[1] == "n":
            self.move_N()
            self.view.draw_position(self.model.position_x, self.model.position_y, self.model.name, self.model.mood)
        elif sys.argv[0] == "robot_controller.py" and sys.argv[1] == "s":
            self.move_S()
            self.view.draw_position(self.model.position_x, self.model.position_y, self.model.name, self.model.mood)
        elif sys.argv[0] == "robot_controller.py" and sys.argv[1] == "e":
            self.move_E()
            self.view.draw_position(self.model.position_x, self.model.position_y, self.model.name, self.model.mood)
        elif sys.argv[0] == "robot_controller.py" and sys.argv[1] == "w":
            self.move_W()
            self.view.draw_position(self.model.position_x, self.model.position_y, self.model.name, self.model.mood)
        elif sys.argv[0] == "robot_controller.py" and sys.argv[1] == "m":
            self.memorize()
            #self.view.draw_position(self.model.position_x, self.model.position_y, self.model.name, self.model.mood)
        elif sys.argv[0] == "robot_controller.py" and sys.argv[1] == "l":
            self.list()

    def printUsage(self):
        start_screen = open('usage.txt', "r")
        for line in start_screen:
            print(line.rstrip())
        start_screen.close()

    def move_N(self):
        self.N = int(input("How far should I run in North direction? "))
        return self.model.m_N(self.N)

    def move_S(self):
        self.S = int(input("How far should I run in South direction? "))
        return self.model.m_S(self.S)

    def move_E(self):
        self.E = int(input("How far should I run in East direction? "))
        return self.model.m_E(self.E)

    def move_W(self):
        self.W = int(input("How far should I run in West direction? "))
        return self.model.m_W(self.W)

    def memorize(self):
        self.mem = str(input("What do you want me to remember? "))
        return self.model.remember(self.mem)

    def list(self):
        return self.model.memory_list()

robot = Control()
robot.flow()
