# Problem 8: Coral Reef Symmetry

Given the `root` of a binary tree representing a coral, return `True` if the coral is symmetric around its center and `False` otherwise. A coral is symmetric if the left and right subtrees are mirror images of each other. 

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity. 

```python
"""
# Example 1

# Input: root = CoralKing
# Expected Output: True

# Example 2

    CoralQueen
     /      \
 CoralX    CoralX
  /  \      /  \
CoralY CoralZ CoralY CoralZ

# Input: root = CoralQueen
# Expected Output: False
"""

class TreeNode:
    def __init__(self, value, left=None):
        self.val = value
        self.left = left
        self.right = right

def is_symmetric(root):
    pass
```   

Example Usage:

![coral1 example tree with dotted line down center to show symmetry](../../Unit%20Assets/symmetric_coral_ex.png)

```python
"""
        A
      /   \
     B     B
    / \   / \
   C  D   D  C
"""
coral1 = TreeNode('A', 
                  TreeNode('B', TreeNode('C'), TreeNode('D')), 
                          TreeNode('B', TreeNode('D'), TreeNode('C')))

"""
        A
      /   \
     B     B
    / \   / \
   C  D   C  D
"""
coral2 = TreeNode('A', 
                  TreeNode('B', TreeNode('C'), TreeNode('D')), 
                          TreeNode('B', TreeNode('C'), TreeNode('D')))

print(is_symmetric(coral1))
print(is_symmetric(coral2))
```

Example Output:

```markdown
True
False
```

<br>
