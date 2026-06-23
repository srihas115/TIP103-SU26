# Problem 5: Minimum Effort Path to the Castle

You are about to embark on a long journey to the castle to make a request of the queen. The kingdom's terrain is represented by a `m x n` 2D array `heights`, where `heights[row][col]` represents the height of the terrain at position `(row, col)`.

You start your journey at the top-left corner of the kingdom `(0, 0)` and need to safely reach the castle, which is located at the bottom-right corner `(rows-1, columns-1)`. You can move **up**, **down**, **left**, or **right** through the kingdom. However, you want to minimize the effort it takes to cross the rugged terrain.

The effort of a path is defined as the maximum absolute difference in heights between two consecutive locations along the path. Your task is to find the minimum effort required to travel from the top-left corner to the castle at the bottom-right.

```python
def min_effort(heights):
    pass
```

Example Usage 1:

!['terrain_1' with minimum effort path highlighted](../../Unit%20Assets/min_effort_ex1.png)

```python
terrain_1 = [
    [1, 2, 2],
    [3, 8, 2],
    [5, 3, 5]
]

print(min_effort(terrain_1))
```

Example Output 1:

```markdown
2
Example 1 Explanation: The path with the minimum effort of 2 can be found by traveling 
through cells with minimal height differences.
```

Example Input 2:

!['terrain_2' with minimum effort path highlighted](../../Unit%20Assets/min_effort_ex2.png)

```python
terrain_2 = [
    [1, 2, 3],
    [3, 8, 4],
    [5, 3, 5]
]

print(min_effort(terrain_2))
```

Example Output 2:

```markdown
1
Example 2 Explanation: The safest path to the castle in this scenario requires 
only an effort of 1, as the height differences between consecutive cells are minimal.
```

<details>
  <summary><strong>✨ AI Hint: Dijkstra's Algorithm</strong></summary>

*Key Skill: Use AI to explain code concepts*

This problem can be solved using Dijkstra's Algorithm, a very popular algorithm for finding the shortest path in a weighted graph.

For a refresher, check out the Advanced section of the [Unit 11 Cheatsheet](https://courses.codepath.org/courses/tip103/unit/11#!cheatsheet).

If you need help understanding Dijkstra's Algorithm, you can ask an AI tool like ChatGPT or GitHub Copilot to explain it to you, and even provide a step-by-step example of the algorithm in action.

We recommend trying to understand the **algorithm** first, and only attempt implementation once you have a solid grasp of how it works.

</details>
