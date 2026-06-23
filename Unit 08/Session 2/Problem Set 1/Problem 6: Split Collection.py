class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def split_collection(collection, target):
    pass

"""
              Money Tree
             /         \
           Hoya        Pilea
           /   \        /   \
        Aloe   Ivy    Orchid  ZZ Plant
"""

# Using build_tree() function at the top of the page
values = ["Money Tree", "Hoya", "Pilea", "Aloe", "Ivy", "Orchid", "ZZ Plant"]
collection = build_tree(values)

# Using print_tree() function at the top of the page
left, right = split_collection(collection, "Hoya")
print_tree(left)
print_tree(right)
