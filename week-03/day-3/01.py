# Create a `Circle` class that takes it's radius as cinstructor parameter
# It should have a `get_circumference` method that returns it's circumference
# It should have a `get_area` method that returns it's area

class Circle():
    def __init__(self, radius):
        self.radius = radius

    def get_circumference(self):
        self.circumference = self.radius*2*3.14
        circumference = self.circumference
        print (circumference)

    def get_area(self):
        return (self.radius ** 2) * 3.14
        #area = self.area
        #print(area)

first = Circle(1)

first.get_circumference()
first.get_area()
