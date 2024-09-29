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

class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def push_front(self, value):
        new_node = Node(value)
        if self.head != None:
            self.head.previous = new_node
        new_node.next = self.head
        self.head = new_node
        if self.tail == None:
            self.tail = self.head

    def push_back(self, value):
        new_node = Node(value)
        if self.tail != None:
            self.tail.next = new_node
        new_node.previous = self.tail
        self.tail = new_node
        if self.head == None:
            self.head = self.tail

    def top_front(self):
        return self.head.value

    def pop_front(self):
        if self.head == None:
            print("Error, empty list")
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head.next.previous = None
            self.head = self.head.next
    
    
    def top_back(self):
        return self.tail.value

    def pop_back(self):
        if self.tail == None:
            print("Error, empty list")
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail.previous.next = None
            self.tail = self.tail.previous


    def find_key(self, value):
        current_node = self.head
        while current_node != None and current_node.value != value:
            current_node = current_node.next
        return current_node
    
    def erase_key(self, value):
        if self.head == None:
            print("Error, empty list")
            return
        if self.head == self.tail and self.head.value == value:
            self.head = self.tail = None
            return
        
        previous_node = self.head
        while previous_node.next != None and previous_node.next.value != value:
             previous_node = previous_node.next
        previous_node.next = previous_node.next.next
        previous_node.next.previous = previous_node
    
    def is_empty(self):
        if self.head == self.tail == None:
            return True
        else:
            return False
    
    def __str__(self):
        string1 = 'head-> '
        current_node = self.head
        while current_node != None:
            string1 += str(current_node.value) + " -> "
            current_node = current_node.next
        string1 += 'null'

        string2 = 'tail-> '
        current_node = self.tail
        while current_node != None:
            string2 += str(current_node.value) + " -> "
            current_node = current_node.previous
        string2 += 'null'
        return string1 + '\n' + string2


mylist = LinkedList()
mylist.push_front(1)
mylist.push_front(2)
mylist.push_front(3)
mylist.push_front(4)
mylist.push_front(5)
print("List initialized:")
print(mylist)
print("Top front:")
print(mylist.top_front())
mylist.pop_front()
print("Pop front:")
print(mylist)
mylist.push_back(0)
print("Push back 0:")
print(mylist)
print("Top back:")
print(mylist.top_back())
mylist.pop_back()
print("Pop back:")
print(mylist)
print("Find key 3:", mylist.find_key(3))
print("Find key 9:", mylist.find_key(9))
mylist.erase_key(2)
print("Erase key 2:")
print(mylist)
print(mylist.is_empty())
print("Pop back one element left:")
mylist.pop_back()
mylist.pop_back()
print(mylist)
mylist.pop_back()
print("Pop back all:")
print(mylist)
mylist.push_back(1)
mylist.push_back(2)
print("List reinitialized: ")
print(mylist)
mylist.pop_front()
mylist.pop_front()
print("Pop front all:")
print(mylist)