import elevator_model
import elevator_view
import sys

class Controller():

    def __init__(self):
        self.model = elevator_model.Model()
        self.view = elevator_view.View()

    def flow(self):
        if sys.argv[0] == "elevator_controller.py" and len(sys.argv)<2:
            self.start_screen()
            self.view.drawing(self.model.levels, self.model.position, self.model.people)
        elif (sys.argv[0] == "elevator_controller.py") and (sys.argv[1] == "-m"):
            self.move()
            self.view.drawing(self.model.levels, self.model.position, self.model.people)
        elif sys.argv[0] == "elevator_controller.py" and sys.argv[1] == "-i":
            self.get_in()
            self.view.drawing(self.model.levels, self.model.position, self.model.people)
        elif sys.argv[0] == "elevator_controller.py" and sys.argv[1] == "-o":
            self.get_out()
            self.view.drawing(self.model.levels, self.model.position, self.model.people)
        elif sys.argv[0] == "elevator_controller.py" and (sys.argv[1] != "-m" or "-i" or "-o") or len(sys.argv)>2:
            print("Unsupported argument")

    def start_screen(self):
        instruct = open ('usage.txt', 'r')
        for line in instruct:
            print(line.rstrip())
        instruct.close()

    def get_in(self):
        self.person_in = int(input("How many person would get on? :"))
        return self.model.people_in(self.person_in)

    def move(self):
        self.to_floor = int(input("To which floor would you move? :"))
        return self.model.move_to(self.to_floor)

    def get_out(self):
        self.person_out = int(input("How many person would get off? :"))
        return self.model.people_out(self.person_out)

elevator = Controller()
elevator.flow()
