# Problem 6: Uniform Coral

Triton is looking for the perfect piece of coral to gift his mother, Amphitrite, for her birthday. Given the `root` of a binary tree representing a coral structure, write a function `is_uniform()` that evaluates the quality of the coral. The function should return `True` if each node in the coral tree has the same value and `False` otherwise.

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity. 

```python
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def is_uniform(root):
    pass
```

Example Usage:

```python
"""
         1
        / \
       1   1
      / \      
     1   1 
"""
coral = TreeNode(1, TreeNode(1, TreeNode(1), TreeNode(1)), TreeNode(1))

"""
   1
  / \
 2   1
"""
coral2 = TreeNode(1, TreeNode(2), TreeNode(1))

print(is_uniform(coral))
print(is_uniform(coral2))
```

Example Output: 

```markdown
True
False
```
