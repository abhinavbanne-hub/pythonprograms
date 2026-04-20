class Stack:
    def __init__(self):
        self.items = []

    # Push element onto stack
    def push(self, item):
        self.items.append(item)

    # Safe pop method
    def safe_pop(self):
        if len(self.items) == 0:
            print("Stack is empty, nothing to pop.")
            return None
        else:
            return self.items.pop()

    # Display stack
    def display(self):
        print("Stack:", self.items)


# Example usage
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

stack.display()

print("Popped:", stack.safe_pop())
print("Popped:", stack.safe_pop())
print("Popped:", stack.safe_pop())

# Trying to pop from empty stack
print("Popped:", stack.safe_pop())