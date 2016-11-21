# Create a "robot" class that manifests a robots's memory
# make sure that you implement the following things:
#  - the robot can remember new things (simple string)
#  - the robot can recall things (as strings)
#  - the robot has a name
#  - the robot has list of possible mood
#  - the robot has a position property
#  - the robot can move by calling a method that sets its position
import random

class Model():

    name_list = ['Bob', 'Joe', 'Sam', 'Elly', 'Tom']
    name = name_list[random.randint(0, len(name_list)-1)]

    mood_list = ['happy', 'sad', 'busy', 'awesome']
    mood = mood_list[random.randint(0,len(mood_list)-1)]

    status_list = open('status.txt', 'r')
    status = status_list.readlines()
    status_list.close()
    position_x = int(status[0])
    position_y = int(status[1])

    def m_N(self, N):
        self.position_y -= N
        self.change_pos()
        return self.position_y

    def m_S(self, S):
        self.position_y += S
        self.change_pos()
        return self.position_y

    def m_E(self, E):
        self.position_x += E
        self.change_pos()
        return self.position_x

    def m_W(self, W):
        self.position_x -= W
        self.change_pos()
        return self.position_x

    def change_pos(self):
        status_list = open('status.txt', 'r')
        status = status_list.readlines()
        status[0] =str(self.position_x)+"\n"
        status[1] =str(self.position_y)
        status_list.close()
        status_list1 = open('status.txt', 'w')
        status_list1.writelines(status)

    def remember(self, mem):
        memories = open('memory.txt', 'a')
        memories.writelines(mem+"\n")
        memories.close()

    def memory_list(self):
        memories = open('memory.txt', 'r')
        memory = memories.readlines()
        for line in memory:
            print(line)
        memories.close()
