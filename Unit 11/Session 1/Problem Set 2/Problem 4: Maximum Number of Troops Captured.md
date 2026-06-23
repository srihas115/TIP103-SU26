# Problem 4: Maximum Number of Troops Captured

You are given a 2D matrix `battlefield` of size `m x n`, where `(row, column)` represents:
- An impassable obstacle if `battlefield[row][column] = 0`, or
- An square containing `battlefield[row][column]` enemy troops, if `battlefield[row][column] > 0`.

Your kingdom can start at any non-obstacle square `(row, column)` and can do the following operations any number of times:
    - Capture all the troops at square `battlefield[row][column]` or
    - Move to any adjacent cell with troops up, down, left, or right. 

Return the maximum number of troops your kingdom can capture if they choose the starting cell optimally. Return `0` if no troops exist on the `battlefield`.  

```python
def capture_max_troops(battlefield):
    pass
```

Example Usage 1:

!['battlefield_1' grid](../../Unit%20Assets/max_troops_captured_ex1.png)

```python
battlefield_1 = [
    [0,2,1,0],
    [4,0,0,3],
    [1,0,0,4],
    [0,3,2,0]]

print(capture_max_troops(battlefield_1))
```

Example Output 1:

```markdown
7
Example 1 Explanation: You can start at square (1, 3) and capture 3 troops, then 
move to square (2, 3) and capture 4 troops. 
```

Example Usage 2:

!['battlefield_2' grid](../../Unit%20Assets/max_troops_captured_ex2.png)

```python
battlefield_2 = [
    [1,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,1]]

print(capture_max_troops(battlefield_2))
```

Example Output 2:

```markdown
1
Example 2 Explanation: You can start at square (0,0) or (3,3) and capture a single
troop. 
```
