class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right

def locate_treasure(grotto, treasure):
    pass

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
