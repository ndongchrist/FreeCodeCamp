
class Node:#Creatimg a class node containing the data
    
    def __init__(self, data):
        self.data = data
    def __repr__(self):
        return "Node data: %s" % self.data    

class Queue:#using a list to implement the queue
    
    def __init__(self):
        self.data = None
        self.size = []
        self.back = -1
        self.front = 5

    def enqueue(self, data):#to add an element to the queue
        if self.back == 5:#testing if the queue is full
            return 'Queue is full'
        else:    
            new_node = Node(data)#if not add the element
            self.back += 1
            self.size.append(data)

    def isfull(self):#verify if the queue is full
        return self.back == self.front
    def isEmpty(self):#verify if queue is empty
        return self.back != self.front

    def dequeue(self):#remove an element from the queue
        if self.back == -1:
            return 'Empty Queue'
        else:
            self.size.pop(self.back)
            self.back += 1    

    def length(self):#returns the number of elements present in the queue
        return self.back  

    def display(self):#just display's the queue
        return print(self.size)         


