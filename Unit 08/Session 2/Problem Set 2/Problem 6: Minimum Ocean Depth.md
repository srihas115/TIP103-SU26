# Problem 6: Minimum Ocean Depth

You have just finished surveying a new, previously unexplored part of the ocean and want to find the shallowest part. Given the `root` of a binary tree representing this new part of the ocean, return its minimum depth. The minimum depth is the number of nodes along the shortest path from the `root` down to the nearest leaf node.

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity. 

```python
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def find_min_depth(root):
    pass
```

Example Usage:

```python
"""
    Shipwreck
   /         \
 Shallows   Reef
           /    \
        Cave    Trench
"""

# Using build_tree() function at top of page
values = ["Shipwreck", "Shallows", "Reef", None, None, "Cave", "Trench"]
ocean = build_tree(values)

print(find_min_depth(ocean))
```

Example Output:

```markdown
2
```
