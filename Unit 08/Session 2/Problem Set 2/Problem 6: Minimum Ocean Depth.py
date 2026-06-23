class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def find_min_depth(root):
    pass

"""
    Shipwreck
   /         \
 Shallows   Reef
           /    \
        Cave    Trench
"""

# Using build_tree() function at top of page
values = ["Shipwreck", "Shallows", "Reef", None, None, "Cave", "Trench"]
ocean = build_tree(values)

print(find_min_depth(ocean))
