class Node:
    def __init__(self, value, next=None, previous=None):
        self.value = value
        self.next = next
        self.previous = previous

    def __str__(self):
        if self == None:
            return 'None'
        string = str(self.value) + ' -> '
        return string

class Queue:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def enqueue(self, value):
        new_node = Node(value)
        if self.head != None:
            self.head.previous = new_node
        new_node.next = self.head
        self.head = new_node
        if self.tail == None:
            self.tail = self.head

    def top_front(self):
        return self.head.value   
    
    def top_back(self):
        return self.tail.value

    def dequeue(self):
        if self.tail == None:
            print("Error, empty list")
            return
        if self.head == self.tail:
            dequeued = self.tail
            self.head = self.tail = None
        else:
            dequeued = self.tail
            self.tail.previous.next = None
            self.tail = self.tail.previous
        return dequeued
    
    def is_empty(self):
        if self.head == self.tail == None:
            return True
        else:
            return False
    
    def __str__(self):
        string1 = 'In'
        current_node = self.head
        while current_node != None:
            string1 += ' -> ' + str(current_node.value)
            current_node = current_node.next
        string1 += ' -> Out'
        return string1

mylist = Queue()
mylist.enqueue(1)
mylist.enqueue(2)
mylist.enqueue(3)
print("Queue initialized:")
print(mylist)
print("Top back:")
print(mylist.top_back())
print("Dequeue:", mylist.dequeue())
print("Queue after dequeuing:")
print(mylist)
print("Is queue empty: ", mylist.is_empty())
print("Dequeue all elements:")
mylist.dequeue()
mylist.dequeue()
print(mylist)