#My first todo Application
#Boglarka Mathe, 16/11/2016
import sys
import os

class ToDoApp():

    def __init__(self):
        self.line_number = 0

    def lines(self):
        with open('todos.txt') as todos:
            self.line_number = len(todos.readlines())
        return self.line_number

    def flow(self):
        if sys.argv[0] == "todo.py" and len(sys.argv)<2:
            self.printUsage()
        elif (sys.argv[0] == "todo.py") and (sys.argv[1] == "-l"):
            self.printList()
        elif sys.argv[0] == "todo.py" and sys.argv[1] == "-a":
            if len(sys.argv) < 3:
                print("Unable to add: No task is provided")
            else:
                self.addToList()
        elif sys.argv[0] == "todo.py" and sys.argv[1] == "-r":
            self.test_param_r()
        elif sys.argv[0] == "todo.py" and sys.argv[1] == "-c" and len(sys.argv) <= 3:
            self.test_param_c()
        elif sys.argv[0] == "todo.py" and sys.argv[1] != "-l" or "-a" or "-r" or "-c":
            print("Unsupported argument")

    def main(self):
        #print(sys.argv)
        if not os.path.exists('todos.txt'):
            first = open('todos.txt', 'w')
            second = open('completed.txt', 'w')
            first.close()
            second.close()
            self.flow()
        else:
            self.flow()

    def test_param_r(self):
        try:
            if len(sys.argv) < 3:
                print("Unable to add: No task is provided")
            elif int(sys.argv[2]) <= self.lines():
                self.remove()
            elif int(sys.argv[2]) > self.lines():
                print("Unable to remove: Index is out of bound")
        except ValueError:#type(sys.argv[2]) == str:
            print("Unable to remove: Index is not a number")

    def test_param_c(self):
        try:
            if len(sys.argv) < 3:
                print("Unable to add: No task is provided")
            elif int(sys.argv[2]) <= self.lines():
                self.complete()
            elif int(sys.argv[2]) > self.lines():
                print("Unable to remove: Index is out of bound")
        except ValueError:#type(sys.argv[2]) == str:
            print("Unable to remove: Index is not a number")


    def printUsage(self):
        start_screen = open('usage.txt', "r")
        for line in start_screen:
            print(line.rstrip())
        start_screen.close()

    def addToList(self):
        todo_list = open('todos.txt', 'a')
        completed_list = open('completed.txt', 'a')
        todo_list.writelines(sys.argv[2]+ "\n")
        completed_list.writelines("todo\n")
        todo_list.close()
        completed_list.close()

    def remove(self):
        todo_list = open('todos.txt', 'r')
        lista = todo_list.readlines()
        todo_list.close()
        todo_list1 = open('todos.txt', 'w')
        for i in range(0, len(lista)):
            if i != (int(sys.argv[2])-1):
                todo_list1.writelines(lista[i])
        todo_list1.close()
        completed_list = open('completed.txt', 'r')
        completed = completed_list.readlines()
        completed.pop(int(sys.argv[2])-1)
        completed_list.close()
        completed_list1 = open('completed.txt', 'w')
        completed_list1.writelines(completed)

    def printList(self):
        todo_list = open('todos.txt', 'r')
        lista = todo_list.readlines()
        if len(lista) == 0:
            print("There's nothing to do")
        complete_list = open('completed.txt', 'r')
        completed = complete_list.readlines()
        for i in range(len(lista)):
            if completed[i] != "ready\n":
                print(i+1, " - [ ] " , lista[i])
            else:
                print(i+1, " - [x] " , lista[i])
        todo_list.close()
        complete_list.close()

    def complete(self):
        #self.start_status()
        completed_list = open('completed.txt', 'r')
        completed = completed_list.readlines()
        completed[int(sys.argv[2])-1] = "ready\n"
        completed_list.close()
        completed_list1 = open('completed.txt', 'w')
        completed_list1.writelines(completed)


todo = ToDoApp()
todo.main()
