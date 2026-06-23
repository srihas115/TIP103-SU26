class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def leftmost_path(root):
    pass

"""
        CaveA
       /      \
    CaveB    CaveC
    /   \        \
CaveD CaveE     CaveF
"""
system_a = TreeNode("CaveA",
                  TreeNode("CaveB", TreeNode("CaveD"), TreeNode("CaveE")),
                          TreeNode("CaveC", None, TreeNode("CaveF")))

"""
  CaveA
      \
      CaveB
        \
        CaveC
"""
system_b = TreeNode("CaveA", None, TreeNode("CaveB", None, TreeNode("CaveC")))

print(leftmost_path(system_a))
print(leftmost_path(system_b))
