# Problem 3: Purging Unwanted Guests

There are unwanted visitors lurking in the rooms of your haunted hotel, and it's time for a clear out. Given the root of a binary tree `hotel` where each node represents a room in the hotel and each node value represents the guest staying in that room. You want to systematically remove visitors in the following order:

- Collect the guests (values) of all leaf nodes and store them in a list. The leaf nodes may be stored in any order.
- Remove all the leaf nodes.
- Repeat until the hotel (tree) is empty.

Return a list of lists, where each inner list represents a collection of leaf nodes. 

```python
class TreeNode():
     def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def purge_hotel(hotel):
    pass
```

Example Usage:

!['hotel' example tree with each set of leaves highlighted before deletion](../../Unit%20Assets/purging_unwanted_guests_ex.png)

```python
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
```

Example Output:

```markdown
Empty
[['💀', '😈', '🧛🏾‍♀️'], ['😱'], ['👻']]
Explanation: 
[['💀', '🧛🏾‍♀️', '😈'], ['😱'], ['👻']] and [['🧛🏾‍♀️', '😈', '💀'], ['😱'], ['👻']] are also possible
answers since it doesn't matter which order the leaves in a given level are returned. 
The tree should always be empty once `purge_hotel()` has been executed.
```

<details>
  <summary><strong>💡 Hint: Choosing your Traversal Method</strong></summary>

This problem can be solved multiple ways, but may work best with a modified depth first search traversal. To learn more about how to choose a traversal algorithm visit the How to Pick a Traversal Algorithm section of the unit cheatsheet.

</details>
