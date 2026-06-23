class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def count_cursed_hallways(hotel, target_sum):
    pass

"""
        10
       /  \
      /    \
     5      -3
    / \       \
   3   2      11
  / \   \
 3  -2   1
"""
# Using build_tree() function included at top of page
room_numbers = [10,5,-3,3,2,None,11,3,-2,None,1]
hotel = build_tree(room_numbers)

print(count_cursed_hallways(hotel, 8))
