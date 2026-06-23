# Problem 3: Properly Reshelve

A well-intentioned reader has improperly put back a book on the shelf. Given the head of a linked list `shelf` where each node represents a book on the shelf, and a value `k` return the head of the linked list after swapping the values of the `kth` node from the beginning and the `kth` node from the end. Assume the list is 1-indexed. Assume `1 <= k < n` where `n` is the length of `shelf`. 

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

def swap_books(shelf, k):
	pass
```

Example Usage:

![Linked list shelf before after swapping values](https://courses.codepath.org/course_images/tip103/unit6_session2/properly_reshelve_ex.jpg)

```python
shelf = Node('Book 1', Node('Book 2', Node('Book 3', Node('Book 4', Node('Book 5')))))

print_linked_list(swap_books(shelf, 2))
```

Example Output:

```markdown
Book 1 -> Book 4 -> Book 3 -> Book 2 -> Book 5
```
