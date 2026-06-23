# Problem 6: Careful Reverse

Given the `head` of a singly linked list and an integer `k`, reverse the first k elements of the linked list. Return the new head of the linked list. If `k` is larger than the length of the list, reverse the entire list.

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
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next
        
def reverse_first_k(head, k):
	pass
```

Example Usage:

```python
head = Node("apple", Node("cherry", Node("orange", Node("peach", Node("pear")))))

print_linked_list(reverse_first_k(head, 3))
```

Example Output:

```markdown
orange -> cherry -> apple -> peach -> pear
```
