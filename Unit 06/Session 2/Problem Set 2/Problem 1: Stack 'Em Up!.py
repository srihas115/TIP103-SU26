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
