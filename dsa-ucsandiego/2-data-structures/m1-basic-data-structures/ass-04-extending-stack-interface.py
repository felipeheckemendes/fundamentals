"""
4 Extending stack interface
Problem Introduction
Stack is an abstract data type supporting the operations Push() and Pop(). 
It is not difficult to implement it in a way that both these operations work in constant time.
In this problem, you goal will be to implement a stack that also supports finding the maximum value and to ensure that all operations still work in constant time.
Problem Description
Task. Implement a stack supporting the operations Push(), Pop(), and Max().
Input Format. The first line of the input contains the number 𝑞 of queries.
Each of the following 𝑞 lines specifies a query of one of the following formats: push v, pop, or max.
Constraints. 1 ≤ 𝑞 ≤ 400 000, 0 ≤ 𝑣 ≤ 10**5.
Output Format. For each max query, output (on a separate line) the maximum value of the stack.
"""

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.max = value
        self.next = next

    def __str__(self):
        if self == None:
            return 'None'
        string = str(self.value) + ' -| '
        return string

class Stack:
    def __init__(self, top=None):
        self.top = top

    def push(self, value):
        new_node = Node(value, self.top)
        if self.top != None and value > self.top.max:
            new_node.max = value
        elif self.top != None:
            new_node.max = self.top.max
        self.top = new_node

    def get_top(self):
        return self.top.value

    def get_max(self):
        return self.top.max

    def pop(self):
        if self.top == None:
            print("Error, empty stack")
            return
        popped = self.top
        self.top = self.top.next
        return popped.value
    
    def is_empty(self):
        if self.top == None:
            return True
        else:
            return False
    
    def __str__(self):
        string = 'top'
        current_node = self.top
        while current_node != None:
            string += ' -> ' + str(current_node.value)
            current_node = current_node.next
        string += ' -> bottom'
        return string

mystack = Stack()
n = int(input())
outputs = []
for i in range(n):
    query = input().split()
    if query[0] == 'push':
        value = int(query[1])
        mystack.push(value)
    elif query[0] == 'pop':
        mystack.pop()
    elif query[0] == 'max':
        outputs.append(mystack.get_max())
for output in outputs:
    print(output)
