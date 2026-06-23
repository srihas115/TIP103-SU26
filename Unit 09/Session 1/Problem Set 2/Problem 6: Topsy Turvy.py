class TreeNode():
     def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.val = value
        self.left = left
        self.right = right

def flip_hotel(hotel):
    pass

"""
      1
    /   \
   2     3
  / \
 4   5
"""

# Using build_tree() function included at top of page
rooms = [1, 2, 3, 4, 5]
hotel = build_tree(rooms)

# Using print_tree() function included at top of page
print_tree(flip_hotel(hotel))
