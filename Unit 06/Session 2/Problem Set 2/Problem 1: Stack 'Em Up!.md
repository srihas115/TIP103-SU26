# Problem 1: Stack 'Em Up!

The library has a stack of returned books waiting to be shelved. Help the library to manage the stack by implementing the **class** `Stack` using a singly linked list. Recall that a stack is a Last-In-First-Out (LIFO) data structure where elements are added to the front (the head) and removed from the front (the head).

Your stack must have the following methods:
- `__init()__`: Initializes an empty stack (provided)
- `push()`: Accepts a tuple of two strings `(title, author)` and adds the element with the specified tuple to the front/top of the stack.
- `pop()`: Removes and returns the element at the front/top of the stack. If the stack is empty, returns `None`.
- `peek()`: Returns the value of the element at the front/top of the stack without removing it. If the stack is empty, returns `None`.
- `is_empty()`: Returns `True` if the stack is empty, and `False` otherwise. 

```python
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing
def print_stack(head):
    current = head.front
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

class Stack:
    def __init__(self):
        self.front = None
    
    def is_empty(self):
        pass

    def push(self, value):
        pass
    
    def pop(self):
        pass
    
    def peek(self):
        pass
    
```

Example Usage:

```python
# Create a new Stack
stack = Stack()

# Add elements to the stack
stack.push(('Educated', 'Tara Westover'))
stack.push(('Gone Girl', 'Gillian Flynn'))
stack.push(('Dune', 'Frank Herbert'))
print_stack(stack)

# View the front element
print("Peek: ", stack.peek()) 

# Remove elements from the stack
print("Pop: ", stack.pop()) 
print("Pop: ", stack.pop()) 

# Check if the stack is empty
print("Is Empty: ", stack.is_empty()) 

# Remove the last element
print("Pop: ", stack.pop()) 

# Check if the queue is empty
print("Is Empty:", stack.is_empty()) 
```

Example Output:

```markdown
('Dune', 'Frank Herbert') -> ('Gone Girl', 'Gillian Flynn') -> ('Educated', 'Tara Westover')
Peek:  ('Dune', 'Frank Herbert')
Pop:  ('Dune', 'Frank Herbert')
Pop:  ('Gone Girl', 'Gillian Flynn')
Is Empty:  False
Pop:  ('Educated', 'Tara Westover')
Is Empty: True
```
