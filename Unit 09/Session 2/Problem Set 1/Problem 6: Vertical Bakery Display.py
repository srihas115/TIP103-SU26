class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def vertical_inventory_display(root):
    pass

"""
         Bread
       /       \
   Croissant    Donut
                /   \
             Bagel Tart
"""
# Using build_tree() function included at the top of the page
inventory_items = ["Bread", "Croissant", "Donut", None, None, "Bagel", "Tart"]
inventory1 = build_tree(inventory_items)

print(vertical_inventory_display(inventory1))

"""
         Bread
       /       \
   Croissant    Donut
   /    \        /   \
Muffin  Scone Bagel Tart
        /       \
      Pie     Cake
"""
inventory_items = ["Bread", "Croissant", "Donut", "Muffin", "Scone", "Bagel", "Tart", None, None, "Pie", None, None, "Cake", None, None]
inventory2 = build_tree(inventory_items)

print(vertical_inventory_display(inventory2))
