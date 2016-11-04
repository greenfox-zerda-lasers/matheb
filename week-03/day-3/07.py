# create a function that takes a list and returns a new list with all the elements doubled

class List():

    dob = []

    def double(self, lista):
        for i in range(len(lista)):
            self.dob.append(lista[i]*2)
        return self.dob

lista = List()

print(lista.double([1, 2, 3]))
