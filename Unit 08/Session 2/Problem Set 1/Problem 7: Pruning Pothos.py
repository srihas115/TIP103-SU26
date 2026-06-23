class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def prune(root, target):
    pass

"""
         Healthy
        /       \
     Dying    Healthy
     /          /  \
   Dying     Dying  New Growth
"""

# Using build_tree() function at the top of the page
values = ["Healthy", "Dying", "Healthy", "Dying", None, "Dying", "New Growth"]
pothos1 = build_tree(values)

# Using print_tree() function at the top of the page
print_tree(prune(pothos1, "Dying"))
