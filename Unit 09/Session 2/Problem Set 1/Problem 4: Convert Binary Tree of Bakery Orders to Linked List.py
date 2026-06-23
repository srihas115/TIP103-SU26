class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def flatten_orders(orders):
    pass

"""
        Croissant
       /         \
    Cupcake      Bagel
   /      \           \
Cake     Pie         Blondies
"""
# Using build_tree() function included at the top of page
items = ["Croissant", "Cupcake", "Bagel", "Cake", "Pie", None, "Blondies"]
orders = build_tree(items)

# Using print_tree() function included at the top of page
print_tree(flatten_orders(orders))
