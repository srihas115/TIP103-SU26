class TreeNode:
    def __init__(self, key, val, left=None, right=None):
        self.key = key      # Plant rarity
        self.val = val      # Plant name
        self.left = left
        self.right = right

def sort_plants(collection):
    pass

"""
         (3, "Monstera")
        /               \
   (1, "Pothos")     (5, "Witchcraft Orchid")
        \                 /
  (2, "Spider Plant")   (4, "Hoya Motoskei")
"""

# Using build_tree() function at the top of page
values = [(3, "Monstera"), (1, "Pothos"), (5, "Witchcraft Orchid"), None, (2, "Spider Plant"), (4, "Hoya Motoskei")]
collection = build_tree(values)

print(sort_plants(collection))
