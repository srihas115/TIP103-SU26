# Problem 7: Biggest Pearl

You are searching through a bed of oysters and searching for the oyster with the largest pearl. Given the `root` of a binary tree where each node represents the size of a pearl, return the size of the largest pearl.

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity. 

```python
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def find_largest_pearl(root):
    pass
```

Example Usage:

```python
"""
         7
        / \
       6   0
      / \      
     5   1 
"""
oysters = TreeNode(7, TreeNode(6, TreeNode(5), TreeNode(1)), TreeNode(0))

"""
   1
  / \
 0   1
"""
oysters2 = TreeNode(1, TreeNode(0), TreeNode(1))

print(find_largest_pearl(oysters))
print(find_largest_pearl(oysters2))
```

Example Output: 

```markdown
7
1
```
