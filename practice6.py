
class ArrayStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def size(self):
        return self.top + 1

    def push(self, x):
        if self.is_full():
            print("STACK OVERFLOW")
            return False

        self.top = self.top + 1
        self.data[self.top] = x
        return True

    def pop(self):
        if self.is_empty():
            print("STACK UNDERFLOW")
            return None

        x = self.data[self.top]
        self.data[self.top] = None
        self.top = self.top - 1
        return x

    def peek(self):
        if self.is_empty():
            print("STACK IS EMPTY")
            return None

        return self.data[self.top]

    def display(self):
        if self.is_empty():
            print("EMPTY")
            return

        i = self.top
        while i >= 0:
            print(self.data[i])
            i = i - 1


# Create a stack with capacity 5
s = ArrayStack(5)

# PUSH
s.push(11)
s.push(25)
s.push(7)

print("Array:", s.data)
print("Top index:", s.top)
print("Size:", s.size())

# PEEK
print("Top element:", s.peek())

# DISPLAY
print("Stack from top to bottom:")
s.display()

# POP
print("Removed element:", s.pop())

print("Array after POP:", s.data)
print("New top:", s.top)
print("New size:", s.size())
