# create a function that takes a list and returns a new list that is reversed

class List():

    rev= []

    def reverse(self, lista):
        for i in range(len(lista)-1, -1, -1):
            self.rev.append(lista[i])
        return self.rev

lista = List()

print(lista.reverse([1, 2, 3]))
