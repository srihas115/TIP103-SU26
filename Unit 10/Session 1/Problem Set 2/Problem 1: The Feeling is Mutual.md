# Problem 1: The Feeling is Mutual

You are given an insider look into the Hollywood gossip with an adjacency matrix `celebrities` where each node labeled 0 to `n` represents a celebrity. `celebrities[i][j] = 1` indicates that celebrity `i` likes celebrity `j` and `celebrities[i][j] = 0` indicates that celebrity `i` dislikes or doesn't know celebrity `j`. Write a function `is_mutual()` that returns `True` if all relationships between celebrities are mutual and `False` otherwise. A relationship between two celebrities is mutual if for any celebrity `i` that likes celebrity `j`, celebrity `j` also likes celebrity `i`. 

```python
def is_mutual(celebrities):
    pass
```

Example Usage:

*Example 1: `celebrities1`*

!['celebrities1' graph diagram](../../Unit%20Assets/the_feeling_is_mutual_ex1.png)

*Example 2: `celebrities2`*
!['celebrities2' graph diagram](../../Unit%20Assets/the_feeling_is_mutual_ex2.png)

```python
celebrities1 = [
                [0, 1, 1, 0],
                [1, 0, 1, 0],
                [1, 1, 0, 1],
                [0, 0, 1, 0]]

celebrities2 = [
                [0, 1, 1, 0],
                [1, 0, 0, 0],
                [1, 1, 0, 1],
                [0, 0, 0, 0]]

print(is_mutual(celebrities1))
print(is_mutual(celebrities2))
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
