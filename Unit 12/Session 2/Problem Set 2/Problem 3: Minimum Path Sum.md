# Problem 3: Minimum Path Sum

Given a `m x n` `grid` filled with non-negative numbers, return the sum of the path from the top left cell to bottom right cell which minimizes the sum of all numbers along its path.

You can only move either down or right at any point in time.

```python
def min_path_sum(grid):
    pass
```

Example Usage:

*Example 1:*
![Example 1 Grid With Minimum Sum Path Highlighted](./minimum_path_sum_ex1.jpg)

```python
grid_1 = [[1,3,1],[1,5,1],[4,2,1]]
grid_2 = [[1,2,3],[4,5,6]]

print(min_path_sum(grid_1))
print(min_path_sum(grid_2))
```

Example Output:

```markdown
7
Example 1 Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

12
```
