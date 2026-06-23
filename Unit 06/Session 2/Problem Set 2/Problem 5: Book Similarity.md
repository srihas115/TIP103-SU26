# Problem 5: Book Similarity

The library sequences books by topic so that it's easy to find related books. Given the head of a linked list `all_books` where each node contains a unique integer values representing a different book in the library, and an integer array `subset` that contains a subset of the values in `all_books`, return the number of *similar* book components in `subset`. Two books are similar if they appear consecutively in the linked list. 

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

def similar_book_count(all_books, subset):
	pass
```

Example Usage:

```python
all_books1 = Node(0, Node(1, Node(2, Node(3))))
subset1 = [0, 1, 3]

all_books2 = Node(0, Node(1, Node(2, Node(3, Node(4)))))
subset2 = [0, 3, 1, 4]

print(similar_book_count(all_books1, subset1))
print(similar_book_count(all_books2, subset2))
```

Example Output:

```markdown
2
Example 1 Explanation: 0 and 1 are similar, so [0, 1] and [3] are the two similar components.

2
Example 2 Explanation: 0 and 1 are similar, 3 and 4 are similar, 
so [0, 1] and and [3, 4] are the similar components.
```
