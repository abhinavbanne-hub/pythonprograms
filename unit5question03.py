from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    # Enqueue element
    def enqueue(self, item):
        self.items.append(item)

    # Safe dequeue method
    def safe_dequeue(self):
        if len(self.items) == 0:
            print("Queue is empty, cannot dequeue.")
            return None
        else:
            return self.items.popleft()

    # Display queue
    def display(self):
        print("Queue:", list(self.items))


# Example usage
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()

print("Dequeued:", q.safe_dequeue())
print("Dequeued:", q.safe_dequeue())
print("Dequeued:", q.safe_dequeue())

# Trying to dequeue from empty queue
print("Dequeued:", q.safe_dequeue())