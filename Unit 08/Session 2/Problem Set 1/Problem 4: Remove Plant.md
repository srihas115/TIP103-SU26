# Problem 4: Remove Plant

A plant in your houseplant collection has become infested with aphids, and unfortunately you need to throw it out. Given the root of a BST `collection` where each node represents a plant in your collection, and a plant `name`, remove the plant node with value `name` from the collection. Return the root of the modified collection. Plants are organized alphabetically in the tree by value. 

If the node with `name` has two children in the tree, replace it with its **inorder predecessor** (rightmost node in its left subtree). You do not need to maintain a balanced tree. 

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.  Assume the input tree is balanced when calculating time and space complexity. 

```python
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def remove_plant(collection, name):
    pass
```

Example Usage:

```python
"""
              Money Tree
             /         \
           Hoya        Pilea
              \        /   \
             Ivy    Orchid  ZZ Plant
"""

# Using build_tree() function at the top of page
values = ["Money Tree", "Hoya", "Pilea", None, "Ivy", "Orchid", "ZZ Plant"]
collection = build_tree(values)

# Using print_tree() function at the top of page
print_tree(remove_plant(collection, "Pilea"))
```

Example Output:

```plaintext
['Money Tree', 'Hoya', 'Orchid', None, 'Ivy', None, 'ZZ Plant']

Explanation:
The resulting tree structure:
             Money Tree
            /         \
          Hoya       Orchid
              \          \
              Ivy      ZZ Plant
```

<details>
  <summary><strong>💡 Hint: Inorder Predecessor</strong></summary>

The largest node smaller than a given node in a binary search tree is also called the **inorder predecessor**. The inorder predecessor of a node in a BST is the node that comes just before the given node in an inorder traversal of the tree.

Consider the following BST:

``` codehilite

20

/  \

10    30

/ \     \

5   15    35

/  \

12    17

```

</details>
