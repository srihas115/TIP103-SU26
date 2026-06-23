# Problem 6: Copying Seating Arrangements

You are organizing the seating arrangement for a big awards ceremony and want to make a copy for your assistant. The seating arrangement is stored in a graph where each `Node` value `val` is the name of a celebrity guest at the ceremony and its array `neighbors` are all the guests sitting in seats adjacent to the celebrity. 

Given a reference to a `Node` in the original seating arrangement `seat`, make a deep copy (clone) of the seating arrangement. Return the copy of the given node. 

We have provided a function `compare_graphs()` to help with testing this function. To use this function, pass in the given node `seat` and the copy of that node your function `copy_seating()` returns. If the two graphs are clones of each other, the function will return `True`. Otherwise, the function will return `False`.

```python
class Node():
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# Function to test if two seating arrangements (graphs) are identical
def compare_graphs(node1, node2, visited=None):
    if visited is None:
        visited = set()
    
    if node1.val != node2.val:
        return False
    
    visited.add(node1)

    if len(node1.neighbors) != len(node2.neighbors):
        return False
    
    for n1, n2 in zip(node1.neighbors, node2.neighbors):
        if n1 not in visited and not compare_graphs(n1, n2, visited):
            return False

    return True

def copy_seating(seat):
    pass
```

Example Usage:

!['arrangement'](../../Unit%20Assets/copying_seating_arrangements.png)

```python
lily = Node("Lily Gladstone")
mark = Node("Mark Ruffalo")
cillian = Node("Cillian Murphy")
danielle = Node("Danielle Brooks")
lily.neighbors.extend([mark, danielle])
mark.neighbors.extend([lily, cillian])
cillian.neighbors.extend([danielle, mark])
danielle.neighbors.extend([lily, cillian])

copy = copy_seating(lily)
print(compare_graphs(lily, copy))
```

Example Output:

```markdown
True
```
