class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count_cookie_paths(root, target_sum):
    pass

"""
    10
   /  \
  5     8
 / \   / \
3   7 12  4
"""
# Using build_tree() function included at the top of the page
cookie_nums = [10, 5, 8, 3, 7, 12, 4]
cookies1 = build_tree(cookie_nums)

"""
    8
   / \
  4   12
 / \    \
2   6    10
"""
cookie_nums = [8, 4, 12, 2, 6, None, 10]
cookies2 = build_tree(cookie_nums)

print(count_cookie_paths(cookies1, 22))
print(count_cookie_paths(cookies2, 14))
