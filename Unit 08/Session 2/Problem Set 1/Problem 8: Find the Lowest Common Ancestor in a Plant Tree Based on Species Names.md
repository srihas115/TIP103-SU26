# Problem 8: Find the Lowest Common Ancestor in a Plant Tree Based on Species Names

Given the `root` of a binary tree where each node represents a different plant species, return the value of the lowest common ancestor (LCA) of two given plants in the tree based on their species names. The species names are represented as strings, and the tree is structured according to lexicographical order (alphabetical order). The lowest common ancestor is defined between two species `p` and `q` as the lowest node in the tree that has both `p` and `q` as descendants (where we allow a node to be a descendant of itself). 

Assume all plants are a unique species. Note that each `TreeNode` has a reference to its parent node.

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity. 

**Note:** the `build_tree()` function will not work for this problem because of the extra `parent` attribute. You must create your own tree manually for testing.

```python
class TreeNode():
    def __init__(self, species, parent=None, left=None, right=None):
        self.val = species
        self.parent = parent # Parent of node
        self.left = left
        self.right = right

def lca(root, p, q):
    pass
```

Example Usage:

```python
"""
          fern
        /      \
       /        \
  cactus        rose
   /  \         /   \
bamboo dahlia lily  oak
"""
fern = TreeNode("fern")
cactus = TreeNode("cactus", fern)
rose = TreeNode("rose", fern)
bamboo = TreeNode("bamboo", cactus)
dahlia = TreeNode("dahlia", cactus)
lily = TreeNode("lily", rose)
oak = TreeNode("oak", rose)

fern.left, fern.right = cactus, rose
cactus.left, cactus.right = bamboo, dahlia
rose.left, rose.right = lily, oak

print(lca(fern, "cactus", "rose"))
print(lca(fern, "bamboo", "oak"))
```

Example Output:

```markdown
fern
Example 1 Explanation: The lowest common ancestor of "cactus" and "rose" is "fern" because "fern" 
is the lowest node in the tree that has both "cactus" and "rose" as descendants.

fern
Example 2 Explanation: The lowest common ancestor of "bamboo" and "oak" is "fern" because "fern" 
is the lowest node in the tree that has both "bamboo" and "oak" as descendants.
```

<br>
