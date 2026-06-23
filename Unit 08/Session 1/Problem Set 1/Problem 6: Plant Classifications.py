class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def get_most_specific(taxonomy):
    pass

"""
           Plantae
          /       \
         /         \
        /           \
Non-flowering     Flowering
   /      \       /        \
Mosses   Ferns Gymnosperms Angiosperms
                             /     \
                        Monocots  Dicots
"""
plant_taxonomy = TreeNode("Plantae",
                          TreeNode("Non-flowering", TreeNode("Mosses"), TreeNode("Ferns")),
                                  TreeNode("Flowering", TreeNode("Gymnosperms"),
                                          TreeNode("Angiosperms", TreeNode("Monocots"), TreeNode("Dicots"))))

print(get_most_specific(plant_taxonomy))
