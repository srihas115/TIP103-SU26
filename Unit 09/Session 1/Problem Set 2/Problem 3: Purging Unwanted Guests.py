class TreeNode():
     def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def purge_hotel(hotel):
    pass

"""
      👻
     /  \
   😱   🧛🏾‍♀️
  /  \
 💀  😈
"""

# Using build_tree() function included at the top of the page
guests = ["👻", "😱", "🧛🏾‍♀️", "💀", "😈"]
hotel = build_tree(guests)

# Using print_tree() function included at the top of the page
print_tree(hotel)
print(purge_hotel(hotel))
