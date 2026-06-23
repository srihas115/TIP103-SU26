class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def count_clusters(hotel):
    pass

"""
     👻
   /    \
  👻     🧛🏾
 /  \      \
👻  🧛🏾      🧛🏾
"""
# Using build_tree() function included at the top of the page
themes = ["👻", "👻", "🧛🏾", "👻", "🧛🏾", None, "🧛🏾"]
hotel = build_tree(themes)

print(count_clusters(themes))
