# Design Stack class with is_empty, push, pop, peek, size methods

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            return "Stack is empty"

    # Return topmost item in stack without removing it   
    def peek(self):
        if len(self.items) > 0:
            return self.items[-1]
        else:
            return "Stack is empty"
        
    def size(self):
        return len(self.items)
    

# Instantiate Stack class
stack = Stack()
# Push items onto stack
stack.push(1)
stack.push(2)
stack.push(3)
# Check if stack is empty
print(stack.is_empty()) # False
# Pop item from stack
print(stack.pop()) # 3
# Peek at topmost item in stack
print(stack.peek()) # 2
# Check size of stack
print(stack.size()) # 2