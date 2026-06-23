# Problem 5: Count Cursed Hallways

The haunted hotel is known for its mysterious hallways, where guests often lose their way. Some hallways are said to be cursed, leading travelers to strange places when they follow a certain sequence of rooms. A hallway is said to be cursed if the sum of its room numbers adds up to a `target_sum`. 

Given the root of a binary tree `hotel` where each node represents a room number in the hotel and an integer `target_sum` that represents the cursed sum, return the number of distinct paths in the hotel where the sum of the room numbers along the path equals `target_sum`

The path can start and end at any room but must follow the direction from parent rooms to child rooms. Your task is to count all such cursed paths that yield the exact `target_sum`. 

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Evaluate the complexities for both a balanced and unbalanced tree.

```python
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def count_cursed_hallways(hotel, target_sum):
    pass
```

Example Usage:

![example tree 'hotel' with paths that add up to 'target_sum' 8 circled](../../Unit%20Assets/count_cursed_hallways_ex.jpg)

```python
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
```

Example Output:

```markdown
3
```
