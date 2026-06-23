# Problem 2: Escaping the Sea Caves II

If you implemented `leftmost_path()` iteratively in the previous problem, implement it recursively. If you implemented it recursively, implement it iteratively.

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity. 

```python
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def leftmost_path(root):
    pass
```

Example Usage:

```python
"""
        CaveA
       /      \
    CaveB    CaveC
    /   \        \
CaveD CaveE     CaveF  
"""
system_a = TreeNode("CaveA", 
                  TreeNode("CaveB", TreeNode("CaveD"), TreeNode("CaveE")), 
                          TreeNode("CaveC", None, TreeNode("CaveF")))

"""
  CaveA
      \
      CaveB
        \
        CaveC  
"""
system_b = TreeNode("CaveA", None, TreeNode("CaveB", None, TreeNode("CaveC")))

print(leftmost_path(system_a))
print(leftmost_path(system_b))
```

Example Output:

```markdown
['CaveA', 'CaveB', 'CaveD']
['CaveA']
```
