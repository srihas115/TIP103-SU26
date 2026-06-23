# Problem 2: Connecting Roads for Winter

As winter approaches, the kingdom's roads must be reinforced to connect various outposts located across the kingdom. Each outpost is represented by a coordinate <code>[x<sub>i</sub>, y<sub>i</sub>]</code> on a 2D map. The cost of reinforcing a road between two outposts located at <code>[x<sub>i</sub>, y<sub>i</sub>]</code> and <code>[x<sub>j</sub>, y<sub>j</sub>]</code> is the _Manhattan distance_ between them, which is calculated as <code>|x<sub>i</sub> - x<sub>j</sub>| + |y<sub>i</sub> - y<sub>j</sub>|</code>, where `|val|` denotes the absolute value of `val`.

Write a function `prepare_winter_roads()` that returns the minimum cost to connect all outposts. All outposts are considered connected if there is exactly one simple path between any two outposts.

```python
def prepare_winter_roads(outposts):
    pass
```

Example Usage:

*Example 1:*
![`outputs_1` mapped on coordinate plane with manhattan distance shown](../../Unit%20Assets/prepare_winter_roads_ex1.png)

```python
outposts_1 = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
outposts_2 = [[3, 12], [-2, 5], [-4, 1], [5, 2], [9, 6]]

print(prepare_winter_roads(outposts_1))
print(prepare_winter_roads(outposts_2))
```

Example Output:

```markdown
20
Example 1 Explanation: The total minimum cost of connecting all the outposts is 20, calculated by finding the minimum spanning tree that connects all the points with the lowest possible road-reinforcement costs.

26
Example 2 Explanation: The kingdom's outposts in this scenario are more spread out, and the minimum total cost of connecting all of them with roads is 26.
```

<details>
  <summary><strong>💡 Hint: Kruskal's Algorithm</strong></summary>

This problem can be solved using Kruskal's Algorithm which finds the Minimum Spanning Tree (MST) of a graph. The MST of a graph is a subgraph of a weighted, connected, and undirected graph that connects all the vertices with the minimum possible total edge weight, while ensuring there are no cycles.

Kruskal's Algorithm Pseudocode:

``` codehilite

def kruskal(Graph G):

1. Initialize an empty set or list MST to store the edges of the Minimum Spanning Tree.

2. Sort all edges of the graph by their weight in non-decreasing order.

3. Initialize a Disjoint Set Union (DSU) data structure for the vertices.

- Each vertex starts in its own set.

4. For each edge (u, v) in the sorted list of edges:

a. If u and v are in different sets (i.e., no cycle is formed by adding this edge):

i. Add the edge (u, v) to the MST.

ii. Union the sets containing u and v (merge the sets).

5. Return the MST.

```

</details>
