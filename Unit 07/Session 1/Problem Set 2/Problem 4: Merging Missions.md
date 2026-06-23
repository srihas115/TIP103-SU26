# Problem 4: Merging Missions

Atlanteans are planning multiple missions to explore the deep ocean, and each mission has a priority level represented as a node in a linked list. You are given the heads of two sorted linked lists, `mission1` and `mission2`, where each node represents a mission with its priority level.

Implement a recursive function `merge_missions()` which merges these two mission lists into one sorted list, ensuring that the combined list maintains the correct order of priorities. The merged list should be made by splicing together the nodes from the first two lists.

Return the head of the merged mission linked list.

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

def merge_missions(mission1, mission2):
    pass
```

Example Usage:

```python
mission1 = Node(1, Node(2, Node(4)))
mission2 = Node(1, Node(3, Node(4)))

print_linked_list(merge_missions(mission1, mission2))
```

```markdown
1 -> 1 -> 2 -> 3 -> 4 -> 4
```
