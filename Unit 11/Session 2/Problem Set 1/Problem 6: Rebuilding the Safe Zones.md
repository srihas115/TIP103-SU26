# Problem 6: Rebuilding the Safe Zones

In the post-apocalyptic world, several survivor camps are scattered across the land. To unite these camps and form a network of safe zones, you need to rebuild the roads between them. However, the rebuilding process comes with a cost, and resources are limited.

You are given an integer `n` representing the number of survivor camps, labeled from `1` to `n`. You are also given an array `connections`, where `connections[i] = [x, y, cost]` indicates that rebuilding the road between camp `x` and camp `y` will cost `cost` resources.

Your goal is to minimize the total cost of connecting all the camps so that there is at least one safe path between every pair of camps. If it is impossible to connect all the camps, return `-1`.

```python
def min_rebuilding_cost(n, connections):
    pass
```

Example Usage 1:

![Example 1 graph diagram](../../Unit%20Assets/rebuilding_safe_zones_ex1.png)

```python
connections_1 = [[1, 2, 5], [1, 3, 6], [2, 3, 1]]

print(min_rebuilding_cost(3, connections_1))
```

Example Output 1:

```markdown
6
Example 1 Explanation:
The minimum cost to connect all the camps is to rebuild the road between camp 2 and camp 3 (cost 1) and the road between camp 1 and camp 2 (cost 5). The total cost is 6.
```

Example Usage 2:

![Example 2 graph diagram](../../Unit%20Assets/rebuilding_safe_zones_ex2.png)

```python
connections_2 = [[1, 3, 2], [2, 4, 4]]
print(min_rebuilding_cost(4, connections_2))
```

Example Output 2:

```markdown
-1
Example 2 Explanation:
It is impossible to connect all 4 camps since there is no connection between camps 1 and 2, and camps 1 and 4.
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
