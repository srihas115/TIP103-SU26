# Problem 6: Split Collection

You've accumulated too many plants, and need to split up your collection. Given the root of a BST `collection` where each node represents a plant in your collection and a value `target`, split the tree into two subtrees where the first subtree has node values that are lexicographically (alphabetically) smaller than or equal to `target` and the second subtree has all nodes that are greater than `target`. It is not necessarily the case that the collection contains a plant (node) with value `target`.

Additionally, most of the structure of the original tree should remain. Formally for any child plant `c` with parent `p` in the original collection, if they are both in the same subtree/subcollection after teh split, then plant `c` should still have the parent `p`. 

Return an array of the two root nodes of the two subtrees in order. 

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity. 

```python
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def split_collection(collection, target):
    pass
```

Example Usage:

![Example input BST 'collection'](../../Unit%20Assets/split_bst_input.png)

```python
"""
              Money Tree
             /         \
           Hoya        Pilea
           /   \        /   \
        Aloe   Ivy    Orchid  ZZ Plant
"""

# Using build_tree() function at the top of the page
values = ["Money Tree", "Hoya", "Pilea", "Aloe", "Ivy", "Orchid", "ZZ Plant"]
collection = build_tree(values)

# Using print_tree() function at the top of the page
left, right = split_collection(collection, "Hoya")
print_tree(left)
print_tree(right)
```

Example Output:

<!-- Output image omitted because the source image is broken. -->

```plaintext
['Hoya', 'Aloe']
['Money Tree', 'Ivy', 'Pilea', None, None, 'Orchid', 'ZZ Plant']

Explanation:
Left Subtree:
   Hoya
   /
Aloe

Right Subtree:
    Money Tree
    /       \
   Ivy     Pilea
          /     \
       Orchid  ZZ Plant
```
