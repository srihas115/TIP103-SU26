# Problem 4: Zombie Infested City Regions

The city is in chaos due to the zombie apocalypse, and has been fenced off into sections according to the severity of the zombie infestation. The city is represented as an `n x n` `grid`, where each `1x1` square in the grid represents a part of the city and contains either a fence or an open area:

- A `'/'` or  `'\\'`  (forward or backslash) represents a _fence_ dividing the square into two triangular zones.
- A `' '` represents an _open area_ with no division in the square.

Given the `grid` represented as an array of strings where each substring is a row and each character in a substring is a column in the row, return the total number of contiguous regions.

Note that backslashes are represented as `'\\'` instead of `'\'` because backslashes are escaped characters. 

```python
def count_regions(grid):
    pass
```

Example Usage 1: 

!['grid_1' regions](../../Unit%20Assets/zombie_infested_city_regions_ex1.png)

```python
grid_1 = [" /","/ "]

print(count_regions(grid_1))
```

Example Output 1: 

```markdown
2
```

Example Usage 2: 

!['grid_2' regions](../../Unit%20Assets/zombie_infested_city_regions_ex2.png)

```python
grid_2 = [" /","  "]

print(count_regions(grid_2))
```

Example Output 2: 

```markdown
1
```

Example Usage 3: 

!['grid_3' regions](../../Unit%20Assets/zombie_infested_city_regions_ex3.png)

```python
grid_3 = ["/\\","\\/"]

print(count_regions(grid_3))
```

Example Output 2: 

```markdown
5
Example Explanation: Recall that because \ characters are escaped, "\\/" refers to \/, 
and "/\\" refers to /\.
```

<details>
  <summary><strong>💡 Hint: Understanding the Input</strong></summary>

To solve this problem, you may find it useful to expand the input `grid` into a binary matrix of `1`s and `0`s similar to what you experienced in the previous problems.

1.  **Understanding the grid**:

- A `"/"` divides the square into two triangular regions: top-left and bottom-right.

- A `"\"` divides the square into two triangular regions: top-right and bottom-left.

- A `" "` (open area) doesn't divide the square at all—it represents a single undivided region.

2.  **Expand the grid**:

- You can break each square in the original `n x n` grid into 4 sub-cells or triangles in a `3n x 3n` grid:

- Divide each cell of the original grid into a 3x3 block to represent the division of space caused by slashes.

- Each block represents how the slashes cut through the square.

- Example:

- For a `"/"`, you can mark the triangular divisions in the expanded 3x3 grid:

``` codehilite

[0, 0, 1]

[0, 1, 0]

[1, 0, 0]

```

</details>
