class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right

def find_flower(inventory, name):
    pass

"""
         Rose
        /    \
      Lilac   Tulip
     /  \       \
  Daisy  Lily  Violet
"""

# using build_tree() function at top of page
values = ["Rose", "Lilac", "Tulip", "Daisy", "Lily", None, "Violet"]
garden = build_tree(values)

print(find_flower(garden, "Lilac"))
print(find_flower(garden, "Sunflower"))
