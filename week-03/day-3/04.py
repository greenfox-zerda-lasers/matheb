# Create a student Class
# that has a method `add_grade`, that takes a grade from 1 to 5
# an other method `get_average`, that returns the average of the
# grades

class Student():

    grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average(self):
        count = 0
        for i in range(len(self.grades)):
            count = count + self.grades[i]
        return(count/(len(self.grades)))

student = Student()

student.add_grade(3)
student.add_grade(3)
student.add_grade(2)
student.add_grade(5)
student.add_grade(1)
student.add_grade(5)
print(student.get_average())
