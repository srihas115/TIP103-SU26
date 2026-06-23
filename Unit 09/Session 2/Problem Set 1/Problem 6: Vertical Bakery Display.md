# Problem 6: Vertical Bakery Display

Your bakery's inventory is organized in a binary tree where each node represents a different bakery item. To make it easier for staff to locate items, you want to create a vertical display of the inventory. The vertical order traversal should be organized column by column, from left to right.

If two items are in the same row and column, they should be listed from left to right, just as they appear in the inventory.

Given the `root` of the binary tree representing the inventory, return a list of lists with the vertical order traversal of the bakery items. Each inner list should represent the `ith` column in the inventory tree, and each inner list's elements should include the values of each bakery item in that column. 

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Evaluate the complexities for both a balanced and unbalanced tree.

```python
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def vertical_inventory_display(root):
    pass
```

Example Usage 1:

!['inventory1' example tree with columns color coded](../../Unit%20Assets/vertical_display_ex1.png)

```python
"""
         Bread
       /       \
   Croissant    Donut
                /   \
             Bagel Tart
"""
# Using build_tree() function included at the top of the page
inventory_items = ["Bread", "Croissant", "Donut", None, None, "Bagel", "Tart"]
inventory1 = build_tree(inventory_items)

print(vertical_inventory_display(inventory1))  
```

Example Output 1:

```plaintext
[['Croissant'], ['Bread', 'Bagel'], ['Donut'], ['Tart']]
```

<br>

Example Usage 2:

!['inventory2' example tree with columns color coded](../../Unit%20Assets/vertical_display_ex2.png)

```python
"""
         Bread
       /       \
   Croissant    Donut
   /    \        /   \
Muffin  Scone Bagel Tart
        /       \
      Pie     Cake
"""  
inventory_items = ["Bread", "Croissant", "Donut", "Muffin", "Scone", "Bagel", "Tart", None, None, "Pie", None, None, "Cake", None, None]
inventory2 = build_tree(inventory_items)

print(vertical_inventory_display(inventory2))  
```

Example Output 2:

```plaintext
[['Muffin'], ['Croissant', 'Pie'], ['Bread', 'Scone', 'Bagel'], ['Donut', 'Cake'], ['Tart']]
```
