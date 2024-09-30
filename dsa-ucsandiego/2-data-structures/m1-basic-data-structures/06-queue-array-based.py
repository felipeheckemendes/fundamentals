class Queue:
    def __init__(self, size=5):
        self.size = size
        self.arr = [None] * size
        self.front_index = 0
        self.back_index = 0

    def enqueue(self, value):
        if self.back_index + 1 == self.front_index or (self.back_index == self.size-1 and self.front_index == 0):
            return "ERROR: not possible to enqueue " + str(value) + ', queue is full.'
        self.arr[self.back_index] = value
        if self.back_index == self.size - 1:
            self.back_index = 0
        else:
            self.back_index += 1
        return "Enqueued: " + str(value)
    
    def top_front(self):
        return self.arr[self.front_index]

    def dequeue(self):
        if self.front_index == self.back_index:
            return "ERROR: empty queue"
        popped = self.arr[self.front_index]
        self.arr[self.front_index] = None
        self.front_index += 1
        return popped

    def __str__(self):
        return str(self.arr)
    

queue = Queue()
print(queue.enqueue(1))
print(queue.enqueue(2))
print(queue.enqueue(3))
print(queue.enqueue(4))
print(queue)
print("Enqueued two elements:", queue)
print("Top:", queue.top_front())
print("Dequeued:", queue.dequeue())
print("Dequeued:", queue.dequeue())
print(queue.enqueue(5))
print(queue.enqueue(6))
print(queue.enqueue(7))
print("Dequeued all elements:", queue)