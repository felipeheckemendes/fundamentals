class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        if self == None:
            return 'None'
        string = str(self.value) + ' -| '
        return string

class Stack:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def push(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        if self.tail == None:
            self.tail = self.head

    def top(self):
        return self.head.value

    def pop(self):
        if self.head == None:
            print("Error, empty stack")
            return
        popped = self.head
        self.head = self.head.next
        return popped.value
    
    def is_empty(self):
        if self.head == self.tail == None:
            return True
        else:
            return False
    
    def __str__(self):
        string = 'top'
        current_node = self.head
        while current_node != None:
            string += ' -> ' + str(current_node.value)
            current_node = current_node.next
        string += ' -> bottom'
        return string


# Testing
mylist = Stack()
mylist.push(1)
mylist.push(2)
print("Stack initialized:\n", mylist)
print("Top:", mylist.top())
print("Pop:", mylist.pop())
print("After popping stack:\n", mylist)
print("Is empty:", mylist.is_empty())
print("Pop:", mylist.pop())
print("After poppint all:\n", mylist)