class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def count_species(node):
    pass

"""
         Shark
       /       \
      /         \
   Grouper     Snapper
   /     \           \
Conch   Tang       Zooplankton
"""

food_chain = TreeNode("Shark",
                    TreeNode("Grouper", TreeNode("Conch"), TreeNode("Tang")),
                            TreeNode("Snapper", None, TreeNode("Zooplankton")))

print(count_species(food_chain))
