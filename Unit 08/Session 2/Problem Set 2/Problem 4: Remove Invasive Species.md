# Problem 4: Remove Invasive Species

As a marine ecologist, you are worried about invasive species wreaking havoc on the local ecosystem. Given the root of a BST `ecosystem` where each node represents a species in a marine ecosystem, and an invasive species `name`, remove the species with value `name` from the ecosystem. Return the root of the modified ecosystem. Species are organized alphabetically in the tree by name (`val`). 

If the node with `name` has two children in the tree, replace it with its **inorder successor** (leftmost node in its right subtree). You do not need to maintain a balanced tree. 

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity. 

```python
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def remove_species(ecosystem, name):
    pass
```

Example Usage:

```python
"""
                Dugong
             /         \
       Brain Coral   Lionfish
              \       /       \
         Clownfish Giant Clam  Seagrass
"""
# Use build_tree() function at top of page
values = ["Dugong", "Brain Coral", "Lionfish", None, "Clownfish", "Giant Clam", "Seagrass"]
ecosystem = build_tree(ecosystem)

# Using print_tree() function at top of page
print_tree(remove_species(ecosystem, "Lionfish"))
```

Example Output:

```plaintext
['Dugong', 'Brain Coral', 'Seagrass', None, 'Clownfish', 'Giant Clam', None]

Explanation:
The resulting tree structure:
             Dugong
            /      \
      Brain Coral  Seagrass
            \         /
        Clownfish  Giant Clam
```
