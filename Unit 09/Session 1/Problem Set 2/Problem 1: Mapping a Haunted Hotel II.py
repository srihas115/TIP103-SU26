class TreeNode():
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def map_hotel(hotel):
    pass

"""
         Lobby
        /     \
       /       \
      101      102
     /   \    /   \
   201  202  203  204
   /                \
 301                302
"""

hotel = Room("Lobby",
                Room(101, Room(201, Room(301)), Room(202)),
                Room(102, Room(203), Room(204, None, Room(302))))

print(map_hotel(hotel))
