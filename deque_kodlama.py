'''
Deque

addRight()
addLeft()

removeRight()
removeLeft()

isEmpty()
size()
'''

class Deque():
    def __init__(self):
        self.elements = []

    def isEmpty(self):
        return self.elements == []
    
    def addLeft(self, element):
        self.elements.insert(0, element)

    def addRight(self, element):
        self.elements.append(element)

    def removeLeft(self):
        return self.elements.pop(0)
    
    def removeRight(self):
        return self.elements.pop()
    
    def size(self):
        return len(self.elements)
    
myDeque = Deque()
myDeque.addRight(10) # append 10
myDeque.addRight(20) # append 20
myDeque.addLeft(30) # append 30
myDeque.addLeft(40) # append 40
myDeque.addRight(50) # append 50
myDeque.size() # 5
myDeque.removeLeft() # remove 40
myDeque.removeLeft() # remove 30
myDeque.removeRight() # remove 50
myDeque.size() # 2