# Problem 6: Reverse Nodes in K-Group

Given the head of a linked list, reverse the nodes of the list `k` at a time, and return the head of the modified list.

`k` is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of `k` then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

```python
class Node():
    def __init__(self, val=0, next=None):
        self.value = val
        self.next = next

def reverse_k_group(head, k):
    pass
```

Example Usage 1:

![Example 1 List Before and After Reversal](../../Unit%20Assets/reverse_nodes_k_group_ex1.jpg)

```python
list_1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))

# Using print_linked_list() function included at top of page
print_linked_list(reverse_k_group(list_1, 2))
```

Example Output 1: 

```markdown
2 -> 1 -> 4 -> 3 -> 5
```

Example Usage 2:

![Example 2 List Before and After Reversal](../../Unit%20Assets/reverse_nodes_k_group_ex2.jpg)

```python
list_2 = Node(1, Node(2, Node(3, Node(4, Node(5)))))

# Using print_linked_list() function included at top of page
print_linked_list(reverse_k_group(list_2, 3))
```

Example Output 2: 

```markdown
3 -> 2 -> 1 -> 4 -> 5
```

<details>
  <summary><strong>💡 Hint: Leetcode Hard</strong></summary>

For an extra challenge on the last problem of the course, this is a Leetcode Hard problem! This is not in scope for the assessments, but meant as an extra fun challenge to continue to push your problem solving skills!

</details>
