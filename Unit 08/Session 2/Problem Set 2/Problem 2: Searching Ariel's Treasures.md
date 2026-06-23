# Problem 2: Searching Ariel's Treasures

The mermaid princess Ariel is looking for a specific item in the grotto where she collects all the various objects from the human world she finds. Ariel's collection of human treasures is stored in a binary search tree (BST) where each node represents a different item in her collection. The items are organized according to their names (`val`s) in alphabetical order in the BST. 

Given the root of the binary search tree `grotto` and a target object `treasure`, write a function `locate_treasure()` that returns `True` if `treasure` is present in the grotto and `False` otherwise.  

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity. 

*Hint: Intro to Binary Search Trees*

```python
class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
         
def locate_treasure(grotto, treasure):
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
values = ["Snarfblat", "Gadget", "Whatzit", "Dinglehopper", "Gizmo", "Whozit"]
grotto = build_tree(values)

print(locate_treasure(grotto, "Dinglehopper"))  
print(locate_treasure(grotto, "Thingamabob")) 
```

Example Output:

```markdown
True
False
```
