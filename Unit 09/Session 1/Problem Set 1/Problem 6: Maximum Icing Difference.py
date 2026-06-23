class TreeNode():
    def __init__(self, sweetness, left=None, right=None):
        self.val = sweetness
        self.left = left
        self.right = right

def max_icing_difference(root):
    pass

"""
            8
           /  \
         3     10
        / \      \
       1   6     14
          /  \    /
         4    7  13
"""

# Using build_tree() function included at top of page
sweetness_levels = [8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13]
display = build_tree(sweetness_levels)

print(max_icing_difference(display))
