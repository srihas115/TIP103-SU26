# Problem 5: Find Most Common Plants in Collection

You have a vast plant collection and want to know which plants you own the most of. Given the `root` of a BST with duplicates where each node is a plant in your collection, return a list with the name(s) (`val`) of the most frequently occurring plant(s) in your collection. If multiple plants tie for the most frequently occuring plant, you may return them in any order. 

Assume your BST organizes plants alphabetically by name and follows the following rules:
- The left subtree of a node contains only nodes with values **less than or equal** to the node's value 
- The right subtree of a node contains only nodes with values **greater than or equal** to the node's value. 
- Both the left and right subtrees must also be BSTs.

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity. 

```python
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def find_most_common(root):
    pass
```

Example Usage:

```python
"""
    Hoya
      \ 
      Pothos
      /
    Pothos
"""

# Using build_tree() function at top of page
values = ["Hoya", None, "Pothos", "Pothos"]
collection1 = build_tree(values)

"""
      Hoya
    /      \ 
  Aloe    Pothos
  /        /
 Aloe   Pothos
"""
values = ["Hoya", "Aloe", "Pothos", "Aloe", None, "Pothos"]
collection2 = build_tree(values)

print(find_most_common(collection1))
print(find_most_common(collection2))
```

Example Output: 

```markdown
['Pothos']
['Aloe', 'Pothos']
```

<details>
  <summary><strong>💡 Hint: Choosing a Traversal Order</strong></summary>

Oftentimes when we solve a binary tree problem, the traversal order doesn't matter. But sometimes, it can help to specifically follow a preorder, inorder, or postorder traversal. This problem would most benefit from a inorder traversal because when traversing a BST, inorder traversal visits the nodes in sorted order from least to greatest. Since the plants are organized alphabetically, an inorder traversal will visit all occurrences of a plant consecutively. This makes it easy to count occurrences as we traverse the tree.

</details>
