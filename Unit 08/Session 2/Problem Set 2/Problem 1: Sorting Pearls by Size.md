# Problem 1: Sorting Pearls by Size

You have a collection of pearls harvested from a local oyster bed. The pearls are organized by their size in a BST, where each node in the BST represents the size of a pearl. 

A function `smallest_to_largest_recursive()` which takes in the BST root `pearls` and returns an array of pearl sizes sorted from smallest to largest has been provided for you.

Implement a new function `smallest_to_largest_iterative()` which provides a iterative solution, taking in the BST root `pearls` and returning an array of pearl sizes sorted from smallest to largest has been provided for you.

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time complexity. 

```python
class Pearl:
    def __init__(self, size, left=None, right=None):
        self.val = size
        self.left = left
        self.right = right

def smallest_to_largest_recursive(pearls):
    sorted_list = []
    
    def inorder_traversal(node):
        if node:
            inorder_traversal(node.left)   
            sorted_list.append(node.val) 
            inorder_traversal(node.right)  
    
    inorder_traversal(pearls)
    return sorted_list

def smallest_to_largest_iterative(pearls):
    pass
```

Example Usage:

```python
"""
        3
       / \
      /   \ 
     1     5
      \   / \
       2 4   8
"""

#  Using build_tree() from the top of the page
values = [3, 1, 5, None, 2, 4, 8]
pearls = build_tree(values)

print(smallest_to_largest_recursive(pearls))
print(smallest_to_largest_iterative(pearls))
```

Example Output:

```markdown
[1, 2, 3, 4, 5, 8]
[1, 2, 3, 4, 5, 8]
```

<details>
  <summary><strong>💡 Hint: Recursive to Iterative Translations</strong></summary>

This problem can be solved using a stack! Often, when we want to translate recursive solutions to iterative solutions, the solution involves creating a stack. This is because behind the scenes, recursive solutions take advantage of a computer's in-built **call stack** which also uses a stack data structure. You can read more about the call stack in the Advanced Section of the Unit 7 cheatsheet if you are curious.

</details>
