# Write a Person class that have a name and a birth_date property
# It should raise an error of the birthdate is less than 0 or more than 2016

class Person():

    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date

    def check_birth_date(self):
        if self.birth_date <= 0 or self.birth_date >2016:
            raise PermissionError("I can't believe you. Please add the correct year!")
        if type(self.birth_date) != int:
            raise ValueError("Are you sure, you gave a year?")

person = Person('Jonny Joe', 0)
print(person.check_birth_date())
