# Problem 2:  Surprise Me

Given the head of a singly linked list of books in a library `catalogue`, suggest a random book to a customer by returning a random node's value from the linked list. Each node must have the same probability of being chosen.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

```python
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

def get_random(catalogue):
    pass
```

Example Usage:

```python
catalogue = Node(('Homegoing', 'Yaa Gyasi'), 
                Node(('Pachinko', 'Min Jin Lee'),
                         Node(('The Night Watchman', 'Louise Erdrich'))))

print(get_random(catalogue))
```

Example Output:

```markdown
('Homegoing', 'Yaa Gyasi')
Explanation: It should be equally likely that ('Pachinko', 'Min Jin Lee') or
('The Night Watchman', 'Louise Erdrich') is returned
```

<details>
  <summary><strong>💡 Hint: Random Library</strong></summary>

You may find it helpful to import Python's [random library](https://docs.python.org/3/library/random.html). Use your skills reading documentation and doing independent research to decide which methods would be most helpful.

</details>
