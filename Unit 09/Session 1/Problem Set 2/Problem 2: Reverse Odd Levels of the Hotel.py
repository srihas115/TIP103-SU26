class TreeNode():
     def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def reverse_odd_levels(hotel):
    pass

"""
        Lobby
      /      \
     102     101
     / \     /  \
   201 202 203 204
"""
hotel = Room("Lobby",
            Room(102, Room(201), Room (202)),
                Room(101, Room(203), Room(204)))

# Using print_tree() function included at the top
print_tree(reverse_odd_levels(hotel))
