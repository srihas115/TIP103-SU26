# Problem 4: Book Display

You want to display popular new books the library has just received in a fun way to visitors.

Given two integers `m` and `n` which represent dimensions of a matrix and the head of a linked list `new_reads` where each node represents a book, generate a `m x n` matrix that contains the values of each book in `new_reads` presented in sprial order (clockwise), starting from the top-left of the matrix. If there are remaining empty spaces, fill them with `None`. 

Return the generated matrix. 

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

def spiralize_books(m, n, new_reads):
	pass
```

Example Usage:

*Example 1*
![new_reads1 shown as a spiral matrix](https://courses.codepath.org/course_images/tip103/unit6_session2/matrix_ex1.png)

*Example 2*
![new_reads2 shown as a spiral matrix](https://courses.codepath.org/course_images/tip103/unit6_session2/matrix_ex2.png)

```python
new_reads1 = Node('Book 1', Node('Book 2', Node('Book 3', Node('Book 4', Node('Book 5', Node('Book 6', 
Node('Book 7', Node('Book 8', Node('Book 9', Node('Book 10', Node('Book 11', Node('Book 12', Node('Book 13')))))))))))))
new_reads2 = Node('Book 1', Node('Book 2', Node('Book 3')))

print(spiralize_books(3, 5, new_reads1))
print(spiralize_books(1, 4, new_reads2))
```

Example Output:

```markdown
[
    ['Book 1', 'Book 2', 'Book 3', 'Book 4', 'Book 5'],
    ['Book 12', 'Book 13', None, None, 'Book 6'],
    ['Book 11', 'Book 10', 'Book 9', 'Book 8', 'Book 7']
]

[['Book 1', 'Book 2', 'Book 3', None]]
```
