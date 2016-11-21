import building
import os
import time

class View():

    building = building.building

    def drawing(self, levels, position, people):

        #os.system('cls' if os.name == 'nt' else 'clear')
        print ("Floor: " + str(position) + "\n" + "People: " + str(people))

        print(self.building['top'])

        if position == 0:
            if people == 0:
                for i in range(levels):
                    print(self.building['no_lift'])
                print(self.building['ground_empty'])
            elif people > 0:
                for i in range(levels):
                    print(self.building['no_lift'])
                print(self.building['ground_full'])
            print(self.building['bottom'])
        elif position > 0:
            if people == 0:
                for i in range(levels, 0, -1):
                    if i == position:
                        print(self.building['nth_empty'])
                    else:
                        print(self.building['no_lift'])
            if people > 0:
                for i in range(levels, 0, -1):
                    if i == position:
                        print(self.building['nth_full'])
                    else:
                        print(self.building['no_lift'])
            print(self.building['ground_no_lift'])
            print(self.building['bottom'])
