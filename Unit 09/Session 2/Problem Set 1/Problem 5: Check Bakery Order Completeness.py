class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def is_complete(root):
    pass

"""
        Croissant
       /         \
    Cupcake      Bagel
   /      \      /
Cake     Pie  Blondies
"""
# Using build_tree() function included at the top of page
items = ["Croissant", "Cupcake", "Bagel", "Cake", "Pie", "Blondies"]
order1 = build_tree(items)

"""
        Croissant
       /         \
    Cupcake      Bagel
   /      \           \
Cake     Pie         Blondies
"""
items = ["Croissant", "Cupcake", "Bagel", "Cake", "Pie", None, "Blondies"]
order2 = build_tree(items)

print(is_complete(order1))
print(is_complete(order2))
