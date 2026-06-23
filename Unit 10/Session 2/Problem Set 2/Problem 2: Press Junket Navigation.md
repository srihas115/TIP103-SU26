# Problem 2: Press Junket Navigation

You've been invited to interview some of your favorite celebrities. Each group is stationed in a different room in the venue numbered `0` to `n-1`. To get to your assigned interview station, you need to navigate from the *entrance* which is room number `0` to your assigned room `target`.

Given an adjacency list `venue_map` where `venue_map[i]` indicates that there is a hallway between room `i` and each room in `venue_map[i]`, return a list representing the path from the entrance to your `target` room. If there are multiple paths, you may return any valid path.

```python
def find_path(venue_map, target):
    pass
```

Example Usage:

!['venue_map' graph diagram](../../Unit%20Assets/venue_map.png)

```python
venue_map = [
    [1, 2],
    [0, 3],
    [0, 4],
    [1, 5],
    [2],
    [3]
]

print(find_path(venue_map, 5))
print(find_path(venue_map, 2))
```

Example Output:

```markdown
[0, 1, 3, 5]
[0, 2]
```

<details>
  <summary><strong>💡 Hint: Path Reconstruction</strong></summary>

This problem requires you to reconstruct the path taken by either BFS or DFS. To reconstruct a path from BFS/DFS, we can keep track of each node's parent (the node from which it was discovered) during the search. After reaching the target, backtrack from the target node to the start using the parent pointers to trace the path.

</details>
