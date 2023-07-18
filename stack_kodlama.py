'''
Stack()

push(item)
pop()
showLast()
size()
isEmpty()
'''

class Stack():
    def __init__(self):
        self.elements = []

    def isEmpty(self):
        return self.elements == []
    
    def push(self, element):
        self.elements.append(element)

    def pop(self):
        return self.elements.pop()

    def showLast(self):
        return self.elements[len(self.elements) - 1]
    
    def size(self):
        return len(self.elements)
    
    def __str__(self):
        return self.elements
    
myStack = Stack()
myStack.isEmpty() # True
myStack.push(10) # append 10
myStack.push(20) # append 20
myStack.push(40) # append 40
myStack.showLast() # 40
myStack.push("a") # append "a"
myStack.showLast() # "a"
myStack.pop() # remove "a"
myStack.showLast() # 40
myStack.__str__() # [10, 20, 40]
myStack.pop() # remove 40
myStack.pop() # remove 20
myStack.pop() #remove 10
myStack.__str__() # []
myStack.isEmpty() # True