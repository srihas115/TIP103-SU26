# Problem 6: Step by Step Directions to Hotel Room

You have a lost guest who needs step by step directions to their hotel room. The hotel is stored in a binary tree where each node represents a room in the hotel. Each room in the hotel is uniquely assigned a value from `1` to `n`. You have the `root` of the hotel with `n` rooms, an integer `current_location` representing the value of the start node `s` and an integer `room_number` representing the value of the destination node `t`. 

Find the shortest path starting from node `s` and ending at node `t`. Return step by step directions for the guest of this path as a string consisting of only uppercase letters `'L'`, `'R'`, and `'U'`. Each letter indicates a specific direction:

- `'L'` means to go from a node to its left child node.
- `'R'` means to go from a node to its right child node.
- `'U'` means to go from a node to its parent node. 

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Evaluate the complexities for both a balanced and unbalanced tree.

```python
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def count_cursed_hallways(hotel, current_location, room_number):
    pass
    
```

Example Usage 1:

![Example tree 'hotel1' with arrows of showing shortest path](../../Unit%20Assets/step_by_step_directions_to_hotel_room_ex1.png)

```python
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
```

Example Output 1:

```markdown
UURL
Explanation: The shortest path is: 3 -> 1 -> 5 -> 2 -> 6
```

Example Usage 2:

![Example tree 'hotel2' with arrows of showing shortest path](../../Unit%20Assets/step_by_step_directions_to_hotel_room_ex2.png)

```python
"""
  2
 /
1
"""
hotel2 = TreeNode(1, TreeNode(2))

print(count_cursed_hallways(hotel2, 2, 1))
```

Example Output 2:

```markdown
L
Explanation: The shortest path is: 2 -> 1
```
