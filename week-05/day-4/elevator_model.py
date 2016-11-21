class Model():
    levels = 12

    def __init__(self):
        status_list = open('status.txt', 'r')
        status = status_list.readlines()
        status_list.close()
        self.position = int(status[0])
        self.people = int(status[1])

    def move_to(self, to_floor):
        if to_floor >= 0 and to_floor <= self.levels:
            self.position += (to_floor - self.position)
            self.change_state()
            return int(self.position)
        else:
            print("This floor is not available")

    def people_in(self, person_in):
        if self.people + person_in >= 0 and self.people + person_in <= 8:
            self.people += person_in
            self.change_state()
            return self.people
        elif self.people + person_in > 8:
            print("You can not get in, there are too many people in the elevator")
        else:
            print("Number of peoples can't be negative")

    def people_out(self, person_out):
        if self.people-person_out >= 0 and self.people-person_out <= 8:
            self.people -= person_out
            self.change_state()
            return self.people
        elif self.people - person_out > 8:
            print("You can not get in, there are too many people in the elevator")
        else:
            print("Number of peoples can't be negative")

    def change_state(self):
        status_list = open('status.txt', 'r')
        status = status_list.readlines()
        status[0] =str(self.position)+"\n"
        status[1] =str(self.people)
        status_list.close()
        status_list1 = open('status.txt', 'w')
        status_list1.writelines(status)
