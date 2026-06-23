# Problem 3: Graph Valid Tree

You have a graph of `n` nodes labeled from `0` to `n - 1`. You are given an integer `n` and a list of edges where <code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> indicates that there is an undirected edge between nodes <code>a<sub>i</sub></code> and <code>b<sub>i</sub></code> in the graph.

Return `True` if the edges of the given graph make up a valid tree, and `False` otherwise.

A graph is a valid tree if it meets two conditions:
- Connected: All nodes must be reachable from any other node, meaning there is exactly one connected component.
- Acyclic: The graph must not contain any cycles.

```python
def valid_tree(n, edges):
    pass
```

Example Usage 1:

![Example 1 Graph](../../Unit%20Assets/graph_valid_tree_ex1.jpg)

```python
edges_1 = [[0,1],[0,2],[0,3],[1,4]]

print(valid_tree(5, edges_1))
```

Example Output 1:

```markdown
True
```

Example Usage 2:

![Example 2 Graph](../../Unit%20Assets/graph_valid_tree_ex2.jpg)

```python
edges_2 = [[0,1],[1,2],[2,3],[1,3],[1,4]]

print(valid_tree(5, edges_2))
```

Example Output 2:

```markdown
False
```
