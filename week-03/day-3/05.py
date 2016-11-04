# Create a `Stack` class that stores elements
# It should have a `size` method that returns number of elements it has
# It should have a `push` method that adds an element to the stack
# It should have a `pop` method that returns the last element form the stack and also deletes it from it

# please don`t use the built in methods

class Stack():

    elements = [1, 2, 3, 4]

    def size(self):
        return len(self.elements)

    def push(self, new):
        self.elements.append(new)
        return self.elements

    def pop(self):
        #return self.elements[len(self.elements)-1]
        #print("hello")
        return self.elements.pop(len(self.elements)-1)
        #return self.elements[len(self.elements)]


stack = Stack()

print(stack.size())
print(stack.push(5))
print(stack.push(6))
print(stack.pop())
print(stack.size())
