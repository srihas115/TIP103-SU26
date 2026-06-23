# Problem 4: Kth Smallest Element in a BST

Given the `root` of a binary search tree, and an integer `k`, return the `kth` smallest value (1-indexed) of all the values of the nodes in the tree.

```python
class TreeNode():
     def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def kth_smallest(root, k):
    pass
```

Example Usage 1:

![Example 1 Tree](./kth_smallest_element_bst_ex1.jpg)

```python
values_1 = [3, 1, 4, None, 2]

# Using build_tree() function included at top of page
tree_1 = build_tree(values_1)
print(kth_smallest(tree_1, 1))
```

Example Output 1: 

```markdown
1
```

Example Usage 2: 

![Example 1 Tree](./kth_smallest_element_bst_ex2.jpg)

```python
values_2 = [5, 3, 6, 2, 4, None, None, 1]

# Using build_tree() function included at top of page
tree_2 = build_tree(values_2)
print(kth_smallest(tree_2, 3))
```

Example Output 2: 

```markdown
3
```
