class TreeNode():
     def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def kth_smallest(root, k):
    pass

values_1 = [3, 1, 4, None, 2]

# Using build_tree() function included at top of page
tree_1 = build_tree(values_1)
print(kth_smallest(tree_1, 1))

values_2 = [5, 3, 6, 2, 4, None, None, 1]

# Using build_tree() function included at top of page
tree_2 = build_tree(values_2)
print(kth_smallest(tree_2, 3))
