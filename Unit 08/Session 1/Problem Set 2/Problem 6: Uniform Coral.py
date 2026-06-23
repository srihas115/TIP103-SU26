class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def is_uniform(root):
    pass

"""
         1
        / \
       1   1
      / \
     1   1
"""
coral = TreeNode(1, TreeNode(1, TreeNode(1), TreeNode(1)), TreeNode(1))

"""
   1
  / \
 2   1
"""
coral2 = TreeNode(1, TreeNode(2), TreeNode(1))

print(is_uniform(coral))
print(is_uniform(coral2))
