# Problem 3: Surrounded Regions

Your kingdom has been battling a neighboring kingdom. You are given an `m x n` matrix `map` containing letters `'X'` and `'O'`. Territory controlled by your kingdom is labeled with `'X'` while territory controlled by the opposing kingdom is labeled `'O'`. 

Territories (cells) in the matrix are considered connected to horizontally and vertically adjacent territories. A _region_ is formed by contiguously connected territories controlled by the same kingdom. Your kingdom can capture an `'O'` region if it is surrounded. The region is surrounded with `'X'` territories if you can connect the region with `'X'` cells and none of the region cells are on the edge of the `map`. 

A surrounded region is captured by replacing all `'O'`s with `'X'`s in the input matrix `map`. Return `map` after modifying it in-place to capture all possible `'O'` regions.

```python
def capture(map):
    pass
```

Example Input:

!['map' before and after capture](../../Unit%20Assets/surrounded_regions_ex1.jpg)

```python
map = [
    ["X","X","X","X"],
    ["X","O","O","X"],
    ["X","X","O","X"],
    ["X","O","X","X"]]

print(capture(map))
```

Example Output:

```markdown
[
    ["X","X","X","X"],
    ["X","X","X","X"],
    ["X","X","X","X"],
    ["X","O","X","X"]
    ]
Example Explanation: The bottom region cannot be captured because it is on the edge 
of the board and cannot be surrounded.
```
