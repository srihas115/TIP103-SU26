class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def find_largest_pearl(root):
    pass

"""
         7
        / \
       6   0
      / \
     5   1
"""
oysters = TreeNode(7, TreeNode(6, TreeNode(5), TreeNode(1)), TreeNode(0))

"""
   1
  / \
 0   1
"""
oysters2 = TreeNode(1, TreeNode(0), TreeNode(1))

print(find_largest_pearl(oysters))
print(find_largest_pearl(oysters2))
