class Stack:
    def __init__(self, size=15):
        self.arr = [None] * size
        self.top_index = 0

    def push(self, value):
        self.arr[self.top_index] = value
        self.top_index += 1
    
    def top(self):
        if self.top_index == 0:
            return None
        return self.arr[self.top_index-1]

    def pop(self):
        if self.top_index == 0:
            return "ERROR: empty stack"
        popped = self.arr[self.top_index-1]
        self.arr[self.top_index-1] = None
        self.top_index -=1
        return popped

    def __str__(self):
        output = 'top'
        for index in range(self.top_index):
            output += ' -> ' + str(self.arr[index])
        output += ' -> bottom'
        return output
    

stack = Stack()
stack.push(4)
stack.push(5)
print("Pushed two elements:", stack)
print("Top:", stack.top())
print("Popped:", stack.pop())
print("Popped:", stack.pop())
print("Popped:", stack.pop())
print("Popped all elements:", stack)