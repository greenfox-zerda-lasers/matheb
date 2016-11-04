# Create a new class called `Person` that has a first_name and a last_name (takes it in it's constructor)
# It should have a `greet` method that prints it's full name

# Create a `Student` class that is the child class of `Person`
# it should have a method to add grades
# it should have a `salute` method that prints it's full name and the average of it's grades as well

class Person():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def greet(self):
        print(self.first_name + self.last_name)

class Student(Person):

    grades = []
    count = 0
    i = 0

    #def __init__(self, first_name, last_name):
        #Person.__init__(self, first_name, last_name)
        #self.grade = grade

    def add_grades(self, grade):
        self.grades.append(grade)
        self.count = self.count + grade
        self.i = self.i + 1

    def salute(self):
        print (self.first_name + self.last_name + str(self.count/self.i))


#student = Student("Kelly ", "Sheep", 5)
#kelly = Person("Kelly ", "Sheep")
kelly = Student("Kelly ", "Sheep ")


kelly.greet()
kelly.add_grades(1)
kelly.add_grades(3)
kelly.add_grades(5)
kelly.add_grades(3)
kelly.salute()
#first.salute()

sam = Person("Sam ", "Flower")
sam.greet()
