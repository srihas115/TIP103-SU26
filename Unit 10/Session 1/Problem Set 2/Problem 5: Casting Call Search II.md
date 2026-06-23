# Problem 5: Casting Call Search II

You are a casting agent for a major Hollywood production and the director has a certain celebrity in mind for the lead role. You have an adjacency matrix `celebs` where `celebs[i][j] = 1` means that celebrity `i` has a connection with celebrity `j`, and `celebs[i][j] = 0` means they don't. Connections are directed meaning that `celebs[i][j] = 1` does not automatically mean `celebs[j][i] = 1`. 

Given a celebrity you know `start_celeb` and the celebrity the director wants to hire `target_celeb`, use **Depth First Search** to return `True` if you can find a path of connections from `start_celeb` to `target_celeb`. Otherwise, return `False`. 

```python
def have_connection(celebs, start_celeb, target_celeb):
    pass
```

Example Usage:

!['celebs' graph diagram](../../Unit%20Assets/casting_call_search.png)

```python
celebs = [
            [0, 1, 0, 0, 0, 0, 0, 0], # Celeb 0
            [0, 1, 1, 0, 0, 0, 0, 0], # Celeb 1
            [0, 0, 0, 1, 0, 1, 0, 0], # Celeb 2
            [0, 0, 0, 0, 1, 0, 1, 0], # Celeb 3
            [0, 0, 0, 1, 0, 0, 0, 1], # Celeb 4
            [0, 1, 0, 0, 0, 0, 0, 0], # Celeb 5
            [0, 0, 0, 1, 0, 0, 0, 1], # Celeb 6
            [0, 0, 0, 0, 1, 0, 1, 0]  # Celeb 7
            ]

print(have_connection(celebs, 0, 6))
print(have_connection(celebs, 3, 5))
```

Example Output:

```markdown
True
False
```

<details>
  <summary><strong>💡 Hint: Depth First Search</strong></summary>

This problem requires you to perform a depth first search traversal of a graph. If you need a primer on how to perform DFS on a graph, check out the unit cheatsheet.

</details>
