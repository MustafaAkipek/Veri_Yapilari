'''
Queue

enqueue(item)
dequeue()
size()
isEmpty()
'''

class Queue():
    def __init__(self):
        self.elements = []

    def isEmpty(self):
        return self.elements == []
    
    def enqueue(self, element):
        self.elements.insert(0, element)

    def dequeue(self):
        return self.elements.pop()
    
    def size(self):
        return len(self.elements)
    
myQueue = Queue()
myQueue.isEmpty()
myQueue.enqueue(10) # append 10
myQueue.enqueue(20) # append 20
myQueue.enqueue(30) # append 30
myQueue.dequeue() # remove 10
myQueue.size() # 2
myQueue.dequeue() # remove 20
myQueue.dequeue() # remove 30
a = myQueue.isEmpty() # True