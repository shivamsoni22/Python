# Implement a queue using two stacks.
class QueueUsingStacks:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, item):
        self.s1.append(item)

    def dequeue(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop() if self.s2 else None

q = QueueUsingStacks()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  # Output: 1
