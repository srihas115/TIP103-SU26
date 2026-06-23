# Problem 7: Combining Shipwreck Loot

The mermaid princess Ariel and her friend Flounder have just finished exploring a new shipwreck and have each stored the items they found in a BST. Given the roots of two binary search trees, `root1` and `root2` where each node represents an item found in the shipwreck, return a list containing all the node values from **both trees** in lexicographical (alphabetical) order. The tree nodes are organized in lexicographical order within each tree.

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity. 

```python
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def combine_loot(root1, root2):
    pass
```

Example Usage:

```python
"""
    Fork                Coin
   /    \              /    \
Coin    Statue     Anchor   Mirror
"""
root1 = TreeNode("Fork", TreeNode("Coin"), TreeNode("Statue"))
root2 = TreeNode("Coin", TreeNode("Anchor"), TreeNode("Mirror"))

"""
    Fork             Necklace
        \              /    
       Necklace     Fork   
"""
root3 = TreeNode("Fork", None, TreeNode("Necklace"))
root4 = TreeNode("Necklace", TreeNode("Fork"))

print(combine_loot(root1, root2))
print(combine_loot(root3, root4))
```

Example Output:

```markdown
['Anchor', 'Coin', 'Coin', 'Fork', 'Mirror', 'Statue']
['Fork', 'Fork', 'Necklace', 'Necklace']
```
