# Problem 3: Add New Treasure to Collection

The mermaid princess Ariel and her pal Flounder visited a new shipwreck and found an exciting new human artifact to add to her collection. Ariel's collection of human treasures is stored in a binary search tree (BST) where each node represents a different item in her collection. Items are organized according to their names (`val`s) in alphabetical order in the BST. 

Given the root of the binary search tree `grotto` and a string `new_item`, write a function `add_treasure()` that adds a new node with value `new_item` to the collection and returns the `root` of the modified tree. If a node with value `new_item` already exists within the tree, return the original tree unmodified. You do not need to maintain balance in the tree. 

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity. 

```python
class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
         
def add_treasure(grotto, new_item):
    pass
```

Example Usage:

```python
"""
             Snarfblat
            /        \
        Gadget       Whatzit
       /     \           \
Dinglehopper Gizmo       Whozit
"""

# Using build_tree() function at the top of page
values = ["Snarfblat", "Gadget", "Whatzit", "Dinglehopper", "Gizmo", None, "Whozit"]
grotto = build_tree(values)

# Using print_tree() function included at top of page
print_tree(add_treasure(grotto, "Thingamabob")) 
```

Example Output:

```markdown
['Snarfblat', 'Gadget', 'Whatzit', 'Dinglehopper', 'Gizmo', 'Thingamabob', 'Whozit']
Explanation: 
Updated tree:
               Snarfblat
            /             \
        Gadget            Whatzit
       /     \           /       \
Dinglehopper Gizmo  Thingamabob  Whozit
```
