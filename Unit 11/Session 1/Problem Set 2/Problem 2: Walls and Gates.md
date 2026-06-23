# Problem 2: Walls and Gates

You have an `m x n` grid `castle` where each square represents a section of the castle. Each square has one of three possible values:
- `-1`: a wall or an obstacle 
- `0`: a gate
- `float('inf')` (infinity): an empty room 

Return the `castle` matrix modified in-place such that each empty rooms value is its distance to its nearest gate. If it is impossible to reach a gate, it should have value infinity.

```python
def walls_and_gates(castle):
    pass
```

Example Usage:

!['castle' example before and after shortest paths found](../../Unit%20Assets/walls_and_gates.jpg)

```python
castle = [
    [float('inf'), -1, 0, float('inf')],            # Row 0
    [float('inf'), float('inf'), float('inf'), -1], # Row 1
    [float('inf'), -1, float('inf'), -1],           # Row 2
    [0, -1, float('inf'), float('inf')]             # Row 3
    ]

print(walls_and_gates(castle))
```

Example Output:

```markdown
[
    [3, -1, 0, 1],
    [2, 2, 1, -1],
    [1, -1, 2, -1],
    [0, -1, 3, 4]
]
```

<details>
  <summary><strong>💡 Hint: Repeating Traversal</strong></summary>

To solve this function, you may need to repeatedly traverse the matrix using BFS or DFS starting from all or multiple cells in the matrix.

</details>
