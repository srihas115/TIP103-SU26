class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def find_duplicate_subtrees(hotel):
    pass

"""
        Lobby
      /       \
    101      123
    /        /  \
  201      101  201
          /
         201
"""
# Using build_tree() function included at top of page
rooms = ["Lobby", 101, 123, 201, None, 101, 201, None, None, 201]
hotel = build_tree(rooms)

# Using print_tree() function included at top of page
subtree_lst = find_duplicate_subtrees(hotel)
for subtree in subtree_lst:
    print_tree(subtree)
