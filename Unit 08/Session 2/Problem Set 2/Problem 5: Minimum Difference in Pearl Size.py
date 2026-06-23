class Pearl:
    def __init__(self, size=0, left=None, right=None):
        self.val = size
        self.left = left
        self.right = right

def min_diff_in_pearl_sizes(pearls):
    pass

"""
        4
       / \
      2   6
     / \   \
    1   3   8
"""
# Use build_tree() function at top of page
values = [4, 2, 6, 1, 3, None, 8]
pearls = build_tree(values)

print(min_diff_in_pearl_sizes(pearls))
