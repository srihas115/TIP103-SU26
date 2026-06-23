class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def most_popular_cookie_combo(root):
    pass

"""
       5
      / \
     2  -3
"""
cookies1 = TreeNode(5, TreeNode(2), TreeNode(-3))

"""
       5
      / \
     2  -5
"""
cookies2 = TreeNode(5, TreeNode(2), TreeNode(-5))

print(most_popular_cookie_combo(cookies1))
print(most_popular_cookie_combo(cookies2))
