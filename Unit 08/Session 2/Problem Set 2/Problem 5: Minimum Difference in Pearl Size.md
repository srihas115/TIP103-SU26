# Problem 5: Minimum Difference in Pearl Size

You are analyzing your collection of pearls stored in a BST where each node represents a pearl with a specific size (`val`). You want to see if you have two pearls of similar size that you can make into a pair of earrings. 

Write a function `min_diff_in_pearl_sizes()` that acceps the root of a BST `pearls`, and returns the minimum difference between the sizes of any two different pearls in the collection. 

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity. 

```python
class Pearl:
    def __init__(self, size=0, left=None, right=None):
        self.val = size
        self.left = left
        self.right = right

def min_diff_in_pearl_sizes(pearls):
    pass

```

Example Usage:

```python
"""
        4
       / \
      2   6
     / \   \
    1   3   8
"""
# Use build_tree() function at top of page
values = [4, 2, 6, 1, 3, None, 8]
pearls = build_tree(values)

print(min_diff_in_pearl_sizes(pearls))  
```

Example Output:

```markdown
1 
Explanation: The difference between pearl sizes 3 and 4, or 2 and 3
```
