# Problem 5: Remove Nth Node From End of List

Given the `head` of a linked list and an integer `n`, write a function `remove_nth_from_end()` that removes the `nth` node from the end of the list. The function should return the head of the modified list.

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

def remove_nth_from_end(head, n):
    pass
```

Example Usage:

```python
head1 = Node("apple", Node("cherry", Node("orange", Node("peach", Node("pear")))))
head2 = Node("Rainbow Trout", Node("Ray"))
head3 = Node("Rainbow Stag")

print_linked_list(remove_nth_from_end(head1, 2))
print_linked_list(remove_nth_from_end(head2, 1))
print_linked_list(remove_nth_from_end(head3, 1))
```

Example Output:

```markdown
apple -> cherry -> orange -> pear
Rainbow Trout

Example 3 Explanation: The last example returns an empty list.
```
