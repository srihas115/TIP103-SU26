# Problem 5: Calculating Yield II

You have a fruit tree represented as a binary tree. Given the `root` of the tree, evaluate the amount of fruit your tree will yield this year. The tree has the following form:

- **Leaf nodes** have an integer value.
- **Non-leaf nodes** have a string value of either `"+"`, `"-"`, `"*"`, or `"-"`.

The **yield** of a the tree is calculated as follows:
- If the node is a leaf node, the yield is the **value** of the node. 
- Otherwise evaluate the node's two children and apply the mathematical operation of its value with the children's evaluations.

Return the result of evaluating the `root` node. 

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity. 

```python
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def calculate_yield(root):
  pass
```

Example Usage:

```python
"""
      +
     / \ 
    /   \
   -     *
  / \   / \
 4   2 10  2
"""

root = TreeNode("+")
root.left = TreeNode("-")
root.right = TreeNode("*")
root.left.left = TreeNode(4)
root.left.right = TreeNode(2)
root.right.left = TreeNode(10)
root.right.right = TreeNode(2)

print(calculate_yield(root))
```

Example Output:

```markdown
22
Explanation:
- 4 - 2 = 2
- 10 * 2 = 20
- 2 + 20 = 22
```
