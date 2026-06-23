# Problem 6: Topsy Turvy

You're walking down the hotel hallway one night and something strange begins to happen - the entire hotel flips upside down. The rooms and their connections were flipped in a peculiar way and now you need to restore order. Given the root of a binary tree `hotel` where each node represents a room in the hotel, write a function `flip_hotel()` that flips the hotel right side up according to the following rules:

1. The original left child becomes the new root
2. The original root becomes the new right child
3. The original right child becomes the new left child. 

![Three node tree showing each step applied to tree](../../Unit%20Assets/topsy_turvy.jpg)

The above steps are done level by level. It is **guaranteed** each right node has a sibling (a left node with the same parent) and has no children.

Return the root of the flipped hotel.

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity. 

```python
class TreeNode():
     def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.val = value
        self.left = left
        self.right = right

def flip_hotel(hotel):
    pass
```

Example Usage:

!['hotel' example tree after each step](../../Unit%20Assets/topsy_turvy_ex.jpg)

```python
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
```

Example Output:

```plaintext
[4, 5, 2, None, None, 3, 1]
Explanation:
Flipped hotel structure:
      4
    /   \
   5     2
        / \
       3   1
```
