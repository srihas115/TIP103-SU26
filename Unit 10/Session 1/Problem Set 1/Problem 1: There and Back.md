# Problem 1: There and Back

As a flight coordinator for CodePath airlines, you have a 0-indexed adjacency list `flights` with `n` nodes where each node represents the ID of a different destination and `flights[i]` is an integer array indicating that there is a flight from destination `i` to each destination in `flights[i]`. Write a function `bidirectional_flights()` that returns `True` if for every flight from a destination `i` to a destination `j` there also exists a flight from destination `j` to destination `i`. Return `False` otherwise.

```python
def bidirectional_flights(flights):
    pass
```

Example Usage:

*Example 1: `flights1`*

!['flights1' graph diagram](../../Unit%20Assets/there_and_back_ex1.png)

*Example 2: `flights2`*
!['flights2' graph diagram](../../Unit%20Assets/there_and_back_ex2.png)

```python
flights1 = [[1, 2], [0], [0, 3], [2]]
flights2 = [[1, 2], [], [0], [2]]

print(bidirectional_flights(flights1))
print(bidirectional_flights(flights2))
```

Example Output:

```markdown
True
False
```

<details>
  <summary><strong>💡 Hint: Introduction to Graphs</strong></summary>

This problem requires you to be familiar with the graph data structure and the different methods for representing graphs. Check out the [Unit 10 Cheatsheet](https://courses.codepath.org/courses/tip103/unit/10#!cheatsheet) if you are unfamiliar with these concepts.

</details>
