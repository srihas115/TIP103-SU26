# Problem 3: Count the Food Chain

Given the `root` of a binary tree representing a marine food chain, return the number of species (nodes) in the chain.

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity. 

```python
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def count_species(node):
    pass
```

Example Usage:

```python
"""
         Shark
       /       \  
      /         \
   Grouper     Snapper
   /     \           \  
Conch   Tang       Zooplankton
"""

food_chain = TreeNode("Shark", 
                    TreeNode("Grouper", TreeNode("Conch"), TreeNode("Tang")),
                            TreeNode("Snapper", None, TreeNode("Zooplankton")))

print(count_species(food_chain))
```

Example Output: 

```markdown
6
```

<details>
  <summary><strong>✨ AI Hint: Traversing Trees</strong></summary>

*Key Skill: Use AI to explain code concepts*

This problem requires you to traverse a binary tree. For a refresher on this topic, check out the Tree Traversal section of the [Unit 8 Cheatsheet](https://courses.codepath.org/courses/tip103/unit/8#!cheatsheet).

Still have questions? Try asking an AI tool like ChatGPT or GitHub Copilot to explain the different types of binary tree traversal. You can use the following prompt as a starting point:

*"You're an expert computer science tutor. Please explain the different types of binary tree traversal, and show me how they would each work on an example tree."*

Hint: Be sure to learn about "preorder", "postorder", and "inorder" traversals!

</details>
