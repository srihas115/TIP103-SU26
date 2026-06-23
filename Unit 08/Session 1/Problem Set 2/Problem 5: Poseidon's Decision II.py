class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def get_decision(root):
    pass

"""
        AND
     /      \
   OR       AND
  /  \       /  \
True False True False
"""

root = TreeNode("AND")
root.left = TreeNode("OR")
root.right = TreeNode("AND")
root.left.left = TreeNode(True)
root.left.right = TreeNode(False)
root.right.left = TreeNode(True)
root.right.right = TreeNode(False)
print(get_decision(root))
