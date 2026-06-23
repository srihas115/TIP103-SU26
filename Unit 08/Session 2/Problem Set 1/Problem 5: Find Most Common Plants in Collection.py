class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def find_most_common(root):
    pass

"""
    Hoya
      \
      Pothos
      /
    Pothos
"""

# Using build_tree() function at top of page
values = ["Hoya", None, "Pothos", "Pothos"]
collection1 = build_tree(values)

"""
      Hoya
    /      \
  Aloe    Pothos
  /        /
 Aloe   Pothos
"""
values = ["Hoya", "Aloe", "Pothos", "Aloe", None, "Pothos"]
collection2 = build_tree(values)

print(find_most_common(collection1))
print(find_most_common(collection2))
