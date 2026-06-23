# Problem 3: Larger Order Tree

You have the root of a binary search tree `orders`, where each node in the tree represents an order and each node's value represents the number of cupcakes the customer ordered. Convert the tree to a 'larger order tree' such that the value of each node in tree is equal to its original value plus the sum of all node values greater than it. 

As a reminder a BST satisfies the following constraints:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time complexity.

```python
class TreeNode():
     def __init__(self, order_size, left=None, right=None):
        self.val = order_size
        self.left = left
        self.right = right

def larger_order_tree(orders):
    pass
```

Examples Usage:

![Example 'orders' tree with both original node vlaue and larger order value listed](../../Unit%20Assets/larger_order_tree.png)

```python
"""
         4
       /   \
      /     \
     1       6
    / \     / \
   0   2   5   7
        \       \
         3       8   
"""
# using build_tree() function included at top of page
order_sizes = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
orders = build_tree(order_sizes)

# using print_tree() function included at top of page
print_tree(larger_order_tree(orders))
```

Example Output:

```plaintext
[30,36,21,36,35,26,15,None,None,None,33,None,None,None,8]
Explanation:
Larger Order Tree:
        30
       /   \
      /     \
     36     21
    / \     / \
   36  35  26  15
         \       \
         33       8   
```

<br>

<details>
  <summary><strong>💡 Hint: Choosing your Traversal Method</strong></summary>

This problem can be solved multiple ways, but may work best with a modified depth first search traversal. To learn more about how to choose a traversal algorithm visit the How to Pick a Traversal Algorithm section of the unit cheatsheet.

</details>
