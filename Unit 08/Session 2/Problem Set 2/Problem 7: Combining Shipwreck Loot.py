class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def combine_loot(root1, root2):
    pass

"""
    Fork                Coin
   /    \              /    \
Coin    Statue     Anchor   Mirror
"""
root1 = TreeNode("Fork", TreeNode("Coin"), TreeNode("Statue"))
root2 = TreeNode("Coin", TreeNode("Anchor"), TreeNode("Mirror"))

"""
    Fork             Necklace
        \              /
       Necklace     Fork
"""
root3 = TreeNode("Fork", None, TreeNode("Necklace"))
root4 = TreeNode("Necklace", TreeNode("Fork"))

print(combine_loot(root1, root2))
print(combine_loot(root3, root4))
