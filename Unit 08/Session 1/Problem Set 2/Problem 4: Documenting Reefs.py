class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def explore_reef(root):
    pass

"""
         CoralA
        /     \
     CoralB  CoralC
     /   \
 CoralD CoralE
"""

reef = TreeNode("CoralA",
                TreeNode("CoralB", TreeNode("CoralD"), TreeNode("CoralE")),
                          TreeNode("CoralC"))

print(explore_reef(reef))
