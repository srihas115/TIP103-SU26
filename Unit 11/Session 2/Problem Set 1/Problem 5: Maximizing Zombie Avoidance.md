# Problem 5: Maximizing Zombie Avoidance

<!-- Dijkstra's -->
<!-- Max heap instead of min heap -->

In a post-apocalyptic world, you need to find the safest path through a series of zombie-infested zones. The zones are connected by roads, but each passage has a probability of success for safely making it through without encountering zombies. You must find the path that maximizes your chances of survival when traveling from one safe zone to another.

You are given an undirected graph with `n` nodes where each node represents a safe zone and each edge represents a road between two zones and has a probability of success. The graph is represented by an edge list, where `edges[i] = [a, b]` means that there is an undirected passage between zone `a` and zone `b` with a probability of success `succ_prob[i]`.

Given two zones, `start` and `end`, find the path that maximizes the probability of survival when traveling from the `start` zone to the `end` zone and return that maximum probability. If there is no safe path from start to end, return `0`. Round your answer to the nearest hundredth. 

```python
def max_survival_probability(n, edges, succ_prob, start, end):
    pass
```

Example Usage 1:

![Example 1 Graph Diagram](../../Unit%20Assets/maximizing_zombie_avoidance_ex1.png)

```python
edges_1 = [[0, 1], [1, 2], [0, 2]]
succ_prob_1 = [0.5, 0.5, 0.2]

print(max_survival_probability(3, edges_1, succ_prob_1, 0, 2))
```

Example Output 1:

```markdown
0.25
Example 1 Explanation:
The possible paths from zone 0 to zone 2 are:
- 0 -> 1 -> 2, with probability 0.5 * 0.5 = 0.25.
- 0 -> 2, with probability 0.2.
The safest path has a probability of 0.25.
```

Example Usage 2:

![Example 2 Graph Diagram](../../Unit%20Assets/maximizing_zombie_avoidance_ex2.png)

```python
edges_2 = [[0, 1], [1, 2], [0, 2]]
succ_prob_2 = [0.5, 0.5, 0.3]

print(max_survival_probability(3, edges_2, succ_prob_2, 0, 2))
```

Example Output 2:

```markdown
0.3
Example 2 Explanation:
The possible paths from zone 0 to zone 2 are:
- 0 -> 1 -> 2, with probability 0.5 * 0.5 = 0.25.
- 0 -> 2, with probability 0.3.
The safest path has a probability of 0.3.
```

Example Usage 3:

![Example 3 Graph Diagram](../../Unit%20Assets/maximizing_zombie_avoidance_ex3.png)

```python
edges_3 = [[0, 1]]
succ_prob_3 = [0.5]

print(max_survival_probability(2, edges_3, succ_prob_3, 0, 1))
```

Example Output 3:

```markdown
0.5
Example 3 Explanation:
There is only one path between zone 0 and zone 1, with a probability of 0.5.
```

<details>
  <summary><strong>✨ AI Hint: Dijkstra's Algorithm</strong></summary>

*Key Skill: Use AI to explain code concepts*

This problem can be solved using Dijkstra's Algorithm, a very popular algorithm for finding the shortest path in a weighted graph.

For a refresher, check out the Advanced section of the [Unit 11 Cheatsheet](https://courses.codepath.org/courses/tip103/unit/11#!cheatsheet).

If you need help understanding Dijkstra's Algorithm, you can ask an AI tool like ChatGPT or GitHub Copilot to explain it to you, and even provide a step-by-step example of the algorithm in action.

We recommend trying to understand the **algorithm** first, and only attempt implementation once you have a solid grasp of how it works.

</details>
