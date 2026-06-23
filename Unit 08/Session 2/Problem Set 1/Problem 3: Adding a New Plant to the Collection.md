# Problem 3: Adding a New Plant to the Collection

You have just purchased a new houseplant and are excited to add it to your collection! Your collection is meticulously organized using a Binary Search Tree (BST) where each node in the tree represents a houseplant in your collection, and houseplants are organized alphabetically by name (`val`).

Given the root of your BST `collection` and a new houseplant `name`, insert a new node with value `name` into your collection. Return the root of your updated collection. If another plant with `name` already exists in the tree, add the new node in the existing node's right subtree. 

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.  Assume the input tree is balanced when calculating time and space complexity. 

```python
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def add_plant(collection, name):
    pass
```

Example Usage:

```python
"""
            Money Tree
        /              \
Fiddle Leaf Fig    Snake Plant
"""

# Using build_tree() function at the top of page
values = ["Money Tree", "Fiddle Leaf Fig", "Snake Plant"]
collection = build_tree(values)

# Using print_tree() function at the top of page
print_tree(add_plant(collection, "Aloe"))
```

Example Output:

```plaintext
['Money Tree', 'Fiddle Leaf Fig', 'Snake Plant', 'Aloe']

Explanation: 
Tree should have the following structure:
           Money Tree
        /              \
 Fiddle Leaf Fig   Snake Plant
   /
 Aloe
```
