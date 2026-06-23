# Problem 6: Pikachu's Journey

Pikachu is navigating a maze of tall grass to reach the next Pokémon Center! The maze is laid out as an `m x n` grid, and Pikachu starts at the top-left corner (i.e., `grid[0][0]`) and must make his way to the bottom-right corner (i.e., `grid[m - 1][n - 1]`).

Pikachu can only move down or right at any point in time. Your task is to help Pikachu calculate the number of possible unique paths he can take to reach the Pokémon Center from the starting position.

Write a function `pikachu_unique_paths()` to calculate the total number of unique paths Pikachu can take.

```python
def pikachu_unique_paths(m, n):
    pass
```

Example Usage:

```python
print(pikachu_unique_paths(3, 7))
print(pikachu_unique_paths(3, 2))
```

Example Output:

```markdown
28  
Example 1 Explanation:  
Pikachu can take 28 unique paths from the top-left corner to the bottom-right corner on a 3x7 grid.

3  
Example 2 Explanation:  
Pikachu can take 3 unique paths from the top-left corner to the bottom-right corner on a 3x2 grid:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
```
