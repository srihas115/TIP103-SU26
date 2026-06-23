# Problem 2: Flower Finding

You are looking to buy a new flower plant for your garden. The nursery you visit stores its inventory in a binary search tree (BST) where each node represents a plant in the store. The plants are organized according to their names (`val`s) in alphabetical order in the BST. 

Given the root of the binary search tree `inventory` and a target flower `name`, write a function `find_flower()` that returns `True` if the flower is present in the garden and `False` otherwise.  

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.  Assume the input tree is balanced when calculating time and space complexity.  

```python
class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
         
def find_flower(inventory, name):
    pass
```

Example Usage:

```python
"""
         Rose
        /    \
      Lilac   Tulip
     /  \       \
  Daisy  Lily  Violet
"""

# using build_tree() function at top of page
values = ["Rose", "Lilac", "Tulip", "Daisy", "Lily", None, "Violet"]
garden = build_tree(values)

print(find_flower(garden, "Lilac"))  
print(find_flower(garden, "Sunflower")) 
```

Example Output:

```markdown
True
False
```

<details>
  <summary><strong>✨ AI Hint: Binary Search Trees</strong></summary>

*Key Skill: Use AI to explain code concepts*

This problem requires you to be familiar with binary search trees (BSTs). This data structure is incredibly useful, and is often used in many coding interviews.

For a refresher on this topic, check out the Binary Search Tree section of the [Unit 8 Cheatsheet](https://courses.codepath.org/courses/tip103/unit/8#!cheatsheet).

To go deeper, you can ask an AI tool like ChatGPT or GitHub Copilot to explain the concept of binary search trees, how they work, and how to implement them in Python. You can also visit the [VisuAlgo BST Visualizer](https://visualgo.net/en/bst) to see how binary search trees work visually.

</details>
