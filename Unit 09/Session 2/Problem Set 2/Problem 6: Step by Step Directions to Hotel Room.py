class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def count_cursed_hallways(hotel, current_location, room_number):
    pass

"""
       5
      / \
     1   2
    /   / \
   3   6   4
"""
# Using build_tree() function included at top of page
room_nums = [5,1,2,3,None,6,4]
hotel1 = build_tree(room_nums)

print(count_cursed_hallways(hotel1, 3, 6))

"""
  2
 /
1
"""
hotel2 = TreeNode(1, TreeNode(2))

print(count_cursed_hallways(hotel2, 2, 1))
