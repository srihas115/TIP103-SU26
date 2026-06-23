class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def distribute_coins(root):
    pass

"""
    3
   / \
  0   0
"""
root1 = TreeNode(3, TreeNode(0), TreeNode(0))

"""
    0
   / \
  3   0
"""
root2 = TreeNode(0, TreeNode(3), TreeNode(0))

print(distribute_coins(root1))
print(distribute_coins(root2))
