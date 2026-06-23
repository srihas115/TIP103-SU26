# Problem 4: Find Eventual Safe Locations

There is a directed graph of `n` nodes where each node represents a location in a zombie infested city. Each node is labeled from `0` to `n - 1`. The graph is represented by a 0-indexed 2D integer array `city` where `city[i]` is an integer array of nodes adjacent to node `i`, meaning there is a directed edge from node `i` to each node in `city[i]`.

A node is a _terminal location_ if it has no outgoing edges. A node is a _safe location_ if every possible path starting from that node leads to a terminal location (or another safe location).

Return an array containing all the safe locations (nodes) of the graph. The answer should be sorted in ascending order.

```python
def eventual_safe_locations(city):
    pass
```

Example Usage:

*Example 1:*
!['city_1' graph diagram](../../Unit%20Assets/eventual_safe_locations.png)

```python
city_1 = [
    [1,2], # Location 0
    [2,3], # Location 1
    [5],   # Location 2
    [0],   # Location 3
    [5],   # Location 4
    [],    # Location 5
    []     # Location 6
    ]

city_2 = [
    [1,2,3,4], # Location 0
    [1,2],     # Location 1
    [3,4],     # Location 2
    [0,4],     # Location 3
    []         # Location 4
    ]

print(eventual_safe_locations(city_1))
print(eventual_safe_locations(city_2))
```

Example Output:

```markdown
[2,4,5,6]
Example 1 Explanation: The given graph is shown above.
Nodes 5 and 6 are terminal locations as there are no outgoing edges from either of them.
Every path starting at locations 2, 4, 5, and 6 all lead to either location 5 or 6.

[4]
Example 2 Explanation:
Only location 4 is a terminal location, and every path starting at node 4 leads to node 4.
```

<details>
  <summary><strong>✨ AI Hint: Topological Sort</strong></summary>

*Key Skill: Use AI to explain code concepts*

This problem may be solved with topological sort. Check out the Advanced section of the [Unit 11 Cheatsheet](https://courses.codepath.org/courses/tip103/unit/11#!cheatsheet) for more information.

If you need more info, you can ask an AI tool like ChatGPT or GitHub Copilot to help you understand topological sort. For example, you can ask:

*"What is topological sort, and when is it useful for solving coding problems?"*

*"Can you walk me through an example of topological sort in action?"*

</details>
