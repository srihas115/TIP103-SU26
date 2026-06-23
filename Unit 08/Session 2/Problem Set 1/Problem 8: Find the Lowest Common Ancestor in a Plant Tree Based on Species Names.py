class TreeNode():
    def __init__(self, species, parent=None, left=None, right=None):
        self.val = species
        self.parent = parent # Parent of node
        self.left = left
        self.right = right

def lca(root, p, q):
    pass

"""
          fern
        /      \
       /        \
  cactus        rose
   /  \         /   \
bamboo dahlia lily  oak
"""
fern = TreeNode("fern")
cactus = TreeNode("cactus", fern)
rose = TreeNode("rose", fern)
bamboo = TreeNode("bamboo", cactus)
dahlia = TreeNode("dahlia", cactus)
lily = TreeNode("lily", rose)
oak = TreeNode("oak", rose)

fern.left, fern.right = cactus, rose
cactus.left, cactus.right = bamboo, dahlia
rose.left, rose.right = lily, oak

print(lca(fern, "cactus", "rose"))
print(lca(fern, "bamboo", "oak"))
